from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class ZigBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "zig"

    @property
    def style_guide(self) -> str:
        return "Zig Idiomatic Style"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""

        indent_str = "    " * indent

        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)

        if isinstance(node, StructDeclaration):
            # Zig structs are typically values assigned to constants: const S = struct { ... };
            prefix = "packed " if node.metadata.get("is_packed") else ("extern " if node.metadata.get("is_extern") else "")
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.fields)
            return f"{prefix}struct {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, VariableDeclaration):
            # Check if initializer is a StructDeclaration. If so, don't put pub on struct definition itself
            is_struct = isinstance(node.initializer, StructDeclaration)
            decl_kw = "const" if node.is_const else "var"
            type_hint = f": {node.type_hint}" if node.type_hint else ""
            init_str = f" = {self.emit(node.initializer, indent).strip()}" if node.initializer else ""
            return f"{indent_str}pub {decl_kw} {node.name}{type_hint}{init_str};"

        if isinstance(node, Assignment):
            return f"{indent_str}{self.emit(node.target)} = {self.emit(node.value)};"

        if isinstance(node, FunctionDeclaration):
            inline_str = "inline " if node.metadata.get("is_inline") else ""
            params_str = ", ".join(self.emit(p) for p in node.params)
            
            # error union type
            ret_type = node.return_type or "void"
            if "!" not in ret_type and ret_type != "void":
                ret_type = "anyerror!" + ret_type
                
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}pub {inline_str}fn {node.name}({params_str}) {ret_type} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, Parameter):
            type_hint = node.type_hint or "anytype"
            return f"{node.name}: {type_hint}"

        if isinstance(node, ReturnStatement):
            val_str = f" {self.emit(node.value)}" if node.value else ""
            return f"{indent_str}return{val_str};"

        if isinstance(node, DeferStatement):
            defer_kw = "errdefer" if node.is_errdefer else "defer"
            # Single statement or block
            if len(node.body) == 1:
                return f"{indent_str}{defer_kw} {self.emit(node.body[0], 0).strip()}"
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}{defer_kw} {{\n{body_str}\n{indent_str}}};"

        if isinstance(node, ComptimeExpression):
            return f"comptime {self.emit(node.expression, 0).strip()}"

        if isinstance(node, IfStatement):
            cond = self.emit(node.condition)
            conseq = "\n".join(self.emit(stmt, indent + 1) for stmt in node.consequent)
            alt_str = ""
            if node.alternate:
                alt_body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.alternate)
                alt_str = f" else {{\n{alt_body}\n{indent_str}}}"
            return f"{indent_str}if ({cond}) {{\n{conseq}\n{indent_str}}}{alt_str}"

        if isinstance(node, WhileLoop):
            inline_str = "inline " if node.metadata.get("is_inline") else ""
            cond = self.emit(node.condition)
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}{inline_str}while ({cond}) {{\n{body}\n{indent_str}}}"

        if isinstance(node, ForInLoop):
            inline_str = "inline " if node.metadata.get("is_inline") else ""
            iter_name = self.emit(node.iterator)
            iterable = self.emit(node.iterable)
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}{inline_str}for ({iterable}) |{iter_name}| {{\n{body}\n{indent_str}}}"

        if isinstance(node, ForLoop):
            # Fallback
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}for (0..) |_| {{\n{body}\n{indent_str}}}"

        if isinstance(node, BinaryExpression):
            return f"{self.emit(node.left)} {node.operator} {self.emit(node.right)}"

        if isinstance(node, UnaryExpression):
            return f"{node.operator}{self.emit(node.argument)}"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            if isinstance(node.value, bool):
                return "true" if node.value else "false"
            return str(node.value)

        if isinstance(node, CallExpression):
            callee_str = self.emit(node.callee)
            args_str = ", ".join(self.emit(arg) for arg in node.args)
            
            # handle 'try' as special prefix in Zig
            if callee_str == "try":
                return f"try {args_str}"
                
            return f"{callee_str}({args_str})"

        return f"{indent_str}// Unknown node: {type(node).__name__}"
