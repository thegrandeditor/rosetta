from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class EiffelBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "eiffel"

    @property
    def style_guide(self) -> str:
        return "Eiffel Software Style"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, ContractedClass):
            bases = "inherit\n" + "\n".join(f"{padding}  {b}" for b in node.bases) if node.bases else ""
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            inv = "invariant\n" + "\n".join(f"{padding}  {self._emit_raw(i)}" for i in node.invariant) if node.invariant else ""
            return f"{padding}class {node.name}\n{bases}\nfeature\n{body}\n{inv}\nend"

        if isinstance(node, ContractedFunction):
            params = "(" + "; ".join(f"{p.name}: {p.type_hint}" for p in node.params) + ")" if node.params else ""
            ret = f": {node.return_type}" if node.return_type else ""
            req = "require\n" + "\n".join(f"{padding}  {self._emit_raw(r)}" for r in node.contract.require) if node.contract and node.contract.require else ""
            ens = "ensure\n" + "\n".join(f"{padding}  {self._emit_raw(e)}" for e in node.contract.ensure) if node.contract and node.contract.ensure else ""
            body = "do\n" + "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{padding}{node.name} {params}{ret}\n{req}\n{body}\n{ens}\n{padding}end"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} := {self._emit_raw(node.value)}"

        if isinstance(node, BinaryExpression):
            op = node.operator
            if op == "==": op = "="
            if op == "!=": op = "/="
            return f"({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            consequent = "\n".join(self.emit(stmt, indent + 1) for stmt in node.consequent)
            alternate = f"\n{padding}else\n" + "\n".join(self.emit(stmt, indent + 1) for stmt in node.alternate) if node.alternate else ""
            return f"{padding}if {self._emit_raw(node.condition)} then\n{consequent}{alternate}\n{padding}end"

        if isinstance(node, WhileLoop):
            # Eiffel loop is from ... until ... loop ... end
            # We map WhileLoop(cond) to until not cond
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{padding}from\n{padding}until\n{padding}  not ({self._emit_raw(node.condition)})\n{padding}loop\n{body}\n{padding}end"

        if isinstance(node, CallExpression):
            args = "(" + ", ".join(self._emit_raw(arg) for arg in node.args) + ")" if node.args else ""
            return f"{padding}{self._emit_raw(node.callee)}{args}"

        if isinstance(node, MemberAccess):
            return f"{self._emit_raw(node.object)}.{node.member}"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str): return f"\"{node.value}\""
            return str(node.value)

        return f"{padding}-- Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        return self.emit(node, 0).strip()
