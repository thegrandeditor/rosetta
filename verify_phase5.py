import subprocess
import os
import sys

languages = {
    "solidity": "rosetta/tests/solidity_test.sol",
    "mojo": "rosetta/tests/mojo_test.mojo",
    "zig": "rosetta/tests/zig_test.zig",
    "carbon": "rosetta/tests/carbon_test.carbon"
}

targets = ["py", "js"]
results = []

print("Running Phase 5 Transpilation Tests...")
print("-" * 50)

for lang, test_file in languages.items():
    for target in targets:
        print(f"Verifying {lang} to {target}...")
        try:
            env = os.environ.copy()
            env["PYTHONPATH"] = "."
            cmd = [sys.executable, "-m", "rosetta.cli.main", test_file, "--to", target]
            result = subprocess.run(cmd, capture_output=True, text=True, env=env)
            if result.returncode == 0:
                results.append((lang, target, "PASS"))
            else:
                results.append((lang, target, f"FAIL: {result.stderr.strip()}"))
        except Exception as e:
            results.append((lang, target, f"ERROR: {str(e)}"))

print("\n--- Phase 5 Verification Matrix ---")
print(f"{'Language':<15} | {'Target':<10} | {'Status'}")
print("-" * 40)
for lang, target, status in results:
    print(f"{lang:<15} | {target:<10} | {status}")

all_pass = all(status == "PASS" for _, _, status in results)
if all_pass:
    print("\nALL PHASE 5 IMPLEMENTED LANGUAGES (SOLIDITY, MOJO, ZIG, CARBON) PASSED!")
else:
    print("\nSOME LANGUAGES FAILED.")
    exit(1)
