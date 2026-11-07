from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class JavaBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "java"

    @property
    def style_guide(self) -> str:
        return "Google Java Style"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""
        padding = "    " * indent
        
        if isinstance(node, Program):
            header = "import java.util.*;\nimport java.util.concurrent.*;\n\n"
            body = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return header + body
        
        if isinstance(node, VariableDeclaration):
            java_type = self._map_type(node.type_hint)
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}{java_type} {node.name}{init};"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} = {self._emit_raw(node.value)};"

        if isinstance(node, FunctionDeclaration):
            # In Java, top-level functions must be in a class. 
            # We'll wrap them in a 'Main' class if they aren't already.
            ret_type = self._map_type(node.return_type, node.is_async)
            params = ", ".join(self._emit_param(p) for p in node.params)
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}public static {ret_type} {node.name}({params}) {{\n{body_str}\n{padding}}}"

        if isinstance(node, ClassDeclaration):
            extends = f" extends {node.bases[0]}" if node.bases else ""
            implements = f" implements {', '.join(node.interfaces)}" if node.interfaces else ""
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}public class {node.name}{extends}{implements} {{\n{body_str}\n{padding}}}"

        if isinstance(node, MethodDeclaration):
            static_kw = "static " if node.is_static else ""
            ret_type = self._map_type(node.return_type, node.is_async)
            params = ", ".join(self._emit_param(p) for p in node.params if p.name != "self")
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}public {static_kw}{ret_type} {node.name}({params}) {{\n{body_str}\n{padding}}}"

        if isinstance(node, ReturnStatement):
            val = f" {self._emit_raw(node.value)}" if node.value else ""
            return f"{padding}return{val};"

        if isinstance(node, CallExpression):
            callee_name = self._emit_raw(node.callee)
            if callee_name == "print":
                args = ", ".join(self._emit_raw(arg) for arg in node.args)
                return f"{padding}System.out.println({args});"
            
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
                # Simplified list initialization
                elements = ", ".join(self._emit_raw(x) for x in node.value)
                return f"Arrays.asList({elements})"
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

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}while ({cond}) {{\n{body}\n{padding}}}"

        if isinstance(node, ForInLoop):
            it = self._emit_raw(node.iterator)
            coll = self._emit_raw(node.iterable)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}for (var {it} : {coll}) {{\n{body}\n{padding}}}"

        if isinstance(node, ForLoop):
            init = self._emit_raw(node.initializer)
            cond = self._emit_raw(node.condition)
            inc = self._emit_raw(node.increment)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}for ({init}; {cond}; {inc}) {{\n{body}\n{padding}}}"

        if isinstance(node, EventDeclaration):
            params = ", ".join(f"{self._map_type(p.type_hint)} {p.name}" for p in node.params)
            return f"{padding}// Event: {node.name}({params})"

        if isinstance(node, EmitStatement):
            call_str = self._emit_raw(node.event_call)
            return f"{padding}// emit {call_str};"

        if isinstance(node, AwaitExpression):
            # Java: CompletableFuture.get()
            return f"{self._emit_raw(node.argument)}.get()"

        if isinstance(node, MemberAccess):
            return f"{self._emit_raw(node.object)}.{node.member}"

        if isinstance(node, MapExpression):
            param = node.function.params[0].name
            body = self._emit_raw(node.function.body)
            return f"{self._emit_raw(node.collection)}.stream().map({param} -> {body}).collect(Collectors.toList())"

        if isinstance(node, FilterExpression):
            param = node.function.params[0].name
            body = self._emit_raw(node.function.body)
            return f"{self._emit_raw(node.collection)}.stream().filter({param} -> {body}).collect(Collectors.toList())"

        if isinstance(node, LambdaExpression):
            params = ", ".join(p.name for p in node.params)
            return f"({params}) -> {self._emit_raw(node.body)}"

        if isinstance(node, UnaryExpression):
            return f"{node.operator}{self._emit_raw(node.argument)}"

        if isinstance(node, YieldExpression):
            return f"yield {self._emit_raw(node.argument) if node.argument else ''}"

        if isinstance(node, ArrayAccess):
            obj = self._emit_raw(node.object)
            indices = "][".join(self._emit_raw(idx) for idx in node.index)
            return f"{obj}[{indices}]"

        if isinstance(node, Label):
            return f"{padding}// Label: {node.name}"

        if isinstance(node, GotoStatement):
            return f"{padding}// goto {node.label};"

        if isinstance(node, ModuleDeclaration):
            body_str = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return f"{padding}// Module: {node.name}\n{body_str}"

        # --- PL/I ---
        if isinstance(node, OnCondition):
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}// ON {node.condition}:\ntry {{\n{body_str}\n{padding}}} catch (Exception e) {{}}"

        if isinstance(node, MemoryAllocation):
            return f"{padding}// malloc({self._emit_raw(node.size)});"

        if isinstance(node, MemoryFree):
            return f"{padding}// free({self._emit_raw(node.argument)});"

        if isinstance(node, TaskDeclaration):
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}public void task_{node.name}() {{\n{body_str}\n{padding}}}"

        # --- Prolog ---
        if isinstance(node, Fact):
            pred = getattr(node, 'predicate', getattr(node, 'name', 'fact'))
            args = ", ".join(self._emit_raw(a) for a in node.terms)
            return f"{padding}// Fact: {pred}({args});"

        if isinstance(node, PrologRule):
            return "\n".join(self.emit(c, indent) for c in node.clauses)

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
            content_str = self.emit(node.content, 0).strip() if node.content else ""
            return f"{padding}// SNOBOL: {label_str}{content_str};"

        if isinstance(node, PatternMatchStatement):
            subj = self._emit_raw(node.subject)
            pat = self._emit_raw(node.pattern)
            return f"{padding}// Pattern match: {pat} in {subj};"

        if isinstance(node, SNOBOLTransfer):
            return f"// SNOBOL transfer"

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
                return f"{padding}System.out.println({(f1 if f1 else f2)});"
            return f"{padding}// RPG: {opcode}({f1}, {f2}, {res});"

        # --- Forth ---
        if isinstance(node, ForthWordDefinition):
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}public void {node.name}() {{\n{body_str}\n{padding}}}"

        if isinstance(node, ForthStackOp):
            op = node.operation.upper()
            if op == "DUP":
                return f"{padding}_stack.push(_stack.peek());"
            if op == "DROP":
                return f"{padding}_stack.pop();"
            if op == ".":
                return f"{padding}System.out.println(_stack.pop());"
            if op in ("+", "-", "*", "/"):
                return f"{padding}_stack.push(_stack.pop() {op} _stack.pop());"
            return f"{padding}_stack.push({node.operation});"

        # --- ML / Functional ---
        if isinstance(node, MLDataTypeDeclaration):
            return f"{padding}class {node.name} {{}}"

        if isinstance(node, MLValDeclaration):
            return f"{padding}var {node.name} = {self._emit_raw(node.initializer)};"

        if isinstance(node, MLFunDeclaration):
            params = ", ".join(self._emit_param(p) for p in node.params)
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body) if isinstance(node.body, list) else f"{'    '*(indent+1)}return {self._emit_raw(node.body)};"
            return f"{padding}public Object {node.name}({params}) {{\n{body_str}\n{padding}}}"

        if isinstance(node, MLLetExpression):
            bindings = "\n".join(self.emit(b, indent) for b in node.bindings)
            body = self.emit(node.body, indent)
            return f"{bindings}\n{body}"

        if isinstance(node, MLCaseExpression):
            expr = self._emit_raw(node.expression)
            arms = []
            for idx, br in enumerate(node.branches):
                pat = self._emit_raw(br.pattern)
                b_body = self._emit_raw(br.body)
                kw = "if" if idx == 0 else "else if"
                arms.append(f"{padding}{kw} (Objects.equals({expr}, {pat})) {{ return {b_body}; }}")
            return "\n".join(arms) if arms else f"{padding}/* match {expr} */"

        return f"{padding}// Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip().rstrip(";")

    def _map_type(self, type_hint: str, is_async: bool = False) -> str:
        mapping = {
            "int": "int",
            "float": "double",
            "str": "String",
            "bool": "boolean",
            "list": "List<Object>",
            "None": "void"
        }
        base_type = mapping.get(type_hint, type_hint or "Object")
        if is_async:
            return f"CompletableFuture<{base_type if base_type != 'void' else 'Void'}>"
        return base_type

    def _emit_param(self, p: Parameter) -> str:
        return f"{self._map_type(p.type_hint)} {p.name}"
