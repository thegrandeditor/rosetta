"""
rosetta/babel/base/modern_parser.py
-----------------------------------
Universal structural parser for C-family, brace-scoped, and Ruby/PHP languages
into canonical Rosetta IR (`Program`, `FunctionDeclaration`, `ClassDeclaration`,
`VariableDeclaration`, `Assignment`, `IfStatement`, `WhileLoop`, `ForLoop`,
`ForInLoop`, `ReturnStatement`, `CallExpression`, `BinaryExpression`, etc.).
"""
from __future__ import annotations
import re
from typing import List, Optional, Tuple
from rosetta.ir.nodes import (
    RosettaNode,
    Program,
    Identifier,
    Literal,
    VariableDeclaration,
    Assignment,
    FunctionDeclaration,
    MethodDeclaration,
    Parameter,
    ReturnStatement,
    CallExpression,
    IfStatement,
    WhileLoop,
    ForLoop,
    ForInLoop,
    BinaryExpression,
    UnaryExpression,
    ClassDeclaration,
    StructDeclaration,
    MemberAccess,
    ArrayAccess,
    MemoryAllocation,
    MemoryFree,
    Dereference,
)


class ModernLanguageParser:
    """
    Parses source code from JavaScript, TypeScript, Java, C++, C, Rust, Go,
    Swift, Kotlin, Ruby, and PHP into Rosetta IR.
    """

    def __init__(self, language_id: str):
        self.language_id = language_id

    def parse(self, source: str) -> Program:
        cleaned = self._strip_comments_and_directives(source)
        lines = [line.strip() for line in cleaned.splitlines() if line.strip()]
        stmts, _ = self._parse_block(lines, 0, in_class=False)
        # Unwrap single top-level wrapper class in Java if it only wraps main/methods,
        # or keep ClassDeclaration intact if it has fields/methods.
        return Program(body=stmts)

    def _strip_comments_and_directives(self, source: str) -> str:
        # Remove PHP tags
        source = re.sub(r"<\?php|\?>", "", source)
        # Remove multi-line /* ... */ comments
        source = re.sub(r"/\*.*?\*/", "", source, flags=re.DOTALL)
        out_lines = []
        for raw_line in source.splitlines():
            line = raw_line.strip()
            if not line:
                continue
            # Remove single-line // or # comments (outside quotes)
            line = self._strip_line_comment(line)
            if not line:
                continue
            # Skip preprocessor / package / import / use / namespace / module boilerplate
            if re.match(
                r"^(#include\b|#import\b|#pragma\b|#!/|package\s+|import\s+|using\s+|use\s+\w+|namespace\s+[A-Za-z0-9_.]+|module\s+[A-Za-z0-9_.:]+|defmodule\s+[A-Za-z0-9_.]+\s+do\b|object\s+[A-Za-z0-9_]+\s*\{?)",
                line,
            ):
                continue
            out_lines.append(line)
        return "\n".join(out_lines)

    def _strip_line_comment(self, line: str) -> str:
        in_str = None
        i = 0
        n = len(line)
        while i < n:
            ch = line[i]
            if ch in ('"', "'") and (i == 0 or line[i - 1] != "\\"):
                if in_str is None:
                    in_str = ch
                elif in_str == ch:
                    in_str = None
            elif in_str is None:
                if line[i : i + 2] == "//":
                    return line[:i].strip()
                if line[i : i + 2] == "--" and self.language_id in ("lua", "haskell", "sql", "ada"):
                    return line[:i].strip()
                if ch == "#" and self.language_id not in ("c", "cpp", "csharp", "objc"):
                    return line[:i].strip()
            i += 1
        return line.strip()

    def _parse_block(
        self, lines: List[str], start: int, in_class: bool = False, single: bool = False
    ) -> Tuple[List[RosettaNode], int]:
        body: List[RosettaNode] = []
        i = start
        n = len(lines)

        while i < n:
            if single and body:
                return body, i
            line = lines[i].strip()
            if not line:
                i += 1
                continue

            # End of block
            if line in ("}", "};", "end", "fi", "done", "END", "END;"):
                return body, i + 1
            if line.startswith("}") and not line.startswith("} else") and not line.startswith("} catch"):
                return body, i + 1

            # Handle `} else if (...) {` or `} else {` on same line
            if line.startswith("} else"):
                return body, i
            # Keyword-style else branches (Lua/Ruby/Julia/Elixir/Bash) end the current block
            if re.match(r"^(?:else|elsif|elseif|elif)\b", line) and not line.endswith(";"):
                return body, i

            # Class / Struct / Impl declaration
            m_class = re.match(
                r"^(?:public\s+|private\s+|internal\s+|open\s+|final\s+|abstract\s+)*(?:(class|struct|interface|impl)\s+)([A-Za-z_]\w*)(?:\s*(?:extends|:|<|for)\s*([A-Za-z0-9_,\s<>]+))?\s*\{?$",
                line,
            )
            if m_class:
                kind = m_class.group(1)
                cname = m_class.group(2)
                bases_raw = m_class.group(3)
                bases = [b.strip() for b in bases_raw.split(",") if b.strip()] if bases_raw else []
                has_open = line.endswith("{") or self.language_id == "ruby"
                next_idx = i + 1
                if not has_open and next_idx < n and lines[next_idx].strip() == "{":
                    next_idx += 1
                c_body, next_idx = self._parse_block(lines, next_idx, in_class=True)
                if kind == "struct":
                    fields = [s for s in c_body if isinstance(s, VariableDeclaration)]
                    other = [s for s in c_body if not isinstance(s, VariableDeclaration)]
                    body.append(StructDeclaration(name=cname, fields=fields))
                    body.extend(other)
                else:
                    body.append(ClassDeclaration(name=cname, bases=bases, body=c_body))
                i = next_idx
                continue

            # Function / Method declaration
            func_match = self._match_function_header(line)
            if func_match:
                fname, params_str, ret_type, is_async, is_static = func_match
                params = self._parse_params(params_str)
                next_idx = i + 1
                if not line.endswith("{") and self.language_id != "ruby":
                    if next_idx < n and lines[next_idx].strip() == "{":
                        next_idx += 1
                f_body, next_idx = self._parse_block(lines, next_idx, in_class=False)
                if in_class:
                    body.append(
                        MethodDeclaration(
                            name=fname,
                            params=params,
                            body=f_body,
                            return_type=ret_type,
                            is_async=is_async,
                            is_static=is_static,
                        )
                    )
                else:
                    body.append(
                        FunctionDeclaration(
                            name=fname,
                            params=params,
                            body=f_body,
                            return_type=ret_type,
                            is_async=is_async,
                        )
                    )
                i = next_idx
                continue

            # If / Else Statement
            m_if = re.match(r"^if\b\s*\(?(.+?)\)?\s*;?\s*(?:\{|then\b|do\b)?$", line)
            if m_if and not line.endswith(";"):
                cond_str = m_if.group(1).strip()
                if cond_str.endswith("{"):
                    cond_str = cond_str[:-1].strip()
                cond_str = cond_str.rstrip(";").strip()
                if cond_str.startswith("[") and cond_str.endswith("]"):
                    cond_str = self._bash_test_to_expr(cond_str.strip("[] "))
                if cond_str.startswith("(") and cond_str.endswith(")"):
                    cond_str = cond_str[1:-1].strip()
                cond = self._parse_expr(cond_str)
                next_idx = i + 1
                if not line.endswith("{") and self.language_id != "ruby" and next_idx < n and lines[next_idx].strip() == "{":
                    next_idx += 1
                consequent, next_idx = self._parse_block(lines, next_idx, in_class=in_class)
                alternate = None
                if next_idx < n:
                    peek = lines[next_idx].strip()
                    if peek.startswith("} else") or re.match(r"^(?:else|elsif|elseif|elif)\b", peek):
                        # Strip leading `} `
                        if peek.startswith("}"):
                            peek = peek[1:].strip()
                        if re.match(r"^(?:else\s+if|elsif|elseif|elif)\b", peek):
                            # Rewrite line in-place as `if ...` and parse a single nested if
                            rewritten = re.sub(r"^(?:else\s+if|elsif|elseif|elif)\b", "if", peek, count=1)
                            lines_copy = list(lines)
                            lines_copy[next_idx] = rewritten
                            alt_stmts, next_idx = self._parse_block(lines_copy, next_idx, in_class=in_class, single=True)
                            alternate = alt_stmts
                        else:
                            next_idx += 1
                            if next_idx < n and lines[next_idx].strip() == "{":
                                next_idx += 1
                            alternate, next_idx = self._parse_block(lines, next_idx, in_class=in_class)
                body.append(IfStatement(condition=cond, consequent=consequent, alternate=alternate))
                i = next_idx
                continue

            # While loop
            m_while = re.match(r"^while\b\s*\(?(.+?)\)?\s*;?\s*(?:\{|do\b)?$", line)
            if m_while and not line.endswith(";"):
                cond_str = m_while.group(1).strip().rstrip("{").strip().rstrip(";").strip()
                if cond_str.startswith("[") and cond_str.endswith("]"):
                    cond_str = self._bash_test_to_expr(cond_str.strip("[] "))
                if cond_str.startswith("(") and cond_str.endswith(")"):
                    cond_str = cond_str[1:-1].strip()
                cond = self._parse_expr(cond_str)
                next_idx = i + 1
                if not line.endswith("{") and self.language_id != "ruby" and next_idx < n and lines[next_idx].strip() == "{":
                    next_idx += 1
                w_body, next_idx = self._parse_block(lines, next_idx, in_class=in_class)
                body.append(WhileLoop(condition=cond, body=w_body))
                i = next_idx
                continue

            # For / Foreach loop
            m_for = re.match(r"^(?:for|foreach)\b\s*\(?(.+?)\)?\s*(?:\{|do\b)?$", line)
            if m_for and not line.endswith(";"):
                header = m_for.group(1).strip().rstrip("{").strip()
                if header.startswith("(") and header.endswith(")"):
                    header = header[1:-1].strip()
                next_idx = i + 1
                if not line.endswith("{") and self.language_id != "ruby" and next_idx < n and lines[next_idx].strip() == "{":
                    next_idx += 1
                f_body, next_idx = self._parse_block(lines, next_idx, in_class=in_class)

                if ";" in header:
                    parts = [p.strip() for p in header.split(";")]
                    init_node = self._parse_simple_statement(parts[0]) if len(parts) > 0 and parts[0] else None
                    cond_node = self._parse_expr(parts[1]) if len(parts) > 1 and parts[1] else None
                    inc_node = self._parse_simple_statement(parts[2]) if len(parts) > 2 and parts[2] else None
                    body.append(
                        ForLoop(
                            initializer=init_node,
                            condition=cond_node,
                            increment=inc_node,
                            body=f_body,
                        )
                    )
                else:
                    # for x in coll / for (auto x : coll) / foreach ($arr as $x)
                    m_in = re.match(r"^(?:let\s+|var\s+|const\s+|val\s+|auto&?\s+)?([A-Za-z_$][\w$]*)\s+(?:in|of|:)\s+(.+)$", header)
                    m_php = re.match(r"^(.+?)\s+as\s+([A-Za-z_$][\w$]*)$", header)
                    if m_in:
                        it_name = m_in.group(1).lstrip("$")
                        coll_expr = self._parse_expr(m_in.group(2))
                        body.append(ForInLoop(iterator=Identifier(name=it_name), iterable=coll_expr, body=f_body))
                    elif m_php:
                        it_name = m_php.group(2).lstrip("$")
                        coll_expr = self._parse_expr(m_php.group(1))
                        body.append(ForInLoop(iterator=Identifier(name=it_name), iterable=coll_expr, body=f_body))
                    else:
                        body.append(WhileLoop(condition=self._parse_expr(header), body=f_body))
                i = next_idx
                continue

            # Simple single-line statement
            stmt = self._parse_simple_statement(line)
            if stmt is not None:
                body.append(stmt)
            i += 1

        return body, i

    def _match_function_header(self, line: str) -> Optional[Tuple[str, str, Optional[str], bool, bool]]:
        # Strip trailing `{`
        clean = line[:-1].strip() if line.endswith("{") else line.strip()
        if clean.endswith(";"):
            return None

        is_async = bool(re.search(r"\basync\b", clean))
        is_static = bool(re.search(r"\bstatic\b", clean))

        # 1. JS/TS/PHP/Rust/Go/Swift/Kotlin/Mojo/Scala/Elixir/Lua/Julia/Move keyword functions
        m = re.match(
            r"^(?:pub\s+|public\s+|private\s+|protected\s+|internal\s+|static\s+|async\s+|override\s+|open\s+|local\s+|entry\s+)*(?:function|fn|func|fun|def|defp)\s+([A-Za-z_]\w*)\s*(?:<[^>]*>)?\s*\(([^)]*)\)\s*(?:(?::|->)\s*([A-Za-z0-9_<>\[\]]+))?\s*(?:=|do)?$",
            clean,
        )
        if m:
            return m.group(1), m.group(2), self._normalize_type(m.group(3)), is_async, is_static

        # 1b. R function assignment: `fname <- function(params)`
        m_r = re.match(r"^([A-Za-z_][\w.]*)\s*(?:<-|=)\s*function\s*\(([^)]*)\)$", clean)
        if m_r:
            return m_r.group(1), m_r.group(2), None, False, False

        # 1c. Bash function: `fname() {` / `function fname {`
        if self.language_id in ("bash", "sh"):
            m_sh = re.match(r"^(?:function\s+)?([A-Za-z_]\w*)\s*(?:\(\s*\))?$", clean)
            if m_sh and (line.endswith("{") or clean.startswith("function")):
                return m_sh.group(1), "", None, False, False

        # 2. Ruby `def name` without parens
        if self.language_id == "ruby":
            m_rb = re.match(r"^def\s+([A-Za-z_]\w*[?!]?)(?:\s*\(([^)]*)\)|\s+([A-Za-z0-9_,\s]+))?$", clean)
            if m_rb:
                params = m_rb.group(2) if m_rb.group(2) is not None else (m_rb.group(3) or "")
                return m_rb.group(1).rstrip("?!"), params, None, False, False

        # 3. C / C++ / Java typed function header: `[modifiers] RetType funcName(params)`
        m_c = re.match(
            r"^(?:public\s+|private\s+|protected\s+|static\s+|virtual\s+|inline\s+|constexpr\s+|async\s+)*([A-Za-z_][\w:<>\[\]\*&\s]*?)\s+([A-Za-z_]\w*)\s*\(([^)]*)\)\s*(?:const)?\s*(?:throws\s+[\w,\s]+)?$",
            clean,
        )
        if m_c:
            ret_raw = m_c.group(1).strip()
            fname = m_c.group(2).strip()
            if fname not in ("if", "while", "for", "switch", "catch", "return", "sizeof", "printf", "println"):
                return fname, m_c.group(3), self._normalize_type(ret_raw), is_async, is_static

        return None

    def _parse_params(self, params_str: str) -> List[Parameter]:
        params: List[Parameter] = []
        if not params_str or not params_str.strip():
            return params
        for raw in params_str.split(","):
            p = raw.strip()
            if not p or p in ("void", "&self", "self", "mut self", "&mut self"):
                if p in ("&self", "self", "mut self", "&mut self"):
                    params.append(Parameter(name="self"))
                continue
            # Remove default value if present
            default_val = None
            if "=" in p:
                p, def_str = [x.strip() for x in p.split("=", 1)]
                default_val = self._parse_expr(def_str)

            # Check `name: type` (TS, Rust, Kotlin, Swift, Python)
            if ":" in p:
                left, right = [x.strip() for x in p.split(":", 1)]
                left = re.sub(r"^(?:let|var|val|mut|inout|_)\s+", "", left).strip().lstrip("$")
                params.append(
                    Parameter(
                        name=left,
                        type_hint=self._normalize_type(right),
                        default_value=default_val,
                    )
                )
            else:
                # Check `Type name` (C, C++, Java, Go `name Type`, PHP `$name`)
                tokens = p.split()
                if len(tokens) >= 2:
                    if self.language_id == "go":
                        pname = tokens[0].lstrip("$")
                        ptype = self._normalize_type(" ".join(tokens[1:]))
                    else:
                        pname = tokens[-1].lstrip("*&$")
                        ptype = self._normalize_type(" ".join(tokens[:-1]))
                    params.append(Parameter(name=pname, type_hint=ptype, default_value=default_val))
                else:
                    params.append(Parameter(name=tokens[0].lstrip("$"), default_value=default_val))
        return params

    def _parse_simple_statement(self, line: str) -> Optional[RosettaNode]:
        stmt = line.strip().rstrip(";").strip()
        if not stmt or stmt in ("{", "}", "end"):
            return None

        # Return statement
        m_ret = re.match(r"^return(?:\s+(.+))?$", stmt)
        if m_ret:
            val_str = m_ret.group(1)
            return ReturnStatement(value=self._parse_expr(val_str.strip()) if val_str else None)

        # C++ std::cout << a << b << std::endl
        if "std::cout" in stmt or stmt.startswith("cout "):
            parts = re.split(r"<<", stmt)
            args = []
            for part in parts[1:]:
                p = part.strip()
                if p in ("std::endl", "endl", '"\\n"', "'\\n'"):
                    continue
                args.append(self._parse_expr(p))
            return CallExpression(callee=Identifier(name="print"), args=args)

        # Print / output statements across languages
        m_print = re.match(
            r"^(?:console\.log|Console\.WriteLine|Console\.Write|System\.out\.println|System\.out\.print|fmt\.Println|fmt\.Printf|fmt\.Print|IO\.puts|putStrLn|NSLog|std::debug::print|println!|print!|println|printf|puts|echo|cat|print|PRINT|SELECT)(?![\w.])\s*(.*)$",
            stmt,
        )
        if m_print:
            rest = m_print.group(1).strip()
            if rest.startswith("(") and rest.endswith(")") and self._parens_balanced(rest[1:-1]):
                rest = rest[1:-1].strip()
            raw_args = self._split_args(rest)
            # Filter format string like `"%d\n"`, `@"%@"` or `"{:?}"` if there are more arguments
            if len(raw_args) > 1 and re.match(r'^@?["\'](?:%[dsf@]|.*\{\:?.*\}).*["\']$', raw_args[0]):
                raw_args = raw_args[1:]
            args = [self._parse_expr(a[1:] if a.startswith('@"') else a) for a in raw_args if a]
            return CallExpression(callee=Identifier(name="print"), args=args)

        # R left-arrow assignment: `x <- expr`
        m_r_assign = re.match(r"^([A-Za-z_][\w.]*)\s*<-\s*(.+)$", stmt)
        if m_r_assign:
            init = self._parse_expr(m_r_assign.group(2))
            return VariableDeclaration(name=m_r_assign.group(1), type_hint=self._infer_literal_type(init), initializer=init)

        # Lua `local`, Perl `my`, SQL `DECLARE @x INT = 5`
        m_local = re.match(r"^(?:local|my|DECLARE)\s+[@$]?([A-Za-z_]\w*)(?:\s+([A-Za-z]\w*))?\s*(?:=\s*(.+))?$", stmt, flags=re.IGNORECASE)
        if m_local:
            init = self._parse_expr(m_local.group(3)) if m_local.group(3) else None
            thint = self._normalize_type(m_local.group(2).lower()) if m_local.group(2) else (self._infer_literal_type(init) if init else None)
            return VariableDeclaration(name=m_local.group(1), type_hint=thint, initializer=init)

        # Go short variable declaration: `x := expr`
        m_walrus = re.match(r"^([A-Za-z_]\w*)\s*:=\s*(.+)$", stmt)
        if m_walrus:
            vname = m_walrus.group(1)
            init = self._parse_expr(m_walrus.group(2))
            return VariableDeclaration(name=vname, type_hint=self._infer_literal_type(init), initializer=init)

        # Keyword Variable declarations: `let`, `const`, `var`, `val`
        m_var = re.match(
            r"^(let\s+mut|let|const|var|val)\s+([A-Za-z_$][\w$]*)\s*(?::\s*([A-Za-z0-9_<>\[\]]+))?\s*(?:=\s*(.+))?$",
            stmt,
        )
        if m_var:
            kw = m_var.group(1)
            vname = m_var.group(2).lstrip("$")
            thint = self._normalize_type(m_var.group(3))
            init = self._parse_expr(m_var.group(4)) if m_var.group(4) else None
            if not thint and init:
                thint = self._infer_literal_type(init)
            is_const = kw in ("const", "val") or (kw == "let" and self.language_id in ("swift", "rust"))
            return VariableDeclaration(name=vname, type_hint=thint, initializer=init, is_const=is_const)

        # Memory Free: `free(p)`, `delete p`, `delete[] p`
        m_free = re.match(r"^(?:free\s*\((.+)\)|delete(?:\[\])?\s+(.+))$", stmt)
        if m_free:
            ptr_str = (m_free.group(1) or m_free.group(2)).strip()
            return MemoryFree(argument=self._parse_expr(ptr_str))

        # C / C++ / Java typed variable declaration: `int x = 10`, `int* p = malloc(100)`, `std::string s = "hi"`
        m_typed = re.match(
            r"^(?:const\s+|final\s+)?(int|long|float|double|bool|boolean|char|void|String|std::string|auto|i32|i64|u32|u64|f32|f64|usize|[A-Za-z_]\w*)(\*+|&|\[\])?\s*(\*+)?\s*([A-Za-z_]\w*)\s*(?:=\s*(.+))?$",
            stmt,
        )
        if m_typed and m_typed.group(4) not in ("if", "while", "for", "return", "class", "struct", "void"):
            is_const = stmt.startswith("const ") or stmt.startswith("final ")
            base_type = self._normalize_type(m_typed.group(1))
            ptr_modifier = (m_typed.group(2) or "") + (m_typed.group(3) or "")
            thint = f"{base_type}{ptr_modifier}".strip() if ptr_modifier else base_type
            vname = m_typed.group(4)
            init = self._parse_expr(m_typed.group(5)) if m_typed.group(5) else None
            return VariableDeclaration(name=vname, type_hint=thint, initializer=init, is_const=is_const)

        # Increment / Decrement `i++`, `i--`, `++i`
        m_inc = re.match(r"^([A-Za-z_$][\w$]*)\s*(\+\+|--)$", stmt)
        if m_inc:
            ident = Identifier(name=m_inc.group(1).lstrip("$"))
            op = "+" if m_inc.group(2) == "++" else "-"
            return Assignment(target=ident, value=BinaryExpression(left=ident, operator=op, right=Literal(value=1)))

        # Compound assignment `x += y`, `x -= y`
        m_comp = re.match(r"^([A-Za-z_$][\w$.\[\]]*)\s*([+\-*/])=\s*(.+)$", stmt)
        if m_comp:
            target = self._parse_expr(m_comp.group(1))
            op = m_comp.group(2)
            rhs = self._parse_expr(m_comp.group(3))
            return Assignment(target=target, value=BinaryExpression(left=target, operator=op, right=rhs))

        # Standard assignment `target = value` (including pointer dereference assignment `*p = value`)
        m_assign = re.match(r"^(\*?[A-Za-z_$][\w$.\[\]]*)\s*=\s*(?!=)(.+)$", stmt)
        if m_assign:
            lhs_raw = m_assign.group(1).strip()
            rhs = self._parse_expr(m_assign.group(2).strip())
            if lhs_raw.startswith("*"):
                target = Dereference(argument=self._parse_expr(lhs_raw[1:].strip()))
            else:
                target = self._parse_expr(lhs_raw)
            return Assignment(target=target, value=rhs)

        return self._parse_expr(stmt)

    def _parse_expr(self, expr_str: str) -> RosettaNode:
        s = expr_str.strip().rstrip(";").strip()
        if not s:
            return Literal(value=None)

        # Strip outer parens if balanced
        while s.startswith("(") and s.endswith(")") and self._parens_balanced(s[1:-1]):
            s = s[1:-1].strip()

        # String literal (including Rust `"hi".to_string()`)
        m_rust_str = re.match(r'^"(.*)"\.to_string\(\)$', s)
        if m_rust_str:
            return Literal(value=m_rust_str.group(1))
        if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
            if len(s) >= 2 and s[1:-1].find(s[0]) == -1:
                return Literal(value=s[1:-1])

        # Boolean / Null literals
        if s in ("true", "True", "TRUE"):
            return Literal(value=True)
        if s in ("false", "False", "FALSE"):
            return Literal(value=False)
        if s in ("null", "nil", "None", "nullptr", "undefined"):
            return Literal(value=None)

        # Numeric literals
        if re.match(r"^-?\d+$", s):
            return Literal(value=int(s))
        if re.match(r"^-?\d+\.\d+$", s):
            return Literal(value=float(s))

        # Array literal `[a, b, c]` or `vec![a, b, c]`
        m_vec = re.match(r"^(?:vec!)?\[(.*)\]$", s)
        if m_vec:
            inner = m_vec.group(1).strip()
            items = [self._parse_expr(x) for x in self._split_args(inner)] if inner else []
            return Literal(value=items)

        # Binary operators (lowest to highest precedence)
        for ops in (
            ("||", "or"),
            ("&&", "and"),
            ("==", "!=", "<=", ">=", "<", ">"),
            ("+", "-"),
            ("*", "/", "%"),
        ):
            split_pos = self._find_top_level_op(s, ops)
            if split_pos is not None:
                idx, op = split_pos
                left_str = s[:idx].strip()
                right_str = s[idx + len(op) :].strip()
                if left_str and right_str:
                    return BinaryExpression(
                        left=self._parse_expr(left_str),
                        operator=op,
                        right=self._parse_expr(right_str),
                    )

        # Unary expression: not, negate, dereference (*p), address-of (&x)
        if s.startswith("!") or s.startswith("not "):
            arg = s[1:].strip() if s.startswith("!") else s[4:].strip()
            return UnaryExpression(operator="not", argument=self._parse_expr(arg))
        if s.startswith("-") and len(s) > 1 and not re.match(r"^-?\d", s):
            return UnaryExpression(operator="-", argument=self._parse_expr(s[1:].strip()))
        if s.startswith("*") and len(s) > 1 and re.match(r"^\*[A-Za-z_$][\w$.\[\]]*$", s):
            return Dereference(argument=self._parse_expr(s[1:].strip()))
        if s.startswith("&") and len(s) > 1 and re.match(r"^&[A-Za-z_$][\w$.\[\]]*$", s):
            return UnaryExpression(operator="&", argument=self._parse_expr(s[1:].strip()))

        # Function / Method call: `callee(args)`
        m_call = re.match(r"^([A-Za-z_$][\w$.:!]*)\s*\((.*)\)$", s)
        if m_call and self._parens_balanced(m_call.group(2)):
            callee_raw = m_call.group(1).strip()
            args_raw = m_call.group(2).strip()
            args = [self._parse_expr(a) for a in self._split_args(args_raw)] if args_raw else []

            # Malloc / Calloc conversion to MemoryAllocation
            if callee_raw in ("malloc", "calloc"):
                alloc_size = args[0] if args else Literal(value=0)
                if callee_raw == "calloc" and len(args) >= 2:
                    alloc_size = BinaryExpression(left=args[0], operator="*", right=args[1])
                return MemoryAllocation(size=alloc_size)

            if "." in callee_raw:
                obj_part, mem_part = callee_raw.rsplit(".", 1)
                callee_node = MemberAccess(object=self._parse_expr(obj_part), member=mem_part)
            else:
                callee_node = Identifier(name=callee_raw.lstrip("$"))
            return CallExpression(callee=callee_node, args=args)

        # Array access: `obj[idx]`
        m_arr = re.match(r"^([A-Za-z_$][\w$.]*)\[(.+)\]$", s)
        if m_arr:
            return ArrayAccess(
                object=self._parse_expr(m_arr.group(1)),
                index=[self._parse_expr(m_arr.group(2))],
            )

        # Member access: `obj.member` or `obj->member`
        if "->" in s:
            obj_part, mem_part = s.rsplit("->", 1)
            return MemberAccess(object=self._parse_expr(obj_part), member=mem_part.strip())
        if "." in s and not re.match(r"^-?\d+\.\d+$", s):
            obj_part, mem_part = s.rsplit(".", 1)
            if re.match(r"^[A-Za-z_]\w*$", mem_part.strip()):
                return MemberAccess(object=self._parse_expr(obj_part), member=mem_part.strip())

        return Identifier(name=s.lstrip("$"))

    def _bash_test_to_expr(self, test: str) -> str:
        """Convert a bash `[ $a -gt 1 ]` test into a C-style expression."""
        ops = {"-eq": "==", "-ne": "!=", "-gt": ">", "-lt": "<", "-ge": ">=", "-le": "<=", "=": "==", "!=": "!="}
        tokens = test.split()
        return " ".join(ops.get(t, t.replace("$", "")) for t in tokens)

    def _find_top_level_op(self, s: str, ops: Tuple[str, ...]) -> Optional[Tuple[int, str]]:
        depth = 0
        in_str = None
        i = len(s) - 1
        while i >= 0:
            ch = s[i]
            if ch in ('"', "'") and (i == 0 or s[i - 1] != "\\"):
                if in_str is None:
                    in_str = ch
                elif in_str == ch:
                    in_str = None
            elif in_str is None:
                if ch in (")", "]", "}"):
                    depth += 1
                elif ch in ("(", "[", "{"):
                    depth -= 1
                elif depth == 0:
                    for op in ops:
                        op_len = len(op)
                        if i - op_len + 1 >= 0 and s[i - op_len + 1 : i + 1] == op:
                            pos = i - op_len + 1
                            # Avoid matching `<=` or `>=` or `==` or `!=` when checking `<` or `>`
                            if op in ("<", ">") and i + 1 < len(s) and s[i + 1] == "=":
                                continue
                            if op in ("<", ">") and pos > 0 and s[pos - 1] in ("-", "="):
                                continue
                            return pos, op
            i -= 1
        return None

    def _parens_balanced(self, s: str) -> bool:
        depth = 0
        in_str = None
        for i, ch in enumerate(s):
            if ch in ('"', "'") and (i == 0 or s[i - 1] != "\\"):
                if in_str is None:
                    in_str = ch
                elif in_str == ch:
                    in_str = None
            elif in_str is None:
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth < 0:
                        return False
        return depth == 0

    def _split_args(self, s: str) -> List[str]:
        if not s.strip():
            return []
        parts = []
        cur = []
        depth = 0
        in_str = None
        for i, ch in enumerate(s):
            if ch in ('"', "'") and (i == 0 or s[i - 1] != "\\"):
                if in_str is None:
                    in_str = ch
                elif in_str == ch:
                    in_str = None
                cur.append(ch)
            elif in_str is None:
                if ch in ("(", "[", "{"):
                    depth += 1
                    cur.append(ch)
                elif ch in (")", "]", "}"):
                    depth -= 1
                    cur.append(ch)
                elif ch == "," and depth == 0:
                    parts.append("".join(cur).strip())
                    cur = []
                else:
                    cur.append(ch)
            else:
                cur.append(ch)
        if cur:
            parts.append("".join(cur).strip())
        return parts

    def _normalize_type(self, raw_type: Optional[str]) -> Optional[str]:
        if not raw_type:
            return None
        t = raw_type.strip().rstrip("*&")
        mapping = {
            "int": "int",
            "i32": "int",
            "i64": "int",
            "u32": "int",
            "u64": "int",
            "usize": "int",
            "Int": "int",
            "Integer": "int",
            "long": "int",
            "number": "float",
            "float": "float",
            "double": "float",
            "f32": "float",
            "f64": "float",
            "Float": "float",
            "Double": "float",
            "string": "str",
            "String": "str",
            "std::string": "str",
            "&str": "str",
            "char": "str",
            "bool": "bool",
            "boolean": "bool",
            "Boolean": "bool",
            "Bool": "bool",
            "void": "None",
            "Unit": "None",
            "()": "None",
        }
        return mapping.get(t, t)

    def _infer_literal_type(self, node: RosettaNode) -> Optional[str]:
        if isinstance(node, Literal):
            if isinstance(node.value, bool):
                return "bool"
            if isinstance(node.value, int):
                return "int"
            if isinstance(node.value, float):
                return "float"
            if isinstance(node.value, str):
                return "str"
            if isinstance(node.value, list):
                return "list"
        return None
