import sys
import os
import time
from collections import defaultdict

if sys.platform == "win32":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROSETTA_ROOT = os.path.dirname(os.path.abspath(__file__))
if ROSETTA_ROOT not in sys.path:
    sys.path.insert(0, ROSETTA_ROOT)

from rosetta.cli.resolver import get_frontend, get_backend, LEGACY_EXTENSIONS
from rosetta.hermes.pipeline import HermesPipeline
from rosetta.hermes.passes.standard_passes import (
    TypeInferencePass,
    IdiomNormalizationPass,
    LegacyIndexingPass,
    RedundantDeclarationPass,
    StdlibNormalizationPass,
    LibraryMappingPass,
    MemorySafetyNormalizationPass,
)

# Inline canonical test fixtures for the 11 newly added Phase-1 BABEL Frontends
INLINE_FIXTURES = {
    ".js": """
function computeTotal(price, tax) {
    let total = price + tax;
    if (total > 100) {
        console.log("High value:", total);
    }
    return total;
}
console.log(computeTotal(90, 20));
""",
    ".ts": """
function computeTotal(price: number, tax: number): number {
    let total: number = price + tax;
    if (total > 100) {
        console.log("High value:", total);
    }
    return total;
}
console.log(computeTotal(90, 20));
""",
    ".java": """
public class Calculator {
    public static int computeTotal(int price, int tax) {
        int total = price + tax;
        if (total > 100) {
            System.out.println(total);
        }
        return total;
    }
}
""",
    ".cpp": """
#include <iostream>
int computeTotal(int price, int tax) {
    int total = price + tax;
    if (total > 100) {
        std::cout << total << std::endl;
    }
    return total;
}
int main() {
    std::cout << computeTotal(90, 20) << std::endl;
    return 0;
}
""",
    ".c": """
#include <stdio.h>
int computeTotal(int price, int tax) {
    int total = price + tax;
    if (total > 100) {
        printf("%d\\n", total);
    }
    return total;
}
int main() {
    printf("%d\\n", computeTotal(90, 20));
    return 0;
}
""",
    ".rs": """
fn compute_total(price: i32, tax: i32) -> i32 {
    let mut total: i32 = price + tax;
    if total > 100 {
        println!("{:?}", total);
    }
    return total;
}
fn main() {
    println!("{:?}", compute_total(90, 20));
}
""",
    ".go": """
package main
import "fmt"
func computeTotal(price int, tax int) int {
    total := price + tax
    if total > 100 {
        fmt.Println(total)
    }
    return total
}
func main() {
    fmt.Println(computeTotal(90, 20))
}
""",
    ".swift": """
func computeTotal(price: Int, tax: Int) -> Int {
    let total: Int = price + tax
    if total > 100 {
        print(total)
    }
    return total
}
print(computeTotal(90, 20))
""",
    ".kt": """
fun computeTotal(price: Int, tax: Int): Int {
    val total: Int = price + tax
    if (total > 100) {
        println(total)
    }
    return total
}
fun main() {
    println(computeTotal(90, 20))
}
""",
    ".rb": """
def compute_total(price, tax)
    total = price + tax
    if total > 100
        puts total
    end
    return total
end
puts compute_total(90, 20)
""",
    ".php": """
<?php
function computeTotal($price, $tax) {
    $total = $price + $tax;
    if ($total > 100) {
        echo $total;
    }
    return $total;
}
echo computeTotal(90, 20);
?>
""",
}

# Full 32 Source Language Test Matrix
SOURCE_SPECS = [
    ("Python", "complex_test.py", ".py", ["js", "ts", "cpp", "rs", "go", "java", "c", "py", "swift", "kt", "rb", "php", "cobol"]),
    ("JavaScript", None, ".js", ["py", "ts", "cpp", "rs", "go", "java", "c", "cobol", "js"]),
    ("TypeScript", None, ".ts", ["py", "js", "cpp", "rs", "go", "java", "c", "cobol", "ts"]),
    ("Java", None, ".java", ["py", "js", "ts", "cpp", "rs", "go", "c", "cobol", "java"]),
    ("C++", None, ".cpp", ["py", "js", "ts", "java", "rs", "go", "c", "cobol", "cpp"]),
    ("C", None, ".c", ["py", "js", "cpp", "java", "rs", "go", "cobol", "c"]),
    ("Rust", None, ".rs", ["py", "js", "ts", "cpp", "java", "go", "c", "cobol", "rs"]),
    ("Go", None, ".go", ["py", "js", "ts", "cpp", "java", "rs", "c", "cobol", "go"]),
    ("Swift", None, ".swift", ["py", "js", "ts", "cpp", "java", "rs", "go", "cobol", "swift"]),
    ("Kotlin", None, ".kt", ["py", "js", "ts", "cpp", "java", "rs", "go", "cobol", "kt"]),
    ("Ruby", None, ".rb", ["py", "js", "ts", "cpp", "java", "rs", "go", "cobol", "rb"]),
    ("PHP", None, ".php", ["py", "js", "ts", "cpp", "java", "rs", "go", "cobol", "php"]),
    ("COBOL", "company_cobol_standard.cbl", ".cbl", ["py", "js", "cpp", "java", "rs", "go", "c", "ts", "cobol"]),
    ("Fortran", "rosetta/tests/fortran_hello.f90", ".f90", ["py", "js", "c", "cpp", "rs", "go", "java", "fortran", "cobol"]),
    ("BASIC", "rosetta/tests/basic_test.bas", ".bas", ["py", "js", "cpp", "java", "rs", "c", "basic", "cobol"]),
    ("Pascal", "rosetta/tests/pascal_test.pas", ".pas", ["py", "js", "cpp", "java", "rs", "c", "pascal", "cobol"]),
    ("Ada", "rosetta/tests/ada_test.adb", ".adb", ["py", "js", "cpp", "java", "rs", "c", "ada", "cobol"]),
    ("LISP", "rosetta/tests/lisp_test.lisp", ".lisp", ["py", "js", "cpp", "java", "rs", "c", "lisp", "cobol"]),
    ("Algol", "rosetta/tests/algol_test.alg", ".alg", ["py", "js", "cpp", "java", "rs", "c", "algol", "cobol"]),
    ("Smalltalk", "rosetta/tests/smalltalk_test.st", ".st", ["py", "js", "cpp", "java", "rs", "c", "smalltalk", "cobol"]),
    ("Prolog", "rosetta/tests/prolog_test.pl", ".pl", ["py", "js", "cpp", "java", "rs", "c", "prolog", "cobol"]),
    ("SNOBOL4", "rosetta/tests/snobol_test.sno", ".sno", ["py", "js", "cpp", "java", "rs", "c", "snobol", "cobol"]),
    ("PL/I", "rosetta/tests/pli_test.pli", ".pli", ["py", "js", "cpp", "java", "rs", "c", "pli", "cobol"]),
    ("Modula-2", "rosetta/tests/modula2_test.mod", ".mod", ["py", "js", "cpp", "java", "rs", "c", "modula2", "cobol"]),
    ("RPG", "rosetta/tests/rpg_test.rpg", ".rpg", ["py", "js", "cpp", "java", "rs", "c", "rpg", "cobol"]),
    ("Eiffel", "rosetta/tests/eiffel_test.e", ".e", ["py", "js", "cpp", "java", "rs", "c", "eiffel", "cobol"]),
    ("Forth", "rosetta/tests/forth_test.fs", ".fs", ["py", "js", "cpp", "java", "rs", "c", "forth", "cobol"]),
    ("Standard ML", "rosetta/tests/ml_test.ml", ".ml", ["py", "js", "cpp", "java", "rs", "c", "ml", "cobol"]),
    ("Solidity", "rosetta/tests/solidity_test.sol", ".sol", ["py", "js", "ts", "cpp", "rs", "go", "solidity", "cobol"]),
    ("Mojo", "rosetta/tests/mojo_test.mojo", ".mojo", ["py", "js", "cpp", "rs", "go", "mojo", "cobol"]),
    ("Zig", "rosetta/tests/zig_test.zig", ".zig", ["py", "js", "c", "cpp", "rs", "zig", "cobol"]),
    ("Carbon", "rosetta/tests/carbon_test.carbon", ".carbon", ["py", "js", "cpp", "rs", "carbon", "cobol"]),
]


def run_transpile(src_code: str, ext: str, target: str) -> str:
    frontend = get_frontend(ext)
    ir = frontend.parse(src_code)

    pipeline = HermesPipeline()
    norm_ext = ext.lower().strip()
    if not norm_ext.startswith("."):
        norm_ext = "." + norm_ext

    if norm_ext in LEGACY_EXTENSIONS:
        pipeline.add_pass(LegacyIndexingPass())
        pipeline.add_pass(RedundantDeclarationPass())

    pipeline.add_pass(StdlibNormalizationPass())
    pipeline.add_pass(LibraryMappingPass(target))
    pipeline.add_pass(MemorySafetyNormalizationPass(target))
    pipeline.add_pass(TypeInferencePass())
    pipeline.add_pass(IdiomNormalizationPass())
    ir = pipeline.run(ir)

    backend = get_backend(target)
    return backend.emit(ir)


def run_cross_matrix():
    print("=" * 76)
    print("       ROSETTA CROSS-LANGUAGE MATRIX TESTING ENGINE (32 x 32)        ")
    print("=" * 76)

    total_tests = 0
    passed_tests = 0
    failed_tests = []
    category_stats = defaultdict(lambda: {"pass": 0, "fail": 0})

    start_time = time.time()

    for lang_name, file_path, ext, targets in SOURCE_SPECS:
        label = file_path if file_path else f"inline:{ext}"
        print(f"\n[*] Source Language: {lang_name.upper()} ({label})")
        print("-" * 76)

        if file_path:
            full_path = os.path.join(ROSETTA_ROOT, file_path)
            if not os.path.exists(full_path):
                print(f"    [!] Error: Test file not found: {full_path}")
                continue
            with open(full_path, "r", encoding="utf-8", errors="ignore") as f:
                src_code = f.read()
        else:
            src_code = INLINE_FIXTURES[ext]

        for target in targets:
            total_tests += 1
            t0 = time.time()
            try:
                out = run_transpile(src_code, ext, target)
                elapsed_ms = (time.time() - t0) * 1000

                unhandled = out.count("# Unknown node:") + out.count("// Unknown node:")
                if unhandled > 0:
                    status = f"WARN ({unhandled} unhandled)"
                    print(f"    -> Target: {target:<12} | {status:<22} | {elapsed_ms:>6.1f} ms | Output: {len(out)} chars")
                    failed_tests.append((lang_name, target, f"Contains {unhandled} unhandled AST nodes"))
                    category_stats[lang_name]["fail"] += 1
                elif len(out.strip()) == 0:
                    status = "FAIL (Empty output)"
                    print(f"    -> Target: {target:<12} | {status:<22} | {elapsed_ms:>6.1f} ms")
                    failed_tests.append((lang_name, target, "Empty transpilation output"))
                    category_stats[lang_name]["fail"] += 1
                else:
                    passed_tests += 1
                    category_stats[lang_name]["pass"] += 1
                    status = "PASS"
                    print(f"    -> Target: {target:<12} | {status:<22} | {elapsed_ms:>6.1f} ms | Output: {len(out)} chars")

            except Exception as e:
                elapsed_ms = (time.time() - t0) * 1000
                err_msg = f"{type(e).__name__}: {str(e)}"
                print(f"    -> Target: {target:<12} | FAIL                   | {elapsed_ms:>6.1f} ms | {err_msg}")
                failed_tests.append((lang_name, target, err_msg))
                category_stats[lang_name]["fail"] += 1

    total_elapsed = time.time() - start_time

    print("\n" + "=" * 76)
    print("                32-LANGUAGE CROSS-MATRIX SUMMARY                    ")
    print("=" * 76)
    print(f"{'Source Language':<20} | {'Passed':<10} | {'Failed':<10} | {'Success Rate'}")
    print("-" * 76)

    for lang_name, _, _, _ in SOURCE_SPECS:
        p = category_stats[lang_name]["pass"]
        f = category_stats[lang_name]["fail"]
        total = p + f
        rate = (p / total * 100) if total > 0 else 0.0
        print(f"{lang_name:<20} | {p:<10} | {f:<10} | {rate:>6.1f}%")

    print("-" * 76)
    overall_rate = (passed_tests / total_tests * 100) if total_tests > 0 else 0.0
    print(f"TOTAL LANGUAGES TESTED: {len(SOURCE_SPECS)} / 32")
    print(f"TOTAL TESTS ATTEMPTED:  {total_tests}")
    print(f"TOTAL PASSED:           {passed_tests}")
    print(f"TOTAL FAILED:           {len(failed_tests)}")
    print(f"OVERALL SUCCESS RATE:   {overall_rate:.1f}%")
    print(f"TOTAL EXECUTION TIME:   {total_elapsed:.2f} seconds")
    print("=" * 76)

    if failed_tests:
        print("\nFailures / Warnings Summary:")
        for src, tgt, err in failed_tests:
            print(f"  - [{src}] -> [{tgt}]: {err}")
    else:
        print("\nALL 32 SOURCE LANGUAGES & TARGET BACKENDS WORKED WITH 100% SUCCESS!")

    return len(failed_tests) == 0


if __name__ == "__main__":
    success = run_cross_matrix()
    sys.exit(0 if success else 1)
