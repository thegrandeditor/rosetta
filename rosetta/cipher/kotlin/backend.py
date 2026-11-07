from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *
from typing import Optional

class KotlinBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "kotlin"

    @property
    def style_guide(self) -> str:
        return "Kotlin Coding Conventions"

    def _map_type(self, type_str: Optional[str]) -> str:
        mapping = {
            "int": "Int",
            "float": "Double",
            "string": "String",
            "bool": "Boolean",
            "list": "List<Any>",
            "any": "Any?"
        }
        return mapping.get(type_str, type_str or "Any?")

    def emit(self, node: RosettaNode) -> str:
        if node is None: return ""

        if isinstance(node, Program):
            return "\n".join(self.emit(stmt) for stmt in node.body)

        if isinstance(node, VariableDeclaration):
            kw = "val" if node.is_const else "var"
            type_anno = f": {self._map_type(node.type_hint)}" if node.type_hint else ""
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"{kw} {node.name}{type_anno}{init}"

        if isinstance(node, Assignment):
            return f"{self.emit(node.target)} = {self.emit(node.value)}"

        if isinstance(node, FunctionDeclaration):
            params = ", ".join(self.emit(p) for p in node.params)
            ret = f": {self._map_type(node.return_type)}" if node.return_type and node.return_type != "void" else ""
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            suspend_kw = "suspend " if node.is_async else ""
            return f"{suspend_kw}fun {node.name}({params}){ret} {{\n    {body}\n}}"

        if isinstance(node, MethodDeclaration):
            params = ", ".join(self.emit(p) for p in node.params if p.name != "self")
            ret = f": {self._map_type(node.return_type)}" if node.return_type and node.return_type != "void" else ""
            body = "\n        ".join(self.emit(stmt) for stmt in node.body)
            suspend_kw = "suspend " if node.is_async else ""
            return f"{suspend_kw}fun {node.name}({params}){ret} {{\n        {body}\n    }}"

        if isinstance(node, Parameter):
            type_anno = self._map_type(node.type_hint)
            return f"{node.name}: {type_anno}"

        if isinstance(node, ClassDeclaration):
            inheritance = f" : {node.bases[0]}()" if node.bases else ""
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"class {node.name}{inheritance} {{\n    {body}\n}}"

        if isinstance(node, ReturnStatement):
            return f"return {self.emit(node.value)}" if node.value else "return"

        if isinstance(node, CallExpression):
            callee = self.emit(node.callee)
            args = ", ".join(self.emit(arg) for arg in node.args)
            return f"{callee}({args})"

        if isinstance(node, Identifier):
            if node.name == "print": return "println"
            if node.name == "self": return "this"
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, bool): return str(node.value).lower()
            if isinstance(node.value, str): return f"\"{node.value}\""
            if isinstance(node.value, list):
                return "listOf(" + ", ".join(self.emit(x) if isinstance(x, RosettaNode) else str(x) for x in node.value) + ")"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({self.emit(node.left)} {node.operator} {self.emit(node.right)})"

        if isinstance(node, UnaryExpression):
            return f"{node.operator}{self.emit(node.argument)}"

        if isinstance(node, IfStatement):
            consequent = "\n    ".join(self.emit(stmt) for stmt in node.consequent)
            code = f"if ({self.emit(node.condition)}) {{\n    {consequent}\n}}"
            if node.alternate:
                alternate = "\n    ".join(self.emit(stmt) for stmt in node.alternate)
                code += f" else {{\n    {alternate}\n}}"
            return code

        if isinstance(node, MemberAccess):
            return f"{self.emit(node.object)}.{node.member}"

        if isinstance(node, AwaitExpression):
            # In Kotlin coroutines, you don't use 'await' keyword for suspend functions, you just call them.
            return self.emit(node.argument)

        if isinstance(node, MapExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.map {{ {param} -> {body} }}"

        if isinstance(node, FilterExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.filter {{ {param} -> {body} }}"

        if isinstance(node, ListComprehension):
            gen = node.generators[0]
            iterable = self.emit(gen.iterable)
            target = gen.target.name
            expr = self.emit(node.expression)
            res = iterable
            for if_cond in gen.ifs:
                res += f".filter {{ {target} -> {self.emit(if_cond)} }}"
            res += f".map {{ {target} -> {expr} }}"
            return res

        if isinstance(node, YieldExpression):
            return f"yield({self.emit(node.argument) if node.argument else ''})"

        return f"/* Unknown node: {type(node).__name__} */"
