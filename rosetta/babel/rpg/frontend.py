from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import Program, RPGOperation, RPGIndicator, Literal, Identifier, VariableDeclaration
from typing import Optional

class RPGFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "rpg"

    @property
    def supported_version(self) -> str:
        return "RPG III/IV"

    def _parse_term(self, val: str):
        if not val:
            return None
        if (val.startswith("'") and val.endswith("'")) or (val.startswith('"') and val.endswith('"')):
            return Literal(value=val[1:-1])
        if val.isdigit():
            return Literal(value=int(val))
        if val.startswith("*"):
            return RPGIndicator(name=val)
        return Identifier(name=val)

    def parse(self, source: str) -> Program:
        lines = source.splitlines()
        body = []
        for line in lines:
            if len(line) < 6:
                continue
            spec = line[5].upper()
            if spec == 'D':
                name = line[6:20].strip()
                if name:
                    body.append(VariableDeclaration(name=name, type_hint=None, initializer=None))
            elif spec == 'C':
                f1 = line[11:25].strip() if len(line) > 11 else ""
                op = line[25:35].strip() if len(line) > 25 else ""
                f2 = line[35:49].strip() if len(line) > 35 else ""
                res = line[49:63].strip() if len(line) > 49 else ""
                ind = line[63:76].strip() if len(line) > 63 else ""
                if op:
                    body.append(RPGOperation(
                        opcode=op.upper(),
                        factor1=self._parse_term(f1),
                        factor2=self._parse_term(f2),
                        result=Identifier(name=res) if res else None,
                        indicators=[ind] if ind else []
                    ))
        return Program(body=body)
