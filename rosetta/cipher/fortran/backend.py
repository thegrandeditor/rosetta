from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class FortranBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "fortran"

    @property
    def style_guide(self) -> str:
        return "Fortran 90"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, ArrayDeclaration):
            type_map = {
                "INTEGER": "INTEGER",
                "REAL": "REAL",
                "DOUBLE PRECISION": "DOUBLE PRECISION",
                "LOGICAL": "LOGICAL",
                "CHARACTER": "CHARACTER(LEN=*)",
                "int": "INTEGER",
                "float": "REAL",
                "bool": "LOGICAL",
                "str": "CHARACTER(LEN=*)"
            }
            ftype = type_map.get(node.type_hint.upper() if node.type_hint else "", "REAL")
            dims = ", ".join(self._emit_raw(d) for d in node.dimensions)
            return f"{padding}{ftype} :: {node.name}({dims})"

        if isinstance(node, VariableDeclaration):
            type_map = {
                "INTEGER": "INTEGER",
                "REAL": "REAL",
                "DOUBLE PRECISION": "DOUBLE PRECISION",
                "LOGICAL": "LOGICAL",
                "CHARACTER": "CHARACTER(LEN=*)",
                "int": "INTEGER",
                "float": "REAL",
                "bool": "LOGICAL",
                "str": "CHARACTER(LEN=*)"
            }
            ftype = type_map.get(node.type_hint.upper() if node.type_hint else "", "REAL")
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}{ftype} :: {node.name}{init}"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} = {self._emit_raw(node.value)}"

        if isinstance(node, ArrayAccess):
            indices = ", ".join(self._emit_raw(idx) for idx in node.index)
            return f"{self._emit_raw(node.object)}({indices})"

        if isinstance(node, GlobalBlock):
            name_str = f"/{node.name}/ " if node.name else ""
            members_str = ", ".join(m.name for m in node.members)
            return f"{padding}COMMON {name_str}{members_str}"

        if isinstance(node, FormatDeclaration):
            items_str = ", ".join(str(item) for item in node.items)
            return f"{node.label} FORMAT({items_str})"

        if isinstance(node, FunctionDeclaration):
            is_func = node.return_type is not None
            keyword = "FUNCTION" if is_func else "SUBROUTINE"
            params = ", ".join(p.name for p in node.params)
            header = f"{padding}{keyword} {node.name}({params})"
            if is_func:
                header = f"{padding}{node.return_type} {header}"
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            footer = f"{padding}END {keyword} {node.name}"
            return f"{header}\n{body_str}\n{footer}"

        if isinstance(node, ReturnStatement):
            return f"{padding}RETURN"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            if callee == "print":
                return f"{padding}WRITE(*,*) {args}"
            if callee == "write":
                # Assuming first arg is unit, second is format
                if len(node.args) >= 2:
                    unit = self._emit_raw(node.args[0])
                    fmt = self._emit_raw(node.args[1])
                    remaining = ", ".join(self._emit_raw(arg) for arg in node.args[2:])
                    return f"{padding}WRITE({unit}, {fmt}) {remaining}"
                return f"{padding}WRITE(*,*) {args}"
            
            if indent > 0:
                return f"{padding}CALL {callee}({args})"
            return f"{callee}({args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            if isinstance(node.value, bool):
                return ".TRUE." if node.value else ".FALSE."
            return str(node.value)

        if isinstance(node, BinaryExpression):
            op_map = {
                "==": "==",
                "!=": "/=",
                "<": "<",
                "<=": "<=",
                ">": ">",
                ">=": ">=",
                "+": "+",
                "-": "-",
                "*": "*",
                "/": "/",
                "**": "**",
                "and": ".AND.",
                "or": ".OR.",
                ":": ":"
            }
            op = op_map.get(node.operator.lower(), node.operator)
            return f"({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        if isinstance(node, UnaryExpression):
            op_map = {
                "not": ".NOT.",
                "-": "-"
            }
            op = op_map.get(node.operator.lower(), node.operator)
            return f"{op}({self._emit_raw(node.argument)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            body_indent = indent + 1
            consequent = "\n".join(self.emit(stmt, body_indent) for stmt in node.consequent)
            res = f"{padding}IF ({cond}) THEN\n{consequent}"
            
            curr_alt = node.alternate
            while curr_alt:
                if isinstance(curr_alt, list) and len(curr_alt) == 1 and isinstance(curr_alt[0], IfStatement):
                    # This is an ELSE IF
                    else_if_node = curr_alt[0]
                    else_if_cond = self._emit_raw(else_if_node.condition)
                    else_if_cons = "\n".join(self.emit(stmt, body_indent) for stmt in else_if_node.consequent)
                    res += f"\n{padding}ELSE IF ({else_if_cond}) THEN\n{else_if_cons}"
                    curr_alt = else_if_node.alternate
                elif isinstance(curr_alt, list):
                    # This is the final ELSE
                    alternate = "\n".join(self.emit(stmt, body_indent) for stmt in curr_alt)
                    res += f"\n{padding}ELSE\n{alternate}"
                    curr_alt = None
                else:
                    curr_alt = None
            
            res += f"\n{padding}END IF"
            return res

        if isinstance(node, ForLoop):
            if isinstance(node.initializer, Assignment) and isinstance(node.initializer.target, Identifier):
                var = node.initializer.target.name
                start = self._emit_raw(node.initializer.value)
                end = "???"
                if isinstance(node.condition, BinaryExpression):
                    end = self._emit_raw(node.condition.right)
                
                body_indent = indent + 1
                body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
                return f"{padding}DO {var} = {start}, {end}\n{body_str}\n{padding}END DO"
            
            return f"{padding}! Unsupported ForLoop"

        if isinstance(node, Label):
            return f"{node.name} CONTINUE"

        if isinstance(node, GotoStatement):
            return f"{padding}GOTO {node.label}"

        # Default for expressions as statements
        if isinstance(node, (CallExpression, BinaryExpression, Literal, Identifier, ArrayAccess)):
             return f"{padding}{self._emit_raw(node)}"

        return f"{padding}! Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip()

# For discovery
FortranBackend = FortranBackend
