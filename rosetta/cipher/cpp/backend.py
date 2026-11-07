from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *
from typing import List, Set, Any

class CppBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "cpp"

    @property
    def style_guide(self) -> str:
        return "ISO C++20"

    def __init__(self):
        self.headers: Set[str] = {"iostream", "vector", "string", "memory", "future", "functional"}

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "    " * indent
        
        if isinstance(node, Program):
            h_content = self._emit_header(node)
            cpp_content = self._emit_source(node)
            return f"/* --- HEADER --- */\n{h_content}\n\n/* --- SOURCE --- */\n{cpp_content}"
        
        return self._emit_node(node, indent)

    def _emit_header(self, node: Program) -> str:
        includes = "\n".join(f"#include <{h}>" for h in sorted(self.headers))
        content = []
        for stmt in node.body:
            if isinstance(stmt, ClassDeclaration):
                content.append(self._emit_class_decl(stmt))
            elif isinstance(stmt, FunctionDeclaration):
                content.append(self._emit_func_proto(stmt))
        return f"#pragma once\n{includes}\n\n" + "\n".join(content)

    def _emit_source(self, node: Program) -> str:
        content = []
        for stmt in node.body:
            if isinstance(stmt, ClassDeclaration):
                content.append(self._emit_class_impl(stmt))
            elif isinstance(stmt, FunctionDeclaration):
                content.append(self._emit_func_impl(stmt))
        
        main_body = []
        for stmt in node.body:
            if not isinstance(stmt, (ClassDeclaration, FunctionDeclaration, StructDeclaration)):
                main_body.append(self._emit_node(stmt, 1))
        
        if main_body:
            main_str = "int main() {\n" + "\n".join(main_body) + "\n    return 0;\n}"
            content.append(main_str)
            
        return "\n".join(content)

    def _emit_class_decl(self, node: ClassDeclaration) -> str:
        bases = f" : public {', public '.join(node.bases)}" if node.bases else ""
        body = []
        for stmt in node.body:
            if isinstance(stmt, VariableDeclaration):
                body.append(f"    {self._map_type(stmt.type_hint)} {stmt.name};")
            elif isinstance(stmt, MethodDeclaration):
                virtual = "virtual " if not stmt.is_static else "static "
                params = ", ".join(self._emit_param(p) for p in stmt.params if p.name != "self")
                ret = self._map_type(stmt.return_type, stmt.is_async)
                body.append(f"    {virtual}{ret} {stmt.name}({params});")
        
        return f"class {node.name}{bases} {{\npublic:\n" + "\n".join(body) + f"\n}};"

    def _emit_class_impl(self, node: ClassDeclaration) -> str:
        methods = []
        for stmt in node.body:
            if isinstance(stmt, MethodDeclaration):
                ret = self._map_type(stmt.return_type, stmt.is_async)
                params = ", ".join(self._emit_param(p) for p in stmt.params if p.name != "self")
                body_str = "\n".join(self._emit_node(s, 1) for s in stmt.body)
                methods.append(f"{ret} {node.name}::{stmt.name}({params}) {{\n{body_str}\n}}")
        return "\n".join(methods)

    def _emit_func_proto(self, node: FunctionDeclaration) -> str:
        ret = self._map_type(node.return_type, node.is_async)
        params = ", ".join(self._emit_param(p) for p in node.params)
        return f"{ret} {node.name}({params});"

    def _emit_func_impl(self, node: FunctionDeclaration) -> str:
        ret = self._map_type(node.return_type, node.is_async)
        params = ", ".join(self._emit_param(p) for p in node.params)
        body_str = "\n".join(self._emit_node(s, 1) for s in node.body)
        return f"{ret} {node.name}({params}) {{\n{body_str}\n}}"

    def _emit_node(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""
        padding = "    " * indent
        
        if isinstance(node, FunctionDeclaration):
            params = ", ".join(self._emit_param(p) for p in node.params)
            body_str = "\n".join(self._emit_node(s, 1) for s in node.body)
            return f"{padding}auto {node.name} = [&]({params}) {{\n{body_str}\n{padding}}};"

        if isinstance(node, VariableDeclaration):
            cpp_type = self._map_type(node.type_hint)
            if node.is_const: cpp_type = "const " + cpp_type
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}{cpp_type} {node.name}{init};"

        if isinstance(node, Assignment):
            target = self._emit_raw(node.target)
            return f"{padding}{target} = {self._emit_raw(node.value)};"

        if isinstance(node, ReturnStatement):
            val = f" {self._emit_raw(node.value)}" if node.value else ""
            return f"{padding}return{val};"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            if callee == "print":
                args = " << ".join(self._emit_raw(a) for a in node.args)
                return f"{padding}std::cout << {args} << std::endl;"
            args = ", ".join(self._emit_raw(a) for a in node.args)
            return f"{padding}{callee}({args})"

        if isinstance(node, Identifier):
            if node.name == "self": return "this"
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str): return f'"{node.value}"'
            if isinstance(node.value, bool): return "true" if node.value else "false"
            if isinstance(node.value, list):
                elements = ", ".join(self._emit_raw(x) for x in node.value)
                return f"std::vector<auto>{{ {elements} }}"
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"({self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)})"

        if isinstance(node, UnaryExpression):
            op = "!" if node.operator.lower() == "not" else node.operator
            return f"{op}({self._emit_raw(node.argument)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = "\n".join(self._emit_node(s, indent + 1) for s in node.consequent)
            res = f"{padding}if ({cond}) {{\n{consequent}\n{padding}}}"
            if node.alternate:
                alternate = "\n".join(self._emit_node(s, indent + 1) for s in node.alternate)
                res += f" else {{\n{alternate}\n{padding}}}"
            return res

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}while ({cond}) {{\n{body}\n{padding}}}"

        if isinstance(node, ForLoop):
            init = self._emit_raw(node.initializer)
            cond = self._emit_raw(node.condition)
            inc = self._emit_raw(node.increment)
            body = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}for ({init}; {cond}; {inc}) {{\n{body}\n{padding}}}"

        if isinstance(node, ForInLoop):
            it = self._emit_raw(node.iterator)
            coll = self._emit_raw(node.iterable)
            body = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}for (auto& {it} : {coll}) {{\n{body}\n{padding}}}"

        if isinstance(node, ModuleDeclaration):
            body = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}namespace {node.name} {{\n{body}\n{padding}}}"

        if isinstance(node, InterfaceDeclaration):
            body = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}class {node.name} {{\n{padding}public:\n{padding}    virtual ~{node.name}() = default;\n{body}\n{padding}}};"

        if isinstance(node, ImplDeclaration):
            body = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}// Implementation of {node.interface_name} for {node.target_type}\n{body}"

        if isinstance(node, DeferStatement):
            body = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}// defer:\n{body}"

        if isinstance(node, EventDeclaration):
            params = ", ".join(f"{self._map_type(p.type_hint)} {p.name}" for p in node.params)
            return f"{padding}// Event: {node.name}({params})"

        if isinstance(node, EmitStatement):
            call_str = self._emit_raw(node.event_call)
            return f"{padding}// emit {call_str};"

        if isinstance(node, ArrayAccess):
            obj = self._emit_raw(node.object)
            indices = "][".join(self._emit_raw(idx) for idx in node.index)
            return f"{obj}[{indices}]"

        if isinstance(node, ArrayDeclaration):
             cpp_type = self._map_type(node.type_hint)
             dims = "".join(f"[{self._emit_raw(d)}]" for d in node.dimensions)
             return f"{padding}{cpp_type} {node.name}{dims};"

        if isinstance(node, Label):
            return f"{node.name}:;"

        if isinstance(node, GotoStatement):
            return f"{padding}goto {node.label};"

        if isinstance(node, GlobalBlock):
            return f"{padding}// Global block: {node.name}"

        if isinstance(node, FormatDeclaration):
            items = ", ".join(str(i) for i in node.items)
            return f"{padding}// Format {node.label}: {items}"

        if isinstance(node, AwaitExpression):
            return f"{self._emit_raw(node.argument)}.get()"

        if isinstance(node, LambdaExpression):
            params = ", ".join(self._emit_param(p) for p in node.params)
            if isinstance(node.body, list):
                body = "\n".join(self._emit_node(s, 1) for s in node.body)
                return f"[&]({params}) {{\n{body}\n}}"
            else:
                body = self._emit_raw(node.body)
                return f"[&]({params}) {{ return {body}; }}"

        if isinstance(node, MemberAccess):
            obj = self._emit_raw(node.object)
            op = "->" if obj == "this" else "."
            return f"{obj}{op}{node.member}"

        if isinstance(node, MapExpression):
            return f"/* map */ {self._emit_raw(node.collection)}"

        # --- Prolog ---
        if isinstance(node, Fact):
            pred = getattr(node, 'predicate', getattr(node, 'name', 'fact'))
            args = ", ".join(self._emit_raw(a) for a in node.terms)
            return f"{padding}// Fact: {pred}({args});"

        if isinstance(node, PrologRule):
            return "\n".join(self._emit_node(c, indent) for c in node.clauses)

        if isinstance(node, PrologClause):
            head = self._emit_raw(node.head)
            body = ", ".join(self._emit_raw(b) for b in node.body)
            return f"{padding}// Rule: {head} :- {body};"

        if isinstance(node, Query):
            terms = ", ".join(self._emit_raw(t) for t in node.terms)
            return f"{padding}// Query: ?- {terms};"

        # --- SNOBOL ---
        if isinstance(node, SNOBOLStatement):
            label_str = f"{node.label}: " if node.label else ""
            content_str = self._emit_node(node.content, 0).strip() if node.content else ""
            return f"{padding}// SNOBOL: {label_str}{content_str};"

        if isinstance(node, PatternMatchStatement):
            subj = self._emit_raw(node.subject)
            pat = self._emit_raw(node.pattern)
            return f"{padding}// Pattern match: {pat} in {subj};"

        if isinstance(node, SNOBOLTransfer):
            return f"// SNOBOL transfer"

        # --- PL/I ---
        if isinstance(node, OnCondition):
            body_str = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}// ON {node.condition}:\ntry {{\n{body_str}\n{padding}}} catch (...) {{}}"

        if isinstance(node, MemoryAllocation):
            type_hint = f"({node.type_hint}*)" if node.type_hint else ""
            return f"{type_hint}malloc({self._emit_raw(node.size)})"

        if isinstance(node, MemoryFree):
            return f"{padding}free({self._emit_raw(node.argument)});"

        if isinstance(node, Dereference):
            return f"*{self._emit_raw(node.argument)}"

        if isinstance(node, TaskDeclaration):
            body_str = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}void task_{node.name}() {{\n{body_str}\n{padding}}}"

        # --- RPG ---
        if isinstance(node, RPGIndicator):
            return f"{padding}{node.name}"

        if isinstance(node, RPGOperation):
            opcode = node.opcode.upper()
            f1 = self._emit_raw(node.factor1)
            f2 = self._emit_raw(node.factor2)
            res = self._emit_raw(node.result)
            if opcode == "ADD":
                return f"{padding}{res} = {(f1 + ' + ') if f1 else ''}{f2};"
            if opcode == "MOVEL":
                return f"{padding}{res} = {f2};"
            if opcode == "DSPLY":
                return f"{padding}std::cout << {(f1 if f1 else f2)} << std::endl;"
            return f"{padding}{opcode}({f1}, {f2}, {res});"

        # --- Forth ---
        if isinstance(node, ForthWordDefinition):
            body_str = "\n".join(self._emit_node(s, indent + 1) for s in node.body)
            return f"{padding}void {node.name}() {{\n{body_str}\n{padding}}}"

        if isinstance(node, ForthStackOp):
            op = node.operation.upper()
            if op == "DUP":
                return f"{padding}if (!_stack.empty()) _stack.push_back(_stack.back());"
            if op == "DROP":
                return f"{padding}if (!_stack.empty()) _stack.pop_back();"
            if op == "SWAP":
                return f"{padding}if (_stack.size() >= 2) std::swap(_stack[_stack.size()-1], _stack[_stack.size()-2]);"
            if op == ".":
                return f"{padding}if (!_stack.empty()) {{ std::cout << _stack.back() << std::endl; _stack.pop_back(); }}"
            if op in ("+", "-", "*", "/"):
                return f"{padding}{{ auto _b = _stack.back(); _stack.pop_back(); auto _a = _stack.back(); _stack.pop_back(); _stack.push_back(_a {op} _b); }}"
            return f"{padding}_stack.push_back({node.operation});"

        # --- ML / Functional ---
        if isinstance(node, MLDataTypeDeclaration):
            return f"{padding}struct {node.name} {{}};"

        if isinstance(node, MLValDeclaration):
            return f"{padding}auto {node.name} = {self._emit_raw(node.initializer)};"

        if isinstance(node, MLFunDeclaration):
            params = ", ".join(self._emit_param(p) for p in node.params)
            body_str = self._emit_node(node.body, indent + 1) if isinstance(node.body, list) else f"{'    '*(indent+1)}return {self._emit_raw(node.body)};"
            return f"{padding}auto {node.name}({params}) {{\n{body_str}\n{padding}}}"

        if isinstance(node, MLLetExpression):
            bindings = "\n".join(self._emit_node(b, indent) for b in node.bindings)
            body = self._emit_node(node.body, indent)
            return f"{bindings}\n{body}"

        if isinstance(node, MLCaseExpression):
            expr = self._emit_raw(node.expression)
            arms = []
            for idx, br in enumerate(node.branches):
                pat = self._emit_raw(br.pattern)
                b_body = self._emit_raw(br.body)
                kw = "if" if idx == 0 else "else if"
                arms.append(f"{padding}{kw} ({expr} == {pat}) {{ return {b_body}; }}")
            return "\n".join(arms) if arms else f"{padding}/* match {expr} */"

        return f"{padding}// Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self._emit_node(node, 0)
        return res.strip().rstrip(";")

    def _map_type(self, type_hint: str, is_async: bool = False) -> str:
        mapping = {
            "int": "int", "float": "double", "str": "std::string",
            "bool": "bool", "list": "std::vector<auto>", "None": "void", "any": "auto"
        }
        t = mapping.get(type_hint, type_hint or "auto")
        if t == "any": t = "auto"
        if is_async: return f"std::future<{t if t != 'void' else 'void'}>"
        return t

    def _emit_param(self, p: Parameter) -> str:
        return f"{self._map_type(p.type_hint)} {p.name}"
