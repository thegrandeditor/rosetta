from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class BasicBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "basic"

    @property
    def style_guide(self) -> str:
        return "Classic BASIC"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            # For classic BASIC, we might need line numbers
            res = []
            line_no = 10
            for stmt in node.body:
                if isinstance(stmt, Label):
                    # Use existing label if it's an integer
                    try:
                        line_no = int(stmt.name)
                        res.append(f"{line_no} REM Label: {stmt.name}")
                    except ValueError:
                        res.append(f"REM Label: {stmt.name}")
                else:
                    res.append(f"{line_no} {self.emit(stmt, 0).strip()}")
                    line_no += 10
            return "\n".join(res)

        if isinstance(node, VariableDeclaration):
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}LET {node.name}{init}"

        if isinstance(node, Assignment):
            return f"{padding}LET {self._emit_raw(node.target)} = {self._emit_raw(node.value)}"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            if callee == "print":
                return f"{padding}PRINT {args}"
            if callee == "input":
                return f"{padding}INPUT {args}"
            if callee.startswith("GOSUB_"):
                return f"{padding}GOSUB {callee[6:]}"
            return f"{padding}{callee}({args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            return str(node.value)

        if isinstance(node, BinaryExpression):
            op_map = {
                "==": "=",
                "!=": "<>",
                "and": "AND",
                "or": "OR",
                "**": "^"
            }
            op = op_map.get(node.operator.lower(), node.operator)
            return f"({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            then_stmt = self._emit_raw(node.consequent[0]) if node.consequent else "REM"
            res = f"{padding}IF {cond} THEN {then_stmt}"
            if node.alternate:
                else_stmt = self._emit_raw(node.alternate[0])
                res += f" ELSE {else_stmt}"
            return res

        if isinstance(node, ForLoop):
            if isinstance(node.initializer, Assignment) and isinstance(node.initializer.target, Identifier):
                var = node.initializer.target.name
                start = self._emit_raw(node.initializer.value)
                end = "???"
                if isinstance(node.condition, BinaryExpression):
                    end = self._emit_raw(node.condition.right)
                
                body = "\n".join(self.emit(stmt, indent) for stmt in node.body)
                return f"{padding}FOR {var} = {start} TO {end}\n{body}\n{padding}NEXT {var}"
            return f"{padding}REM Unsupported ForLoop"

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return f"{padding}WHILE {cond}\n{body}\n{padding}WEND"

        if isinstance(node, GotoStatement):
            return f"{padding}GOTO {node.label}"

        if isinstance(node, Label):
            return f"{padding}REM Label: {node.name}"

        return f"{padding}REM Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip()

BasicBackend = BasicBackend
