from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class PascalBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "pascal"

    @property
    def style_guide(self) -> str:
        return "Standard Pascal"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            body = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return f"PROGRAM ROSETTA_PROG;\n{body}\nBEGIN\nEND."

        if isinstance(node, VariableDeclaration):
            return f"{padding}{node.name} : {node.type_hint or 'Integer'};"

        if isinstance(node, ArrayDeclaration):
            dims = ", ".join(self._emit_raw(d) for d in node.dimensions)
            return f"{padding}{node.name} : ARRAY [{dims}] OF {node.type_hint or 'Integer'};"

        if isinstance(node, RecordDeclaration):
            fields = "\n".join(self.emit(f, indent+1) for f in node.fields)
            return f"{padding}{node.name} : RECORD\n{fields}\n{padding}END;"

        if isinstance(node, WithStatement):
            objs = ", ".join(self._emit_raw(o) for o in node.objects)
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{padding}WITH {objs} DO\n{padding}BEGIN\n{body}\n{padding}END;"

        if isinstance(node, FunctionDeclaration):
            kw = "FUNCTION" if node.return_type else "PROCEDURE"
            params = "; ".join(f"{p.name} : {p.type_hint or 'Integer'}" for p in node.params)
            ret = f" : {node.return_type}" if node.return_type else ""
            header = f"{padding}{kw} {node.name}({params}){ret};"
            
            # Pascal has declarations before BEGIN
            decls = []
            stmts = []
            for stmt in node.body:
                if isinstance(stmt, VariableDeclaration):
                    decls.append(stmt)
                else:
                    stmts.append(stmt)
            
            var_part = ""
            if decls:
                var_part = f"{padding}VAR\n" + "\n".join(self.emit(d, indent+1) for d in decls) + "\n"
            
            body_str = "\n".join(self.emit(s, indent+1) for s in stmts)
            return f"{header}\n{var_part}{padding}BEGIN\n{body_str}\n{padding}END;"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} := {self._emit_raw(node.value)};"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            if callee == "print":
                return f"{padding}WRITELN({args});"
            return f"{padding}{callee}({args});"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f"'{node.value}'"
            return str(node.value).upper() if isinstance(node.value, bool) else str(node.value)

        if isinstance(node, BinaryExpression):
            op_map = {
                "==": "=",
                "!=": "<>",
                "and": "AND",
                "or": "OR"
            }
            op = op_map.get(node.operator.lower(), node.operator)
            return f"({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = "\n".join(self.emit(s, indent+1) for s in node.consequent)
            res = f"{padding}IF {cond} THEN\n{padding}BEGIN\n{consequent}\n{padding}END"
            if node.alternate:
                alternate = "\n".join(self.emit(s, indent+1) for s in node.alternate)
                res += f"\n{padding}ELSE\n{padding}BEGIN\n{alternate}\n{padding}END"
            return res + ";"

        if isinstance(node, ForLoop):
            if isinstance(node.initializer, Assignment) and isinstance(node.initializer.target, Identifier):
                var = node.initializer.target.name
                start = self._emit_raw(node.initializer.value)
                end = "???"
                if isinstance(node.condition, BinaryExpression):
                    end = self._emit_raw(node.condition.right)
                body = "\n".join(self.emit(s, indent+1) for s in node.body)
                return f"{padding}FOR {var} := {start} TO {end} DO\n{padding}BEGIN\n{body}\n{padding}END;"
            return f"{padding}{{ Unsupported ForLoop }}"

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{padding}WHILE {cond} DO\n{padding}BEGIN\n{body}\n{padding}END;"

        if isinstance(node, RecordAccess):
            return f"{self._emit_raw(node.object)}.{node.field}"

        return f"{padding}{{ Unknown node: {type(node).__name__} }}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip().strip(';')

PascalBackend = PascalBackend
