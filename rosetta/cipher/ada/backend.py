from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *

class AdaBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "ada"

    @property
    def style_guide(self) -> str:
        return "Ada 2005"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        padding = "   " * indent
        
        if isinstance(node, Program):
            return "\n".join(self.emit(stmt, indent) for stmt in node.body)
        
        if isinstance(node, ModuleDeclaration):
            body = "\n".join(self.emit(stmt, indent+1) for stmt in node.body)
            return f"{padding}PACKAGE {node.name} IS\n{body}\n{padding}END {node.name};"

        if isinstance(node, VariableDeclaration):
            init = f" := {self._emit_raw(node.initializer)}" if node.initializer else ""
            return f"{padding}{node.name} : {node.type_hint or 'Integer'}{init};"

        if isinstance(node, FunctionDeclaration):
            is_func = node.return_type is not None
            kw = "FUNCTION" if is_func else "PROCEDURE"
            params = "; ".join(f"{p.name} : {p.type_hint or 'Integer'}" for p in node.params)
            ret = f" RETURN {node.return_type}" if is_func else ""
            header = f"{padding}{kw} {node.name}({params}){ret} IS"
            
            decls = []
            stmts = []
            for s in node.body:
                if isinstance(s, (VariableDeclaration, FunctionDeclaration)):
                    decls.append(s)
                else:
                    stmts.append(s)
            
            decl_str = "\n".join(self.emit(d, indent+1) for d in decls)
            body_str = "\n".join(self.emit(s, indent+1) for s in stmts)
            
            return f"{header}\n{decl_str}\n{padding}BEGIN\n{body_str}\n{padding}END {node.name};"

        if isinstance(node, Assignment):
            return f"{padding}{self._emit_raw(node.target)} := {self._emit_raw(node.value)};"

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            args = ", ".join(self._emit_raw(arg) for arg in node.args)
            if callee == "print":
                return f"{padding}Ada.Text_IO.Put_Line({args});"
            return f"{padding}{callee}({args});"

        if isinstance(node, Identifier):
            return node.name

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            return str(node.value).upper() if isinstance(node.value, bool) else str(node.value)

        if isinstance(node, BinaryExpression):
            op_map = {
                "==": "=",
                "!=": "/=",
                "and": "AND",
                "or": "OR",
                "xor": "XOR",
                "not": "NOT"
            }
            op = op_map.get(node.operator.lower(), node.operator)
            return f"({self._emit_raw(node.left)} {op} {self._emit_raw(node.right)})"

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            consequent = "\n".join(self.emit(s, indent+1) for s in node.consequent)
            res = f"{padding}IF {cond} THEN\n{consequent}"
            if node.alternate:
                alternate = "\n".join(self.emit(s, indent+1) for s in node.alternate)
                res += f"\n{padding}ELSE\n{alternate}"
            return res + f"\n{padding}END IF;"

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{padding}WHILE {cond} LOOP\n{body}\n{padding}END LOOP;"

        if isinstance(node, ForInLoop):
            iterator = self._emit_raw(node.iterator)
            iterable = self._emit_raw(node.iterable)
            # range(1, 10) => 1 .. 10
            if isinstance(node.iterable, CallExpression) and self._emit_raw(node.iterable.callee) == "range":
                iterable = f"{self._emit_raw(node.iterable.args[0])} .. {self._emit_raw(node.iterable.args[1])}"
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{padding}FOR {iterator} IN {iterable} LOOP\n{body}\n{padding}END LOOP;"

        if isinstance(node, TaskDeclaration):
            return f"{padding}TASK {node.name};\n{padding}TASK BODY {node.name} IS\n{padding}BEGIN\n{padding}END {node.name};"

        if isinstance(node, TryCatch):
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            handlers = "\n".join(self.emit(h, indent+1) for h in node.handlers)
            return f"{padding}BEGIN\n{body}\n{padding}EXCEPTION\n{handlers}\n{padding}END;"

        if isinstance(node, ExceptionHandler):
            body = "\n".join(self.emit(s, indent+1) for s in node.body)
            return f"{padding}WHEN OTHERS =>\n{body}"

        return f"{padding}-- Unknown node: {type(node).__name__}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None: return ""
        res = self.emit(node, 0)
        return res.strip().strip(';')

AdaBackend = AdaBackend
