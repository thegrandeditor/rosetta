from rosetta.ir.nodes import *

class Test_grammarBackend:
    @property
    def language_id(self) -> str:
        return "test_grammar"

    def emit(self, node: RosettaNode) -> str:
        if isinstance(node, Program):
            return "\n".join(self.emit(n) for n in node.body)
        elif isinstance(node, VariableDeclaration):
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"let {node.name}{init};"
        elif isinstance(node, Assignment):
            return f"{self.emit(node.target)} = {self.emit(node.value)};"
        elif isinstance(node, FunctionDeclaration):
            body = "\n".join("  " + self.emit(n) for n in node.body)
            return f"fn {node.name}() {{\n{body}\n}}"
        elif isinstance(node, IfStatement):
            conseq = "\n".join("  " + self.emit(n) for n in node.consequent)
            alt = ""
            if node.alternate:
                alt_body = "\n".join("  " + self.emit(n) for n in node.alternate)
                alt = f" else {{\n{alt_body}\n}}"
            return f"if ({self.emit(node.condition)}) {{\n{conseq}\n}}{alt}"
        elif isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            return str(node.value)
        elif isinstance(node, Identifier):
            return node.name
        elif isinstance(node, CallExpression):
            args = ", ".join(self.emit(a) for a in node.args)
            return f"{self.emit(node.callee)}({args})"
        elif isinstance(node, ReturnStatement):
            val = f" {self.emit(node.value)}" if node.value else ""
            return f"return{val};"
        return f"// Unhandled node: {type(node).__name__}"
