import ast
from typing import Any
from rosetta.babel.base.base import BabelFrontend
from rosetta.ir.nodes import *

class PythonFrontend(BabelFrontend):
    @property
    def language_id(self) -> str:
        return "python"

    @property
    def supported_version(self) -> str:
        return "3.11+"

    def parse(self, source: str) -> RosettaNode:
        tree = ast.parse(source)
        return self._visit(tree)

    def _visit(self, node: Any) -> RosettaNode:
        if isinstance(node, ast.Module):
            return Program(body=[self._visit(stmt) for stmt in node.body])

        if isinstance(node, ast.Assign):
            # Simplified: assuming single target
            target = self._visit(node.targets[0])
            value = self._visit(node.value)
            return Assignment(target=target, value=value)

        if isinstance(node, ast.AnnAssign):
            # type hinted assignment
            target = self._visit(node.target)
            value = self._visit(node.value) if node.value else None
            type_hint = ast.unparse(node.annotation)
            return VariableDeclaration(name=target.name, type_hint=type_hint, initializer=value)

        if isinstance(node, ast.Name):
            return Identifier(name=node.id)

        if isinstance(node, ast.Constant):
            return Literal(value=node.value)

        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            name = node.name
            params = [Parameter(name=arg.arg, type_hint=ast.unparse(arg.annotation) if arg.annotation else None) for arg in node.args.args]
            body = [self._visit(stmt) for stmt in node.body]
            return_type = ast.unparse(node.returns) if node.returns else None
            decorators = [self._visit(dec) for dec in node.decorator_list]
            
            if isinstance(node.parent_node if hasattr(node, 'parent_node') else None, ast.ClassDef):
                # This logic would need parent tracking, but for now we'll distinguish in the class visitor
                return MethodDeclaration(name=name, params=params, body=body, return_type=return_type, is_async=isinstance(node, ast.AsyncFunctionDef), decorators=decorators)
            
            return FunctionDeclaration(name=name, params=params, body=body, return_type=return_type, is_async=isinstance(node, ast.AsyncFunctionDef), decorators=decorators)

        if isinstance(node, ast.ClassDef):
            name = node.name
            bases = [ast.unparse(base) for base in node.bases]
            body = []
            for stmt in node.body:
                visited = self._visit(stmt)
                if isinstance(visited, FunctionDeclaration):
                    # Convert to MethodDeclaration
                    visited = MethodDeclaration(
                        name=visited.name, 
                        params=visited.params, 
                        body=visited.body, 
                        return_type=visited.return_type, 
                        is_async=visited.is_async, 
                        decorators=visited.decorators
                    )
                body.append(visited)
            return ClassDeclaration(name=name, bases=bases, body=body)

        if isinstance(node, ast.Return):
            value = self._visit(node.value) if node.value else None
            return ReturnStatement(value=value)

        if isinstance(node, ast.Call):
            callee = self._visit(node.func)
            args = [self._visit(arg) for arg in node.args]
            return CallExpression(callee=callee, args=args)

        if isinstance(node, ast.Expr):
            return self._visit(node.value)

        if isinstance(node, ast.BinOp):
            left = self._visit(node.left)
            right = self._visit(node.right)
            ops = {
                ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/",
                ast.Mod: "%", ast.Pow: "**", ast.LShift: "<<", ast.RShift: ">>",
                ast.BitOr: "|", ast.BitXor: "^", ast.BitAnd: "&", ast.FloorDiv: "//"
            }
            return BinaryExpression(left=left, operator=ops[type(node.op)], right=right)

        if isinstance(node, ast.If):
            condition = self._visit(node.test)
            consequent = [self._visit(stmt) for stmt in node.body]
            alternate = [self._visit(stmt) for stmt in node.orelse] if node.orelse else None
            return IfStatement(condition=condition, consequent=consequent, alternate=alternate)

        if isinstance(node, ast.ListComp):
            expression = self._visit(node.elt)
            generators = []
            for gen in node.generators:
                target = self._visit(gen.target)
                iterable = self._visit(gen.iter)
                ifs = [self._visit(if_node) for if_node in gen.ifs]
                generators.append(ComprehensionGenerator(target=target, iterable=iterable, ifs=ifs))
            return ListComprehension(expression=expression, generators=generators)

        if isinstance(node, ast.Await):
            return AwaitExpression(argument=self._visit(node.value))

        if isinstance(node, ast.Yield):
            return YieldExpression(argument=self._visit(node.value) if node.value else None)

        if isinstance(node, ast.Compare):
            left = self._visit(node.left)
            ops = {
                ast.Eq: "==", ast.NotEq: "!=", ast.Lt: "<", ast.LtE: "<=",
                ast.Gt: ">", ast.GtE: ">=", ast.Is: "===", ast.IsNot: "!==",
                ast.In: "in", ast.NotIn: "not in"
            }
            # Simplified: assuming single comparison
            return BinaryExpression(left=left, operator=ops[type(node.ops[0])], right=self._visit(node.comparators[0]))

        if isinstance(node, ast.List):
            return Literal(value=[self._visit(elt) for elt in node.elts])

        if isinstance(node, ast.UnaryOp):
            ops = {ast.UAdd: "+", ast.USub: "-", ast.Not: "!", ast.Invert: "~"}
            return UnaryExpression(operator=ops[type(node.op)], argument=self._visit(node.operand))

        if isinstance(node, ast.Attribute):
            return MemberAccess(object=self._visit(node.value), member=node.attr)

        if isinstance(node, ast.Lambda):
            params = [Parameter(name=arg.arg) for arg in node.args.args]
            body = self._visit(node.body)
            return LambdaExpression(params=params, body=body)

        if isinstance(node, ast.BoolOp):
            op = "&&" if isinstance(node.op, ast.And) else "||"
            res = self._visit(node.values[0])
            for val in node.values[1:]:
                res = BinaryExpression(left=res, operator=op, right=self._visit(val))
            return res

        if isinstance(node, ast.For):
            iterator = self._visit(node.target)
            iterable = self._visit(node.iter)
            body = [self._visit(stmt) for stmt in node.body]
            return ForInLoop(iterator=iterator, iterable=iterable, body=body)

        if isinstance(node, ast.While):
            condition = self._visit(node.test)
            body = [self._visit(stmt) for stmt in node.body]
            return WhileLoop(condition=condition, body=body)

        if isinstance(node, ast.Pass):
            return Program(body=[])

        return RosettaNode(metadata={"raw_ast": ast.dump(node)})
