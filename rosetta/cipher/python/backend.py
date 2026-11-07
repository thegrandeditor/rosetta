from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class PythonBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "python"

    @property
    def style_guide(self) -> str:
        return "PEP 8"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""
        padding = "    " * indent
        
        if isinstance(node, Program):
            if not node.body: return "# [COMPILER WARNING] BABEL generated an empty AST. Check grammar rules or EOF newline."
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, VariableDeclaration):
            type_hint = f": {node.type_hint}" if node.type_hint else ""
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"{padding}{node.name}{type_hint}{init}"

        if isinstance(node, Assignment):
            return f"{padding}{self.emit(node.target)} = {self.emit(node.value)}"

        if isinstance(node, FunctionDeclaration):
            async_kw = "async " if node.is_async else ""
            decorators = "".join(f"{padding}@{self.emit(d)}\n" for d in node.decorators)
            params = ", ".join(self._emit_param(p) for p in node.params)
            ret = f" -> {node.return_type}" if node.return_type else ""
            
            # Simple body handling
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            
            return f"{decorators}{padding}{async_kw}def {node.name}({params}){ret}:\n{body_str}"

        if isinstance(node, MethodDeclaration):
            # Same as function for Python
            return self.emit(FunctionDeclaration(
                name=node.name, params=node.params, body=node.body,
                return_type=node.return_type, is_async=node.is_async,
                decorators=node.decorators
            ), indent)

        if isinstance(node, ContractedFunction):
            decorators = "".join(f"{padding}@{self.emit(d)}\n" for d in node.decorators)
            params = ", ".join(self._emit_param(p) for p in node.params)
            ret = f" -> {node.return_type}" if node.return_type else ""
            
            body_indent = indent + 1
            body_nodes = []
            if node.contract:
                for req in node.contract.require:
                    body_nodes.append(f"{'    ' * body_indent}assert {self._emit_raw(req)}, 'Precondition failed'")
            
            for stmt in node.body:
                body_nodes.append(self.emit(stmt, body_indent))
                
            if node.contract:
                for ens in node.contract.ensure:
                     # 'old' is tricky in Python, but we can emit a comment or simple assert
                     body_nodes.append(f"{'    ' * body_indent}assert {self._emit_raw(ens)}, 'Postcondition failed'")
            
            body_str = "\n".join(body_nodes)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            
            return f"{decorators}{padding}def {node.name}({params}){ret}:\n{body_str}"

        if isinstance(node, ContractedClass):
            bases = f"({', '.join(node.bases)})" if node.bases else ""
            body_indent = indent + 1
            body_nodes = []
            for stmt in node.body:
                body_nodes.append(self.emit(stmt, body_indent))
            
            if node.invariant:
                inv_body = "\n".join(f"{'    ' * (body_indent+1)}assert {self._emit_raw(inv)}, 'Invariant failed'" for inv in node.invariant)
                body_nodes.append(f"{'    ' * body_indent}def _check_invariant(self):\n{inv_body}")
                
            body_str = "\n".join(body_nodes)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}class {node.name}{bases}:\n{body_str}"
            
        if isinstance(node, (StructDeclaration, MojoStructDeclaration)):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(f, body_indent) for f in node.fields)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}class {node.name}:\n{body_str}"

        if isinstance(node, ClassDeclaration):
            bases = f"({', '.join(node.bases)})" if node.bases else ""
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}class {node.name}{bases}:\n{body_str}"

        if isinstance(node, InterfaceDeclaration):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}class {node.name}:\n{body_str}"

        if isinstance(node, ImplDeclaration):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}class {node.target_type}_as_{node.interface_name}:\n{body_str}"

        if isinstance(node, ReturnStatement):
            val = f" {self._emit_raw(node.value)}" if node.value else ""
            return f"{padding}return{val}"

        if isinstance(node, CallExpression):
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            return f"{padding}{self._emit_raw(node.callee)}({args})"

        if isinstance(node, Identifier):
            return f"{padding}{node.name}"

        if isinstance(node, Literal):
            if isinstance(node.value, list):
                return f"{padding}[" + ", ".join(self._emit_raw(x) if isinstance(x, RosettaNode) else repr(x) for x in node.value) + "]"
            return f"{padding}{repr(node.value)}"

        if isinstance(node, BinaryExpression):
            op = node.operator
            if op == "=":
                op = "=="
            if op == " ":
                return f"{padding}({self._emit_raw(node.left)} + {self._emit_raw(node.right)})"
            if op in [".", "$"]:
                # Mapping capture to a comment or pseudo-code for Python
                return f"{padding}({self._emit_raw(node.left)} # {op} {self._emit_raw(node.right)})"
            return f"{padding}({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        if isinstance(node, UnaryExpression):
            op = node.operator + (" " if node.operator.isalpha() else "")
            return f"{padding}{op}{self._emit_raw(node.argument)}"

        if isinstance(node, ForInLoop):
            iterator = self._emit_raw(node.iterator)
            iterable = self._emit_raw(node.iterable)
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}for {iterator} in {iterable}:\n{body_str}"

        if isinstance(node, ArrayDeclaration):
            # Python doesn't have fixed-size arrays in the same way, but we can initialize a list or use numpy
            # For now, let's just use comments and a simple list initialization
            dims_str = " * ".join(self._emit_raw(d) for d in node.dimensions)
            return f"{padding}{node.name} = [None] * ({dims_str})  # Array of {node.type_hint}"

        if isinstance(node, ArrayAccess):
            indices = "][".join(self._emit_raw(idx) for idx in node.index)
            # Handle 1-based indexing if necessary? For now just emit as is.
            return f"{self._emit_raw(node.object)}[{indices}]"

        if isinstance(node, GlobalBlock):
            members = ", ".join(m.name for m in node.members)
            return f"{padding}# Global block: {node.name}\nglobal {members}"

        if isinstance(node, FormatDeclaration):
            return f"{padding}# Format {node.label}: {node.items}"

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}while {cond}:\n{body_str}"

        if isinstance(node, ForLoop):
            # Map C-style ForLoop to while if it's not a simple range
            # But usually it's used for range-like loops from Fortran
            init = self._emit_raw(node.initializer)
            cond = self._emit_raw(node.condition)
            inc = self._emit_raw(node.increment)
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            
            # Simple conversion to while
            res = f"{padding}{init}\n{padding}while {cond}:\n{body_str}\n{'    ' * body_indent}{inc}"
            return res

        if isinstance(node, IfStatement):
            cond = self.emit(node.condition)
            body_indent = indent + 1
            consequent = "\n".join(self.emit(stmt, body_indent) for stmt in node.consequent)
            res = f"{padding}if {cond}:\n{consequent}"
            if node.alternate:
                alternate = "\n".join(self.emit(stmt, body_indent) for stmt in node.alternate)
                res += f"\n{padding}else:\n{alternate}"
            return res

        if isinstance(node, ListComprehension):
            expr = self.emit(node.expression)
            gens = " ".join(self._emit_comp_gen(g) for g in node.generators)
            return f"[{expr} {gens}]"

        if isinstance(node, AwaitExpression):
            return f"await {self.emit(node.argument)}"

        if isinstance(node, YieldExpression):
            val = f" {self.emit(node.argument)}" if node.argument else ""
            return f"yield{val}"

        if isinstance(node, Label):
            return f"{padding}# Label: {node.name}"

        if isinstance(node, GotoStatement):
            return f"{padding}# GOTO {node.label}"

        if isinstance(node, MemberAccess):
            return f"{self.emit(node.object)}.{node.member}"

        if isinstance(node, SNOBOLStatement):
            label_str = f"# Label: {node.label}\n{padding}" if node.label else ""
            content_str = self.emit(node.content, indent).strip() if node.content else ""
            transfer_str = f"  # {self._emit_raw(node.transfer)}" if node.transfer else ""
            return f"{padding}{label_str}{content_str}{transfer_str}"

        if isinstance(node, PatternMatchStatement):
            subj = self._emit_raw(node.subject)
            pat = self._emit_raw(node.pattern)
            if node.replacement:
                repl = self._emit_raw(node.replacement)
                return f"{padding}if {pat} in {subj}: {subj} = {subj}.replace({pat}, {repl}, 1)"
            return f"{padding}{pat} in {subj}"

        if isinstance(node, SNOBOLTransfer):
            res = "GOTO: "
            if node.unconditional_label: res += node.unconditional_label
            else:
                if node.success_label: res += f"S->{node.success_label} "
                if node.failure_label: res += f"F->{node.failure_label}"
            return res

        if isinstance(node, MemoryAllocation):
            type_hint = f"  # Type: {node.type_hint}" if node.type_hint else ""
            return f"[0] * ({self._emit_raw(node.size)}){type_hint}"

        if isinstance(node, MemoryFree):
            return f"{padding}# [GC automatic reclamation: freed {self._emit_raw(node.argument)}]"

        if isinstance(node, Dereference):
            return f"{self._emit_raw(node.argument)}"

        if isinstance(node, OnCondition):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            return f"{padding}# ON {node.condition}:\n{padding}try:\n{body_str}\n{padding}except Exception as e: pass"

        if isinstance(node, TaskDeclaration):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}def task_{node.name}():\n{body_str}"

        if isinstance(node, ModuleDeclaration):
            body_str = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return f"{padding}# Module: {node.name}\n{body_str}"

        if isinstance(node, InterfaceDeclaration):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}class {node.name}:\n{body_str}"

        if isinstance(node, ImplDeclaration):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}# Implementation of {node.interface_name} for {node.target_type}:\n{body_str}"

        if isinstance(node, DeferStatement):
            body_str = "\n".join(self.emit(stmt, indent) for stmt in node.body)
            return f"{padding}# defer:\n{body_str}"

        if isinstance(node, EventDeclaration):
            params = ", ".join(p.name for p in node.params)
            return f"{padding}# Event: {node.name}({params})"

        if isinstance(node, EmitStatement):
            call_str = self._emit_raw(node.event_call)
            return f"{padding}# emit {call_str}"

        # --- Forth ---
        if isinstance(node, ForthWordDefinition):
            body_indent = indent + 1
            body_str = "\n".join(self.emit(stmt, body_indent) for stmt in node.body)
            if not body_str: body_str = f"{'    ' * body_indent}pass"
            return f"{padding}def {node.name}():\n{body_str}"

        if isinstance(node, ForthStackOp):
            op = node.operation
            if op == "DUP": return f"{padding}_stack.append(_stack[-1])"
            if op == "DROP": return f"{padding}_stack.pop()"
            if op == "SWAP": return f"{padding}_stack[-1], _stack[-2] = _stack[-2], _stack[-1]"
            if op == "OVER": return f"{padding}_stack.append(_stack[-2])"
            if op == "POP": return f"{padding}_stack.pop()"
            if op == ".": return f"{padding}print(_stack.pop())"
            if op in ["+", "-", "*", "/", "MOD"]:
                py_op = op if op != "MOD" else "%"
                return f"{padding}b = _stack.pop(); a = _stack.pop(); _stack.append(eval(f'{{a}} {py_op} {{b}}'))"
            return f"{padding}# Forth OP: {op}"

        # --- Prolog ---
        if isinstance(node, Fact):
            pred = getattr(node, 'predicate', getattr(node, 'name', 'fact'))
            args = ", ".join(self._emit_raw(a) for a in node.terms)
            table_name = f"{pred.upper()}_RELATION"
            return f"{padding}{table_name} = getattr(globals(), '{table_name}', [])\n{padding}{table_name}.append(({args}))\n{padding}def {pred}(*args): return args in {table_name}"

        if isinstance(node, PrologRule):
            return "\n".join(self.emit(c, indent) for c in node.clauses)

        if isinstance(node, PrologClause):
            head = self._emit_raw(node.head)
            body = ", ".join(self._emit_raw(b) for b in node.body)
            return f"{padding}# Rule: {head} :- {body}"

        if isinstance(node, Query):
            terms = ", ".join(self._emit_raw(t) for t in node.terms)
            return f"{padding}# Query: ?- {terms}"

        # --- ML ---
        if isinstance(node, MLDataTypeDeclaration):
            return f"{padding}class {node.name}:\n{'    ' * (indent + 1)}pass"
        if isinstance(node, MLValDeclaration):
            return self.emit(VariableDeclaration(name=node.name, initializer=node.initializer), indent)

        if isinstance(node, MLFunDeclaration):
            return self.emit(FunctionDeclaration(name=node.name, params=node.params, body=node.body), indent)

        if isinstance(node, MLCaseExpression):
            expr = self._emit_raw(node.expression)
            # Use Python 3.10 match if possible, otherwise if/else
            branches = []
            for b in node.branches:
                pat = self._emit_raw(b.pattern)
                body = self.emit(b.body, indent + 1).strip()
                branches.append(f"{padding}    case {pat}: return {body}")
            branches_str = "\n".join(branches)
            return f"{padding}match {expr}:\n{branches_str}"

        if isinstance(node, MLLetExpression):
            bindings = "\n".join(self.emit(b, indent) for b in node.bindings)
            body = self.emit(node.body, indent)
            return f"{bindings}\n{body}"

        if isinstance(node, LambdaExpression):
            params = ", ".join(p.name for p in node.params)
            return f"lambda {params}: {self._emit_raw(node.body)}"

        if isinstance(node, MapExpression):
            return f"map({self._emit_raw(node.function)}, {self._emit_raw(node.collection)})"

        if isinstance(node, FilterExpression):
            return f"filter({self._emit_raw(node.function)}, {self._emit_raw(node.collection)})"

        # --- RPG ---
        if isinstance(node, RPGIndicator):
            return f"{padding}{node.name}"

        if isinstance(node, RPGOperation):
            opcode = node.opcode.upper()
            f1 = self._emit_raw(node.factor1)
            f2 = self._emit_raw(node.factor2)
            res = self._emit_raw(node.result)
            if opcode == "ADD":
                return f"{padding}{res} = {f1 if f1 else res} + {f2}"
            if opcode == "MOVEL":
                return f"{padding}{res} = {f2}"
            if opcode == "DSPLY":
                return f"{padding}print({f1 if f1 else f2})"
            return f"{padding}{opcode}({f1}, {f2}, {res})"

        # Statements that aren't wrapped in padding yet
        if isinstance(node, (CallExpression, AwaitExpression, YieldExpression, BinaryExpression, MemberAccess, Literal, Identifier)):
             return f"{padding}{self._emit_raw(node)}"

        return f"{padding}# Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        # Recursive call without padding
        res = self.emit(node, 0)
        return res.strip()

    def _emit_param(self, p: Parameter) -> str:
        hint = f": {p.type_hint}" if p.type_hint else ""
        default = f"={self._emit_raw(p.default_value)}" if p.default_value else ""
        return f"{p.name}{hint}{default}"

    def _emit_comp_gen(self, g: ComprehensionGenerator) -> str:
        target = self._emit_raw(g.target)
        iterable = self._emit_raw(g.iterable)
        ifs = "".join(f" if {self._emit_raw(i)}" for i in g.ifs)
        return f"for {target} in {iterable}{ifs}"
