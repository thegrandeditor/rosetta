from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class RustBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "rust"

    @property
    def style_guide(self) -> str:
        return "Rustfmt"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""
        padding = "    " * indent
        
        if isinstance(node, Program):
            # No specific header for Rust except maybe some allow attributes
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, VariableDeclaration):
            mut_kw = "mut " if not node.is_const else ""
            rust_type = self._map_type(node.type_hint)
            init = f" = {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}let {mut_kw}{node.name}: {rust_type}{init};"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} = {self._emit_raw(node.value)};"

        if isinstance(node, FunctionDeclaration):
            async_kw = "async " if node.is_async else ""
            params = ", ".join(self._emit_param(p) for p in node.params)
            ret = f" -> {self._map_type(node.return_type)}" if node.return_type else ""
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}{async_kw}fn {node.name}({params}){ret} {{\n{body_str}\n{padding}}}"

        if isinstance(node, (StructDeclaration, MojoStructDeclaration)):
            fields = [f"    pub {f.name}: {self._map_type(f.type_hint)}," for f in node.fields]
            return f"{padding}pub struct {node.name} {{\n" + "\n".join(fields) + f"\n{padding}}}"

        if isinstance(node, ClassDeclaration):
            # Map Class to struct + impl
            fields = []
            for stmt in node.body:
                if isinstance(stmt, VariableDeclaration):
                    fields.append(f"    pub {stmt.name}: {self._map_type(stmt.type_hint)},")
            
            struct_str = f"{padding}pub struct {node.name} {{\n" + "\n".join(fields) + f"\n{padding}}}\n\n"
            
            methods = []
            for stmt in node.body:
                if isinstance(stmt, MethodDeclaration):
                    methods.append(self.emit(stmt, indent + 1))
            
            impl_str = f"{padding}impl {node.name} {{\n" + "\n".join(methods) + f"\n{padding}}}"
            return struct_str + impl_str

        if isinstance(node, MethodDeclaration):
            async_kw = "async " if node.is_async else ""
            # Self handling
            rust_params = []
            for p in node.params:
                if p.name == "self":
                    rust_params.append("&self")
                else:
                    rust_params.append(self._emit_param(p))
            params = ", ".join(rust_params)
            ret = f" -> {self._map_type(node.return_type)}" if node.return_type else ""
            
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}pub {async_kw}fn {node.name}({params}){ret} {{\n{body_str}\n{padding}}}"

        if isinstance(node, ReturnStatement):
            val = f" {self._emit_raw(node.value)}" if node.value else ""
            return f"{padding}return{val};"

        if isinstance(node, CallExpression):
            callee_name = self._emit_raw(node.callee)
            if callee_name == "print":
                args = ", ".join(self._emit_raw(arg) for arg in node.args)
                # Simple println! macro
                return f'{padding}println!("{{:?}}", {args});'
            
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            return f"{padding}{callee_name}({args})"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}".to_string()'
            if isinstance(node.value, bool):
                return str(node.value).lower()
            if isinstance(node.value, list):
                elements = ", ".join(self._emit_raw(x) for x in node.value)
                return f"vec![{elements}]"
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
            return f"{padding}while {cond} {{\n{body}\n{padding}}}"

        if isinstance(node, ForInLoop):
            it = self._emit_raw(node.iterator)
            coll = self._emit_raw(node.iterable)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}for {it} in {coll} {{\n{body}\n{padding}}}"

        if isinstance(node, ForLoop):
            init = self._emit_raw(node.initializer)
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}{init};\n{padding}while {cond} {{\n{body}\n{padding}}}"

        if isinstance(node, ModuleDeclaration):
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}pub mod {node.name} {{\n{body}\n{padding}}}"

        if isinstance(node, InterfaceDeclaration):
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}pub trait {node.name} {{\n{body}\n{padding}}}"

        if isinstance(node, ImplDeclaration):
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}impl {node.interface_name} for {node.target_type} {{\n{body}\n{padding}}}"

        if isinstance(node, EventDeclaration):
            params = ", ".join(f"{p.name}: {self._map_type(p.type_hint)}" for p in node.params)
            return f"{padding}// Event: {node.name}({params})"

        if isinstance(node, EmitStatement):
            call_str = self._emit_raw(node.event_call)
            return f"{padding}// emit {call_str};"

        if isinstance(node, AwaitExpression):
            return f"{self._emit_raw(node.argument)}.await"

        if isinstance(node, YieldExpression):
            return f"yield {self._emit_raw(node.argument) if node.argument else ''}"

        if isinstance(node, MemberAccess):
            return f"{self._emit_raw(node.object)}.{node.member}"

        if isinstance(node, LambdaExpression):
            params = ", ".join(p.name for p in node.params)
            return f"|{params}| {{ {self._emit_raw(node.body)} }}"

        if isinstance(node, MapExpression):
            param = node.function.params[0].name
            body = self._emit_raw(node.function.body)
            return f"{self._emit_raw(node.collection)}.into_iter().map(|{param}| {body}).collect::<Vec<_>>()"

        if isinstance(node, FilterExpression):
            param = node.function.params[0].name
            body = self._emit_raw(node.function.body)
            return f"{self._emit_raw(node.collection)}.into_iter().filter(|{param}| {body}).collect::<Vec<_>>()"

        if isinstance(node, DeferStatement):
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}// defer:\n{body_str}"

        if isinstance(node, ArrayAccess):
            obj = self._emit_raw(node.object)
            indices = "][".join(self._emit_raw(idx) for idx in node.index)
            return f"{obj}[{indices}]"

        if isinstance(node, Label):
            return f"{padding}// Label: {node.name}"

        if isinstance(node, GotoStatement):
            return f"{padding}// goto {node.label};"

        # --- PL/I ---
        if isinstance(node, OnCondition):
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}// ON {node.condition}:\n{padding}if true {{\n{body_str}\n{padding}}}"

        if isinstance(node, MemoryAllocation):
            return f"vec![0u8; {self._emit_raw(node.size)}]"

        if isinstance(node, MemoryFree):
            return f"{padding}drop({self._emit_raw(node.argument)});"

        if isinstance(node, Dereference):
            return f"*{self._emit_raw(node.argument)}"

        if isinstance(node, TaskDeclaration):
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}fn task_{node.name}() {{\n{body_str}\n{padding}}}"

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
                return f'println!("{{}}", {(f1 if f1 else f2)});'
            return f"{padding}// RPG: {opcode}({f1}, {f2}, {res});"

        # --- Forth ---
        if isinstance(node, ForthWordDefinition):
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"{padding}fn {node.name}() {{\n{body_str}\n{padding}}}"

        if isinstance(node, ForthStackOp):
            op = node.operation.upper()
            if op == "DUP":
                return f"{padding}if let Some(&_top) = _stack.last() {{ _stack.push(_top); }}"
            if op == "DROP":
                return f"{padding}_stack.pop();"
            if op == ".":
                return f'{padding}if let Some(_top) = _stack.pop() {{ println!("{{:?}}", _top); }}'
            if op in ("+", "-", "*", "/"):
                return f"{padding}if let (Some(_b), Some(_a)) = (_stack.pop(), _stack.pop()) {{ _stack.push(_a {op} _b); }}"
            return f"{padding}_stack.push({node.operation});"

        # --- ML / Functional ---
        if isinstance(node, MLDataTypeDeclaration):
            return f"{padding}pub struct {node.name};"

        if isinstance(node, MLValDeclaration):
            return f"{padding}let {node.name} = {self._emit_raw(node.initializer)};"

        if isinstance(node, MLFunDeclaration):
            params = ", ".join(self._emit_param(p) for p in node.params)
            body_str = "\n".join(self.emit(s, indent + 1) for s in node.body) if isinstance(node.body, list) else f"{'    '*(indent+1)}{self._emit_raw(node.body)}"
            return f"{padding}pub fn {node.name}({params}) {{\n{body_str}\n{padding}}}"

        if isinstance(node, MLLetExpression):
            bindings = "\n".join(self.emit(b, indent) for b in node.bindings)
            body = self.emit(node.body, indent)
            return f"{bindings}\n{body}"

        if isinstance(node, MLCaseExpression):
            expr = self._emit_raw(node.expression)
            arms = [f"{padding}    {self._emit_raw(br.pattern)} => {self._emit_raw(br.body)}," for br in node.branches]
            arms.append(f"{padding}    _ => Default::default(),")
            return f"{padding}match {expr} {{\n" + "\n".join(arms) + f"\n{padding}}}"

        return f"{padding}// Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip().rstrip(";")

    def _map_type(self, type_hint: str) -> str:
        mapping = {
            "int": "i32",
            "float": "f64",
            "str": "String",
            "bool": "bool",
            "list": "Vec<Box<dyn Any>>", # Crude
            "None": "()",
            "void": "()"
        }
        if not type_hint: return "()"
        return mapping.get(type_hint, type_hint)

    def _emit_param(self, p: Parameter) -> str:
        return f"{p.name}: {self._map_type(p.type_hint)}"
