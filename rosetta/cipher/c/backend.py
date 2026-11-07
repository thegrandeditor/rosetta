from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class CBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "c"

    @property
    def style_guide(self) -> str:
        return "C99 / GNU"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "    " * indent
        
        if isinstance(node, Program):
            # Include standard headers
            header = "#include <stdio.h>\n#include <stdlib.h>\n#include <stdbool.h>\n\n"
            body = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return header + body
        
        if isinstance(node, VariableDeclaration):
            c_type = self._map_type(node.type_hint)
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}{c_type} {node.name}{init};"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} = {self._emit_raw(node.value)};"

        if isinstance(node, FunctionDeclaration):
            ret_type = self._map_type(node.return_type)
            params = ", ".join(self._emit_param(p) for p in node.params)
            if not params: params = "void"
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}{ret_type} {node.name}({params}) {{\n{body_str}\n{padding}}}"

        if isinstance(node, ClassDeclaration):
            # C doesn't have classes, so we emit a comment and translate methods as global functions
            comment = f"{padding}/* Class {node.name} translated to structs and functions */\n"
            # Emit a struct for state
            struct_fields = []
            for stmt in node.body:
                if isinstance(stmt, VariableDeclaration):
                    struct_fields.append(f"    {self._map_type(stmt.type_hint)} {stmt.name};")
            
            struct_str = f"{padding}typedef struct {{\n" + "\n".join(struct_fields) + f"\n{padding}}} {node.name};\n"
            
            # Emit methods as functions with 'self' as first param
            methods = []
            for stmt in node.body:
                if isinstance(stmt, MethodDeclaration):
                    # Prefix method name with class name
                    stmt.name = f"{node.name}_{stmt.name}"
                    # Add pointer to struct as first param if not static
                    if not stmt.is_static:
                        stmt.params.insert(0, Parameter(name="self", type_hint=f"{node.name}*"))
                    methods.append(self.emit(stmt, indent))
            
            return comment + struct_str + "\n".join(methods)

        if isinstance(node, MethodDeclaration):
            return self.emit(FunctionDeclaration(
                name=node.name, params=node.params, body=node.body,
                return_type=node.return_type, is_async=node.is_async
            ), indent)

        if isinstance(node, ReturnStatement):
            val = f" {self._emit_raw(node.value)}" if node.value else ""
            return f"{padding}return{val};"

        if isinstance(node, CallExpression):
            callee_name = self._emit_raw(node.callee)
            if callee_name == "print":
                # Very simple printf mapping
                format_str = self._guess_format_str(node.args)
                args = ", ".join(self._emit_raw(arg) for arg in node.args)
                return f'{padding}printf("{format_str}\\n", {args});'
            
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            return f"{padding}{callee_name}({args});"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            if isinstance(node.value, bool):
                return "true" if node.value else "false"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            body_indent = indent + 1
            consequent = "\n".join(self.emit(stmt, body_indent) for stmt in node.consequent)
            res = f"{padding}if ({cond}) {{\n{consequent}\n{padding}}}"
            if node.alternate:
                alternate = "\n".join(self.emit(stmt, body_indent) for stmt in node.alternate)
                res += f" else {{\n{alternate}\n{padding}}}"
            return res

        if isinstance(node, MemberAccess):
            # Handle pointer access if it's 'self'
            op = "->" if self._emit_raw(node.object) == "self" else "."
            return f"{self._emit_raw(node.object)}{op}{node.member}"

        if isinstance(node, MemoryAllocation):
            type_hint = f"({self._map_type(node.type_hint)}*)" if node.type_hint else ""
            return f"{type_hint}malloc({self._emit_raw(node.size)})"

        if isinstance(node, MemoryFree):
            return f"{padding}free({self._emit_raw(node.argument)});"

        if isinstance(node, Dereference):
            return f"*{self._emit_raw(node.argument)}"

        if isinstance(node, (MapExpression, FilterExpression)):
            return f"/* {type(node).__name__} */ {self._emit_raw(node.collection)}"

        return f"{padding}/* Unknown node: {type(node).__name__} */"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip().rstrip(";")

    def _map_type(self, type_hint: str) -> str:
        mapping = {
            "int": "int",
            "float": "float",
            "str": "char*",
            "bool": "bool",
            "list": "void*", # Simplified
            "None": "void"
        }
        if not type_hint: return "void"
        return mapping.get(type_hint, type_hint)

    def _emit_param(self, p: Parameter) -> str:
        return f"{self._map_type(p.type_hint)} {p.name}"

    def _guess_format_str(self, args: List[RosettaNode]) -> str:
        # Crude guesswork for printf
        formats = []
        for arg in args:
            if isinstance(arg, Literal):
                if isinstance(arg.value, int): formats.append("%d")
                elif isinstance(arg.value, float): formats.append("%f")
                else: formats.append("%s")
            else:
                formats.append("%s") # Fallback
        return " ".join(formats)
