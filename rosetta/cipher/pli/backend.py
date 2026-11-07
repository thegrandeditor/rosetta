from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class PLIBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "pli"

    @property
    def style_guide(self) -> str:
        return "Standard PL/I"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "  " * indent
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, FunctionDeclaration):
            params = f"({', '.join(p.name for p in node.params)})" if node.params else ""
            options = " OPTIONS(MAIN)" if node.name.upper() == "HELLO" else "" # Heuristic
            header = f"{padding}{node.name}: PROCEDURE{params}{options};"
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            footer = f"{padding}END {node.name};"
            return f"{header}\n{body}\n{footer}"

        if isinstance(node, VariableDeclaration):
            attr = f" {node.type_hint}" if node.type_hint else ""
            init = f" INIT({self._emit_raw(node.initializer)})" if node.initializer else ""
            return f"{padding}DECLARE {node.name}{attr}{init};"

        if isinstance(node, ArrayDeclaration):
            dims = f"({', '.join(self._emit_raw(d) for d in node.dimensions)})"
            attr = f" {node.type_hint}" if node.type_hint else ""
            init = f" INIT({self._emit_raw(node.initializer)})" if node.initializer else ""
            return f"{padding}DECLARE {node.name}{dims}{attr}{init};"

        if isinstance(node, TaskDeclaration):
            return f"{padding}DECLARE {node.name} TASK;"

        if isinstance(node, EntryDeclaration):
            params = f"({', '.join(p.name for p in node.params)})" if node.params else ""
            ret = f" RETURNS({node.return_type})" if node.return_type else ""
            return f"{padding}{node.name}: ENTRY{params}{ret};"

        if isinstance(node, MemoryAllocation):
            type_str = f" {node.type_hint}" if node.type_hint else ""
            return f"{padding}ALLOCATE{type_str};"

        if isinstance(node, MemoryFree):
            return f"{padding}FREE {self._emit_raw(node.argument)};"

        if isinstance(node, OnCondition):
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{padding}ON {node.condition}\n{body}"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} = {self._emit_raw(node.value)};"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            if callee in ["put", "get"]:
                return f"{padding}{callee.upper()} LIST({', '.join(self._emit_raw(a) for a in node.args)});"
            args = f"({', '.join(self._emit_raw(a) for a in node.args)})" if node.args else ""
            return f"{padding}CALL {callee}{args};"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = "\n".join(self.emit(stmt, indent + 1) for stmt in node.consequent)
            res = f"{padding}IF {cond} THEN\n{consequent}"
            if node.alternate:
                alternate = "\n".join(self.emit(stmt, indent + 1) for stmt in node.alternate)
                res += f"\n{padding}ELSE\n{alternate}"
            return res

        if isinstance(node, ForLoop):
            init = self._emit_raw(node.initializer)
            # Extract var and start from init (Assignment)
            if isinstance(node.initializer, Assignment) and isinstance(node.initializer.target, Identifier):
                var = node.initializer.target.name
                start = self._emit_raw(node.initializer.value)
                # Extract end from condition (BinaryExpression)
                end = "???"
                if isinstance(node.condition, BinaryExpression):
                    end = self._emit_raw(node.condition.right)
                
                body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
                return f"{padding}DO {var} = {start} TO {end};\n{body}\n{padding}END;"
            return f"{padding}/* Complex DO loop */"

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{padding}DO WHILE({cond});\n{body}\n{padding}END;"

        if isinstance(node, ReturnStatement):
            val = f" ({self._emit_raw(node.value)})" if node.value else ""
            return f"{padding}RETURN{val};"

        if isinstance(node, Label):
            return f"{node.name}:"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str): return f"'{node.value}'"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)})"

        return f"{padding}/* Unknown node: {type(node).__name__} */"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        return self.emit(node, 0).strip().strip(';')
