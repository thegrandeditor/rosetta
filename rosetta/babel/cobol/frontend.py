import re
from antlr4 import *
from rosetta.babel.base.base import BabelFrontend
from rosetta.babel.cobol.grammar.CobolLexer import CobolLexer
from rosetta.babel.cobol.grammar.CobolParser import CobolParser
from rosetta.babel.cobol.antlr_visitor import RosettaCobolVisitor
from rosetta.ir.nodes import Program

class PatchedCobolLexer(CobolLexer):
    """
    Ensures numeric literals are not hijacked by PICTURE_STRING when matching purely digits.
    """
    def nextToken(self):
        t = super().nextToken()
        if t.type == CobolLexer.PICTURE_STRING and re.match(r'^\d+(\.\d+)?$', t.text):
            t.type = CobolLexer.NUMBER
        return t

class CobolAntlrFrontend(BabelFrontend):

    @property
    def language_id(self) -> str:
        return "cobol"

    @property
    def supported_version(self) -> str:
        return "COBOL-85 (Subset)"

    @property
    def source_extensions(self) -> list[str]:
        return [".cbl", ".cob"]

    def preprocess(self, source_code: str) -> str:
        source_code = source_code.replace('\u2018', "'").replace('\u2019', "'")
        source_code = source_code.replace('\u201c', '"').replace('\u201d', '"')
        source_code = source_code.replace('\xa0', ' ')
        source_code = source_code.replace('\r\n', '\n').replace('\r', '\n')
        
        cleaned_lines = []
        COBOL_STATEMENTS = {
            'DISPLAY', 'MOVE', 'PERFORM', 'IF', 'COMPUTE', 'STOP',
            'ADD', 'SUBTRACT', 'MULTIPLY', 'DIVIDE', 'INITIALIZE',
            'SET', 'EVALUATE', 'CALL', 'READ', 'WRITE', 'OPEN', 'CLOSE', 'GO'
        }
        
        in_procedure = False
        final_lines = []
        for line in source_code.splitlines():
            line_strip = line.strip()
            if not line_strip:
                continue
            # Strip COBOL comments
            if line_strip.startswith('*'):
                continue
            if 'ordered/structured' in line_strip or 'multi-dimensional table' in line_strip:
                continue
            
            upper = line_strip.upper().rstrip('.')
            if 'PROCEDURE DIVISION' in upper:
                in_procedure = True
                final_lines.append(line_strip)
                continue
            if in_procedure:
                first_word = line_strip.split()[0].upper().rstrip('.') if line_strip.split() else ""
                if first_word in COBOL_STATEMENTS:
                    final_lines.append("MAIN.")
                in_procedure = False
            final_lines.append(line_strip)
            
        return '\r\n'.join(final_lines) + '\r\n'

    def parse(self, source_code: str) -> Program:
        preprocessed_source = self.preprocess(source_code)
        input_stream = InputStream(preprocessed_source)
        lexer = PatchedCobolLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CobolParser(stream)
        tree = parser.program()
        visitor = RosettaCobolVisitor()
        return visitor.visit(tree)

# For backward compatibility and discovery
CobolFrontend = CobolAntlrFrontend