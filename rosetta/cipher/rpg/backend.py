from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class RPGBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "rpg"

    @property
    def style_guide(self) -> str:
        return "Fixed-format RPG IV"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, RPGOperation):
            f1 = self._emit_raw(node.factor1).ljust(14) if node.factor1 else " " * 14
            op = node.opcode.ljust(10)
            f2 = self._emit_raw(node.factor2).ljust(14) if node.factor2 else " " * 14
            res = self._emit_raw(node.result).ljust(14) if node.result else " " * 14
            ind = "".join(node.indicators).ljust(7)
            return f"     C{f1}{op}{f2}{res}{ind}"

        if isinstance(node, Assignment):
            # Map Assignment to MOVEL or EVAL
            target = self._emit_raw(node.target).ljust(14)
            value = self._emit_raw(node.value).ljust(14)
            return f"     C              MOVEL     {value}{target}"

        if isinstance(node, BinaryExpression):
            if node.operator == "+":
                 f1 = self._emit_raw(node.left).ljust(14)
                 f2 = self._emit_raw(node.right).ljust(14)
                 return f"     C{f1}ADD       {f2}" # Result is tricky here without target
            return f"(* Op {node.operator} *)"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str): return f"'{node.value}'"
            return str(node.value)

        return f"     * Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        return self.emit(node, 0).strip()
