import subprocess
import os
import sys

languages = [
    ("fortran", "rosetta/tests/fortran_hello.f90"),
    ("basic", "rosetta/tests/basic_test.bas"),
    ("pascal", "rosetta/tests/pascal_test.pas"),
    ("ada", "rosetta/tests/ada_test.adb"),
    ("lisp", "rosetta/tests/lisp_test.lisp"),
    ("algol", "rosetta/tests/algol_test.alg"),
    ("smalltalk", "rosetta/tests/smalltalk_test.st"),
    ("prolog", "rosetta/tests/prolog_test.pl"),
    # COBOL is already somewhat tested, but let's add it
    ("cobol", "rosetta/tests/cobol_to_python/hello.cbl")
]

targets = ["py", "js"]

print(f"{'Language':<15} | {'Target':<10} | {'Status':<10}")
print("-" * 40)

for lang, test_file in languages:
    if not os.path.exists(test_file):
        print(f"{lang:<15} | {'N/A':<10} | SKIP (File not found: {test_file})")
        continue
        
    for target in targets:
        try:
            env = os.environ.copy()
            env["PYTHONPATH"] = "."
            cmd = [sys.executable, "-m", "rosetta.cli.main", test_file, "--to", target]
            result = subprocess.run(cmd, capture_output=True, text=True, env=env)
            
            if result.returncode == 0:
                print(f"{lang:<15} | {target:<10} | PASS")
            else:
                print(f"{lang:<15} | {target:<10} | FAIL")
                # print(f"Error: {result.stderr}")
        except Exception as e:
            print(f"{lang:<15} | {target:<10} | ERROR ({str(e)})")
