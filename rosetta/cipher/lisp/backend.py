from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class LispBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "lisp"

    @property
    def style_guide(self) -> str:
        return "Common Lisp"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, FunctionDeclaration):
            params = " ".join(p.name for p in node.params)
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{padding}(DEFUN {node.name} ({params})\n{body})"

        if isinstance(node, VariableDeclaration):
            return f"{padding}(LET (({node.name} {self._emit_raw(node.initializer)})))"

        if isinstance(node, Assignment):
            return f"{padding}(SETQ {self._emit_raw(node.target)} {self._emit_raw(node.value)})"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = " ".join(self._emit_raw(arg) for arg in node.args)
            if callee == "print":
                 return f"{padding}(PRINT {args})"
            return f"{padding}({callee} {args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({node.operator} {self._emit_raw(node.left)} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = " ".join(self._emit_raw(s) for s in node.consequent)
            alternate = " ".join(self._emit_raw(s) for s in node.alternate) if node.alternate else ""
            return f"{padding}(IF {cond} {consequent} {alternate})"

        if isinstance(node, MacroDeclaration):
            params = " ".join(p.name for p in node.params)
            body = self._emit_raw(node.body)
            return f"{padding}(DEFMACRO {node.name} ({params}) {body})"

        return f"{padding}; Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip()

LispBackend = LispBackend
