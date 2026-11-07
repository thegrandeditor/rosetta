from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class GoBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "go"

    @property
    def style_guide(self) -> str:
        return "Gofmt"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""
        padding = "\t" * indent
        
        if isinstance(node, Program):
            header = "package main\n\nimport (\n\t\"fmt\"\n)\n\n"
            body = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return header + body
        
        if isinstance(node, VariableDeclaration):
            go_type = self._map_type(node.type_hint)
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}var {node.name} {go_type}{init}"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} = {self._emit_raw(node.value)}"

        if isinstance(node, FunctionDeclaration):
            params = ", ".join(self._emit_param(p) for p in node.params)
            ret = f" {self._map_type(node.return_type)}" if node.return_type else ""
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}func {node.name}({params}){ret} {{\n{body_str}\n{padding}}}"

        if isinstance(node, (StructDeclaration, MojoStructDeclaration)):
            fields = [f"\t{f.name} {self._map_type(f.type_hint)}" for f in node.fields]
            return f"{padding}type {node.name} struct {{\n" + "\n".join(fields) + f"\n{padding}}}\n\n"

        if isinstance(node, ClassDeclaration):
            # Struct for state
            fields = []
            for stmt in node.body:
                if isinstance(stmt, VariableDeclaration):
                    fields.append(f"\t{stmt.name} {self._map_type(stmt.type_hint)}")
            
            struct_str = f"{padding}type {node.name} struct {{\n" + "\n".join(fields) + f"\n{padding}}}\n\n"
            
            # Receiver functions
            methods = []
            for stmt in node.body:
                if isinstance(stmt, MethodDeclaration):
                    # func (self *ClassName) MethodName(params) ret { ... }
                    params_list = []
                    for p in stmt.params:
                        if p.name != "self":
                            params_list.append(self._emit_param(p))
                    params = ", ".join(params_list)
                    ret = f" {self._map_type(stmt.return_type)}" if stmt.return_type else ""
                    
                    body_indent = indent + 1
                    body_str = "\n".join(self.emit(stmt, body_indent) for stmt in stmt.body)
                    
                    receiver = f"({stmt.params[0].name} *{node.name})" if stmt.params and stmt.params[0].name == "self" else ""
                    methods.append(f"{padding}func {receiver} {stmt.name}({params}){ret} {{\n{body_str}\n{padding}}}")
            
            return struct_str + "\n\n".join(methods)

        if isinstance(node, ReturnStatement):
            val = f" {self._emit_raw(node.value)}" if node.value else ""
            return f"{padding}return{val}"

        if isinstance(node, CallExpression):
            callee_name = self._emit_raw(node.callee)
            if callee_name == "print":
                args = ", ".join(self._emit_raw(arg) for arg in node.args)
                return f"{padding}fmt.Println({args})"
            
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            return f"{padding}{callee_name}({args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            if isinstance(node.value, bool):
                return str(node.value).lower()
            if isinstance(node.value, list):
                elements = ", ".join(self._emit_raw(x) for x in node.value)
                return f"[]interface{{}}{{{elements}}}"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)})"

        if isinstance(node, UnaryExpression):
            return f"{node.operator}{self._emit_raw(node.argument)}"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            body_indent = indent + 1
            consequent = "\n".join(self.emit(stmt, body_indent) for stmt in node.consequent)
            res = f"{padding}if {cond} {{\n{consequent}\n{padding}}}"
            if node.alternate:
                alternate = "\n".join(self.emit(stmt, body_indent) for stmt in node.alternate)
                res += f" else {{\n{alternate}\n{padding}}}"
            return res

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}for {cond} {{\n{body}\n{padding}}}"

        if isinstance(node, ForInLoop):
            it = self._emit_raw(node.iterator)
            coll = self._emit_raw(node.iterable)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}for _, {it} := range {coll} {{\n{body}\n{padding}}}"

        if isinstance(node, ForLoop):
            init = self._emit_raw(node.initializer)
            cond = self._emit_raw(node.condition)
            inc = self._emit_raw(node.increment)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}for {init}; {cond}; {inc} {{\n{body}\n{padding}}}"

        if isinstance(node, EventDeclaration):
            params = ", ".join(f"{p.name} {self._map_type(p.type_hint)}" for p in node.params)
            return f"{padding}// Event: {node.name}({params})"

        if isinstance(node, EmitStatement):
            call_str = self._emit_raw(node.event_call)
            return f"{padding}// emit {call_str}"

        if isinstance(node, MemberAccess):
            return f"{self._emit_raw(node.object)}.{node.member}"

        if isinstance(node, MapExpression):
            return f"map({self._emit_raw(node.collection)}, {self._emit_raw(node.function)})"

        if isinstance(node, FilterExpression):
            return f"filter({self._emit_raw(node.collection)}, {self._emit_raw(node.function)})"

        if isinstance(node, LambdaExpression):
            params = ", ".join(self._emit_param(p) for p in node.params)
            # Simplified: assuming single expression body
            return f"func({params}) interface{{}} {{ return {self._emit_raw(node.body)} }}"

        if isinstance(node, AwaitExpression):
            return f"await({self._emit_raw(node.argument)})"

        if isinstance(node, YieldExpression):
            return f"yield({self._emit_raw(node.argument) if node.argument else ''})"

        if isinstance(node, MemoryAllocation):
            return f"make([]byte, {self._emit_raw(node.size)})"

        if isinstance(node, MemoryFree):
            return f"{padding}// [GC managed: freed {self._emit_raw(node.argument)}]"

        if isinstance(node, Dereference):
            return f"*{self._emit_raw(node.argument)}"

        return f"{padding}// Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip()

    def _map_type(self, type_hint: str) -> str:
        mapping = {
            "int": "int",
            "float": "float64",
            "str": "string",
            "bool": "bool",
            "list": "[]interface{}",
            "None": "",
            "void": ""
        }
        if not type_hint: return ""
        return mapping.get(type_hint, type_hint)

    def _emit_param(self, p: Parameter) -> str:
        return f"{p.name} {self._map_type(p.type_hint)}"
