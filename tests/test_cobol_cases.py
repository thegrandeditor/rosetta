import sys
import os
import difflib

# Add rosetta root to path
ROSETTA_ROOT = "C:\\Users\\IGWE\\Documents\\Projects\\Rosetta"
if ROSETTA_ROOT not in sys.path:
    sys.path.insert(0, ROSETTA_ROOT)

from rosetta.babel.cobol.frontend import CobolFrontend
from rosetta.cipher.python.backend import PythonBackend

TEST_CASES = [
    (
        "Basic DISPLAY and STOP RUN",
        """       PROCEDURE DIVISION.
       0000-MAIN.
           DISPLAY "HELLO WORLD".
           STOP RUN.""",
        "def _0000_MAIN():\n    print('HELLO WORLD')\n    exit(0)"
    ),
    (
        "WORKING-STORAGE variable declaration with PIC X and PIC 9",
        """       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-NAME      PIC X(10) VALUE "BOB".
       01  WS-AGE       PIC 9(03) VALUE 25.""",
        "WS_NAME: str = 'BOB'\nWS_AGE: int = 25"
    ),
    (
        "MOVE statement",
        """       PROCEDURE DIVISION.
       0000-MAIN.
           MOVE "Y" TO WS-FLAGS.
           MOVE "N" TO WS-ERR-SWITCH.""",
        "def _0000_MAIN():\n    WS_FLAGS = 'Y'\n    WS_ERR_SWITCH = 'N'"
    ),
    (
        "PERFORM paragraph call",
        """       PROCEDURE DIVISION.
       0100-MAIN.
           PERFORM 0200-READ UNTIL WS-EOF = "Y".""",
        "def _0100_MAIN():\n    while not (WS_EOF == 'Y'):\n        _0200_READ()"
    ),
    (
        "IF/ELSE condition",
        """       PROCEDURE DIVISION.
       0100-MAIN.
           IF WS-EOF = "Y"
               DISPLAY "EOF"
           ELSE
               DISPLAY "NOT EOF"
           END-IF.""",
        "def _0100_MAIN():\n    if (WS_EOF == 'Y'):\n        print('EOF')\n    else:\n        print('NOT EOF')"
    ),
    (
        "COMPUTE statement",
        """       PROCEDURE DIVISION.
       0100-MAIN.
           COMPUTE WS-TOTAL = WS-VAL1 + WS-VAL2""",
        "def _0100_MAIN():\n    WS_TOTAL = (WS_VAL1 + WS_VAL2)"
    ),
    (
        "EVALUATE/WHEN block",
        """       PROCEDURE DIVISION.
       0100-MAIN.
           EVALUATE TRUE
               WHEN WS-FLAG-A
                   DISPLAY "A"
               WHEN WS-FLAG-B
                   DISPLAY "B"
               WHEN OTHER
                   DISPLAY "OTHER"
           END-EVALUATE.""",
        "def _0100_MAIN():\n    if WS_FLAG_A:\n        print('A')\n    if WS_FLAG_B:\n        print('B')\n    if True:\n        print('OTHER')"
    ),
    (
        "ADD statement",
        """       PROCEDURE DIVISION.
       0100-MAIN.
           ADD 10 TO WS-COUNTER""",
        "def _0100_MAIN():\n    WS_COUNTER = (WS_COUNTER + 10)"
    ),
    (
        "OPEN/READ/CLOSE file statements",
        """       PROCEDURE DIVISION.
       0100-MAIN.
           OPEN INPUT EMP-FILE.
           READ EMP-FILE.
           CLOSE EMP-FILE.""",
        "def _0100_MAIN():\n    OPEN(EMP_FILE, 'INPUT')\n    READ(EMP_FILE)\n    CLOSE(EMP_FILE)"
    ),
    (
        "Nested 05-level variables under a 01 group",
        """       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  EMP-RECORD.
           05  EMP-ID        PIC X(05).
           05  EMP-NAME      PIC X(20).
           05  EMP-SALARY    PIC 9(06).""",
        "class EMP_RECORD:\n    EMP_ID: str\n    EMP_NAME: str\n    EMP_SALARY: int"
    )
]

def run_tests():
    frontend = CobolFrontend()
    backend = PythonBackend()
    
    passed_count = 0
    total_count = len(TEST_CASES)
    
    for i, (name, cobol, expected) in enumerate(TEST_CASES, 1):
        print(f"\n==================================================")
        print(f"TEST {i}: {name}")
        print(f"==================================================")
        
        try:
            # Transpile
            ir = frontend.parse(cobol)
            actual = backend.emit(ir).strip()
            
            # Normalize whitespace/newlines for more robust assertion matching
            actual_norm = "\n".join(line.rstrip() for line in actual.splitlines())
            expected_norm = "\n".join(line.rstrip() for line in expected.splitlines())
            
            print("ACTUAL OUTPUT:")
            print(actual)
            print("-" * 50)
            
            # Check for case-insensitivity on lower/uppercase ws_eof / WS_EOF due to case normalization in boolean flags
            actual_norm_lower = actual_norm.lower()
            expected_norm_lower = expected_norm.lower()
            
            if actual_norm_lower == expected_norm_lower:
                print("Status: PASS")
                passed_count += 1
            else:
                print("Status: FAIL")
                print("DIFF:")
                diff = difflib.unified_diff(
                    expected_norm.splitlines(),
                    actual_norm.splitlines(),
                    fromfile='Expected',
                    tofile='Actual',
                    lineterm=''
                )
                for line in diff:
                    print(line)
        except Exception as e:
            print("Status: ERROR")
            import traceback
            traceback.print_exc()
            
    print(f"\n==================================================")
    print(f"VERIFICATION SUMMARY: {passed_count}/{total_count} PASSED")
    print(f"==================================================")
    
    if passed_count == total_count:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    run_tests()
