from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class RubyBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "ruby"

    @property
    def style_guide(self) -> str:
        return "Ruby Style Guide"

    def emit(self, node: RosettaNode) -> str:
        if node is None: return ""
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt) for stmt in node.body)
        
        if isinstance(node, VariableDeclaration):
            if node.initializer:
                return f"{node.name} = {self.emit(node.initializer)}"
            return ""

        if isinstance(node, Assignment):
            return f"{self.emit(node.target)} = {self.emit(node.value)}"

        if isinstance(node, FunctionDeclaration):
            params = ", ".join(p.name for p in node.params)
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"def {node.name}({params})\n  {body}\nend"

        if isinstance(node, MethodDeclaration):
            params = ", ".join(p.name for p in node.params if p.name != "self")
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"def {node.name}({params})\n    {body}\n  end"

        if isinstance(node, ClassDeclaration):
            extends = f" < {node.bases[0]}" if node.bases else ""
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"class {node.name}{extends}\n  {body}\nend"

        if isinstance(node, ReturnStatement):
            return f"return {self.emit(node.value)}" if node.value else "return"

        if isinstance(node, CallExpression):
            callee = self.emit(node.callee)
            args = ", ".join(self.emit(arg) for arg in node.args)
            return f"{callee}({args})"

        if isinstance(node, Identifier):
            if node.name == "print": return "puts"
            if node.name == "self": return "self"
            return node.name

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
            consequent = "\n  ".join(self.emit(stmt) for stmt in node.consequent)
            code = f"if {self.emit(node.condition)}\n  {consequent}"
            if node.alternate:
                alternate = "\n  ".join(self.emit(stmt) for stmt in node.alternate)
                code += f"\nelse\n  {alternate}"
            code += "\nend"
            return code

        if isinstance(node, WhileLoop):
            cond = self.emit(node.condition)
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"while {cond}\n  {body}\nend"

        if isinstance(node, ForInLoop):
            it = self.emit(node.iterator)
            coll = self.emit(node.iterable)
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"for {it} in {coll} do\n  {body}\nend"

        if isinstance(node, EventDeclaration):
            params = ", ".join(self.emit(p) for p in node.params)
            return f"# Event: {node.name}({params})"

        if isinstance(node, EmitStatement):
            call_str = self.emit(node.event_call)
            return f"# emit {call_str}"

        if isinstance(node, MemberAccess):
            return f"{self.emit(node.object)}.{node.member}"

        if isinstance(node, YieldExpression):
            return f"yield {self.emit(node.argument) if node.argument else ''}"

        if isinstance(node, AwaitExpression):
            # Ruby doesn't have native await in core, often uses Fibers or gems.
            # For now, we'll just emit the argument call.
            return self.emit(node.argument)

        if isinstance(node, MapExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.map {{ |{param}| {body} }}"

        if isinstance(node, FilterExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.select {{ |{param}| {body} }}"

        if isinstance(node, ListComprehension):
            gen = node.generators[0]
            iterable = self.emit(gen.iterable)
            target = gen.target.name
            expr = self.emit(node.expression)
            res = f"{iterable}"
            for if_cond in gen.ifs:
                res += f".select {{ |{target}| {self.emit(if_cond)} }}"
            res += f".map {{ |{target}| {expr} }}"
            return res

        return f"# Unknown node: {type(node).__name__}"
