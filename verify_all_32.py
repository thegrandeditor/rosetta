import subprocess
import os
import sys

print("==================================================")
print("ROSETTA ENGINE - 32 LANGUAGE VERIFICATION SUITE")
print("==================================================\n")

# Phase 1: All 31 backend targets using the "company size code" complex_test.py
input_file = "complex_test.py"
targets = [
    # Phase 1
    ("JavaScript", "js"),
    ("TypeScript", "ts"),
    ("Python", "py"),
    ("C", "c"),
    ("C++", "cpp"),
    ("Java", "java"),
    ("Rust", "rs"),
    ("Go", "go"),
    ("Ruby", "rb"),
    ("PHP", "php"),
    ("Swift", "swift"),
    ("Kotlin", "kt"),
    # Phase 3
    ("Fortran", "fortran"),
    ("BASIC", "basic"),
    ("Pascal", "pascal"),
    ("Ada", "ada"),
    ("LISP", "lisp"),
    ("Algol", "algol"),
    ("Smalltalk", "smalltalk"),
    ("Prolog", "prolog"),
    # Phase 4
    ("SNOBOL4", "snobol"),
    ("PL/I", "pli"),
    ("Modula-2", "modula2"),
    ("RPG", "rpg"),
    ("Eiffel", "eiffel"),
    ("Forth", "forth"),
    ("ML", "ml"),
    # Phase 5
    ("Solidity", "solidity"),
    ("Mojo", "mojo"),
    ("Zig", "zig"),
    ("Carbon", "carbon")
]

results = []

print("Running Transpilation Tests on Company-Size Python Code (complex_test.py)...")
print("-" * 65)

for name, target in targets:
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = "."
        cmd = [sys.executable, "-m", "rosetta.cli.main", input_file, "--to", target]
        result = subprocess.run(cmd, capture_output=True, text=True, env=env)
        
        if result.returncode == 0:
            results.append((name, target, "PASS", ""))
            print(f"{name:<15} ({target:<8}) | Status: PASS")
        else:
            err_msg = result.stderr.strip().split('\n')[-1]
            results.append((name, target, "FAIL", err_msg))
            print(f"{name:<15} ({target:<8}) | Status: FAIL - {err_msg}")
    except Exception as e:
        results.append((name, target, "ERROR", str(e)))
        print(f"{name:<15} ({target:<8}) | Status: ERROR - {str(e)}")

# Phase 2: COBOL (Source-Only Language, 32nd Language)
print("\nVerifying COBOL Source-Only Language (32nd Language)...")
print("-" * 65)
cobol_input = "rosetta/tests/cobol_to_python/hello.cbl"
if os.path.exists(cobol_input):
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = "."
        cmd = [sys.executable, "-m", "rosetta.cli.main", cobol_input, "--to", "py"]
        result = subprocess.run(cmd, capture_output=True, text=True, env=env)
        if result.returncode == 0:
            results.append(("COBOL", "cbl (to py)", "PASS", ""))
            print("COBOL           (cbl)      | Status: PASS (Transpiles to Python successfully)")
        else:
            err_msg = result.stderr.strip().split('\n')[-1]
            results.append(("COBOL", "cbl (to py)", "FAIL", err_msg))
            print(f"COBOL           (cbl)      | Status: FAIL - {err_msg}")
    except Exception as e:
        results.append(("COBOL", "cbl (to py)", "ERROR", str(e)))
        print(f"COBOL           (cbl)      | Status: ERROR - {str(e)}")
else:
    results.append(("COBOL", "cbl (to py)", "SKIP", "hello.cbl not found"))
    print("COBOL           (cbl)      | Status: SKIP (hello.cbl not found)")

print("\n" + "=" * 65)
print("FINAL MATRIX SUMMARY")
print("==================================================")
print(f"{'Language':<15} | {'Target/Ext':<12} | {'Status':<10} | {'Details'}")
print("-" * 65)
for name, target, status, details in results:
    details_str = f"({details})" if details else ""
    print(f"{name:<15} | {target:<12} | {status:<10} | {details_str}")

all_pass = all(status == "PASS" for _, _, status, _ in results)
if all_pass:
    print("\nALL 32 LANGUAGES VERIFIED SUCCESSFULLY!")
    sys.exit(0)
else:
    print("\nVERIFICATION COMPLETED WITH SOME FAILURES.")
    sys.exit(1)
