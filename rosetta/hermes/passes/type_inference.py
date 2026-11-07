from rosetta.hermes.pipeline import HermesPass
from rosetta.ir.nodes import *
from typing import Dict, Any, Optional, Set

class TypeInferencePass(HermesPass):
    def __init__(self):
        self.symbol_table: List[Dict[str, str]] = [{}] # Stack of scopes
        self.function_types: Dict[str, str] = {} # function_name -> return_type
        self.recursion_depth: Dict[str, int] = {}

    def _push_scope(self):
        self.symbol_table.append({})

    def _pop_scope(self):
        self.symbol_table.pop()

    def _set_type(self, name: str, type_hint: str):
        self.symbol_table[-1][name] = type_hint

    def _get_type(self, name: str) -> str:
        for scope in reversed(self.symbol_table):
            if name in scope:
                return scope[name]
        return "any"

    def _find_return_types(self, body: List[RosettaNode]) -> List[str]:
        types = []
        for node in body:
            if isinstance(node, ReturnStatement) and node.value:
                types.append(self.infer_type(node.value))
            elif isinstance(node, IfStatement):
                types.extend(self._find_return_types(node.consequent))
                if node.alternate:
                    types.extend(self._find_return_types(node.alternate))
            elif isinstance(node, (WhileLoop, ForLoop, ForInLoop)):
                types.extend(self._find_return_types(node.body))
        return types

    def infer_type(self, node: RosettaNode) -> str:
        if isinstance(node, Literal):
            if isinstance(node.value, bool): return "bool"
            if isinstance(node.value, int): return "int"
            if isinstance(node.value, float): return "float"
            if isinstance(node.value, str): return "string"
            if isinstance(node.value, list): return "list"
            return "any"
        
        if isinstance(node, Identifier):
            return self._get_type(node.name)
        
        if isinstance(node, MemberAccess) and isinstance(node.object, Identifier) and node.object.name == "self":
            return self._get_type(f"self.{node.member}")

        if isinstance(node, BinaryExpression):
            left_t = self.infer_type(node.left)
            right_t = self.infer_type(node.right)
            
            if node.operator in ['+', '-', '*', '/']:
                if left_t == "float" or right_t == "float": return "float"
                if left_t == "int" and right_t == "int": return "int"
                if node.operator == '+' and (left_t == "string" or right_t == "string"): return "string"
            
            if node.operator in ['==', '!=', '<', '>', '<=', '>=']: return "bool"
            return left_t if left_t == right_t else "any"

        if isinstance(node, CallExpression):
            if isinstance(node.callee, Identifier):
                # Handle recursive calls
                name = node.callee.name
                if name in self.function_types:
                    return self.function_types[name]
            if isinstance(node.callee, MemberAccess):
                if node.callee.member in ["map", "filter"]: return "list"
            return "any"

        if isinstance(node, ListComprehension): return "list"
        if isinstance(node, MapExpression) or isinstance(node, FilterExpression): return "list"
        if isinstance(node, LambdaExpression): return "function"
        
        return "any"

    def transform(self, node: RosettaNode) -> RosettaNode:
        if node is None: return None
        if not isinstance(node, RosettaNode):
            if isinstance(node, list):
                return [self.transform(item) for item in node]
            return node

        if isinstance(node, Program):
            node.body = [self.transform(s) for s in node.body]
            return node
        
        if isinstance(node, ClassDeclaration):
            self._push_scope()
            node.body = [self.transform(s) for s in node.body]
            self._pop_scope()
            return node

        if isinstance(node, FunctionDeclaration):
            # Register function name in current scope before entering
            self._set_type(node.name, node.return_type or "any")
            
            self._push_scope()
            for param in node.params:
                self._set_type(param.name, param.type_hint or "any")
            
            # Simple recursion check
            depth = self.recursion_depth.get(node.name, 0)
            if depth < 2:
                self.recursion_depth[node.name] = depth + 1
                node.body = [self.transform(s) for s in node.body]
                self.recursion_depth[node.name] = depth
            
            if not node.return_type or node.return_type == "any":
                ret_types = self._find_return_types(node.body)
                if ret_types:
                    node.return_type = ret_types[0]
            
            if node.return_type:
                self.function_types[node.name] = node.return_type
                # Update in parent scope too
                if len(self.symbol_table) > 1:
                    self.symbol_table[-2][node.name] = node.return_type
            
            self._pop_scope()
            return node

        if isinstance(node, VariableDeclaration):
            if node.initializer:
                node.initializer = self.transform(node.initializer)
                inferred = self.infer_type(node.initializer)
                if not node.type_hint or node.type_hint == "any":
                    node.type_hint = inferred
            self._set_type(node.name, node.type_hint or "any")
            return node

        if isinstance(node, Assignment):
            node.value = self.transform(node.value)
            inferred = self.infer_type(node.value)
            if isinstance(node.target, Identifier):
                name = node.target.name
                self._set_type(name, inferred)
                node.target.metadata["type"] = inferred
            elif isinstance(node.target, MemberAccess) and isinstance(node.target.object, Identifier) and node.target.object.name == "self":
                self._set_type(f"self.{node.target.member}", inferred)
            return node

        # Default traversal
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        return node

