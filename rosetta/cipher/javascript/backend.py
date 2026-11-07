from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class JavaScriptBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "javascript"

    @property
    def style_guide(self) -> str:
        return "ES2024 Modern"

    def _contains_yield(self, node: RosettaNode) -> bool:
        if isinstance(node, YieldExpression):
            return True
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                if self._contains_yield(val): return True
            elif isinstance(val, list):
                for item in val:
                    if isinstance(item, RosettaNode) and self._contains_yield(item):
                        return True
        return False

    def emit(self, node: RosettaNode) -> str:
        if node is None: return ""
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt) for stmt in node.body)
        
        if isinstance(node, ArrayDeclaration):
            # JS doesn't have fixed-size arrays easily, use a comment
            return f"/* Array {node.name} of {node.type_hint} */ let {node.name} = [];"

        if isinstance(node, VariableDeclaration):
            kw = "const" if node.is_const else "let"
            init = f" = {self.emit(node.initializer)}" if node.initializer else ""
            return f"{kw} {node.name}{init};"

        if isinstance(node, MethodDeclaration):
            async_kw = "async " if node.is_async else ""
            static_kw = "static " if node.is_static else ""
            is_generator = any(self._contains_yield(stmt) for stmt in node.body)
            gen_star = "*" if is_generator else ""
            name = "constructor" if node.name == "__init__" else node.name
            params = ", ".join(p.name for p in node.params if p.name != "self")
            body = "\n    ".join(self.emit(stmt) for stmt in node.body)
            js_method = f"{static_kw}{async_kw}{gen_star}{name}({params}) {{\n    {body}\n  }}"
            if node.decorators:
                decorators_str = " ".join([f"@{self.emit(d)}" for d in node.decorators])
                return f"/* {decorators_str} */\n  {js_method}"
            return js_method

        if isinstance(node, FunctionDeclaration):
            async_kw = "async " if node.is_async else ""
            is_generator = any(self._contains_yield(stmt) for stmt in node.body)
            gen_star = "*" if is_generator else ""
            params = ", ".join(p.name for p in node.params)
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            js_func = f"{async_kw}function{gen_star} {node.name}({params}) {{\n  {body}\n}}"
            if node.decorators:
                for dec in reversed(node.decorators):
                    js_func = f"{node.name} = {self.emit(dec)}({js_func});"
            return js_func

        if isinstance(node, ClassDeclaration):
            extends = f" extends {node.bases[0]}" if node.bases else ""
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"class {node.name}{extends} {{\n  {body}\n}}"

        if isinstance(node, InterfaceDeclaration):
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"class {node.name} {{\n  {body}\n}}"

        if isinstance(node, ImplDeclaration):
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"class {node.target_type}_as_{node.interface_name} {{\n  {body}\n}}"

        if isinstance(node, ModuleDeclaration):
            body = "\n".join(self.emit(stmt) for stmt in node.body)
            pkg_cmt = f"/* Module {node.name} */\n" if node.name else ""
            return f"{pkg_cmt}{body}"

        if isinstance(node, ReturnStatement):
            return f"return {self.emit(node.value) if node.value else ''};"

        if isinstance(node, CallExpression):
            callee_str = self.emit(node.callee)
            # Refined heuristic: only 'new' if it's CamelCase (Starts with Uppercase AND has lowercase)
            # OR if it's specifically marked as a class (we could use metadata here if we had it)
            # Fortran subroutines are often ALL CAPS, so CamelCase check helps.
            is_camel_case = callee_str and callee_str[0].isupper() and any(c.islower() for c in callee_str)
            prefix = "new " if is_camel_case and "." not in callee_str else ""
            args = ", ".join(self.emit(arg) for arg in node.args)
            return f"{prefix}{callee_str}({args})"

        if isinstance(node, Identifier):
            if node.name == "print": return "console.log"
            if node.name == "self": return "this"
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, list):
                return "[" + ", ".join(self.emit(x) for x in node.value) + "]"
            if isinstance(node.value, str): return f"'{node.value}'"
            if isinstance(node.value, bool): return str(node.value).lower()
            return str(node.value)

        if isinstance(node, BinaryExpression):
            op = node.operator
            if op == " ": op = "+"
            if op in [".", "$"]:
                return f"({self.emit(node.left)} /* {op} */ {self.emit(node.right)})"
            return f"({self.emit(node.left)} {op} {self.emit(node.right)})"

        if isinstance(node, UnaryExpression):
            return f"{node.operator}{self.emit(node.argument)}"

        if isinstance(node, YieldExpression):
            return f"yield {self.emit(node.argument) if node.argument else ''}"

        if isinstance(node, WhileLoop):
            cond = self.emit(node.condition)
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"while ({cond}) {{\n  {body}\n}}"

        if isinstance(node, ForLoop):
            init = self.emit(node.initializer).strip(';')
            cond = self.emit(node.condition)
            inc = self.emit(node.increment).strip(';')
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"for ({init}; {cond}; {inc}) {{\n  {body}\n}}"

        if isinstance(node, ForInLoop):
            it = self.emit(node.iterator)
            coll = self.emit(node.iterable)
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"for (const {it} of {coll}) {{\n  {body}\n}}"

        if isinstance(node, EventDeclaration):
            params = ", ".join(self.emit(p) for p in node.params)
            return f"/* Event: {node.name}({params}) */"

        if isinstance(node, EmitStatement):
            call_str = self.emit(node.event_call)
            return f"/* emit */ {call_str};"

        if isinstance(node, ArrayDeclaration):
            # JS doesn't have fixed-size arrays easily, use a comment
            return f"/* Array {node.name} of {node.type_hint} */ let {node.name} = [];"

        if isinstance(node, ArrayAccess):
            indices = "][".join(self.emit(idx) for idx in node.index)
            return f"{self.emit(node.object)}[{indices}]"

        if isinstance(node, GlobalBlock):
            return f"/* Global block {node.name}: {', '.join(m.name for m in node.members)} */"

        if isinstance(node, FormatDeclaration):
            return f"/* Format {node.label}: {node.items} */"

        if isinstance(node, Label):
            return f"{node.name}: continue; // Label"

        if isinstance(node, GotoStatement):
            return f"/* GOTO {node.label} - JS does not support GOTO */"

        if isinstance(node, IfStatement):
            consequent = "\n    ".join(self.emit(stmt) for stmt in node.consequent)
            js = f"if ({self.emit(node.condition)}) {{\n    {consequent}\n  }}"
            if node.alternate:
                alternate = "\n    ".join(self.emit(stmt) for stmt in node.alternate)
                js += f" else {{\n    {alternate}\n  }}"
            return js

        if isinstance(node, LambdaExpression):
            params = ", ".join(p.name for p in node.params)
            body = self.emit(node.body)
            return f"({params}) => {body}"

        if isinstance(node, MapExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.map({param} => {body})"

        if isinstance(node, FilterExpression):
            param = node.function.params[0].name
            body = self.emit(node.function.body)
            return f"{self.emit(node.collection)}.filter({param} => {body})"

        if isinstance(node, ListComprehension):
            # Fallback if normalization pass was skipped
            gen = node.generators[0]
            iterable = self.emit(gen.iterable)
            target = self.emit(gen.target)
            expr = self.emit(node.expression)
            res = iterable
            for if_cond in gen.ifs:
                res += f".filter({target} => {self.emit(if_cond)})"
            res += f".map({target} => {expr})"
            return res

        if isinstance(node, AwaitExpression):
            return f"await {self.emit(node.argument)}"

        if isinstance(node, MemberAccess):
            return f"{self.emit(node.object)}.{node.member}"

        if isinstance(node, SNOBOLStatement):
            label_str = f"{node.label}: " if node.label else ""
            content_str = self.emit(node.content).strip() if node.content else ""
            transfer_str = f" /* {self.emit(node.transfer)} */" if node.transfer else ""
            return f"{label_str}{content_str}{transfer_str}"

        if isinstance(node, PatternMatchStatement):
            subj = self.emit(node.subject)
            pat = self.emit(node.pattern)
            if node.replacement:
                repl = self.emit(node.replacement)
                return f"if ({subj}.includes({pat})) {subj} = {subj}.replace({pat}, {repl})"
            return f"{subj}.includes({pat})"

        if isinstance(node, SNOBOLTransfer):
            res = "GOTO: "
            if node.unconditional_label: res += node.unconditional_label
            else:
                if node.success_label: res += f"S->{node.success_label} "
                if node.failure_label: res += f"F->{node.failure_label}"
            return res

        if isinstance(node, MemoryAllocation):
            type_hint = f" /* Type: {node.type_hint} */" if node.type_hint else ""
            return f"new Array({self.emit(node.size)}).fill(0){type_hint}"

        if isinstance(node, MemoryFree):
            return f"/* [GC automatic reclamation: freed {self.emit(node.argument)}] */"

        if isinstance(node, Dereference):
            return f"{self.emit(node.argument)}"

        if isinstance(node, OnCondition):
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"/* ON {node.condition}: */\ntry {{\n  {body}\n}} catch (e) {{}}"

        # --- Forth ---
        if isinstance(node, ForthWordDefinition):
            body = "\n  ".join(self.emit(stmt) for stmt in node.body)
            return f"function {node.name}() {{\n  {body}\n}}"

        if isinstance(node, ForthStackOp):
            op = node.operation
            if op == "DUP": return "_stack.push(_stack[_stack.length - 1]);"
            if op == "DROP": return "_stack.pop();"
            if op == "SWAP": return "[_stack[_stack.length-1], _stack[_stack.length-2]] = [_stack[_stack.length-2], _stack[_stack.length-1]];"
            if op == "OVER": return "_stack.push(_stack[_stack.length - 2]);"
            if op == "POP": return "_stack.pop();"
            if op == ".": return "console.log(_stack.pop());"
            if op in ["+", "-", "*", "/", "MOD"]:
                js_op = op if op != "MOD" else "%"
                return f"{{ let b = _stack.pop(); let a = _stack.pop(); _stack.push(eval(`${{a}} {js_op} ${{b}}`)); }}"
            return f"/* Forth OP: {op} */"

        # --- ML ---
        if isinstance(node, MLValDeclaration):
            return self.emit(VariableDeclaration(name=node.name, initializer=node.initializer))

        if isinstance(node, MLFunDeclaration):
            return self.emit(FunctionDeclaration(name=node.name, params=node.params, body=node.body))

        if isinstance(node, MLCaseExpression):
            expr = self.emit(node.expression)
            branches = []
            for b in node.branches:
                pat = self.emit(b.pattern)
                body = self.emit(b.body)
                branches.append(f"if ({expr} === {pat}) return {body};")
            return "\n".join(branches)

        if isinstance(node, MLLetExpression):
            bindings = "\n".join(self.emit(b) for b in node.bindings)
            body = self.emit(node.body)
            return f"{{\n{bindings}\n  return {body};\n}}"

        # --- RPG ---
        if isinstance(node, RPGOperation):
            opcode = node.opcode.upper()
            f1 = self.emit(node.factor1)
            f2 = self.emit(node.factor2)
            res = self.emit(node.result)
            if opcode == "ADD":
                return f"{res} = {(f1 if f1 else res)} + {f2};"
            if opcode == "MOVEL":
                return f"{res} = {f2};"
            if opcode == "DSPLY":
                return f"console.log({f1 if f1 else f2});"
            return f"{opcode}({f1}, {f2}, {res});"

        if isinstance(node, Assignment):
            target_str = self.emit(node.target)
            return f"{target_str} = {self.emit(node.value)};"

        if isinstance(node, LambdaExpression):
            params = ", ".join(p.name for p in node.params)
            body = self.emit(node.body)
            return f"({params}) => {body}"

        return f"/* Unknown node: {type(node).__name__} */"
