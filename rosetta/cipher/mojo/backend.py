from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class MojoBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "mojo"

    @property
    def style_guide(self) -> str:
        return "Mojo Idiomatic Style"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""

        indent_str = "    " * indent

        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)

        if isinstance(node, MojoStructDeclaration):
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.fields)
            return f"{indent_str}struct {node.name}:\n{body_str}"

        if isinstance(node, StructDeclaration):
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.fields)
            return f"{indent_str}struct {node.name}:\n{body_str}"

        if isinstance(node, VariableDeclaration):
            decl_kw = "let" if node.is_const else "var"
            type_hint = f": {node.type_hint}" if node.type_hint else ""
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"{indent_str}{decl_kw} {node.name}{type_hint}{init}"

        if isinstance(node, Assignment):
            return f"{indent_str}{self.emit(node.target)} = {self.emit(node.value)}"

        if isinstance(node, FunctionDeclaration):
            fn_kw = "fn" if node.metadata.get("is_mojo_fn", True) else "def"
            params_str = ", ".join(self.emit(p) for p in node.params)
            
            ret_str = f" -> {node.return_type}" if node.return_type else ""
            
            decs = "".join(f"{indent_str}@{self.emit(d)}\n" for d in node.decorators)
            
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            if not body_str.strip():
                body_str = f"{indent_str}    pass"
                
            return f"{decs}{indent_str}{fn_kw} {node.name}({params_str}){ret_str}:\n{body_str}"

        if isinstance(node, Parameter):
            mode = node.metadata.get("mojo_mode", "")
            mode_str = f"{mode} " if mode else ""
            type_hint = f": {node.type_hint}" if node.type_hint else ""
            default = f" = {self.emit(node.default_value)}" if node.default_value else ""
            return f"{mode_str}{node.name}{type_hint}{default}"

        if isinstance(node, ReturnStatement):
            val_str = f" {self.emit(node.value)}" if node.value else ""
            return f"{indent_str}return{val_str}"

        if isinstance(node, IfStatement):
            cond = self.emit(node.condition)
            conseq = "\n".join(self.emit(stmt, indent + 1) for stmt in node.consequent)
            alt_str = ""
            if node.alternate:
                alt_body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.alternate)
                alt_str = f"\n{indent_str}else:\n{alt_body}"
            return f"{indent_str}if {cond}:\n{conseq}{alt_str}"

        if isinstance(node, WhileLoop):
            cond = self.emit(node.condition)
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}while {cond}:\n{body}"

        if isinstance(node, ForLoop):
            # Mojo has standard for loops like Python
            init = self.emit(node.initializer).strip() if node.initializer else "i"
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}for {init}:\n{body}"

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
                return "True" if node.value else "False"
            return str(node.value)

        if isinstance(node, CallExpression):
            callee_str = self.emit(node.callee)
            args_str = ", ".join(self.emit(arg) for arg in node.args)
            return f"{callee_str}({args_str})"

        return f"{indent_str}# Unknown node: {type(node).__name__}"
