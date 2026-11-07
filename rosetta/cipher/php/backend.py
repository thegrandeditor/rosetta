from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class PHPBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "php"

    @property
    def style_guide(self) -> str:
        return "PSR-12"

    def _fmt_name(self, name: str) -> str:
        if name in ["this", "self"]: return "$this"
        return f"${name}"

    def emit(self, node: RosettaNode) -> str:
        if node is None: return ""

        if isinstance(node, Program):
            return "<?php\n\n" + "\n".join(self.emit(stmt) for stmt in node.body)

        if isinstance(node, VariableDeclaration):
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"{self._fmt_name(node.name)}{init};"

        if isinstance(node, Assignment):
            return f"{self.emit(node.target)} = {self.emit(node.value)};"

        if isinstance(node, FunctionDeclaration):
            params = ", ".join(f"{self.emit(p)}" for p in node.params)
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"function {node.name}({params}) {{\n    {body}\n}}"

        if isinstance(node, MethodDeclaration):
            visibility = "public "
            static_kw = "static " if node.is_static else ""
            params = ", ".join(f"{self.emit(p)}" for p in node.params if p.name != "self")
            body = "\n        ".join(self.emit(stmt) for stmt in node.body)
            return f"{visibility}{static_kw}function {node.name}({params}) {{\n        {body}\n    }}"

        if isinstance(node, Parameter):
            type_hint = f"{node.type_hint} " if node.type_hint and node.type_hint != "any" else ""
            return f"{type_hint}{self._fmt_name(node.name)}"

        if isinstance(node, ClassDeclaration):
            extends = f" extends {node.bases[0]}" if node.bases else ""
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"class {node.name}{extends} {{\n    {body}\n}}"

        if isinstance(node, ReturnStatement):
            return f"return {self.emit(node.value)};" if node.value else "return;"

        if isinstance(node, CallExpression):
            callee = self.emit(node.callee)
            if callee.startswith("$") and "(" not in callee:
                # If it's a variable being called, we need to handle it or it might be a method call
                pass
            args = ", ".join(self.emit(arg) for arg in node.args)
            return f"{callee}({args})"

        if isinstance(node, Identifier):
            if node.name == "print": return "print"
            if node.name == "self": return "$this"
            # Classes and functions don't get $ prefix in PHP, but variables do.
            # For now, assume if it's not a known class-like name, it's a variable.
            if node.name[0].isupper(): return node.name
            return self._fmt_name(node.name)

        if isinstance(node, Literal):
            if isinstance(node.value, bool): return str(node.value).lower()
            if isinstance(node.value, str): return f"'{node.value}'"
            if isinstance(node.value, list):
                return "[" + ", ".join(self.emit(x) if isinstance(x, RosettaNode) else str(x) for x in node.value) + "]"
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

        if isinstance(node, WhileLoop):
            cond = self.emit(node.condition)
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"while ({cond}) {{\n    {body}\n}}"

        if isinstance(node, ForInLoop):
            it = self.emit(node.iterator).lstrip("$")
            coll = self.emit(node.iterable)
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"foreach ({coll} as ${it}) {{\n    {body}\n}}"

        if isinstance(node, EventDeclaration):
            params = ", ".join(self.emit(p) for p in node.params)
            return f"// Event: {node.name}({params})"

        if isinstance(node, EmitStatement):
            call_str = self.emit(node.event_call)
            return f"// emit {call_str};"

        if isinstance(node, MemberAccess):
            obj = self.emit(node.object)
            return f"{obj}->{node.member}"

        if isinstance(node, YieldExpression):
            return f"yield {self.emit(node.argument) if node.argument else ''}"

        if isinstance(node, AwaitExpression):
            # PHP 8.1+ has Fibers, but no native 'await' keyword like JS.
            return self.emit(node.argument)

        if isinstance(node, MapExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"array_map(fn(${param}) => {body}, {self.emit(node.collection)})"

        if isinstance(node, FilterExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"array_filter({self.emit(node.collection)}, fn(${param}) => {body})"

        if isinstance(node, ListComprehension):
            # Simplified: convert to array_map/filter
            gen = node.generators[0]
            iterable = self.emit(gen.iterable)
            target = gen.target.name
            expr = self.emit(node.expression)
            res = iterable
            for if_cond in gen.ifs:
                res = f"array_filter({res}, fn(${target}) => {self.emit(if_cond)})"
            return f"array_map(fn(${target}) => {expr}, {res})"

        return f"// Unknown node: {type(node).__name__}"
