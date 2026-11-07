from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class Modula2Backend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "modula2"

    @property
    def style_guide(self) -> str:
        return "PIM4 Standard"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, ModuleDeclaration):
            header = f"{padding}MODULE {node.name};"
            # Imports/Exports not in IR yet
            body = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            footer = f"{padding}END {node.name}."
            return f"{header}\n{body}\n{footer}"

        if isinstance(node, FunctionDeclaration):
            params = f"({', '.join(p.name + ': ' + (p.type_hint or 'INTEGER') for p in node.params)})" if node.params else ""
            ret = f": {node.return_type}" if node.return_type else ""
            header = f"{padding}PROCEDURE {node.name}{params}{ret};"
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            footer = f"{padding}END {node.name};"
            return f"{header}\n{padding}BEGIN\n{body}\n{footer}"

        if isinstance(node, VariableDeclaration):
            kw = "CONST" if node.is_const else "VAR"
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            type_str = f": {node.type_hint or 'INTEGER'}" if not node.is_const else ""
            return f"{padding}{kw} {node.name}{type_str}{init};"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} := {self._emit_raw(node.value)};"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = f"({', '.join(self._emit_raw(a) for a in node.args)})" if node.args else ""
            return f"{padding}{callee}{args};"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = "\n".join(self.emit(stmt, indent + 1) for stmt in node.consequent)
            res = f"{padding}IF {cond} THEN\n{consequent}"
            if node.alternate:
                alternate = "\n".join(self.emit(stmt, indent + 1) for stmt in node.alternate)
                res += f"\n{padding}ELSE\n{alternate}"
            res += f"\n{padding}END;"
            return res

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{padding}WHILE {cond} DO\n{body}\n{padding}END;"

        if isinstance(node, ForLoop):
             # FOR i := start TO end DO ... END;
             var = "i"
             start = "1"
             end = "10"
             if isinstance(node.initializer, Assignment) and isinstance(node.initializer.target, Identifier):
                 var = node.initializer.target.name
                 start = self._emit_raw(node.initializer.value)
             if isinstance(node.condition, BinaryExpression):
                 end = self._emit_raw(node.condition.right)
             body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
             return f"{padding}FOR {var} := {start} TO {end} DO\n{body}\n{padding}END;"

        if isinstance(node, ReturnStatement):
            val = f" {self._emit_raw(node.value)}" if node.value else ""
            return f"{padding}RETURN{val};"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str): return f"'{node.value}'"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            op = node.operator
            if op == "==": op = "="
            if op == "!=": op = "#"
            return f"({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        return f"{padding}(* Unknown node: {type(node).__name__} *)"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        return self.emit(node, 0).strip().strip(';')
