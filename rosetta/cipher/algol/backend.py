from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class AlgolBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "algol"

    @property
    def style_guide(self) -> str:
        return "ALGOL 60"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            body = "\n".join(self.emit(stmt, indent+1) for stmt in node.body)
            return f"BEGIN\n{body}\nEND"

        if isinstance(node, VariableDeclaration):
            return f"{padding}{node.type_hint or 'REAL'} {node.name}"

        if isinstance(node, FunctionDeclaration):
            params = "(" + ", ".join(p.name for p in node.params) + ")" if node.params else ""
            header = f"{padding}PROCEDURE {node.name}{params};"
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{header}\n{padding}BEGIN\n{body}\n{padding}END"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} := {self._emit_raw(node.value)}"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            if callee == "print":
                return f"{padding}OUTSTRING(1, {args})"
            return f"{padding}{callee}({args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            return str(node.value).upper() if isinstance(node.value, bool) else str(node.value)

        if isinstance(node, BinaryExpression):
            op_map = {
                "==": "=",
                "!=": "<>",
            }
            op = op_map.get(node.operator.lower(), node.operator)
            return f"({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = "\n".join(self.emit(s, indent+1) for s in node.consequent)
            res = f"{padding}IF {cond} THEN\n{consequent}"
            if node.alternate:
                alternate = "\n".join(self.emit(s, indent+1) for s in node.alternate)
                res += f"\n{padding}ELSE\n{alternate}"
            return res

        if isinstance(node, ForLoop):
             if isinstance(node.initializer, Assignment) and isinstance(node.initializer.target, Identifier):
                var = node.initializer.target.name
                start = self._emit_raw(node.initializer.value)
                step = "1"
                if isinstance(node.increment, Assignment) and isinstance(node.increment.value, BinaryExpression):
                    step = self._emit_raw(node.increment.value.right)
                limit = "???"
                if isinstance(node.condition, BinaryExpression):
                    limit = self._emit_raw(node.condition.right)
                
                body = "\n".join(self.emit(s, indent+1) for s in node.body)
                return f"{padding}FOR {var} := {start} STEP {step} UNTIL {limit} DO\n{padding}BEGIN\n{body}\n{padding}END"
             return f"{padding}COMMENT Unsupported ForLoop;"

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{padding}WHILE {cond} DO\n{padding}BEGIN\n{body}\n{padding}END"

        if isinstance(node, list):
            return "\n".join(self.emit(s, indent) for s in node)

        return f"{padding}COMMENT Unknown node: {type(node).__name__};"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip()

AlgolBackend = AlgolBackend
