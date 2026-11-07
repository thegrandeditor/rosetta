
from rosetta.ir.nodes import *
from rosetta.hermes.passes.type_inference import TypeInferencePass

def test_type_inference_basic():
    # x = 10
    # y = "hello"
    # z = x
    # def f(a: int): return a + 1
    # b = f(x)
    program = Program(body=[
        Assignment(target=Identifier(name="x"), value=Literal(value=10)),
        Assignment(target=Identifier(name="y"), value=Literal(value="hello")),
        VariableDeclaration(name="z", initializer=Identifier(name="x")),
        FunctionDeclaration(
            name="add_one",
            params=[Parameter(name="a", type_hint="int")],
            body=[ReturnStatement(value=BinaryExpression(left=Identifier(name="a"), operator="+", right=Literal(value=1)))]
        ),
        VariableDeclaration(name="b", initializer=CallExpression(callee=Identifier(name="add_one"), args=[Identifier(name="x")]))
    ])

    ti_pass = TypeInferencePass()
    inferred_ir = ti_pass.transform(program)

    # Check results
    x_decl = inferred_ir.body[0]
    assert isinstance(x_decl, VariableDeclaration)
    assert x_decl.type_hint == "int"

    y_decl = inferred_ir.body[1]
    assert isinstance(y_decl, VariableDeclaration)
    assert y_decl.type_hint == "string"

    z_decl = inferred_ir.body[2]
    assert isinstance(z_decl, VariableDeclaration)
    assert z_decl.type_hint == "int"

    func_decl = inferred_ir.body[3]
    assert func_decl.return_type == "int"

    b_decl = inferred_ir.body[4]
    assert b_decl.type_hint == "int"

    print("Type inference test passed!")

if __name__ == "__main__":
    test_type_inference_basic()
