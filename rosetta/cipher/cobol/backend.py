from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import *


class CobolBackend(CipherBackend):
    @property
    def language_id(self) -> str:
        return "cobol"

    @property
    def style_guide(self) -> str:
        return "ANS COBOL-85 / ISO COBOL-2002"

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""
        padding = "    " * indent

        if isinstance(node, Program):
            ws_items = []
            proc_items = []
            paragraphs = []

            for stmt in node.body:
                if isinstance(stmt, VariableDeclaration):
                    ws_items.append(self._emit_working_storage(stmt))
                elif isinstance(stmt, ArrayDeclaration):
                    ws_items.append(self._emit_array_storage(stmt))
                elif isinstance(stmt, (FunctionDeclaration, MethodDeclaration, ForthWordDefinition, TaskDeclaration)):
                    paragraphs.append(self._emit_paragraph(stmt))
                elif isinstance(stmt, ClassDeclaration):
                    for member in stmt.body:
                        if isinstance(member, VariableDeclaration):
                            ws_items.append(self._emit_working_storage(member))
                        elif isinstance(member, (MethodDeclaration, FunctionDeclaration)):
                            paragraphs.append(self._emit_paragraph(member))
                else:
                    emitted = self.emit(stmt, 2)
                    if emitted.strip():
                        proc_items.append(emitted)

            lines = [
                "       IDENTIFICATION DIVISION.",
                "       PROGRAM-ID. ROSETTA-OUT.",
                "       DATA DIVISION.",
                "       WORKING-STORAGE SECTION.",
            ]
            if ws_items:
                lines.extend(ws_items)
            else:
                lines.append("       01 WS-TEMP PIC S9(9) VALUE 0.")

            lines.append("       PROCEDURE DIVISION.")
            lines.append("       MAIN-PARAGRAPH.")
            if proc_items:
                lines.extend(proc_items)
            elif paragraphs:
                first_name = self._cobol_name(getattr(node.body[0], "name", "MAIN-LOGIC"))
                lines.append(f"           PERFORM {first_name}.")
            lines.append("           STOP RUN.")

            if paragraphs:
                lines.extend(paragraphs)

            return "\n".join(lines)

        if isinstance(node, VariableDeclaration):
            if node.initializer is not None:
                return f"           MOVE {self._emit_raw(node.initializer)} TO {self._cobol_name(node.name)}."
            return f"      *    VAR {self._cobol_name(node.name)}"

        if isinstance(node, Assignment):
            target = self._cobol_name(self._emit_raw(node.target))
            if isinstance(node.value, BinaryExpression):
                return f"           COMPUTE {target} = {self._emit_raw(node.value)}."
            return f"           MOVE {self._emit_raw(node.value)} TO {target}."

        if isinstance(node, CallExpression):
            callee = self._emit_raw(node.callee)
            if callee in ("print", "DISPLAY", "println", "console.log"):
                args = " ".join(self._emit_raw(a) for a in node.args)
                return f"           DISPLAY {args}."
            return f"           PERFORM {self._cobol_name(callee)}."

        if isinstance(node, ReturnStatement):
            if node.value:
                return f"           MOVE {self._emit_raw(node.value)} TO WS-TEMP.\n           GOBACK."
            return "           GOBACK."

        if isinstance(node, IfStatement):
            cond = self._emit_raw(node.condition)
            cons = "\n".join(self.emit(s, indent + 1) for s in node.consequent)
            res = f"           IF {cond} THEN\n{cons}"
            if node.alternate:
                alt = "\n".join(self.emit(s, indent + 1) for s in node.alternate)
                res += f"\n           ELSE\n{alt}"
            res += "\n           END-IF."
            return res

        if isinstance(node, WhileLoop):
            cond = self._emit_raw(node.condition)
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"           PERFORM UNTIL NOT ({cond})\n{body}\n           END-PERFORM."

        if isinstance(node, (ForLoop, ForInLoop)):
            body = "\n".join(self.emit(s, indent + 1) for s in node.body)
            return f"           PERFORM\n{body}\n           END-PERFORM."

        if isinstance(node, Identifier):
            return self._cobol_name(node.name)

        if isinstance(node, Literal):
            if isinstance(node.value, str):
                return f'"{node.value}"'
            if isinstance(node.value, bool):
                return '"TRUE"' if node.value else '"FALSE"'
            return str(node.value)

        if isinstance(node, BinaryExpression):
            return f"{self._emit_raw(node.left)} {node.operator} {self._emit_raw(node.right)}"

        if isinstance(node, UnaryExpression):
            return f"{node.operator} {self._emit_raw(node.argument)}"

        if isinstance(node, Label):
            return f"       {self._cobol_name(node.name)}."

        if isinstance(node, GotoStatement):
            return f"           GO TO {self._cobol_name(node.label)}."

        if isinstance(node, RPGOperation):
            op = node.opcode.upper()
            f1 = self._emit_raw(node.factor1)
            f2 = self._emit_raw(node.factor2)
            res = self._emit_raw(node.result)
            if op == "ADD":
                return f"           ADD {f2} TO {res}."
            if op == "MOVEL":
                return f"           MOVE {f2} TO {res}."
            if op == "DSPLY":
                return f"           DISPLAY {f1 or f2}."
            return f"      *    RPG {op} {f1} {f2} {res}"

        if isinstance(node, Fact):
            pred = getattr(node, "predicate", getattr(node, "name", "fact"))
            args = " ".join(self._emit_raw(t) for t in node.terms)
            return f'           DISPLAY "FACT {pred}: " {args}.'

        if isinstance(node, ForthStackOp):
            return f'           DISPLAY "FORTH-OP {node.operation}".'

        return f"      *    {type(node).__name__}"

    def _emit_working_storage(self, node: VariableDeclaration) -> str:
        name = self._cobol_name(node.name)
        pic = "PIC S9(9)"
        val_clause = ""
        if node.type_hint in ("str", "string", "String"):
            pic = "PIC X(64)"
        elif node.type_hint in ("float", "double", "f64"):
            pic = "PIC S9(9)V9(4)"
        elif isinstance(node.initializer, Literal) and isinstance(node.initializer.value, str):
            pic = "PIC X(64)"

        if isinstance(node.initializer, Literal):
            if isinstance(node.initializer.value, str):
                val_clause = f' VALUE "{node.initializer.value}"'
            elif isinstance(node.initializer.value, (int, float)):
                val_clause = f" VALUE {node.initializer.value}"
        return f"       01 {name} {pic}{val_clause}."

    def _emit_array_storage(self, node: ArrayDeclaration) -> str:
        name = self._cobol_name(node.name)
        dim = self._emit_raw(node.dimensions[0]) if node.dimensions else "10"
        return f"       01 {name}-TABLE.\n          05 {name} PIC S9(9) OCCURS {dim} TIMES."

    def _emit_paragraph(self, node: FunctionDeclaration) -> str:
        name = self._cobol_name(node.name)
        body_lines = [self.emit(s, 2) for s in node.body]
        body_str = "\n".join(b for b in body_lines if b.strip())
        if not body_str:
            body_str = "           CONTINUE."
        return f"       {name}.\n{body_str}"

    def _emit_raw(self, node: RosettaNode) -> str:
        if node is None:
            return ""
        return self.emit(node, 0).strip().rstrip(".")

    def _cobol_name(self, name: str) -> str:
        if not name:
            return "WS-VAR"
        cleaned = name.replace("_", "-").upper()
        if cleaned[0].isdigit():
            cleaned = "L-" + cleaned
        return cleaned
