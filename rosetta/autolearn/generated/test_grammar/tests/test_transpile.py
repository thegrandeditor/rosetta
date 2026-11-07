from rosetta.ir.nodes import *
from rosetta.autolearn.generated.test_grammar.cipher.backend import Test_grammarBackend

def test_draft_backend():
    backend = Test_grammarBackend()
    prog = Program(body=[
        VariableDeclaration(name="x", initializer=Literal(value=42)),
        FunctionDeclaration(name="hello", params=[], body=[
            ReturnStatement(value=Identifier(name="x"))
        ])
    ])
    code = backend.emit(prog)
    assert "let x = 42;" in code
    assert "fn hello()" in code
    print("Draft backend test passed!")

if __name__ == "__main__":
    test_draft_backend()
