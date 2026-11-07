"""
rosetta/cipher/base/universal.py
--------------------------------
Spec-driven CIPHER backend base class.

New target languages only need to declare their syntax (keywords, block
delimiters, type map, literal spellings) and override the few constructs that
differ structurally (functions, classes, print, program wrapper). Everything
else (expressions, control flow, blocks, indentation) is shared.
"""
from __future__ import annotations

from typing import Dict, List, Optional

from rosetta.cipher.base.base import CipherBackend
from rosetta.ir.nodes import (
    ArrayAccess,
    Assignment,
    BinaryExpression,
    CallExpression,
    ClassDeclaration,
    Dereference,
    ForInLoop,
    ForLoop,
    FunctionDeclaration,
    Identifier,
    IfStatement,
    Literal,
    MemberAccess,
    MethodDeclaration,
    Parameter,
    Program,
    ReturnStatement,
    RosettaNode,
    StructDeclaration,
    UnaryExpression,
    VariableDeclaration,
    WhileLoop,
)

_DECL_TYPES = (FunctionDeclaration, ClassDeclaration, StructDeclaration)


class UniversalBackend(CipherBackend):
    # ---- identity -------------------------------------------------------
    LANG = "universal"
    STYLE = "Rosetta Universal"

    # ---- lexical spec ---------------------------------------------------
    INDENT = "    "
    STMT_END = ";"
    COMMENT = "//"
    TRUE, FALSE, NULL = "true", "false", "null"
    AND, OR, NOT = "&&", "||", "!"
    OP_MAP: Dict[str, str] = {}
    CONCAT: Optional[str] = None  # string concatenation operator if not "+"
    QUOTE = '"'
    LIST_OPEN, LIST_CLOSE = "[", "]"
    VAR_SIGIL = ""  # prefix for variable references (bash `$`, perl `$`, sql `@`)
    TYPES: Dict[str, str] = {}
    DEFAULT_TYPE = ""

    # ---- block spec (format strings: {c}=condition, {i}=iterator) -------
    IF_OPEN = "if ({c}) {{"
    ELSEIF = "}} else if ({c}) {{"
    ELSE = "}} else {{"
    IF_CLOSE = "}"
    WHILE_OPEN = "while ({c}) {{"
    FORIN_OPEN = "for ({i} in {c}) {{"
    LOOP_CLOSE = "}"
    BLOCK_CLOSE = "}"
    EMPTY_BODY = ""

    # ---- top-level program wrapping -------------------------------------
    HEADER = ""
    FOOTER = ""

    # =====================================================================
    @property
    def language_id(self) -> str:
        return self.LANG

    @property
    def style_guide(self) -> str:
        return self.STYLE

    def emit(self, node: RosettaNode, indent: int = 0) -> str:
        if node is None:
            return ""
        if isinstance(node, Program):
            return self.program(node).rstrip() + "\n"
        if self._is_statement(node):
            return self.stmt(node, indent)
        return self.expr(node)

    # ---- program --------------------------------------------------------
    def program(self, node: Program) -> str:
        decls = [s for s in node.body if isinstance(s, _DECL_TYPES)]
        stmts = [s for s in node.body if not isinstance(s, _DECL_TYPES)]
        return self.wrap_program(decls, stmts)

    def wrap_program(self, decls: List[RosettaNode], stmts: List[RosettaNode]) -> str:
        parts = [self.stmt(d, 0) for d in decls] + [self.stmt(s, 0) for s in stmts]
        return self.HEADER + "\n".join(p for p in parts if p) + self.FOOTER

    # ---- helpers --------------------------------------------------------
    def pad(self, indent: int) -> str:
        return self.INDENT * indent

    def block(self, stmts: List[RosettaNode], indent: int) -> str:
        lines = [self.stmt(s, indent) for s in (stmts or [])]
        lines = [l for l in lines if l.strip()]
        if not lines:
            return self.pad(indent) + self.EMPTY_BODY if self.EMPTY_BODY else ""
        return "\n".join(lines)

    def _join(self, *parts: str) -> str:
        return "\n".join(p for p in parts if p != "")

    def type_of(self, t: Optional[str]) -> str:
        if not t:
            return self.DEFAULT_TYPE
        return self.TYPES.get(t, t)

    def infer_type(self, node: VariableDeclaration) -> Optional[str]:
        if node.type_hint:
            return node.type_hint
        init = node.initializer
        if isinstance(init, Literal):
            v = init.value
            if isinstance(v, bool):
                return "bool"
            if isinstance(v, int):
                return "int"
            if isinstance(v, float):
                return "float"
            if isinstance(v, str):
                return "str"
            if isinstance(v, list):
                return "list"
        return None

    @staticmethod
    def is_print(node: RosettaNode) -> bool:
        return (
            isinstance(node, CallExpression)
            and isinstance(node.callee, Identifier)
            and node.callee.name in ("print", "println", "puts", "echo")
        )

    @staticmethod
    def is_str(node: RosettaNode) -> bool:
        return isinstance(node, Literal) and isinstance(node.value, str)

    def _is_statement(self, node: RosettaNode) -> bool:
        return isinstance(
            node,
            (
                VariableDeclaration,
                Assignment,
                FunctionDeclaration,
                ClassDeclaration,
                StructDeclaration,
                ReturnStatement,
                IfStatement,
                WhileLoop,
                ForLoop,
                ForInLoop,
            ),
        ) or self.is_print(node)

    # ---- statements -----------------------------------------------------
    def stmt(self, node: RosettaNode, indent: int, in_class: Optional[str] = None) -> str:
        p = self.pad(indent)
        if isinstance(node, VariableDeclaration):
            return self.var_decl(node, indent, in_class)
        if isinstance(node, Assignment):
            return f"{p}{self.target(node.target)} = {self.expr(node.value)}{self.STMT_END}"
        if isinstance(node, FunctionDeclaration):
            return self.func(node, indent, in_class)
        if isinstance(node, ClassDeclaration):
            return self.klass(node, indent)
        if isinstance(node, StructDeclaration):
            return self.klass(ClassDeclaration(name=node.name, body=list(node.fields)), indent)
        if isinstance(node, ReturnStatement):
            return self.ret(node, indent)
        if isinstance(node, IfStatement):
            return self.if_stmt(node, indent)
        if isinstance(node, WhileLoop):
            return self.while_loop(node, indent)
        if isinstance(node, ForInLoop):
            return self.for_in(node, indent)
        if isinstance(node, ForLoop):
            return self.for_loop(node, indent)
        if self.is_print(node):
            return p + self.print_stmt(node.args)
        return f"{p}{self.expr(node)}{self.STMT_END}"

    def target(self, node: RosettaNode) -> str:
        return self.expr(node)

    def var_decl(self, node: VariableDeclaration, indent: int, in_class: Optional[str] = None) -> str:
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        return f"{self.pad(indent)}var {node.name}{init}{self.STMT_END}"

    def ret(self, node: ReturnStatement, indent: int) -> str:
        val = f" {self.expr(node.value)}" if node.value is not None else ""
        return f"{self.pad(indent)}return{val}{self.STMT_END}"

    def print_stmt(self, args: List[RosettaNode]) -> str:
        return f"print({', '.join(self.expr(a) for a in args)}){self.STMT_END}"

    def if_stmt(self, node: IfStatement, indent: int, chained: bool = False) -> str:
        p = self.pad(indent)
        head = (self.ELSEIF if chained else self.IF_OPEN).format(c=self.cond(node.condition))
        out = [p + head, self.block(node.consequent, indent + 1)]
        alt = node.alternate
        if alt:
            if len(alt) == 1 and isinstance(alt[0], IfStatement) and self.ELSEIF:
                out.append(self.if_stmt(alt[0], indent, chained=True))
                return self._join(*out)
            out += [p + self.ELSE.format(), self.block(alt, indent + 1)]
        out.append(p + self.IF_CLOSE)
        return self._join(*out)

    def cond(self, node: RosettaNode) -> str:
        return self.expr(node)

    def while_loop(self, node: WhileLoop, indent: int) -> str:
        p = self.pad(indent)
        return self._join(
            p + self.WHILE_OPEN.format(c=self.cond(node.condition)),
            self.block(node.body, indent + 1),
            p + self.LOOP_CLOSE,
        )

    def for_in(self, node: ForInLoop, indent: int) -> str:
        p = self.pad(indent)
        return self._join(
            p + self.FORIN_OPEN.format(i=self.expr(node.iterator).lstrip(self.VAR_SIGIL) if self.VAR_SIGIL else self.expr(node.iterator), c=self.expr(node.iterable)),
            self.block(node.body, indent + 1),
            p + self.LOOP_CLOSE,
        )

    def for_loop(self, node: ForLoop, indent: int) -> str:
        # Lower C-style for loops to init + while for maximum portability.
        out = []
        if node.initializer is not None:
            out.append(self.stmt(node.initializer, indent))
        body = list(node.body or [])
        if node.increment is not None:
            body.append(node.increment)
        cond = node.condition if node.condition is not None else Literal(value=True)
        out.append(self.while_loop(WhileLoop(condition=cond, body=body), indent))
        return self._join(*out)

    def func(self, node: FunctionDeclaration, indent: int, in_class: Optional[str] = None) -> str:
        p = self.pad(indent)
        params = ", ".join(self.param(x) for x in self.real_params(node))
        return self._join(
            f"{p}function {node.name}({params}) {{",
            self.block(node.body, indent + 1),
            p + self.BLOCK_CLOSE,
        )

    def real_params(self, node: FunctionDeclaration) -> List[Parameter]:
        return [x for x in node.params if x.name not in ("self", "this")]

    def has_value_return(self, stmts: Optional[List[RosettaNode]]) -> bool:
        for s in stmts or []:
            if isinstance(s, ReturnStatement) and s.value is not None:
                return True
            if isinstance(s, (FunctionDeclaration, ClassDeclaration)):
                continue
            for attr in ("consequent", "alternate", "body"):
                sub = getattr(s, attr, None)
                if isinstance(sub, list) and self.has_value_return(sub):
                    return True
        return False

    def ret_type(self, node: FunctionDeclaration, unknown: str, void: str) -> str:
        rt = node.return_type
        if rt == "None":
            return void
        if rt:
            return self.type_of(rt)
        return unknown if self.has_value_return(node.body) else void

    @staticmethod
    def split_decls(decls: List[RosettaNode]):
        classes = [d for d in decls if isinstance(d, (ClassDeclaration, StructDeclaration))]
        funcs = [d for d in decls if isinstance(d, FunctionDeclaration)]
        return classes, funcs

    def param(self, prm: Parameter) -> str:
        return prm.name

    def klass(self, node: ClassDeclaration, indent: int) -> str:
        p = self.pad(indent)
        base = f" extends {node.bases[0]}" if node.bases else ""
        members = [self.stmt(s, indent + 1, in_class=node.name) for s in node.body]
        return self._join(f"{p}class {node.name}{base} {{", *members, p + "}")

    # ---- expressions ----------------------------------------------------
    def expr(self, node: RosettaNode) -> str:
        if node is None:
            return ""
        if isinstance(node, Identifier):
            return self.ident(node.name)
        if isinstance(node, Literal):
            return self.literal(node.value)
        if isinstance(node, BinaryExpression):
            return self.binary(node)
        if isinstance(node, UnaryExpression):
            if node.operator in ("not", "!"):
                sep = " " if self.NOT.isalpha() else ""
                return f"{self.NOT}{sep}{self.expr(node.argument)}"
            return f"{node.operator}{self.expr(node.argument)}"
        if isinstance(node, CallExpression):
            if self.is_print(node):
                return self.print_stmt(node.args).rstrip(self.STMT_END) if self.STMT_END else self.print_stmt(node.args)
            return self.call(node)
        if isinstance(node, MemberAccess):
            return f"{self.expr(node.object)}.{node.member}"
        if isinstance(node, ArrayAccess):
            idx = ", ".join(self.expr(i) for i in node.index)
            return f"{self.expr(node.object)}[{idx}]"
        if isinstance(node, Dereference):
            return self.expr(node.argument)
        if isinstance(node, VariableDeclaration):
            return self.var_decl(node, 0).strip()
        if isinstance(node, Assignment):
            return self.stmt(node, 0).strip()
        return f"{self.COMMENT} unsupported: {type(node).__name__}"

    def ident(self, name: str) -> str:
        if name in ("self", "this"):
            return self.self_name()
        return f"{self.VAR_SIGIL}{name}"

    def self_name(self) -> str:
        return "this"

    def callee(self, node: RosettaNode) -> str:
        if isinstance(node, Identifier):
            return node.name
        if isinstance(node, MemberAccess):
            return f"{self.expr(node.object)}.{node.member}"
        return self.expr(node)

    def call(self, node: CallExpression) -> str:
        args = ", ".join(self.expr(a) for a in node.args)
        return f"{self.callee(node.callee)}({args})"

    def string(self, s: str) -> str:
        q = self.QUOTE
        esc = s.replace("\\", "\\\\").replace(q, "\\" + q)
        return f"{q}{esc}{q}"

    def literal(self, v) -> str:
        if isinstance(v, bool):
            return self.TRUE if v else self.FALSE
        if v is None:
            return self.NULL
        if isinstance(v, str):
            return self.string(v)
        if isinstance(v, list):
            return self.list_lit(v)
        return str(v)

    def list_lit(self, items: list) -> str:
        inner = ", ".join(self.expr(x) if isinstance(x, RosettaNode) else self.literal(x) for x in items)
        return f"{self.LIST_OPEN}{inner}{self.LIST_CLOSE}"

    def map_op(self, op: str) -> str:
        if op in ("&&", "and"):
            return self.AND
        if op in ("||", "or"):
            return self.OR
        return self.OP_MAP.get(op, op)

    def operand(self, node: RosettaNode) -> str:
        s = self.expr(node)
        return f"({s})" if isinstance(node, BinaryExpression) else s

    def binary(self, node: BinaryExpression) -> str:
        left, right = self.operand(node.left), self.operand(node.right)
        op = node.operator
        if op == "+" and self.CONCAT and (self.is_str(node.left) or self.is_str(node.right)):
            return f"{left} {self.CONCAT} {right}"
        return f"{left} {self.map_op(op)} {right}"
