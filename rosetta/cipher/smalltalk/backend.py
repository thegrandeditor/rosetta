from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class SmalltalkBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "smalltalk"

    @property
    def style_guide(self) -> str:
        return "ANSI Smalltalk"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)

        if isinstance(node, ClassDeclaration):
            super_cls = node.bases[0] if node.bases else "Object"
            header = f"{super_cls} subclass: #{node.name} instanceVariableNames: ''"
            body = "\n".join(self.emit(m, indent+1) for m in node.body)
            return f"{header}\n{body}"

        if isinstance(node, MethodDeclaration):
            params = " ".join(f"{p.name}: {p.name}" for p in node.params) # Simplified
            header = f"{node.name} {params}"
            body = "\n  ".join(self.emit(s, 0).strip() for s in node.body)
            return f"\n{header}\n  [{body}]"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} := {self._emit_raw(node.value)}."

        if isinstance(node, CallExpression):
            receiver = self._emit_raw(node.receiver) if hasattr(node, 'receiver') and node.receiver else "Transcript"
            callee = self._emit_raw(node.callee)
            args = " ".join(self._emit_raw(arg) for arg in node.args)
            if callee == "print":
                 return f"{padding}Transcript show: {args}; cr."
            return f"{padding}{receiver} {callee} {args}"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f"'{node.value}'"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = " ".join(self._emit_raw(s) for s in node.consequent)
            res = f"{padding}{cond} ifTrue: [ {consequent} ]"
            if node.alternate:
                alternate = " ".join(self._emit_raw(s) for s in node.alternate)
                res += f" ifFalse: [ {alternate} ]"
            return res + "."

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = " ".join(self._emit_raw(s) for s in node.body)
            return f"{padding}[ {cond} ] whileTrue: [ {body} ]."

        if isinstance(node, LambdaExpression):
            params = " ".join(f":{p.name}" for p in node.params)
            sep = " | " if params else ""
            body = " ".join(self._emit_raw(s) for s in (node.body if isinstance(node.body, list) else [node.body]))
            return f"[ {params}{sep}{body} ]"

        return f"{padding}\" Unknown node: {type(node).__name__} \""

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip().strip('.')

SmalltalkBackend = SmalltalkBackend
