from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *
from typing import Optional

class SwiftBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "swift"

    @property
    def style_guide(self) -> str:
        return "Swift API Design Guidelines"

    def _map_type(self, type_str: Optional[str]) -> str:
        mapping = {
            "int": "Int",
            "float": "Double",
            "string": "String",
            "bool": "Bool",
            "list": "[Any]",
            "any": "Any"
        }
        return mapping.get(type_str, type_str or "Any")

    def emit(self, node: RosettaNode) -> str:
        if node is None: return ""

        if isinstance(node, Program):
            return "\n".join(self.emit(stmt) for stmt in node.body)

        if isinstance(node, VariableDeclaration):
            kw = "let" if node.is_const else "var"
            type_anno = f": {self._map_type(node.type_hint)}" if node.type_hint else ""
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"{kw} {node.name}{type_anno}{init}"

        if isinstance(node, Assignment):
            return f"{self.emit(node.target)} = {self.emit(node.value)}"

        if isinstance(node, FunctionDeclaration):
            params = ", ".join(self.emit(p) for p in node.params)
            ret = f" -> {self._map_type(node.return_type)}" if node.return_type and node.return_type != "void" else ""
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            async_kw = "async " if node.is_async else ""
            return f"{async_kw}func {node.name}({params}){ret} {{\n    {body}\n}}"

        if isinstance(node, MethodDeclaration):
            params = ", ".join(self.emit(p) for p in node.params if p.name != "self")
            ret = f" -> {self._map_type(node.return_type)}" if node.return_type and node.return_type != "void" else ""
            body = "\n        ".join(self.emit(stmt) for stmt in node.body)
            static_kw = "static " if node.is_static else ""
            async_kw = "async " if node.is_async else ""
            return f"{static_kw}{async_kw}func {node.name}({params}){ret} {{\n        {body}\n    }}"

        if isinstance(node, Parameter):
            type_anno = self._map_type(node.type_hint)
            return f"_ {node.name}: {type_anno}"

        if isinstance(node, ClassDeclaration):
            inheritance = f": {', '.join(node.bases)}" if node.bases else ""
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"class {node.name}{inheritance} {{\n    {body}\n}}"

        if isinstance(node, ReturnStatement):
            return f"return {self.emit(node.value)}" if node.value else "return"

        if isinstance(node, CallExpression):
            callee = self.emit(node.callee)
            args = ", ".join(self.emit(arg) for arg in node.args)
            return f"{callee}({args})"

        if isinstance(node, Identifier):
            if node.name == "print": return "print"
            if node.name == "self": return "self"
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, bool): return str(node.value).lower()
            if isinstance(node.value, str): return f"\"{node.value}\""
            if isinstance(node.value, list):
                return "[" + ", ".join(self.emit(x) if isinstance(x, RosettaNode) else str(x) for x in node.value) + "]"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({self.emit(node.left)} {node.operator} {self.emit(node.right)})"

        if isinstance(node, UnaryExpression):
            return f"{node.operator}{self.emit(node.argument)}"

        if isinstance(node, IfStatement):
            consequent = "\n    ".join(self.emit(stmt) for stmt in node.consequent)
            code = f"if {self.emit(node.condition)} {{\n    {consequent}\n}}"
            if node.alternate:
                alternate = "\n    ".join(self.emit(stmt) for stmt in node.alternate)
                code += f" else {{\n    {alternate}\n}}"
            return code

        if isinstance(node, MemberAccess):
            return f"{self.emit(node.object)}.{node.member}"

        if isinstance(node, AwaitExpression):
            return f"await {self.emit(node.argument)}"

        if isinstance(node, MapExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.map {{ {param} in {body} }}"

        if isinstance(node, FilterExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.filter {{ {param} in {body} }}"

        if isinstance(node, ListComprehension):
            gen = node.generators[0]
            iterable = self.emit(gen.iterable)
            target = gen.target.name
            expr = self.emit(node.expression)
            res = iterable
            for if_cond in gen.ifs:
                res += f".filter {{ {target} in {self.emit(if_cond)} }}"
            res += f".map {{ {target} in {expr} }}"
            return res

        if isinstance(node, YieldExpression):
            return f"/* yield */ {self.emit(node.argument) if node.argument else ''}"

        return f"/* Unknown node: {type(node).__name__} */"
