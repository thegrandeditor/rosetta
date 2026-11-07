import re
from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.solidity.grammar.SolidityLexer import SolidityLexer
from rosetta.babel.solidity.grammar.SolidityParser import SolidityParser
from rosetta.babel.solidity.antlr_visitor import RosettaSolidityVisitor
from rosetta.ir.nodes import Program

class SolidityFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "solidity"

    @property
    def supported_version(self) -> str:
        return "Solidity ^0.8.0"

    def preprocess(self, source: str) -> str:
        # Normalize line endings
        source = source.replace('\r\n', '\n').replace('\r', '\n')
        # 1. Map member access foo.bar to foo_bar (e.g. msg.sender -> msg_sender)
        source = re.sub(r'(\b[a-zA-Z_]\w*)\.([a-zA-Z_]\w*)', r'\1_\2', source)
        # 2. Map mapping/index access arr[x] to arr(x)
        source = re.sub(r'\[([^\]\n]+)\]', r'(\1)', source)
        # 3. Normalize single-statement if-blocks for Solidity grammar compatibility
        lines = []
        in_if_block = 0
        for line in source.splitlines():
            line_str = line.strip()
            if line_str.startswith('if') and line_str.endswith('{'):
                line = line[:line.rfind('{')]
                in_if_block += 1
            elif in_if_block > 0 and line_str == '}':
                in_if_block -= 1
                continue
            lines.append(line)
        return '\n'.join(lines)

    def parse(self, source: str) -> Program:
        preprocessed = self.preprocess(source)
        input_stream = InputStream(preprocessed)
        lexer = SolidityLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SolidityParser(stream)
        tree = parser.program()
        
        visitor = RosettaSolidityVisitor()
        return visitor.visit(tree)
