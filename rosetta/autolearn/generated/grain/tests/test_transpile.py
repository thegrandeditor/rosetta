from rosetta.ir.nodes import *
from rosetta.autolearn.generated.grain.cipher.backend import GrainBackend

def test_draft_backend():
    backend = GrainBackend()
    prog = Program(body=[
        VariableDeclaration(name="x", initializer=Literal(value=42)),
        FunctionDeclaration(name="hello", params=[], body=[
            ReturnStatement(value=Identifier(name="x"))
        ])
    ])
    code = backend.emit(prog)
    assert f"{backend.VAR_KW} x = 42;" in code
    assert f"{backend.FN_KW} hello()" in code
    print("Draft backend test passed!")

if __name__ == "__main__":
    test_draft_backend()
