from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *


class SolidityBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "solidity"

    @property
    def style_guide(self) -> str:
        return "Solidity ^0.8.20 Style"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""

        indent_str = "    " * indent

        if isinstance(node, Program):
            has_contract = any(isinstance(stmt, (SmartContractDeclaration, ClassDeclaration)) for stmt in node.body)
            if not has_contract:
                body_lines = []
                for stmt in node.body:
                    res = self.emit(stmt, 1)
                    if res.strip():
                        body_lines.append(res)
                body_str = "\n".join(body_lines)
                return (
                    "// SPDX-License-Identifier: MIT\n"
                    "pragma solidity ^0.8.20;\n\n"
                    "import \"hardhat/console.sol\";\n\n"
                    f"contract RosettaTranspiled {{\n{body_str}\n}}"
                )
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)

        if isinstance(node, SmartContractDeclaration):
            decl_type = "contract"
            if node.is_interface:
                decl_type = "interface"
            elif node.is_library:
                decl_type = "library"

            bases_str = ""
            if node.bases:
                bases_str = " is " + ", ".join(node.bases)

            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}{decl_type} {node.name}{bases_str} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, ClassDeclaration):
            bases_str = ""
            if node.bases:
                bases_str = " is " + ", ".join(node.bases)
            body_str = "\n".join(self.emit(stmt, indent + 1) for stmt in node.body)
            return f"{indent_str}contract {node.name}{bases_str} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, VariableDeclaration):
            raw_type = node.type_hint or "string"
            type_hint = self._map_type(raw_type)
            const_str = " constant" if node.is_const else ""
            init_str = f" = {self.emit(node.initializer)}" if node.initializer else ""
            if "mapping" in type_hint:
                return f"{indent_str}{type_hint} public {node.name};"
            return f"{indent_str}{type_hint} public{const_str} {node.name}{init_str};"

        if isinstance(node, Assignment):
            target = self.emit(node.target)
            val = self.emit(node.value)
            return f"{indent_str}{target} = {val};"

        if isinstance(node, FunctionDeclaration):
            name = node.name
            params_str = ", ".join(self.emit(p) for p in node.params)

            decs = [self.emit(d) for d in node.decorators]
            visibility = "public"
            mutability = ""
            modifiers = []

            for d in decs:
                if d in ["public", "private", "internal", "external"]:
                    visibility = d
                elif d in ["pure", "view", "payable"]:
                    mutability = " " + d
                else:
                    modifiers.append(d)

            mods_str = " ".join(modifiers)
            if mods_str:
                mods_str = " " + mods_str

            ret_str = ""
            if node.return_type:
                ret_str = f" returns ({self._map_type(node.return_type)})"

            if name == "constructor":
                body_str = "\n".join(self._emit_stmt(s, indent + 1) for s in node.body)
                return f"{indent_str}constructor({params_str}) {visibility}{mutability}{mods_str} {{\n{body_str}\n{indent_str}}}"

            if name in ["fallback", "receive"]:
                body_str = "\n".join(self._emit_stmt(s, indent + 1) for s in node.body)
                return f"{indent_str}{name}() external{mutability} {{\n{body_str}\n{indent_str}}}"

            body_str = "\n".join(self._emit_stmt(s, indent + 1) for s in node.body)
            return f"{indent_str}function {name}({params_str}) {visibility}{mutability}{mods_str}{ret_str} {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, Parameter):
            type_hint = self._map_type(node.type_hint or "string")
            storage = ""
            if type_hint in ["string", "bytes"] or "[]" in type_hint:
                storage = " memory"
            return f"{type_hint}{storage} {node.name}"

        if isinstance(node, ReturnStatement):
            val_str = f" {self.emit(node.value)}" if node.value else ""
            return f"{indent_str}return{val_str};"

        if isinstance(node, ModifierDeclaration):
            params_str = ", ".join(self.emit(p) for p in node.params)
            body_str = "\n".join(self._emit_stmt(s, indent + 1) for s in node.body)
            if "_;" not in body_str:
                body_str += f"\n{indent_str}    _;"
            return f"{indent_str}modifier {node.name}({params_str}) {{\n{body_str}\n{indent_str}}}"

        if isinstance(node, EventDeclaration):
            params_str = ", ".join(f"{self._map_type(p.type_hint or 'string')} {p.name}" for p in node.params)
            return f"{indent_str}event {node.name}({params_str});"

        if isinstance(node, EmitStatement):
            return f"{indent_str}emit {self.emit(node.event_call)};"

        if isinstance(node, IfStatement):
            cond = self.emit(node.condition)
            conseq = "\n".join(self._emit_stmt(s, indent + 1) for s in node.consequent)
            alt_str = ""
            if node.alternate:
                alt_body = "\n".join(self._emit_stmt(s, indent + 1) for s in node.alternate)
                alt_str = f" else {{\n{alt_body}\n{indent_str}}}"
            return f"{indent_str}if ({cond}) {{\n{conseq}\n{indent_str}}}{alt_str}"

        if isinstance(node, WhileLoop):
            cond = self.emit(node.condition)
            body = "\n".join(self._emit_stmt(s, indent + 1) for s in node.body)
            return f"{indent_str}while ({cond}) {{\n{body}\n{indent_str}}}"

        if isinstance(node, ForLoop):
            init = self.emit(node.initializer).strip().rstrip(";") if node.initializer else ""
            cond = self.emit(node.condition).strip() if node.condition else ""
            incr = self.emit(node.increment).strip().rstrip(";") if node.increment else ""
            body = "\n".join(self._emit_stmt(s, indent + 1) for s in node.body)
            return f"{indent_str}for ({init}; {cond}; {incr}) {{\n{body}\n{indent_str}}}"

        if isinstance(node, BinaryExpression):
            return f"({self.emit(node.left)} {node.operator} {self.emit(node.right)})"

        if isinstance(node, UnaryExpression):
            op = "!" if node.operator.lower() == "not" else node.operator
            return f"{op}({self.emit(node.argument)})"

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
            if callee_str in ("print", "DISPLAY"):
                callee_str = "console.log"
            args_str = ", ".join(self.emit(arg) for arg in node.args)
            return f"{indent_str}{callee_str}({args_str})"

        return f"{indent_str}// {type(node).__name__}"

    def _emit_stmt(self, node: RosettaNode, indent: int) -> str:
        s = self.emit(node, indent).rstrip(";")
        if not s.strip():
            return ""
        if s.endswith("}") or s.startswith("    //"):
            return s
        return s + ";"

    def _map_type(self, t: str) -> str:
        if not t:
            return "string"
        mapping = {
            "str": "string",
            "string": "string",
            "String": "string",
            "int": "int256",
            "float": "int256",
            "bool": "bool",
            "boolean": "bool",
            "None": "void",
        }
        return mapping.get(t, t)
