import subprocess
import os
import sys

languages = {
    "snobol": "rosetta/tests/snobol_test.sno",
    "pli": "rosetta/tests/pli_test.pli",
    "modula2": "rosetta/tests/modula2_test.mod",
    "rpg": "rosetta/tests/rpg_test.rpg",
    "eiffel": "rosetta/tests/eiffel_test.e",
    "forth": "rosetta/tests/forth_test.fs",
    "ml": "rosetta/tests/ml_test.ml"
}

targets = ["py", "js"]

results = []

for lang, test_file in languages.items():
    for target in targets:
        print(f"Verifying {lang} to {target}...")
        try:
            cmd = [sys.executable, "-m", "rosetta.cli.main", test_file, "--to", target]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode == 0:
                results.append((lang, target, "PASS"))
            else:
                results.append((lang, target, f"FAIL: {result.stderr.strip()}"))
        except Exception as e:
            results.append((lang, target, f"ERROR: {str(e)}"))

print("\n--- Phase 4 Verification Matrix ---")
print(f"{'Language':<15} | {'Target':<10} | {'Status'}")
print("-" * 40)
for lang, target, status in results:
    print(f"{lang:<15} | {target:<10} | {status}")

all_pass = all(status == "PASS" for _, _, status in results)
if all_pass:
    print("\nALL PHASE 4 LANGUAGES PASSED!")
else:
    print("\nSOME LANGUAGES FAILED.")
    exit(1)
