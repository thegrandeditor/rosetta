from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional, Any, Dict, Union

@dataclass(kw_only=True)
class RosettaNode:
    """Base node for all ROSETTA IR constructs."""
    metadata: Dict[str, Any] = field(default_factory=dict)

# --- Basic / Imperative ---

@dataclass
class Program(RosettaNode):
    body: List[RosettaNode] = field(default_factory=list)

@dataclass
class Identifier(RosettaNode):
    name: str

@dataclass
class Literal(RosettaNode):
    value: Any

@dataclass
class VariableDeclaration(RosettaNode):
    name: str
    type_hint: Optional[str] = None
    initializer: Optional[RosettaNode] = None
    is_const: bool = False

@dataclass
class Assignment(RosettaNode):
    target: RosettaNode
    value: RosettaNode

@dataclass
class FunctionDeclaration(RosettaNode):
    name: str
    params: List[Parameter]
    body: List[RosettaNode]
    return_type: Optional[str] = None
    is_async: bool = False
    decorators: List[RosettaNode] = field(default_factory=list)

@dataclass
class Parameter(RosettaNode):
    name: str
    type_hint: Optional[str] = None
    default_value: Optional[RosettaNode] = None

@dataclass
class ReturnStatement(RosettaNode):
    value: Optional[RosettaNode] = None

@dataclass
class CallExpression(RosettaNode):
    callee: RosettaNode
    args: List[RosettaNode] = field(default_factory=list)

@dataclass
class IfStatement(RosettaNode):
    condition: RosettaNode
    consequent: List[RosettaNode]
    alternate: Optional[List[RosettaNode]] = None

@dataclass
class WhileLoop(RosettaNode):
    condition: RosettaNode
    body: List[RosettaNode]

@dataclass
class ForLoop(RosettaNode):
    initializer: Optional[RosettaNode]
    condition: Optional[RosettaNode]
    increment: Optional[RosettaNode]
    body: List[RosettaNode]

@dataclass
class ForInLoop(RosettaNode):
    iterator: RosettaNode
    iterable: RosettaNode
    body: List[RosettaNode]

@dataclass
class BinaryExpression(RosettaNode):
    left: RosettaNode
    operator: str
    right: RosettaNode

@dataclass
class UnaryExpression(RosettaNode):
    operator: str
    argument: RosettaNode

@dataclass
class Label(RosettaNode):
    name: str

@dataclass
class GotoStatement(RosettaNode):
    label: str

# --- OOP ---

@dataclass
class ClassDeclaration(RosettaNode):
    name: str
    bases: List[str] = field(default_factory=list)
    body: List[RosettaNode] = field(default_factory=list)
    interfaces: List[str] = field(default_factory=list)

@dataclass
class MethodDeclaration(FunctionDeclaration):
    is_static: bool = False
    is_abstract: bool = False

@dataclass
class MemberAccess(RosettaNode):
    object: RosettaNode
    member: str

# --- Functional Patterns ---

@dataclass
class MapExpression(RosettaNode):
    collection: RosettaNode
    function: LambdaExpression

@dataclass
class FilterExpression(RosettaNode):
    collection: RosettaNode
    function: LambdaExpression

# --- Functional ---

@dataclass
class LambdaExpression(RosettaNode):
    params: List[Parameter]
    body: Union[RosettaNode, List[RosettaNode]]

@dataclass
class ListComprehension(RosettaNode):
    expression: RosettaNode
    generators: List[ComprehensionGenerator]

@dataclass
class ComprehensionGenerator(RosettaNode):
    target: RosettaNode
    iterable: RosettaNode
    ifs: List[RosettaNode] = field(default_factory=list)

# --- Low-level ---

@dataclass
class StructDeclaration(RosettaNode):
    name: str
    fields: List[VariableDeclaration]

@dataclass
class PointerType(RosettaNode):
    base_type: str

@dataclass
class MemoryAllocation(RosettaNode):
    size: RosettaNode
    type_hint: Optional[str] = None

@dataclass
class Dereference(RosettaNode):
    argument: RosettaNode

# --- Declarative / Others ---

@dataclass
class RecordDeclaration(RosettaNode):
    name: str
    fields: List[VariableDeclaration]

@dataclass
class Fact(RosettaNode):
    predicate: str
    terms: List[RosettaNode]

@dataclass
class Query(RosettaNode):
    predicate: str
    terms: List[RosettaNode]

@dataclass
class ArrayAccess(RosettaNode):
    object: RosettaNode
    index: List[RosettaNode]

@dataclass
class ArrayDeclaration(VariableDeclaration):
    dimensions: List[RosettaNode] = field(default_factory=list)

@dataclass
class GlobalBlock(RosettaNode):
    name: Optional[str] = None
    members: List[VariableDeclaration] = field(default_factory=list)

@dataclass
class FormatDeclaration(RosettaNode):
    label: str
    items: List[Any]

@dataclass
class TryCatch(RosettaNode):
    body: List[RosettaNode]
    handlers: List[ExceptionHandler]
    finally_body: Optional[List[RosettaNode]] = None

@dataclass
class ExceptionHandler(RosettaNode):
    exception_type: Optional[str]
    variable: Optional[str]
    body: List[RosettaNode]

@dataclass
class TaskDeclaration(RosettaNode):
    name: str
    body: List[RosettaNode]

@dataclass
class GenericDeclaration(RosettaNode):
    name: str
    parameters: List[Parameter]
    declaration: RosettaNode

@dataclass
class MacroDeclaration(RosettaNode):
    name: str
    params: List[Parameter]
    body: RosettaNode

@dataclass
class PrologClause(RosettaNode):
    head: Fact
    body: List[Union[Fact, Query]]

@dataclass
class PrologRule(RosettaNode):
    clauses: List[PrologClause]

@dataclass
class WithStatement(RosettaNode):
    objects: List[RosettaNode]
    body: List[RosettaNode]

@dataclass
class ModuleDeclaration(RosettaNode):
    name: str
    body: List[RosettaNode]
    exports: List[str] = field(default_factory=list)

@dataclass
class RecordAccess(RosettaNode):
    object: RosettaNode
    field: str

@dataclass
class AwaitExpression(RosettaNode):
    argument: RosettaNode

@dataclass
class PatternMatchStatement(RosettaNode):
    subject: RosettaNode
    pattern: RosettaNode
    replacement: Optional[RosettaNode] = None

@dataclass
class SNOBOLTransfer(RosettaNode):
    success_label: Optional[str] = None
    failure_label: Optional[str] = None
    unconditional_label: Optional[str] = None

@dataclass
class SNOBOLStatement(RosettaNode):
    label: Optional[str] = None
    content: Optional[RosettaNode] = None
    transfer: Optional[SNOBOLTransfer] = None

@dataclass
class MemoryFree(RosettaNode):
    argument: RosettaNode

@dataclass
class OnCondition(RosettaNode):
    condition: str
    body: List[RosettaNode]

@dataclass
class EntryDeclaration(FunctionDeclaration):
    parent_procedure: Optional[str] = None

@dataclass
class Contract(RosettaNode):
    require: List[RosettaNode] = field(default_factory=list)
    ensure: List[RosettaNode] = field(default_factory=list)

@dataclass
class ContractedFunction(FunctionDeclaration):
    contract: Optional[Contract] = None

@dataclass
class ContractedClass(ClassDeclaration):
    invariant: List[RosettaNode] = field(default_factory=list)

@dataclass
class ImportStatement(RosettaNode):
    module_name: Optional[str]
    symbols: List[str]

@dataclass
class ExportStatement(RosettaNode):
    symbols: List[str]

@dataclass
class CoroutineDeclaration(FunctionDeclaration):
    pass

@dataclass
class YieldExpression(RosettaNode):
    argument: Optional[RosettaNode] = None

# --- Forth ---

@dataclass
class ForthStackOp(RosettaNode):
    operation: str # DUP, DROP, SWAP, OVER, etc.

@dataclass
class ForthWordDefinition(FunctionDeclaration):
    pass

# --- ML ---

@dataclass
class MLValDeclaration(VariableDeclaration):
    pattern: Optional[RosettaNode] = None

@dataclass
class MLFunDeclaration(FunctionDeclaration):
    pass

@dataclass
class MLDataTypeDeclaration(RosettaNode):
    name: str
    constructors: List[MLConstructor]

@dataclass
class MLConstructor(RosettaNode):
    name: str
    types: List[str] = field(default_factory=list)

@dataclass
class MLCaseExpression(RosettaNode):
    expression: RosettaNode
    branches: List[MLCaseBranch]

@dataclass
class MLCaseBranch(RosettaNode):
    pattern: RosettaNode
    body: RosettaNode

@dataclass
class MLLetExpression(RosettaNode):
    bindings: List[RosettaNode]
    body: RosettaNode

# --- RPG ---

@dataclass
class RPGIndicator(RosettaNode):
    name: str # e.g., *IN01

@dataclass
class RPGOperation(RosettaNode):
    opcode: str
    factor1: Optional[RosettaNode] = None
    factor2: Optional[RosettaNode] = None
    result: Optional[RosettaNode] = None
    indicators: List[str] = field(default_factory=list)

# --- Solidity ---

@dataclass
class SmartContractDeclaration(ClassDeclaration):
    is_interface: bool = False
    is_library: bool = False

@dataclass
class MappingType(RosettaNode):
    key_type: str
    value_type: str

@dataclass
class ModifierDeclaration(FunctionDeclaration):
    pass

@dataclass
class EventDeclaration(RosettaNode):
    name: str
    params: List[Parameter]

@dataclass
class EmitStatement(RosettaNode):
    event_call: CallExpression

# --- Mojo ---

@dataclass
class SIMDType(RosettaNode):
    base_type: str
    size: int

@dataclass
class MojoStructDeclaration(StructDeclaration):
    pass

# --- Zig ---

@dataclass
class ComptimeExpression(RosettaNode):
    expression: RosettaNode

@dataclass
class DeferStatement(RosettaNode):
    body: List[RosettaNode]
    is_errdefer: bool = False

@dataclass
class ErrorUnionType(RosettaNode):
    error_set: Optional[str]
    value_type: str

# --- Carbon ---

@dataclass
class InterfaceDeclaration(RosettaNode):
    name: str
    body: List[RosettaNode]

@dataclass
class ImplDeclaration(RosettaNode):
    interface_name: str
    target_type: str
    body: List[RosettaNode]
