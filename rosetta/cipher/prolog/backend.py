from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class PrologBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "prolog"

    @property
    def style_guide(self) -> str:
        return "ISO Prolog"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)

        if isinstance(node, Fact):
            pred = getattr(node, 'predicate', getattr(node, 'name', 'fact'))
            args = ", ".join(self._emit_raw(arg) for arg in node.terms)
            return f"{pred}({args})."

        if isinstance(node, PrologRule):
            return "\n".join(self.emit(c, indent) for c in node.clauses)

        if isinstance(node, PrologClause):
            head = self._emit_raw(node.head)
            body = ", ".join(self._emit_raw(b) for b in node.body)
            return f"{head} :- {body}."

        if isinstance(node, Query):
            terms = ", ".join(self._emit_raw(t) for t in node.terms)
            return f"?- {terms}."

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            return f"{callee}({args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, list):
                return "[" + ", ".join(self._emit_raw(v) if isinstance(v, RosettaNode) else str(v) for v in node.value) + "]"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"{self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)}"

        return f"{padding}% Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        if isinstance(node, Fact):
            pred = getattr(node, 'predicate', getattr(node, 'name', 'fact'))
            args = ", ".join(self._emit_raw(arg) for arg in node.terms)
            return f"{pred}({args})"
        res = self.emit(node, 0)
        return res.strip().strip('.')

PrologBackend = PrologBackend
