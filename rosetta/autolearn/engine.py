import os
import re

class AutoLearnEngine:
    def __init__(self, generated_root: str = None):
        # Always write next to this package (independent of the current working
        # directory) so the resolver can auto-discover learned languages.
        self.generated_root = generated_root or os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated")

    @staticmethod
    def _pick_keyword(content: str, candidates, default: str) -> str:
        for kw in candidates:
            if re.search(r"['\"]" + re.escape(kw) + r"['\"]", content) or re.search(r"\b" + re.escape(kw) + r"\b", content):
                return kw
        return default

    def learn_from_grammar(self, grammar_path: str, output_lang_name: str = None) -> str:
        """Reads a .g4 file and generates draft frontend, backend, IR mappings, and starter test."""
        if not os.path.exists(grammar_path):
            raise FileNotFoundError(f"Grammar file not found: {grammar_path}")
            
        with open(grammar_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Get grammar name
        grammar_name = "DraftLang"
        match = re.search(r"grammar\s+([A-Za-z0-9_]+)\s*;", content)
        if match:
            grammar_name = match.group(1)
            
        grammar_name = grammar_name[0].upper() + grammar_name[1:]
        lang_id = (output_lang_name or grammar_name).lower()
        
        # Analyze rules
        rules = re.findall(r"([a-z][A-Za-z0-9_]*)\s*:", content)
        
        functions = []
        variables = []
        control_flow = []
        classes = []
        expressions = []
        
        for rule in rules:
            rule_lower = rule.lower()
            if any(k in rule_lower for k in ["func", "fn", "def", "method", "procedure"]):
                functions.append(rule)
            elif any(k in rule_lower for k in ["var", "decl", "let", "assign", "const"]):
                variables.append(rule)
            elif any(k in rule_lower for k in ["if", "else", "while", "for", "loop", "cond", "branch"]):
                control_flow.append(rule)
            elif any(k in rule_lower for k in ["class", "struct", "object", "interface", "contract"]):
                classes.append(rule)
            elif any(k in rule_lower for k in ["expr", "term", "factor", "primary", "literal", "value"]):
                expressions.append(rule)

        # Build paths
        if not re.match(r"^[a-z][a-z0-9_]*$", lang_id):
            raise ValueError(f"Invalid language id {lang_id!r}: use letters, digits and underscores only")
        base_dir = os.path.join(self.generated_root, lang_id)
        os.makedirs(os.path.join(base_dir, "babel"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, "cipher"), exist_ok=True)
        os.makedirs(os.path.join(base_dir, "tests"), exist_ok=True)

        # Infer surface keywords from the grammar so the draft backend speaks the language
        fn_kw = self._pick_keyword(content, ["function", "func", "fn", "def", "fun", "sub", "procedure", "proc"], "fn")
        var_kw = self._pick_keyword(content, ["let", "var", "val", "local", "my", "dim", "auto"], "let")
        print_kw = self._pick_keyword(content, ["println", "print", "puts", "echo", "say", "write", "display", "output"], "print")
        
        # 1. Draft Babel Frontend
        frontend_code = self._generate_babel_frontend(lang_id, grammar_name, rules, functions, variables, control_flow, classes, expressions)
        frontend_path = os.path.join(base_dir, "babel", "frontend.py")
        with open(frontend_path, "w", encoding="utf-8") as f:
            f.write(frontend_code)
            
        # 2. Draft Cipher Backend
        backend_code = self._generate_cipher_backend(lang_id, grammar_name, fn_kw, var_kw, print_kw)
        backend_path = os.path.join(base_dir, "cipher", "backend.py")
        with open(backend_path, "w", encoding="utf-8") as f:
            f.write(backend_code)
            
        # 3. Starter Test File
        test_code = self._generate_starter_test(lang_id, grammar_name)
        test_path = os.path.join(base_dir, "tests", "test_transpile.py")
        with open(test_path, "w", encoding="utf-8") as f:
            f.write(test_code)
            
        # Write grammar file copy
        with open(os.path.join(base_dir, f"{grammar_name}.g4"), "w", encoding="utf-8") as f:
            f.write(content)

        # 4. Hot-register into the live resolver (CLI / MCP / Web Studio)
        try:
            from rosetta.cli.resolver import discover_learned_languages
            discover_learned_languages()
        except Exception:
            pass

        return f"Successfully generated Babel frontend, Cipher backend, and tests for '{lang_id}' in '{base_dir}'! It is now registered as '.{lang_id}' (source) and '{lang_id}' (target)."

    def learn_from_bnf(self, bnf_path: str, output_lang_name: str = None) -> str:
        """Parses a BNF/EBNF grammar file, converts to draft .g4, and generates Babel/Cipher."""
        if not os.path.exists(bnf_path):
            raise FileNotFoundError(f"BNF file not found: {bnf_path}")
            
        with open(bnf_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        lang_id = (output_lang_name or os.path.basename(bnf_path).split(".")[0]).lower()
        grammar_name = lang_id.capitalize()
        
        # Simple BNF to ANTLR conversion
        # Replace ::= with : and end with ;
        g4_lines = [f"grammar {grammar_name};", ""]
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("//"):
                continue
            if "::=" in line:
                parts = line.split("::=")
                lhs = parts[0].strip().replace("<", "").replace(">", "")
                rhs = parts[1].strip()
                # Clean up <rule> references
                rhs = re.sub(r"<([A-Za-z0-9_]+)>", r"\1", rhs)
                g4_lines.append(f"{lhs} : {rhs} ;")
            elif "=" in line:
                parts = line.split("=")
                lhs = parts[0].strip()
                rhs = parts[1].strip()
                g4_lines.append(f"{lhs} : {rhs} ;")
        
        # Add basic lexer rules if missing
        g4_lines.extend([
            "",
            "ID : [a-zA-Z_][a-zA-Z0-9_]* ;",
            "NUMBER : [0-9]+ ;",
            "STRING : '\"' ~[\"]* '\"' ;",
            "WS : [ \\t\\r\\n]+ -> skip ;"
        ])
        
        g4_content = "\n".join(g4_lines)
        temp_g4_path = os.path.join("rosetta", "autolearn", f"{grammar_name}.g4")
        os.makedirs(os.path.dirname(temp_g4_path), exist_ok=True)
        with open(temp_g4_path, "w", encoding="utf-8") as f:
            f.write(g4_content)
            
        msg = self.learn_from_grammar(temp_g4_path, lang_id)
        os.remove(temp_g4_path)
        return msg

    def learn_from_corpus(self, corpus_path: str, output_lang_name: str = None) -> str:
        """Analyzes a folder/file of sample codes, infers constructs, generates .g4, and generates Babel/Cipher."""
        if not os.path.exists(corpus_path):
            raise FileNotFoundError(f"Corpus path not found: {corpus_path}")
            
        lang_id = (output_lang_name or os.path.basename(corpus_path.rstrip("/\\"))).lower()
        grammar_name = lang_id.capitalize()
        
        # Read all files in corpus
        sample_code = ""
        if os.path.isdir(corpus_path):
            for root, _, files in os.walk(corpus_path):
                for file in files:
                    with open(os.path.join(root, file), "r", encoding="utf-8", errors="ignore") as f:
                        sample_code += f.read() + "\n"
        else:
            with open(corpus_path, "r", encoding="utf-8", errors="ignore") as f:
                sample_code = f.read()

        # Simple heuristic analysis of keywords
        keywords = set(re.findall(r"\b[a-zA-Z_][a-zA-Z0-9_]*\b", sample_code))
        
        # Let's generate a basic g4 grammar based on inferred keywords
        g4_lines = [
            f"grammar {grammar_name};",
            "",
            "program : statement* EOF ;",
            "",
            "statement : assignment | function_decl | if_stmt | return_stmt | expr_stmt ;",
            "",
            "expr_stmt : expression ';' ;",
            ""
        ]
        
        # Infer assignments
        if "=" in sample_code:
            g4_lines.append("assignment : ID '=' expression ';' ;")
        else:
            g4_lines.append("assignment : ID ':=' expression ';' ;")
            
        # Infer function definitions
        if "function" in keywords or "func" in keywords or "fn" in keywords or "def" in keywords:
            fn_kw = "function" if "function" in keywords else ("func" if "func" in keywords else ("fn" if "fn" in keywords else "def"))
            g4_lines.append(f"function_decl : '{fn_kw}' ID '(' parameter_list? ')' block ;")
            g4_lines.append("parameter_list : ID (',' ID)* ;")
        else:
            g4_lines.append("function_decl : ID '(' parameter_list? ')' block ;")
            g4_lines.append("parameter_list : ID (',' ID)* ;")
            
        # Infer if statements
        if "if" in keywords:
            g4_lines.append("if_stmt : 'if' '('? expression ')'? block ('else' block)? ;")
        else:
            g4_lines.append("if_stmt : 'IF' expression 'THEN' block ;")
            
        # Infer return statements
        if "return" in keywords:
            g4_lines.append("return_stmt : 'return' expression? ';' ;")
        else:
            g4_lines.append("return_stmt : 'RETURN' expression? ';' ;")
            
        g4_lines.extend([
            "block : '{' statement* '}' | statement ;",
            "",
            "expression : primary (op=('+'|'-'|'*'|'/') primary)* ;",
            "primary : ID | NUMBER | STRING ;",
            "",
            "ID : [a-zA-Z_][a-zA-Z0-9_]* ;",
            "NUMBER : [0-9]+ ;",
            "STRING : '\"' ~[\"]* '\"' | '\\'' ~[']* '\\'' ;",
            "WS : [ \\t\\r\\n]+ -> skip ;"
        ])
        
        g4_content = "\n".join(g4_lines)
        temp_g4_path = os.path.join("rosetta", "autolearn", f"{grammar_name}.g4")
        os.makedirs(os.path.dirname(temp_g4_path), exist_ok=True)
        with open(temp_g4_path, "w", encoding="utf-8") as f:
            f.write(g4_content)
            
        msg = self.learn_from_grammar(temp_g4_path, lang_id)
        os.remove(temp_g4_path)
        return msg

    def _generate_babel_frontend(self, lang_id, grammar_name, rules, functions, variables, control_flow, classes, expressions):
        class_name = f"{grammar_name}Frontend"
        visitor_name = f"Rosetta{grammar_name}Visitor"
        
        methods = []
        for rule in rules:
            capitalized_rule = rule[0].upper() + rule[1:]
            
            # Smart default generation based on classification
            body = "        return self.visitChildren(ctx)"
            
            if rule in functions:
                body = (
                    "        # Automatically identified function rule\n"
                    "        name = ctx.ID().getText() if ctx.ID() else 'anonymous'\n"
                    "        return FunctionDeclaration(name=name, params=[], body=[])"
                )
            elif rule in variables:
                body = (
                    "        # Automatically identified variable/assignment rule\n"
                    "        name = ctx.ID().getText() if ctx.ID() else 'temp'\n"
                    "        return VariableDeclaration(name=name, initializer=None)"
                )
            elif rule in control_flow:
                body = (
                    "        # Automatically identified control flow rule\n"
                    "        return IfStatement(condition=Literal(value=True), consequent=[])"
                )
            elif rule in classes:
                body = (
                    "        # Automatically identified class rule\n"
                    "        name = ctx.ID().getText() if ctx.ID() else 'MyClass'\n"
                    "        return ClassDeclaration(name=name, body=[])"
                )
            elif rule in expressions:
                body = (
                    "        # Automatically identified expression rule\n"
                    "        if ctx.getChildCount() == 1:\n"
                    "            return self.visit(ctx.getChild(0))\n"
                    "        return Literal(value=ctx.getText())"
                )
                
            methods.append(f"""    def visit{capitalized_rule}(self, ctx):
{body}""")

        visitor_code = "\n\n".join(methods)
        
        return f"""from rosetta.babel.base.modern_parser import ModernLanguageParser
try:
    from antlr4 import *  # noqa: F401,F403  (used once ANTLR parser classes are generated)
except ImportError:  # pragma: no cover
    pass
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class {visitor_name}(object):
    def visit(self, tree):
        if not tree:
            return None
        return tree.accept(self)

    def visitChildren(self, node):
        result = []
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            res = self.visit(child)
            if res:
                if isinstance(res, list):
                    result.extend(res)
                else:
                    result.append(res)
        return result

    def visitProgram(self, ctx):
        body = []
        for i in range(ctx.getChildCount()):
            res = self.visit(ctx.getChild(i))
            if res:
                if isinstance(res, list):
                    body.extend(res)
                else:
                    body.append(res)
        return Program(body=body)

{visitor_code}

class {class_name}(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "{lang_id}"

    @property
    def supported_version(self) -> str:
        return "Draft Standard"

    def parse(self, source: str) -> Program:
        # If ANTLR has generated {grammar_name}Lexer/{grammar_name}Parser next to the
        # grammar, the visitor above can be wired in. Until then, use Rosetta's
        # universal structural parser so the learned language works immediately.
        return ModernLanguageParser("{lang_id}").parse(source)
"""

    def _generate_cipher_backend(self, lang_id, grammar_name, fn_kw="fn", var_kw="let", print_kw="print"):
        class_name = f"{grammar_name}Backend"
        return f'''"""Auto-learned CIPHER backend for '{lang_id}' (generated by rosetta learn)."""
from rosetta.cipher.base.universal import UniversalBackend
from rosetta.ir.nodes import *


class {class_name}(UniversalBackend):
    LANG = "{lang_id}"
    STYLE = "Auto-learned draft"
    FN_KW = "{fn_kw}"
    VAR_KW = "{var_kw}"
    PRINT_KW = "{print_kw}"

    def var_decl(self, node, indent, in_class=None):
        init = f" = {{self.expr(node.initializer)}}" if node.initializer is not None else ""
        return f"{{self.pad(indent)}}{{self.VAR_KW}} {{node.name}}{{init}}{{self.STMT_END}}"

    def func(self, node, indent, in_class=None):
        p = self.pad(indent)
        params = ", ".join(x.name for x in self.real_params(node))
        return self._join(f"{{p}}{{self.FN_KW}} {{node.name}}({{params}}) {{{{", self.block(node.body, indent + 1), p + "}}")

    def print_stmt(self, args):
        return f"{{self.PRINT_KW}}({{', '.join(self.expr(a) for a in args)}}){{self.STMT_END}}"
'''

    def _generate_starter_test(self, lang_id, grammar_name=None):
        cls = f"{grammar_name or lang_id.capitalize()}Backend"
        return f"""from rosetta.ir.nodes import *
from rosetta.autolearn.generated.{lang_id}.cipher.backend import {cls}

def test_draft_backend():
    backend = {cls}()
    prog = Program(body=[
        VariableDeclaration(name="x", initializer=Literal(value=42)),
        FunctionDeclaration(name="hello", params=[], body=[
            ReturnStatement(value=Identifier(name="x"))
        ])
    ])
    code = backend.emit(prog)
    assert f"{{backend.VAR_KW}} x = 42;" in code
    assert f"{{backend.FN_KW}} hello()" in code
    print("Draft backend test passed!")

if __name__ == "__main__":
    test_draft_backend()
"""
