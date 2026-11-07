from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class MLBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "ml"

    @property
    def style_guide(self) -> str:
        return "Standard ML"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, MLValDeclaration):
            init = self._emit_raw(node.initializer)
            if node.pattern:
                return f"{padding}val {self._emit_raw(node.pattern)} = {init}"
            return f"{padding}val {node.name} = {init}"

        if isinstance(node, MLFunDeclaration):
            params = " ".join(p.name for p in node.params)
            # Find the ReturnStatement in body
            body_expr = "()"
            for stmt in node.body:
                if isinstance(stmt, ReturnStatement):
                    body_expr = self._emit_raw(stmt.value)
                    break
            return f"{padding}fun {node.name} {params} = {body_expr}"

        if isinstance(node, MLDataTypeDeclaration):
            constrs = " | ".join(self._emit_raw(c) for c in node.constructors)
            return f"{padding}datatype {node.name} = {constrs}"

        if isinstance(node, MLConstructor):
            types = " of " + " * ".join(node.types) if node.types else ""
            return f"{node.name}{types}"

        if isinstance(node, MLLetExpression):
            bindings = "\n".join(self.emit(b, indent + 1) for b in node.bindings)
            body = self.emit(node.body, indent + 1).strip()
            return f"{padding}let\n{bindings}\nin\n  {body}\nend"

        if isinstance(node, MLCaseExpression):
            expr = self._emit_raw(node.expression)
            branches = "\n".join(f"{padding}  | {self._emit_raw(b.pattern)} => {self._emit_raw(b.body)}" for b in node.branches)
            # First branch uses 'of'
            branches = branches.replace("  | ", "  ", 1)
            return f"{padding}case {expr} of\n{branches}"

        if isinstance(node, BinaryExpression):
            return f"({self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)})"

        if isinstance(node, CallExpression):
            args = " ".join(self._emit_raw(arg) for arg in node.args)
            return f"({self._emit_raw(node.callee)} {args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if node.value is True: return "true"
            if node.value is False: return "false"
            if isinstance(node.value, list) and not node.value: return "[]"
            if isinstance(node.value, str): return f'"{node.value}"'
            return str(node.value)

        return f"(* Unknown node: {type(node).__name__} *)"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        return self.emit(node, 0).strip()
