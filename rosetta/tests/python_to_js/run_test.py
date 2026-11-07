import sys
import os
from rosetta.cli.main import main

# Mock sys.argv
sys.argv = ["rosetta", "rosetta/tests/python_to_js/input.py", "--to", "js"]

# Redirect stdout to capture the output
import io
from contextlib import redirect_stdout

f = io.StringIO()
with redirect_stdout(f):
    main()

output = f.getvalue()
print("--- Emitted JavaScript ---")
print(output)

# Save the output
with open("rosetta/tests/python_to_js/output.js", "w") as out:
    out.write(output)
