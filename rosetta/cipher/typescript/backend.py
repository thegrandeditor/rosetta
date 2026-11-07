from rosetta.cipher.javascript.backend import JavaScriptBackend
from rosetta.ir.nodes import *
from typing import Optional

class TypeScriptBackend(JavaScriptBackend):
    @property
    def language_id(self) -> str:
        return "typescript"

    def _get_ts_type(self, type_str: Optional[str]) -> str:
        if not type_str: return "any"
        if type_str in ["int", "float", "number"]: return "number"
        if type_str in ["str", "string"]: return "string"
        if type_str in ["bool", "boolean"]: return "boolean"
        if type_str == "list": return "any[]"
        return type_str

    def emit(self, node: RosettaNode) -> str:
        if node is None: return ""

        if isinstance(node, MethodDeclaration):
            async_kw = "async " if node.is_async else ""
            static_kw = "static " if node.is_static else ""
            is_generator = any(self._contains_yield(stmt) for stmt in node.body)
            gen_star = "*" if is_generator else ""
            name = "constructor" if node.name == "__init__" else node.name
            params = ", ".join(self.emit(p) for p in node.params if p.name != "self")
            
            if name == "constructor":
                ret_type = ""
            else:
                ret_type = f": {self._get_ts_type(node.return_type)}" if node.return_type else ": void"
            
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            return f"{static_kw}{async_kw}{gen_star}{name}({params}){ret_type} {{\n    {body}\n  }}"

        if isinstance(node, FunctionDeclaration):
            async_kw = "async " if node.is_async else ""
            is_generator = any(self._contains_yield(stmt) for stmt in node.body)
            gen_star = "*" if is_generator else ""
            params = ", ".join(self.emit(p) for p in node.params)
            ret_type = f": {self._get_ts_type(node.return_type)}" if node.return_type else ": void"
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"{async_kw}function{gen_star} {node.name}({params}){ret_type} {{\n  {body}\n}}"

        if isinstance(node, VariableDeclaration):
            kw = "const" if node.is_const else "let"
            type_anno = f": {self._get_ts_type(node.type_hint)}" if node.type_hint else ": any"
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"{kw} {node.name}{type_anno}{init};"

        if isinstance(node, Parameter):
            type_anno = f": {self._get_ts_type(node.type_hint)}" if node.type_hint else ": any"
            default = f" = {self.emit(node.default_value)}" if node.default_value else ""
            return f"{node.name}{type_anno}{default}"

        # Fallback to JavaScriptBackend for other nodes
        return super().emit(node)
