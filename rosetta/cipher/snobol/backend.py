from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class SnobolBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "snobol"

    @property
    def style_guide(self) -> str:
        return "Standard SNOBOL4"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, SNOBOLStatement):
            label = node.label if node.label else ""
            content = f" {self._emit_raw(node.content)}" if node.content else ""
            transfer = f" {self._emit_raw(node.transfer)}" if node.transfer else ""
            return f"{label}{content}{transfer}"

        if isinstance(node, PatternMatchStatement):
            subj = self._emit_raw(node.subject)
            pat = self._emit_raw(node.pattern)
            repl = f" = {self._emit_raw(node.replacement)}" if node.replacement else ""
            return f"{subj} {pat}{repl}"

        if isinstance(node, SNOBOLTransfer):
            if node.unconditional_label:
                return f":({node.unconditional_label})"
            res = ":"
            if node.success_label:
                res += f"S({node.success_label})"
            if node.failure_label:
                res += f"F({node.failure_label})"
            return res

        if isinstance(node, Assignment):
            return f"{self._emit_raw(node.target)} = {self._emit_raw(node.value)}"

        if isinstance(node, BinaryExpression):
            if node.operator == " ":
                return f"{self._emit_raw(node.left)} {self._emit_raw(node.right)}"
            if node.operator in ["|", ".", "$"]:
                 return f"{self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)}"
            return f"{self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)}"

        if isinstance(node, ArrayAccess):
            indices = ", ".join(self._emit_raw(idx) for idx in node.index)
            return f"{self._emit_raw(node.object)}<{indices}>"

        if isinstance(node, UnaryExpression):
            return f"{node.operator}{self._emit_raw(node.argument)}"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                 return f"'{node.value}'"
            return str(node.value)

        if isinstance(node, CallExpression):
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            return f"{self._emit_raw(node.callee)}({args})"

        if isinstance(node, VariableDeclaration):
            # SNOBOL doesn't have declarations, but we can treat it as an assignment
            if node.initializer:
                return f"{node.name} = {self._emit_raw(node.initializer)}"
            return ""

        return f"* Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        return self.emit(node, 0).strip()
