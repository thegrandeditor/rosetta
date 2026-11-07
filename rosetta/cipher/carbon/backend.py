from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class CarbonBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "carbon"

    @property
    def style_guide(self) -> str:
        return "Carbon Style Guide"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""

        indent_str = "    " * indent

        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)

        if isinstance(node, VariableDeclaration):
            decl_kw = "let" if node.is_const else "var"
            type_str = f": {node.type_hint}" if node.type_hint else ""
            init_str = f" = {self.emit(node.initializer).strip()}" if node.initializer else ""
            return f"{indent_str}{decl_kw} {node.name}{type_str}{init_str};"

        if isinstance(node, Assignment):
            return f"{indent_str}{self.emit(node.target).strip()} = {self.emit(node.value).strip()};"

        if isinstance(node, FunctionDeclaration):
            params_str = ", ".join(self.emit(p).strip() for p in node.params)
            ret_str = f" -> {node.return_type}" if node.return_type else ""
            
            body_lines = []
            for stmt in node.body:
                body_lines.append(self.emit(stmt, indent + 1))
            body_str = "\n".join(body_lines)
            
            return f"{indent_str}fn {node.name}({params_str}){ret_str} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, Parameter):
            type_str = f": {node.type_hint}" if node.type_hint else ""
            return f"{node.name}{type_str}"

        if isinstance(node, ReturnStatement):
            val = f" {self.emit(node.value).strip()}" if node.value else ""
            return f"{indent_str}return{val};"

        if isinstance(node, CallExpression):
            callee_str = self.emit(node.callee).strip()
            args_str = ", ".join(self.emit(arg).strip() for arg in node.args)
            return f"{indent_str}{callee_str}({args_str})"

        if isinstance(node, IfStatement):
            cond = self.emit(node.condition).strip()
            conseq = "\n".join(self.emit(stmt, indent + 1) for stmt in node.consequent)
            alt_str = ""
            if node.alternate:
                alt_body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.alternate)
                alt_str = f" else {{\n{alt_body}\n{indent_str}}}"
            return f"{indent_str}if ({cond}) {{\n{conseq}\n{indent_str}}}{alt_str}"

        if isinstance(node, WhileLoop):
            cond = self.emit(node.condition).strip()
            body = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}while ({cond}) {{\n{body}\n{indent_str}}}"

        if isinstance(node, BinaryExpression):
            return f"{indent_str}{self.emit(node.left).strip()} {node.operator} {self.emit(node.right).strip()}"

        if isinstance(node, UnaryExpression):
            return f"{indent_str}{node.operator}{self.emit(node.argument).strip()}"

        if isinstance(node, Identifier):
            return f"{indent_str}{node.name}"

        if isinstance(node, Literal):
            if isinstance(node.value, list):
                return f"{indent_str}[" + ", ".join(self.emit(x).strip() for x in node.value) + "]"
            if isinstance(node.value, str):
                return f'{indent_str}"{node.value}"'
            if isinstance(node.value, bool):
                return f"{indent_str}true" if node.value else f"{indent_str}false"
            return f"{indent_str}{str(node.value)}"

        if isinstance(node, ClassDeclaration):
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}class {node.name} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, InterfaceDeclaration):
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}interface {node.name} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, ImplDeclaration):
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}impl {node.target_type} as {node.interface_name} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, ModuleDeclaration):
            body_str = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            pkg_stmt = f"{indent_str}package {node.name} api;\n" if node.name else ""
            if body_str:
                return f"{pkg_stmt}{body_str}"
            return f"{pkg_stmt}"

        if isinstance(node, ImportStatement):
            return f"{indent_str}import {node.module_name or ''};"

        if isinstance(node, MLCaseExpression):
            expr = self.emit(node.expression).strip()
            branches = "\n".join(self.emit(b, indent + 1) for b in node.branches)
            return f"{indent_str}match ({expr}) {{\n{branches}\n{indent_str}}}"

        if isinstance(node, MLCaseBranch):
            pattern = self.emit(node.pattern).strip()
            if isinstance(node.body, list):
                body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
                if len(node.body) > 1 or (len(node.body) == 1 and not isinstance(node.body[0], Program)):
                    body_str = f"{{\n{body_str}\n{indent_str}}}"
                else:
                    body_str = body_str.strip()
            else:
                body_str = self.emit(node.body).strip()
            return f"{indent_str}case {pattern} => {body_str}"

        return f"{indent_str}// Unknown node: {type(node).__name__}"
