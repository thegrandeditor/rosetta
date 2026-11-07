"""
rosetta/cipher/universal/backends.py
------------------------------------
CIPHER backends for the Rosetta universal language expansion:

    C#, Dart, Lua, R, Julia, Scala, Haskell, Elixir, Bash,
    SQL (T-SQL), Objective-C, Move, Perl

Each backend is built on :class:`UniversalBackend` and only declares the syntax
that differs from the shared C-family defaults.
"""
from __future__ import annotations

from typing import Dict, List, Optional

from rosetta.cipher.base.universal import UniversalBackend
from rosetta.ir.nodes import (
    Assignment,
    BinaryExpression,
    CallExpression,
    ClassDeclaration,
    ForInLoop,
    FunctionDeclaration,
    Identifier,
    IfStatement,
    Literal,
    MemberAccess,
    Parameter,
    ReturnStatement,
    RosettaNode,
    StructDeclaration,
    UnaryExpression,
    VariableDeclaration,
    WhileLoop,
)

_CTOR_NAMES = ("__init__", "constructor", "init", "new")


def _ctor_and_members(node: ClassDeclaration):
    """Split a class body into (fields, constructor, methods)."""
    fields = [s for s in node.body if isinstance(s, VariableDeclaration)]
    funcs = [s for s in node.body if isinstance(s, FunctionDeclaration)]
    ctor = next((f for f in funcs if f.name in _CTOR_NAMES or f.name == node.name), None)
    methods = [f for f in funcs if f is not ctor]
    return fields, ctor, methods


# =============================================================================
# C#
# =============================================================================
class CSharpBackend(UniversalBackend):
    LANG, STYLE = "csharp", "Microsoft C# Coding Conventions"
    TYPES = {"int": "int", "float": "double", "str": "string", "bool": "bool",
             "list": "List<object>", "None": "void"}
    FORIN_OPEN = "foreach (var {i} in {c}) {{"
    HEADER = "using System;\nusing System.Collections.Generic;\n\n"

    def list_lit(self, items):
        inner = ", ".join(self.expr(x) for x in items)
        return f"new List<object> {{ {inner} }}"

    def var_decl(self, node, indent, in_class=None):
        p = self.pad(indent)
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        t = self.infer_type(node)
        if in_class:
            return f"{p}public {self.type_of(t) if t else 'dynamic'} {node.name}{init};"
        if node.initializer is None:
            return f"{p}{self.type_of(t) if t else 'dynamic'} {node.name};"
        return f"{p}var {node.name}{init};"

    def param(self, prm):
        return f"{self.type_of(prm.type_hint) if prm.type_hint else 'dynamic'} {prm.name}"

    def print_stmt(self, args):
        if len(args) == 1:
            return f"Console.WriteLine({self.expr(args[0])});"
        return f"Console.WriteLine(string.Join(\" \", {', '.join(self.expr(a) for a in args)}));"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        ret = self.ret_type(node, "dynamic", "void")
        params = ", ".join(self.param(x) for x in self.real_params(node))
        if in_class and (node.name in _CTOR_NAMES or node.name == in_class):
            head = f"{p}public {in_class}({params}) {{"
        else:
            static = "" if in_class else "static "
            head = f"{p}public {static}{ret} {node.name}({params}) {{"
        return self._join(head, self.block(node.body, indent + 1), p + "}")

    def klass(self, node, indent):
        p = self.pad(indent)
        base = f" : {node.bases[0]}" if node.bases else ""
        members = [self.stmt(s, indent + 1, in_class=node.name) for s in node.body]
        return self._join(f"{p}public class {node.name}{base} {{", *members, p + "}") + "\n"

    def wrap_program(self, decls, stmts):
        classes, funcs = self.split_decls(decls)
        out = [self.HEADER.rstrip("\n") + "\n"]
        out += [self.klass(c if isinstance(c, ClassDeclaration) else ClassDeclaration(name=c.name, body=list(c.fields)), 0) for c in classes]
        out.append("public class Program {")
        out += [self.func(f, 1) + "\n" for f in funcs]
        out.append("    public static void Main(string[] args) {")
        out.append(self.block(stmts, 2))
        out.append("    }")
        out.append("}")
        return self._join(*out)


# =============================================================================
# Dart
# =============================================================================
class DartBackend(UniversalBackend):
    LANG, STYLE = "dart", "Effective Dart"
    TYPES = {"int": "int", "float": "double", "str": "String", "bool": "bool",
             "list": "List<dynamic>", "None": "void"}
    QUOTE = "'"
    FORIN_OPEN = "for (var {i} in {c}) {{"

    def string(self, s):
        return "'" + s.replace("\\", "\\\\").replace("'", "\\'").replace("$", "\\$") + "'"

    def var_decl(self, node, indent, in_class=None):
        p = self.pad(indent)
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        t = self.infer_type(node)
        if node.initializer is None or in_class:
            kw = self.type_of(t) if t else "dynamic"
        else:
            kw = "final" if node.is_const else "var"
        return f"{p}{kw} {node.name}{init};"

    def param(self, prm):
        return f"{self.type_of(prm.type_hint) if prm.type_hint else 'dynamic'} {prm.name}"

    def print_stmt(self, args):
        if len(args) == 1:
            return f"print({self.expr(args[0])});"
        return f"print([{', '.join(self.expr(a) for a in args)}].join(' '));"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = ", ".join(self.param(x) for x in self.real_params(node))
        if in_class and (node.name in _CTOR_NAMES or node.name == in_class):
            head = f"{p}{in_class}({params}) {{"
        else:
            head = f"{p}{self.ret_type(node, 'dynamic', 'void')} {node.name}({params}) {{"
        return self._join(head, self.block(node.body, indent + 1), p + "}")

    def wrap_program(self, decls, stmts):
        out = [self.stmt(d, 0) + "\n" for d in decls]
        if stmts:
            out += ["void main() {", self.block(stmts, 1), "}"]
        return self._join(*out)


# =============================================================================
# Lua
# =============================================================================
class LuaBackend(UniversalBackend):
    LANG, STYLE = "lua", "Lua Style Guide (Olivine Labs)"
    STMT_END, COMMENT = "", "--"
    NULL = "nil"
    AND, OR, NOT = "and", "or", "not"
    OP_MAP = {"!=": "~="}
    CONCAT = ".."
    LIST_OPEN, LIST_CLOSE = "{", "}"
    IF_OPEN, ELSEIF, ELSE, IF_CLOSE = "if {c} then", "elseif {c} then", "else", "end"
    WHILE_OPEN, LOOP_CLOSE, BLOCK_CLOSE = "while {c} do", "end", "end"
    FORIN_OPEN = "for _, {i} in ipairs({c}) do"
    _LIBS = {"math", "string", "table", "os", "io", "coroutine", "utf8", "debug"}

    def self_name(self):
        return "self"

    def callee(self, node):
        if isinstance(node, MemberAccess):
            obj = node.object
            if isinstance(obj, Identifier) and obj.name in self._LIBS:
                return f"{obj.name}.{node.member}"
            return f"{self.expr(obj)}:{node.member}"
        return super().callee(node)

    def var_decl(self, node, indent, in_class=None):
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        return f"{self.pad(indent)}local {node.name}{init}"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = ", ".join(x.name for x in self.real_params(node))
        head = f"{p}function {in_class}:{node.name}({params})" if in_class else f"{p}local function {node.name}({params})"
        return self._join(head, self.block(node.body, indent + 1), p + "end")

    def klass(self, node, indent):
        p = self.pad(indent)
        fields, ctor, methods = _ctor_and_members(node)
        cparams = ", ".join(x.name for x in self.real_params(ctor)) if ctor else ""
        out = [f"{p}local {node.name} = {{}}", f"{p}{node.name}.__index = {node.name}", ""]
        if node.bases:
            out.insert(1, f"{p}setmetatable({node.name}, {{ __index = {node.bases[0]} }})")
        out.append(f"{p}function {node.name}.new({cparams})")
        out.append(f"{p}    local self = setmetatable({{}}, {node.name})")
        for f in fields:
            out.append(f"{p}    self.{f.name} = {self.expr(f.initializer) if f.initializer is not None else 'nil'}")
        if ctor:
            body = self.block(ctor.body, indent + 1)
            if body:
                out.append(body)
        out += [f"{p}    return self", f"{p}end", ""]
        out += [self.func(m, indent, in_class=node.name) + "\n" for m in methods]
        return self._join(*out)


# =============================================================================
# R
# =============================================================================
class RBackend(UniversalBackend):
    LANG, STYLE = "r", "Tidyverse Style Guide"
    STMT_END, COMMENT = "", "#"
    TRUE, FALSE, NULL = "TRUE", "FALSE", "NULL"
    LIST_OPEN, LIST_CLOSE = "c(", ")"
    INDENT = "  "

    def self_name(self):
        return ".self"

    def expr(self, node):
        if isinstance(node, MemberAccess):
            return f"{self.expr(node.object)}${node.member}"
        return super().expr(node)

    def callee(self, node):
        if isinstance(node, MemberAccess):
            return f"{self.expr(node.object)}${node.member}"
        return super().callee(node)

    def binary(self, node):
        if node.operator == "+" and (self.is_str(node.left) or self.is_str(node.right)):
            return f"paste0({self.expr(node.left)}, {self.expr(node.right)})"
        if node.operator == "%":
            return f"{self.operand(node.left)} %% {self.operand(node.right)}"
        return super().binary(node)

    def var_decl(self, node, indent, in_class=None):
        init = self.expr(node.initializer) if node.initializer is not None else "NULL"
        return f"{self.pad(indent)}{node.name} <- {init}"

    def stmt(self, node, indent, in_class=None):
        if isinstance(node, Assignment):
            return f"{self.pad(indent)}{self.target(node.target)} <- {self.expr(node.value)}"
        return super().stmt(node, indent, in_class)

    def ret(self, node, indent):
        val = self.expr(node.value) if node.value is not None else ""
        return f"{self.pad(indent)}return({val})"

    def print_stmt(self, args):
        if len(args) == 1:
            return f"print({self.expr(args[0])})"
        return f"cat({', '.join(self.expr(a) for a in args)}, \"\\n\")"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = ", ".join(x.name for x in self.real_params(node))
        return self._join(f"{p}{node.name} <- function({params}) {{", self.block(node.body, indent + 1), p + "}")

    def klass(self, node, indent):
        p = self.pad(indent)
        fields, ctor, methods = _ctor_and_members(node)
        fl = ", ".join(f'{f.name} = "ANY"' for f in fields)
        out = [f'{p}{node.name} <- setRefClass("{node.name}",']
        if node.bases:
            out.append(f'{p}  contains = "{node.bases[0]}",')
        out.append(f"{p}  fields = list({fl}),")
        out.append(f"{p}  methods = list(")
        ms = []
        if ctor:
            ms.append(FunctionDeclaration(name="initialize", params=ctor.params, body=ctor.body))
        ms += methods
        rendered = []
        for m in ms:
            params = ", ".join(x.name for x in self.real_params(m))
            rendered.append(self._join(f"{p}    {m.name} = function({params}) {{", self.block(m.body, indent + 3), f"{p}    }}"))
        out.append(",\n".join(rendered))
        out += [f"{p}  )", f"{p})"]
        return self._join(*out)


# =============================================================================
# Julia
# =============================================================================
class JuliaBackend(UniversalBackend):
    LANG, STYLE = "julia", "Julia Style Guide"
    STMT_END, COMMENT = "", "#"
    NULL = "nothing"
    CONCAT = "*"
    TYPES = {"int": "Int", "float": "Float64", "str": "String", "bool": "Bool",
             "list": "Vector{Any}", "None": "Nothing"}
    IF_OPEN, ELSEIF, ELSE, IF_CLOSE = "if {c}", "elseif {c}", "else", "end"
    WHILE_OPEN, FORIN_OPEN, LOOP_CLOSE, BLOCK_CLOSE = "while {c}", "for {i} in {c}", "end", "end"

    def self_name(self):
        return "self"

    def var_decl(self, node, indent, in_class=None):
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else " = nothing"
        const = "const " if node.is_const and indent == 0 else ""
        return f"{self.pad(indent)}{const}{node.name}{init}"

    def param(self, prm):
        return f"{prm.name}::{self.type_of(prm.type_hint)}" if prm.type_hint else prm.name

    def print_stmt(self, args):
        parts = []
        for i, a in enumerate(args):
            if i:
                parts.append('" "')
            parts.append(self.expr(a))
        return f"println({', '.join(parts)})"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = [self.param(x) for x in self.real_params(node)]
        if in_class:
            params.insert(0, f"self::{in_class}")
        rt = node.return_type
        ret = f"::{self.type_of(rt)}" if rt and rt != "None" else ""
        return self._join(f"{p}function {node.name}({', '.join(params)}){ret}", self.block(node.body, indent + 1), p + "end")

    def klass(self, node, indent):
        p = self.pad(indent)
        fields, ctor, methods = _ctor_and_members(node)
        out = [f"{p}mutable struct {node.name}"]
        for f in fields:
            t = self.infer_type(f)
            out.append(f"{p}    {f.name}{'::' + self.type_of(t) if t else ''}")
        out.append(f"{p}end\n")
        for m in methods:
            out.append(self.func(m, indent, in_class=node.name) + "\n")
        return self._join(*out)


# =============================================================================
# Scala
# =============================================================================
class ScalaBackend(UniversalBackend):
    LANG, STYLE = "scala", "Scala Style Guide"
    STMT_END = ""
    INDENT = "  "
    TYPES = {"int": "Int", "float": "Double", "str": "String", "bool": "Boolean",
             "list": "List[Any]", "None": "Unit"}
    LIST_OPEN, LIST_CLOSE = "List(", ")"
    FORIN_OPEN = "for ({i} <- {c}) {{"

    def var_decl(self, node, indent, in_class=None):
        kw = "val" if node.is_const else "var"
        t = self.infer_type(node)
        th = f": {self.type_of(t)}" if node.type_hint or node.initializer is None else ""
        if node.initializer is None and not t:
            th = ": Any"
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else " = null"
        return f"{self.pad(indent)}{kw} {node.name}{th}{init}"

    def param(self, prm):
        return f"{prm.name}: {self.type_of(prm.type_hint) if prm.type_hint else 'Any'}"

    def print_stmt(self, args):
        if len(args) == 1:
            return f"println({self.expr(args[0])})"
        return f"println(List({', '.join(self.expr(a) for a in args)}).mkString(\" \"))"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = ", ".join(self.param(x) for x in self.real_params(node))
        ret = self.ret_type(node, "Any", "Unit")
        return self._join(f"{p}def {node.name}({params}): {ret} = {{", self.block(node.body, indent + 1), p + "}")

    def wrap_program(self, decls, stmts):
        classes, funcs = self.split_decls(decls)
        out = [self.stmt(c, 0) + "\n" for c in classes]
        out.append("object Main {")
        out += [self.func(f, 1) + "\n" for f in funcs]
        out += ["  def main(args: Array[String]): Unit = {", self.block(stmts, 2), "  }", "}"]
        return self._join(*out)


# =============================================================================
# Haskell
# =============================================================================
class HaskellBackend(UniversalBackend):
    LANG, STYLE = "haskell", "Haskell Style Guide (tibbe)"
    STMT_END, COMMENT = "", "--"
    INDENT = "  "
    TRUE, FALSE, NULL = "True", "False", "Nothing"
    NOT = "not"
    OP_MAP = {"!=": "/="}
    CONCAT = "++"
    TYPES = {"int": "Int", "float": "Double", "str": "String", "bool": "Bool",
             "list": "[Int]", "None": "()"}
    HEADER = "module Main where\n\nimport Control.Monad (forM_, when)\n\n"

    def binary(self, node):
        if node.operator == "%":
            return f"{self.operand(node.left)} `mod` {self.operand(node.right)}"
        return super().binary(node)

    def call(self, node):
        args = " ".join(self._arg(a) for a in node.args)
        return f"{self.callee(node.callee)} {args}".strip()

    def _arg(self, a):
        s = self.expr(a)
        return f"({s})" if isinstance(a, (BinaryExpression, CallExpression, UnaryExpression)) or (s.startswith("-")) else s

    def expr(self, node):
        if isinstance(node, MemberAccess):
            return f"({node.member} {self._arg(node.object)})"
        return super().expr(node)

    def self_name(self):
        return "self"

    def _show(self, a):
        return self.expr(a) if self.is_str(a) else f"show {self._arg(a)}"

    def print_stmt(self, args):
        if len(args) == 1:
            a = args[0]
            return f"putStrLn {self.expr(a)}" if self.is_str(a) else f"print {self._arg(a)}"
        return f"putStrLn (unwords [{', '.join(self._show(a) for a in args)}])"

    def var_decl(self, node, indent, in_class=None):
        init = self.expr(node.initializer) if node.initializer is not None else "undefined"
        return f"{self.pad(indent)}let {node.name} = {init}"

    def stmt(self, node, indent, in_class=None):
        p = self.pad(indent)
        if isinstance(node, Assignment):
            return f"{p}let {self.target(node.target)} = {self.expr(node.value)}"
        if isinstance(node, WhileLoop):
            return self._join(
                f"{p}-- NOTE(rosetta): imperative while-loop; Haskell values are immutable,",
                f"{p}-- so this runs at most once. Rewrite as a recursive function.",
                f"{p}when ({self.expr(node.condition)}) $ do",
                self.block(node.body, indent + 1) or f"{p}  return ()",
            )
        if isinstance(node, ForInLoop):
            return self._join(
                f"{p}forM_ {self._arg(node.iterable)} $ \\{self.expr(node.iterator)} -> do",
                self.block(node.body, indent + 1) or f"{p}  return ()",
            )
        return super().stmt(node, indent, in_class)

    def ret(self, node, indent):
        val = self._arg(node.value) if node.value is not None else "()"
        return f"{self.pad(indent)}return {val}"

    def if_stmt(self, node, indent, chained=False):
        p = self.pad(indent)
        return self._join(
            f"{p}if {self.expr(node.condition)}",
            f"{p}  then do",
            self.block(node.consequent, indent + 2) or f"{p}    return ()",
            f"{p}  else do",
            self.block(node.alternate or [], indent + 2) or f"{p}    return ()",
        )

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = [x.name for x in node.params if x.name != "this"]
        head = " ".join([node.name] + params)
        body = node.body or []
        # Pure function: single `return expr`
        if len(body) == 1 and isinstance(body[0], ReturnStatement) and body[0].value is not None:
            sig = ""
            if all(x.type_hint for x in node.params) and node.return_type and node.return_type != "None":
                sig = f"{p}{node.name} :: " + " -> ".join([self.type_of(x.type_hint) for x in node.params] + [self.type_of(node.return_type)]) + "\n"
            return f"{sig}{p}{head} = {self.expr(body[0].value)}"
        return self._join(f"{p}{head} = do", self.block(body, indent + 1) or f"{p}  return ()")

    def klass(self, node, indent):
        fields, ctor, methods = _ctor_and_members(node)
        fl = ", ".join(f"{f.name} :: {self.type_of(self.infer_type(f)) or 'Int'}" for f in fields)
        rec = f"data {node.name} = {node.name} {{ {fl} }} deriving (Show)" if fields else f"data {node.name} = {node.name} deriving (Show)"
        return self._join(rec, "", *[self.func(m, 0) + "\n" for m in methods])

    def wrap_program(self, decls, stmts):
        out = [self.HEADER.rstrip("\n") + "\n"]
        out += [self.stmt(d, 0) + "\n" for d in decls]
        out += ["main :: IO ()", "main = do", self.block(stmts, 1) or "  return ()"]
        return self._join(*out)


# =============================================================================
# Elixir
# =============================================================================
class ElixirBackend(UniversalBackend):
    LANG, STYLE = "elixir", "Elixir Style Guide / mix format"
    STMT_END, COMMENT = "", "#"
    INDENT = "  "
    NULL = "nil"
    CONCAT = "<>"
    IF_OPEN, ELSEIF, ELSE, IF_CLOSE = "if {c} do", "", "else", "end"
    FORIN_OPEN, LOOP_CLOSE, BLOCK_CLOSE = "for {i} <- {c} do", "end", "end"

    def string(self, s):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("#{", "\\#{") + '"'

    def self_name(self):
        return "self"

    def var_decl(self, node, indent, in_class=None):
        init = self.expr(node.initializer) if node.initializer is not None else "nil"
        return f"{self.pad(indent)}{node.name} = {init}"

    def ret(self, node, indent):
        return f"{self.pad(indent)}{self.expr(node.value) if node.value is not None else 'nil'}"

    def print_stmt(self, args):
        if len(args) == 1:
            return f"IO.puts({self.expr(args[0])})"
        interp = " ".join(f"#{{{self.expr(a)}}}" for a in args)
        return f'IO.puts("{interp}")'

    def while_loop(self, node, indent):
        p = self.pad(indent)
        body = self.block(node.body, indent + 1)
        commented = "\n".join(f"{p}# {l.strip()}" for l in body.splitlines())
        return self._join(
            f"{p}# NOTE(rosetta): Elixir has no while-loops; rewrite with recursion:",
            f"{p}# while {self.expr(node.condition)} do",
            commented,
            f"{p}# end",
        )

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = [x.name for x in self.real_params(node)]
        if in_class:
            params.insert(0, "self")
        return self._join(f"{p}def {node.name}({', '.join(params)}) do", self.block(node.body, indent + 1), p + "end")

    def klass(self, node, indent):
        p = self.pad(indent)
        fields, ctor, methods = _ctor_and_members(node)
        fl = ", ".join(f"{f.name}: {self.expr(f.initializer) if f.initializer is not None else 'nil'}" for f in fields)
        out = [f"{p}defmodule {node.name} do"]
        if fields:
            out.append(f"{p}  defstruct [{fl}]\n")
        out += [self.func(m, indent + 1, in_class=node.name) + "\n" for m in methods]
        out.append(f"{p}end")
        return self._join(*out)

    def wrap_program(self, decls, stmts):
        classes, funcs = self.split_decls(decls)
        out = [self.stmt(c, 0) + "\n" for c in classes]
        out.append("defmodule Main do")
        out += [self.func(f, 1) + "\n" for f in funcs]
        out += ["  def main do", self.block(stmts, 2) or "    :ok", "  end", "end", "", "Main.main()"]
        return self._join(*out)


# =============================================================================
# Bash
# =============================================================================
class BashBackend(UniversalBackend):
    LANG, STYLE = "bash", "Google Shell Style Guide"
    STMT_END, COMMENT = "", "#"
    INDENT = "  "
    TRUE, FALSE, NULL = "true", "false", '""'
    IF_OPEN, ELSEIF, ELSE, IF_CLOSE = "if {c}; then", "elif {c}; then", "else", "fi"
    WHILE_OPEN, LOOP_CLOSE, BLOCK_CLOSE = "while {c}; do", "done", "}"
    EMPTY_BODY = ":"
    HEADER = "#!/usr/bin/env bash\nset -euo pipefail\n\n"
    _ARITH = {"+", "-", "*", "/", "%"}
    _CMP = {"==", "!=", "<", ">", "<=", ">="}

    def __init__(self):
        self._depth = 0

    # -- expressions --
    def ident(self, name):
        return f"${{{name}}}"

    def string(self, s):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("$", "\\$").replace("`", "\\`") + '"'

    def list_lit(self, items):
        return "(" + " ".join(self.expr(x) for x in items) + ")"

    def arith(self, node):
        if isinstance(node, Identifier):
            return node.name
        if isinstance(node, Literal) and not isinstance(node.value, str):
            return "1" if node.value is True else "0" if node.value is False else str(node.value)
        if isinstance(node, BinaryExpression):
            sub = lambda n: f"({self.arith(n)})" if isinstance(n, BinaryExpression) else self.arith(n)
            return f"{sub(node.left)} {self.map_op(node.operator)} {sub(node.right)}"
        if isinstance(node, UnaryExpression):
            op = "!" if node.operator in ("not", "!") else node.operator
            return f"{op}{self.arith(node.argument)}"
        return self.expr(node)

    def _stringy(self, node):
        return self.is_str(node) or (isinstance(node, BinaryExpression) and node.operator == "+" and (self._stringy(node.left) or self._stringy(node.right)))

    def binary(self, node):
        if node.operator == "+" and self._stringy(node):
            return '"' + self._interp(node) + '"'
        return f"$(( {self.arith(node)} ))"

    def _interp(self, node):
        if isinstance(node, BinaryExpression) and node.operator == "+":
            return self._interp(node.left) + self._interp(node.right)
        if self.is_str(node):
            return self.string(node.value)[1:-1]
        if isinstance(node, Identifier):
            return f"${{{node.name}}}"
        return self.expr(node)

    def call(self, node):
        return f"$({self._cmd(node)})"

    def _cmd(self, node):
        return " ".join([self.callee(node.callee)] + [self._quote(a) for a in node.args])

    def _quote(self, a):
        s = self.expr(a)
        return f'"{s}"' if s.startswith("$") and not s.startswith('"') else s

    def cond(self, node):
        if isinstance(node, BinaryExpression) and node.operator in self._CMP and (self._stringy(node.left) or self._stringy(node.right)):
            return f'[[ {self._quote(node.left)} {node.operator} {self._quote(node.right)} ]]'
        if isinstance(node, Literal) and isinstance(node.value, bool):
            return "true" if node.value else "false"
        return f"(( {self.arith(node)} ))"

    # -- statements --
    def stmt(self, node, indent, in_class=None):
        p = self.pad(indent)
        if isinstance(node, Assignment):
            return f"{p}{self.arith(node.target)}={self._quote(node.value)}"
        if isinstance(node, CallExpression) and not self.is_print(node):
            return p + self._cmd(node)
        if isinstance(node, ClassDeclaration):
            return f"{p}# NOTE(rosetta): class '{node.name}' has no Bash equivalent; methods emitted as functions\n" + "\n".join(
                self.func(m, indent) + "\n" for m in node.body if isinstance(m, FunctionDeclaration))
        return super().stmt(node, indent, in_class)

    def var_decl(self, node, indent, in_class=None):
        val = self._quote(node.initializer) if node.initializer is not None else '""'
        kw = "local " if self._depth > 0 else ""
        return f"{self.pad(indent)}{kw}{node.name}={val}"

    def for_in(self, node, indent):
        p = self.pad(indent)
        it = node.iterable
        coll = f'"${{{it.name}[@]}}"' if isinstance(it, Identifier) else (" ".join(self.expr(x) for x in it.value) if isinstance(it, Literal) and isinstance(it.value, list) else self.expr(it))
        return self._join(f"{p}for {self.arith(node.iterator)} in {coll}; do", self.block(node.body, indent + 1) or p + "  :", p + "done")

    def ret(self, node, indent):
        p = self.pad(indent)
        if node.value is None:
            return f"{p}return"
        return f"{p}echo {self._quote(node.value)}\n{p}return 0"

    def print_stmt(self, args):
        return "echo " + " ".join(self._quote(a) for a in args)

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        self._depth += 1
        try:
            locals_ = [f'{p}  local {x.name}="${i + 1}"' for i, x in enumerate(self.real_params(node))]
            body = self.block(node.body, indent + 1)
        finally:
            self._depth -= 1
        return self._join(f"{p}{node.name}() {{", *locals_, body or p + "  :", p + "}")


# =============================================================================
# SQL (T-SQL)
# =============================================================================
class SQLBackend(UniversalBackend):
    LANG, STYLE = "sql", "T-SQL (SQL Server) Style"
    COMMENT = "--"
    TRUE, FALSE, NULL = "1", "0", "NULL"
    QUOTE = "'"
    VAR_SIGIL = "@"
    AND, OR, NOT = "AND", "OR", "NOT"
    OP_MAP = {"==": "=", "!=": "<>"}
    TYPES = {"int": "INT", "float": "FLOAT", "str": "NVARCHAR(MAX)", "bool": "BIT",
             "list": "NVARCHAR(MAX)", "None": ""}
    DEFAULT_TYPE = "SQL_VARIANT"

    def __init__(self):
        self._procs: set = set()
        self._funcs: set = set()

    def string(self, s):
        return "N'" + s.replace("'", "''") + "'"

    def list_lit(self, items):
        return "N'[" + ", ".join(self.expr(x).replace("'", "") for x in items) + "]'"

    def binary(self, node):
        if node.operator == "+" and (self.is_str(node.left) or self.is_str(node.right)):
            return f"CONCAT({self.expr(node.left)}, {self.expr(node.right)})"
        return super().binary(node)

    def call(self, node):
        name = self.callee(node.callee)
        args = ", ".join(self.expr(a) for a in node.args)
        if name in self._funcs:
            return f"dbo.{name}({args})"
        return f"{name}({args})"

    def var_decl(self, node, indent, in_class=None):
        t = self.type_of(self.infer_type(node)) or self.DEFAULT_TYPE
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        return f"{self.pad(indent)}DECLARE @{node.name} {t}{init};"

    def stmt(self, node, indent, in_class=None):
        p = self.pad(indent)
        if isinstance(node, Assignment):
            return f"{p}SET {self.target(node.target)} = {self.expr(node.value)};"
        if isinstance(node, CallExpression) and not self.is_print(node):
            name = self.callee(node.callee)
            if name in self._procs:
                return f"{p}EXEC dbo.{name} {', '.join(self.expr(a) for a in node.args)};"
            return f"{p}SELECT {self.call(node)};"
        if isinstance(node, ForInLoop):
            return f"{p}-- NOTE(rosetta): FOR-IN over {self.expr(node.iterable)} requires a CURSOR or set-based rewrite"
        return super().stmt(node, indent, in_class)

    def _begin_end(self, head, stmts, indent):
        p = self.pad(indent)
        return self._join(p + head, p + "BEGIN", self.block(stmts, indent + 1) or p + "    RETURN;", p + "END")

    def if_stmt(self, node, indent, chained=False):
        p = self.pad(indent)
        out = self._begin_end(f"IF {self.expr(node.condition)}", node.consequent, indent)
        if node.alternate:
            if len(node.alternate) == 1 and isinstance(node.alternate[0], IfStatement):
                out += f"\n{p}ELSE\n" + self.if_stmt(node.alternate[0], indent)
            else:
                out += "\n" + self._begin_end("ELSE", node.alternate, indent)
        return out

    def while_loop(self, node, indent):
        return self._begin_end(f"WHILE {self.expr(node.condition)}", node.body, indent)

    def ret(self, node, indent):
        val = f" {self.expr(node.value)}" if node.value is not None else ""
        return f"{self.pad(indent)}RETURN{val};"

    def print_stmt(self, args):
        if len(args) == 1:
            return f"PRINT {self.expr(args[0])};"
        sep = ", ' ', "
        return f"PRINT CONCAT({sep.join(self.expr(a) for a in args)});"

    def func(self, node, indent, in_class=None):
        params = ", ".join(f"@{x.name} {self.type_of(x.type_hint) or self.DEFAULT_TYPE}" for x in self.real_params(node))
        body = self.block(node.body, 1)
        if node.name in self._funcs:
            ret = self.ret_type(node, self.DEFAULT_TYPE, self.DEFAULT_TYPE)
            return f"CREATE OR ALTER FUNCTION dbo.{node.name}({params})\nRETURNS {ret}\nAS\nBEGIN\n{body}\nEND;\nGO"
        return f"CREATE OR ALTER PROCEDURE dbo.{node.name} {params}\nAS\nBEGIN\n{body}\nEND;\nGO"

    def klass(self, node, indent):
        fields, ctor, methods = _ctor_and_members(node)
        cols = [f"    {f.name} {self.type_of(self.infer_type(f)) or self.DEFAULT_TYPE}" for f in fields] or ["    id INT IDENTITY PRIMARY KEY"]
        out = f"-- class {node.name} modeled as a table\nCREATE TABLE {node.name} (\n" + ",\n".join(cols) + "\n);\nGO"
        if methods:
            out += "\n" + "\n".join(f"-- NOTE(rosetta): method {node.name}.{m.name} must be ported manually" for m in methods)
        return out

    def wrap_program(self, decls, stmts):
        classes, funcs = self.split_decls(decls)
        for f in funcs:
            (self._funcs if self.has_value_return(f.body) else self._procs).add(f.name)
        out = [self.stmt(c, 0) + "\n" for c in classes] + [self.func(f, 0) + "\n" for f in funcs]
        out.append(self.block(stmts, 0))
        return self._join(*out)


# =============================================================================
# Objective-C
# =============================================================================
class ObjectiveCBackend(UniversalBackend):
    LANG, STYLE = "objc", "Apple Objective-C Conventions"
    TRUE, FALSE, NULL = "YES", "NO", "nil"
    TYPES = {"int": "int", "float": "double", "str": "NSString *", "bool": "BOOL",
             "list": "NSArray *", "None": "void"}
    FORIN_OPEN = "for (id {i} in {c}) {{"
    HEADER = "#import <Foundation/Foundation.h>\n\n"

    def __init__(self):
        self._env: Dict[str, str] = {}

    def string(self, s):
        return '@"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

    def self_name(self):
        return "self"

    def _box(self, x):
        if isinstance(x, Literal):
            if isinstance(x.value, bool):
                return "@YES" if x.value else "@NO"
            if isinstance(x.value, (int, float)):
                return f"@{x.value}"
            if isinstance(x.value, str):
                return self.string(x.value)
        k = self.kind(x)
        return f"@({self.expr(x)})" if k in ("int", "float", "bool") else self.expr(x)

    def list_lit(self, items):
        return "@[" + ", ".join(self._box(x) for x in items) + "]"

    def kind(self, node) -> Optional[str]:
        if isinstance(node, Literal):
            v = node.value
            return "bool" if isinstance(v, bool) else "int" if isinstance(v, int) else "float" if isinstance(v, float) else "str" if isinstance(v, str) else "list" if isinstance(v, list) else None
        if isinstance(node, Identifier):
            return self._env.get(node.name)
        if isinstance(node, BinaryExpression):
            if node.operator in ("==", "!=", "<", ">", "<=", ">=", "&&", "||", "and", "or"):
                return "bool"
            l, r = self.kind(node.left), self.kind(node.right)
            if "str" in (l, r):
                return "str"
            if "float" in (l, r):
                return "float"
            if l == "int" or r == "int":
                return "int"
        return None

    def _fmt(self, node):
        k = self.kind(node)
        return {"int": "%d", "bool": "%d", "float": "%f"}.get(k, "%@")

    def binary(self, node):
        if node.operator == "+" and self.kind(node) == "str":
            return f'[NSString stringWithFormat:@"{self._fmt(node.left)}{self._fmt(node.right)}", {self.expr(node.left)}, {self.expr(node.right)}]'
        return super().binary(node)

    def call(self, node):
        if isinstance(node.callee, MemberAccess):
            obj = self.expr(node.callee.object)
            if not node.args:
                return f"[{obj} {node.callee.member}]"
            args = " :".join(self.expr(a) for a in node.args)
            return f"[{obj} {node.callee.member}:{args}]"
        return super().call(node)

    def _decl(self, t, name):
        return f"{t}{name}" if t.endswith("*") else f"{t} {name}"

    def var_decl(self, node, indent, in_class=None):
        t = self.infer_type(node)
        if t:
            self._env[node.name] = t
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        return f"{self.pad(indent)}{self._decl(self.type_of(t) if t else 'id', node.name)}{init};"

    def print_stmt(self, args):
        if len(args) == 1 and self.is_str(args[0]):
            return f"NSLog({self.string(args[0].value)});"
        fmt = " ".join(self._fmt(a) for a in args)
        return f'NSLog(@"{fmt}", {", ".join(self.expr(a) for a in args)});'

    def param(self, prm):
        if prm.type_hint:
            self._env[prm.name] = prm.type_hint
        return self._decl(self.type_of(prm.type_hint) if prm.type_hint else "id", prm.name)

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = ", ".join(self.param(x) for x in self.real_params(node)) or "void"
        ret = self.ret_type(node, "id", "void")
        return self._join(f"{p}{self._decl(ret, node.name)}({params}) {{", self.block(node.body, indent + 1), p + "}")

    def _selector(self, m: FunctionDeclaration) -> str:
        ret = self.ret_type(m, "id", "void")
        ps = self.real_params(m)
        if not ps:
            return f"- ({ret}){m.name}"
        parts = [f"{m.name}:({self.type_of(ps[0].type_hint) if ps[0].type_hint else 'id'}){ps[0].name}"]
        parts += [f":({self.type_of(x.type_hint) if x.type_hint else 'id'}){x.name}" for x in ps[1:]]
        return f"- ({ret})" + " ".join(parts)

    def klass(self, node, indent):
        fields, ctor, methods = _ctor_and_members(node)
        base = node.bases[0] if node.bases else "NSObject"
        out = [f"@interface {node.name} : {base}"]
        for f in fields:
            t = self.infer_type(f)
            out.append(f"@property (nonatomic) {self._decl(self.type_of(t) if t else 'id', f.name)};")
        out += [self._selector(m) + ";" for m in methods]
        out += ["@end", "", f"@implementation {node.name}"]
        for m in methods:
            for x in self.real_params(m):
                self.param(x)
            out.append(self._join(self._selector(m) + " {", self.block(m.body, 1), "}"))
        out.append("@end\n")
        return self._join(*out)

    def wrap_program(self, decls, stmts):
        out = [self.HEADER.rstrip("\n") + "\n"] + [self.stmt(d, 0) + "\n" for d in decls]
        out += ["int main(int argc, const char * argv[]) {", "    @autoreleasepool {", self.block(stmts, 2), "    }", "    return 0;", "}"]
        return self._join(*out)


# =============================================================================
# Move (Aptos / Sui smart contracts)
# =============================================================================
class MoveBackend(UniversalBackend):
    LANG, STYLE = "move", "Move Coding Conventions"
    TYPES = {"int": "u64", "float": "u64", "str": "vector<u8>", "bool": "bool",
             "list": "vector<u64>", "None": ""}
    NULL = "0"
    LIST_OPEN, LIST_CLOSE = "vector[", "]"

    def string(self, s):
        return 'b"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'

    def self_name(self):
        return "self"

    def var_decl(self, node, indent, in_class=None):
        t = self.infer_type(node)
        th = f": {self.type_of(t)}" if t else ""
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        return f"{self.pad(indent)}let {node.name}{th}{init};"

    def print_stmt(self, args):
        out = []
        for a in args:
            if self.is_str(a):
                out.append(f"debug::print(&string::utf8({self.expr(a)}));")
            else:
                out.append(f"debug::print(&{self.operand(a)});")
        return " ".join(out)

    def for_in(self, node, indent):
        p = self.pad(indent)
        return self._join(
            f"{p}vector::for_each_ref(&{self.operand(node.iterable)}, |{self.expr(node.iterator)}| {{",
            self.block(node.body, indent + 1),
            f"{p}}});",
        )

    def param(self, prm):
        return f"{prm.name}: {self.type_of(prm.type_hint) if prm.type_hint else 'u64'}"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = [self.param(x) for x in self.real_params(node)]
        if in_class:
            params.insert(0, f"self: &mut {in_class}")
        ret = self.ret_type(node, "u64", "")
        ret = f": {ret}" if ret else ""
        return self._join(f"{p}public fun {node.name}({', '.join(params)}){ret} {{", self.block(node.body, indent + 1), p + "}")

    def klass(self, node, indent):
        p = self.pad(indent)
        fields, ctor, methods = _ctor_and_members(node)
        fl = [f"{p}    {f.name}: {self.type_of(self.infer_type(f)) or 'u64'}," for f in fields]
        out = [f"{p}struct {node.name} has copy, drop, store {{", *fl, p + "}\n"]
        out += [self.func(m, indent, in_class=node.name) + "\n" for m in methods]
        return self._join(*out)

    def wrap_program(self, decls, stmts):
        out = ["module 0x1::main {", "    use std::debug;", "    use std::string;", "    use std::vector;", ""]
        out += [self.stmt(d, 1) + "\n" for d in decls]
        if stmts:
            out += ["    public entry fun main() {", self.block(stmts, 2), "    }"]
        out.append("}")
        return self._join(*out)


# =============================================================================
# Perl
# =============================================================================
class PerlBackend(UniversalBackend):
    LANG, STYLE = "perl", "perlstyle"
    COMMENT = "#"
    TRUE, FALSE, NULL = "1", "0", "undef"
    VAR_SIGIL = "$"
    CONCAT = "."
    ELSEIF = "}} elsif ({c}) {{"
    FORIN_OPEN = "foreach my ${i} (@{{{c}}}) {{"
    HEADER = "use strict;\nuse warnings;\n\n"

    def string(self, s):
        return '"' + s.replace("\\", "\\\\").replace('"', '\\"').replace("$", "\\$").replace("@", "\\@") + '"'

    def binary(self, node):
        if node.operator in ("==", "!=") and (self.is_str(node.left) or self.is_str(node.right)):
            op = "eq" if node.operator == "==" else "ne"
            return f"{self.operand(node.left)} {op} {self.operand(node.right)}"
        return super().binary(node)

    def expr(self, node):
        if isinstance(node, MemberAccess):
            return f"{self.expr(node.object)}->{{{node.member}}}"
        return super().expr(node)

    def self_name(self):
        return "$self"

    def callee(self, node):
        if isinstance(node, MemberAccess):
            return f"{self.expr(node.object)}->{node.member}"
        return super().callee(node)

    def var_decl(self, node, indent, in_class=None):
        init = f" = {self.expr(node.initializer)}" if node.initializer is not None else ""
        return f"{self.pad(indent)}my ${node.name}{init};"

    def print_stmt(self, args):
        if len(args) == 1:
            return f'print {self.expr(args[0])}, "\\n";'
        return f'print join(" ", {", ".join(self.expr(a) for a in args)}), "\\n";'

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        names = [f"${x.name}" for x in self.real_params(node)]
        if in_class:
            names.insert(0, "$self")
        unpack = [f"{p}    my ({', '.join(names)}) = @_;"] if names else []
        return self._join(f"{p}sub {node.name} {{", *unpack, self.block(node.body, indent + 1), p + "}")

    def klass(self, node, indent):
        fields, ctor, methods = _ctor_and_members(node)
        out = [f"package {node.name};"]
        if node.bases:
            out.append(f"use parent -norequire, '{node.bases[0]}';")
        cparams = [f"${x.name}" for x in self.real_params(ctor)] if ctor else []
        fl = ", ".join(f"{f.name} => {self.expr(f.initializer) if f.initializer is not None else 'undef'}" for f in fields)
        out += ["", "sub new {", f"    my ({', '.join(['$class'] + cparams)}) = @_;", f"    my $self = bless {{ {fl} }}, $class;"]
        if ctor:
            b = self.block(ctor.body, 1)
            if b:
                out.append(b)
        out += ["    return $self;", "}", ""]
        out += [self.func(m, 0, in_class=node.name) + "\n" for m in methods]
        out.append("package main;\n")
        return self._join(*out)

    def wrap_program(self, decls, stmts):
        classes, funcs = self.split_decls(decls)
        out = [self.HEADER.rstrip("\n") + "\n"]
        out += [self.stmt(c, 0) for c in classes]
        out += [self.func(f, 0) + "\n" for f in funcs]
        out.append(self.block(stmts, 0))
        return self._join(*out)


UNIVERSAL_BACKENDS = {
    "csharp": CSharpBackend,
    "dart": DartBackend,
    "lua": LuaBackend,
    "r": RBackend,
    "julia": JuliaBackend,
    "scala": ScalaBackend,
    "haskell": HaskellBackend,
    "elixir": ElixirBackend,
    "bash": BashBackend,
    "sql": SQLBackend,
    "objc": ObjectiveCBackend,
    "move": MoveBackend,
    "perl": PerlBackend,
}
