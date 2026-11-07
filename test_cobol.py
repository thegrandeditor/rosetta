from rosetta.babel.cobol.frontend import CobolAntlrFrontend
from rosetta.cipher.python.backend import PythonBackend

code = "       DATA DIVISION.\n       WORKING-STORAGE SECTION.\n       01 GREETING PIC X(12) VALUE 'HELLO ROSETTA'.\n       PROCEDURE DIVISION.\n           DISPLAY GREETING.\n           STOP RUN."

frontend = CobolAntlrFrontend()
ir = frontend.parse(code)
print('Nodes:', len(ir.body))
for n in ir.body:
    print(repr(n))
print('---OUTPUT---')
backend = PythonBackend()
print(backend.emit(ir))
