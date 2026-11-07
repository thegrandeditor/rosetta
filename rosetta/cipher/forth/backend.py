from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class ForthBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "forth"

    @property
    def style_guide(self) -> str:
        return "Standard Forth"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if isinstance(node, Program):
            return " ".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, ForthWordDefinition):
            body = " ".join(self.emit(stmt, indent) for stmt in node.body)
            return f": {node.name} {body} ;"

        if isinstance(node, ForthStackOp):
            return node.operation

        if isinstance(node, Literal):
            return str(node.value)

        if isinstance(node, CallExpression):
            return self._emit_raw(node.callee)

        if isinstance(node, IfStatement):
            # condition in Forth is already on stack
            consequent = " ".join(self.emit(stmt, indent) for stmt in node.consequent)
            alternate = f" ELSE {' '.join(self.emit(stmt, indent) for stmt in node.alternate)}" if node.alternate else ""
            return f"IF {consequent}{alternate} THEN"

        if isinstance(node, WhileLoop):
            body = " ".join(self.emit(stmt, indent) for stmt in node.body)
            return f"BEGIN {body} UNTIL" # Note: UNTIL pops from stack

        if isinstance(node, BinaryExpression):
            # Map high-level binary ops back to stack ops
            left = self.emit(node.left)
            right = self.emit(node.right)
            op = node.operator
            if op == "+": return f"{left} {right} +"
            if op == "-": return f"{left} {right} -"
            if op == "*": return f"{left} {right} *"
            if op == "/": return f"{left} {right} /"
            return f"{left} {right} {op}"

        return f"( Unknown node: {type(node).__name__} )"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        return self.emit(node, 0).strip()
