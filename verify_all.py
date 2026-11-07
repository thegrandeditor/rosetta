import subprocess
import os
import sys

targets = ["js", "ts", "py", "c", "cpp", "java", "rs", "go", "rb", "php", "swift", "kt"]
input_file = "complex_test.py"

print(f"{'Target':<10} | {'Status':<10}")
print("-" * 22)

for target in targets:
    try:
        env = os.environ.copy()
        env["PYTHONPATH"] = "."
        cmd = [sys.executable, "rosetta/cli/main.py", input_file, "--to", target]
        result = subprocess.run(cmd, capture_output=True, text=True, env=env)
        
        if result.returncode == 0:
            print(f"{target:<10} | PASS")
        else:
            print(f"{target:<10} | FAIL")
            # print(result.stderr) # Uncomment for debugging
    except Exception as e:
        print(f"{target:<10} | ERROR ({str(e)})")

# Also test COBOL frontend
cobol_input = "rosetta/tests/cobol_to_python/hello.cbl"
if os.path.exists(cobol_input):
    print("\nTesting COBOL Frontend...")
    env = os.environ.copy()
    env["PYTHONPATH"] = "."
    cmd = [sys.executable, "rosetta/cli/main.py", cobol_input, "--to", "py"]
    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    if result.returncode == 0:
        print("COBOL -> Python: PASS")
    else:
        print("COBOL -> Python: FAIL")
