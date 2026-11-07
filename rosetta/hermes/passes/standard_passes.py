from rosetta.hermes.pipeline import HermesPass
from rosetta.ir.nodes import *
from .type_inference import TypeInferencePass
import copy

class IdiomNormalizationPass(HermesPass):
    def transform(self, node: RosettaNode) -> RosettaNode:
        # Recursively visit children first
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        # Actual Transformation: ListComprehension -> Map/Filter
        if isinstance(node, ListComprehension):
            gen = node.generators[0] 
            target_param = Parameter(name=gen.target.name)
            res = gen.iterable
            for if_cond in gen.ifs:
                res = FilterExpression(
                    collection=res,
                    function=LambdaExpression(params=[target_param], body=if_cond)
                )
            return MapExpression(
                collection=res,
                function=LambdaExpression(params=[target_param], body=node.expression)
            )

        # Handle Decorators: Map to specialized MethodCalls or Metadata
        if isinstance(node, FunctionDeclaration) and node.decorators:
            for deco in node.decorators:
                if isinstance(deco, Identifier) and deco.name == "staticmethod":
                    if isinstance(node, MethodDeclaration):
                        node.is_static = True
                # Add more decorator mappings here
                node.metadata[f"decorator_{deco.name if isinstance(deco, Identifier) else 'unknown'}"] = True
            node.decorators = [] # Clear them once processed

        # Handle map() and filter() calls
        if isinstance(node, CallExpression) and isinstance(node.callee, Identifier):
            if node.callee.name == "map" and len(node.args) == 2:
                func = node.args[0]
                coll = node.args[1]
                if isinstance(func, LambdaExpression):
                    return MapExpression(collection=coll, function=func)
            elif node.callee.name == "filter" and len(node.args) == 2:
                func = node.args[0]
                coll = node.args[1]
                if isinstance(func, LambdaExpression):
                    return FilterExpression(collection=coll, function=func)

        return node

class ScopeResolutionPass(HermesPass):
    def __init__(self):
        self.scopes: List[Dict[str, RosettaNode]] = [{}]
        self.lifetimes: Dict[str, Dict[str, Any]] = {} # var_name -> {declared_at, last_used_at}

    def _push_scope(self):
        self.scopes.append({})

    def _pop_scope(self):
        self.scopes.pop()

    def transform(self, node: RosettaNode) -> RosettaNode:
        if isinstance(node, (Program, ClassDeclaration, FunctionDeclaration)):
            self._push_scope()
            for attr in vars(node):
                val = getattr(node, attr)
                if isinstance(val, list):
                    setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])
            self._pop_scope()
            return node

        if isinstance(node, VariableDeclaration):
            self.scopes[-1][node.name] = node
            node.metadata["scope_depth"] = len(self.scopes)
            return node

        if isinstance(node, Identifier):
            # Track usage for lifetimes
            node.metadata["scope_depth"] = self._find_scope(node.name)
            return node

        # Default traversal
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])
        return node

    def _find_scope(self, name: str) -> int:
        for i, scope in enumerate(reversed(self.scopes)):
            if name in scope:
                return len(self.scopes) - i
        return 0

class DesugarListCompPass(HermesPass):
    def transform(self, node: RosettaNode) -> RosettaNode:
        if isinstance(node, Program):
            new_body = []
            for s in node.body:
                transformed = self.transform(s)
                if isinstance(transformed, Program):
                    new_body.extend(transformed.body)
                else:
                    new_body.append(transformed)
            node.body = new_body
            return node
            
        if isinstance(node, (FunctionDeclaration, MethodDeclaration, ClassDeclaration)):
            new_body = []
            for s in node.body:
                transformed = self.transform(s)
                if isinstance(transformed, Program):
                    new_body.extend(transformed.body)
                else:
                    new_body.append(transformed)
            node.body = new_body
            return node

        if isinstance(node, Assignment):
            if isinstance(node.value, ListComprehension):
                comp = node.value
                target_var = node.target
                init_stmt = Assignment(target=target_var, value=Literal(value=[]))
                gen = comp.generators[0]
                append_call = CallExpression(
                    callee=MemberAccess(object=target_var, member="append"),
                    args=[comp.expression]
                )
                loop_body = [append_call]
                for if_cond in reversed(gen.ifs):
                    loop_body = [IfStatement(condition=if_cond, consequent=loop_body)]
                for_loop = ForInLoop(
                    iterator=gen.target,
                    iterable=gen.iterable,
                    body=loop_body
                )
                return Program(body=[init_stmt, for_loop])

        return node

class LegacyIndexingPass(HermesPass):
    """Converts 1-based indexing to 0-based by subtracting 1 from all ArrayAccess indices."""
    def transform(self, node: RosettaNode) -> RosettaNode:
        # Recursively visit children first
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        if isinstance(node, ArrayAccess):
            new_indices = []
            for idx in node.index:
                if isinstance(idx, Literal) and isinstance(idx.value, int):
                    new_indices.append(Literal(value=idx.value - 1))
                else:
                    new_indices.append(BinaryExpression(
                        left=idx,
                        operator="-",
                        right=Literal(value=1)
                    ))
            node.index = new_indices

        return node

class RedundantDeclarationPass(HermesPass):
    """Removes variable declarations that duplicate function parameters, 
    common in legacy languages like Fortran where parameters must be typed in the body."""
    def transform(self, node: RosettaNode) -> RosettaNode:
        # Recursively visit children first
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        if isinstance(node, (FunctionDeclaration, MethodDeclaration)):
            param_names = {p.name for p in node.params}
            new_body = []
            for stmt in node.body:
                if isinstance(stmt, VariableDeclaration) and stmt.name in param_names and stmt.initializer is None:
                    continue
                new_body.append(stmt)
            node.body = new_body

        return node



class StdlibNormalizationPass(HermesPass):
    """
    Normalizes cross-language standard library calls, I/O intrinsics,
    collection methods, and math helpers into canonical Rosetta IR forms.
    """
    PRINT_ALIASES = frozenset({
        "print", "println", "println!", "print!", "printf",
        "puts", "echo", "DISPLAY", "WriteLn", "writeln", "Put_Line"
    })
    MEMBER_PRINT_ALIASES = frozenset({
        ("console", "log"),
        ("console", "info"),
        ("fmt", "Println"),
        ("fmt", "Printf"),
        ("fmt", "Print"),
        ("out", "println"),
        ("out", "print"),
        ("debug", "print"),
        ("io", "put_string"),
    })

    def transform(self, node: RosettaNode) -> RosettaNode:
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        if isinstance(node, CallExpression):
            if isinstance(node.callee, Identifier) and node.callee.name in self.PRINT_ALIASES:
                node.callee = Identifier(name="print")
                return node

            if isinstance(node.callee, MemberAccess):
                obj = node.callee.object
                mem = node.callee.member
                obj_name = obj.name if isinstance(obj, Identifier) else (obj.member if isinstance(obj, MemberAccess) else "")
                if (obj_name, mem) in self.MEMBER_PRINT_ALIASES:
                    return CallExpression(callee=Identifier(name="print"), args=node.args)
                if mem in ("len", "size", "count", "length") and len(node.args) == 0:
                    return CallExpression(callee=Identifier(name="len"), args=[obj])
                if mem in ("push", "push_back") and len(node.args) == 1:
                    node.callee.member = "append"
                    return node

        return node


class MemorySafetyNormalizationPass(HermesPass):
    """
    Eliminates manual memory leaks, adapts C/C++ malloc/free to target memory models:
    - In garbage-collected targets (Python, JS, TS, Go, Java, Swift, Kotlin, etc.),
      frees are safely eliminated and mallocs become typed buffer allocations.
    - Dereference operators on reference-passing languages are converted to direct variable accesses.
    """
    GC_TARGETS = frozenset({
        "py", "python", "js", "javascript", "ts", "typescript",
        "go", "java", "kt", "kotlin", "swift", "rb", "ruby", "php"
    })

    def __init__(self, target_lang: str = "py"):
        self.target_lang = target_lang.lower().lstrip(".")

    def transform(self, node: RosettaNode) -> RosettaNode:
        # Transform children first
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        # Filter statement lists to eliminate free() in GC languages
        if self.target_lang in self.GC_TARGETS:
            if hasattr(node, "body") and isinstance(node.body, list):
                cleaned_body = []
                for stmt in node.body:
                    if isinstance(stmt, MemoryFree):
                        continue
                    if isinstance(stmt, CallExpression) and isinstance(stmt.callee, Identifier) and stmt.callee.name == "free":
                        continue
                    cleaned_body.append(stmt)
                node.body = cleaned_body

        # Handle MemoryAllocation
        if isinstance(node, MemoryAllocation):
            if self.target_lang in ("py", "python"):
                return BinaryExpression(left=Literal(value=[0]), operator="*", right=node.size)
            elif self.target_lang in ("js", "javascript", "ts", "typescript"):
                return CallExpression(
                    callee=MemberAccess(object=CallExpression(callee=Identifier(name="Array"), args=[node.size]), member="fill"),
                    args=[Literal(value=0)]
                )
            elif self.target_lang == "go":
                return CallExpression(callee=Identifier(name="make"), args=[Identifier(name="[]byte"), node.size])
            elif self.target_lang in ("rs", "rust"):
                return CallExpression(callee=Identifier(name="vec!"), args=[Literal(value=0), node.size])

        # Handle Dereference in GC languages (dereferencing a reference variable in Python/JS is direct access)
        if isinstance(node, Dereference) and self.target_lang in self.GC_TARGETS:
            return node.argument

        return node


class LibraryMappingPass(HermesPass):
    """
    Translates third-party and standard library ecosystem calls:
    - HTTP requests: fetch() <-> requests.get() <-> http.Get()
    - JSON serialization: JSON.stringify() <-> json.dumps() <-> json.Marshal()
    - Math functions: Math.sqrt() <-> math.sqrt() <-> math.Sqrt()
    - Timestamps: Date.now() <-> time.time() <-> time.Now()
    - String manipulation: toUpperCase() <-> upper() <-> strings.ToUpper()
    """
    MATH_FUNCS = frozenset({"sqrt", "floor", "ceil", "abs", "round", "pow", "sin", "cos", "tan", "log", "min", "max"})

    def __init__(self, target_lang: str = "py"):
        self.target_lang = target_lang.lower().lstrip(".")

    def transform(self, node: RosettaNode) -> RosettaNode:
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        if isinstance(node, CallExpression):
            # 1. HTTP calls: fetch(url) / axios.get(url) / requests.get(url) / http.Get(url)
            is_fetch = (isinstance(node.callee, Identifier) and node.callee.name == "fetch")
            is_requests_get = (isinstance(node.callee, MemberAccess) and 
                               isinstance(node.callee.object, Identifier) and 
                               node.callee.object.name in ("requests", "http", "axios") and 
                               node.callee.member.lower() in ("get", "getasync"))
            
            if is_fetch or is_requests_get:
                url_arg = node.args[0] if node.args else Literal(value="")
                if self.target_lang in ("py", "python"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="requests"), member="get"), args=[url_arg])
                elif self.target_lang in ("js", "javascript", "ts", "typescript"):
                    return CallExpression(callee=Identifier(name="fetch"), args=[url_arg])
                elif self.target_lang == "go":
                    return CallExpression(callee=MemberAccess(object=Identifier(name="http"), member="Get"), args=[url_arg])

            # 2. JSON Serialization
            is_json_dump = False
            dump_arg = None
            if isinstance(node.callee, MemberAccess):
                obj_name = node.callee.object.name if isinstance(node.callee.object, Identifier) else ""
                mem_name = node.callee.member
                if (obj_name == "JSON" and mem_name == "stringify") or (obj_name == "json" and mem_name in ("dumps", "Marshal")):
                    is_json_dump = True
                    dump_arg = node.args[0] if node.args else None

            if is_json_dump and dump_arg is not None:
                if self.target_lang in ("py", "python"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="json"), member="dumps"), args=[dump_arg])
                elif self.target_lang in ("js", "javascript", "ts", "typescript"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="JSON"), member="stringify"), args=[dump_arg])
                elif self.target_lang == "go":
                    return CallExpression(callee=MemberAccess(object=Identifier(name="json"), member="Marshal"), args=[dump_arg])

            is_json_load = False
            load_arg = None
            if isinstance(node.callee, MemberAccess):
                obj_name = node.callee.object.name if isinstance(node.callee.object, Identifier) else ""
                mem_name = node.callee.member
                if (obj_name == "JSON" and mem_name == "parse") or (obj_name == "json" and mem_name in ("loads", "Unmarshal")):
                    is_json_load = True
                    load_arg = node.args[0] if node.args else None

            if is_json_load and load_arg is not None:
                if self.target_lang in ("py", "python"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="json"), member="loads"), args=[load_arg])
                elif self.target_lang in ("js", "javascript", "ts", "typescript"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="JSON"), member="parse"), args=[load_arg])
                elif self.target_lang == "go":
                    return CallExpression(callee=MemberAccess(object=Identifier(name="json"), member="Unmarshal"), args=[load_arg])

            # 3. Math functions
            math_func = None
            math_args = node.args
            if isinstance(node.callee, MemberAccess):
                obj_name = node.callee.object.name if isinstance(node.callee.object, Identifier) else ""
                if obj_name in ("Math", "math") and node.callee.member.lower() in self.MATH_FUNCS:
                    math_func = node.callee.member.lower()
            elif isinstance(node.callee, Identifier) and node.callee.name.lower() in self.MATH_FUNCS:
                math_func = node.callee.name.lower()

            if math_func:
                if self.target_lang in ("py", "python"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="math"), member=math_func), args=math_args)
                elif self.target_lang in ("js", "javascript", "ts", "typescript", "java"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="Math"), member=math_func), args=math_args)
                elif self.target_lang == "go":
                    return CallExpression(callee=MemberAccess(object=Identifier(name="math"), member=math_func.capitalize()), args=math_args)
                elif self.target_lang in ("c", "cpp"):
                    return CallExpression(callee=Identifier(name=math_func), args=math_args)

            # 4. Timestamps
            is_timestamp = False
            if isinstance(node.callee, MemberAccess):
                obj_name = node.callee.object.name if isinstance(node.callee.object, Identifier) else ""
                if (obj_name == "Date" and node.callee.member == "now") or (obj_name == "time" and node.callee.member in ("time", "Now")):
                    is_timestamp = True
            elif isinstance(node.callee, Identifier) and node.callee.name in ("time", "now"):
                is_timestamp = True

            if is_timestamp:
                if self.target_lang in ("py", "python"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="time"), member="time"), args=[])
                elif self.target_lang in ("js", "javascript", "ts", "typescript"):
                    return CallExpression(callee=MemberAccess(object=Identifier(name="Date"), member="now"), args=[])
                elif self.target_lang == "go":
                    return CallExpression(callee=MemberAccess(object=Identifier(name="time"), member="Now"), args=[])

            # 5. String case
            if isinstance(node.callee, MemberAccess):
                mem = node.callee.member
                str_obj = node.callee.object
                if mem in ("toUpperCase", "upper") and len(node.args) == 0:
                    if self.target_lang in ("py", "python"):
                        return CallExpression(callee=MemberAccess(object=str_obj, member="upper"), args=[])
                    elif self.target_lang in ("js", "javascript", "ts", "typescript"):
                        return CallExpression(callee=MemberAccess(object=str_obj, member="toUpperCase"), args=[])
                    elif self.target_lang == "go":
                        return CallExpression(callee=MemberAccess(object=Identifier(name="strings"), member="ToUpper"), args=[str_obj])

                if mem in ("toLowerCase", "lower") and len(node.args) == 0:
                    if self.target_lang in ("py", "python"):
                        return CallExpression(callee=MemberAccess(object=str_obj, member="lower"), args=[])
                    elif self.target_lang in ("js", "javascript", "ts", "typescript"):
                        return CallExpression(callee=MemberAccess(object=str_obj, member="toLowerCase"), args=[])
                    elif self.target_lang == "go":
                        return CallExpression(callee=MemberAccess(object=Identifier(name="strings"), member="ToLower"), args=[str_obj])

        return node


class ParadigmNormalizationPass(HermesPass):
    """
    Normalizes declarative and stack paradigms into idiomatic imperative forms:
    - Forth words & stack operations are adapted with automatic stack initialization.
    - Prolog clauses/rules are mapped to relational query structures.
    """
    def __init__(self, target_lang: str = "py"):
        self.target_lang = target_lang.lower().lstrip(".")

    def transform(self, node: RosettaNode) -> RosettaNode:
        for attr in vars(node):
            val = getattr(node, attr)
            if isinstance(val, RosettaNode):
                setattr(node, attr, self.transform(val))
            elif isinstance(val, list):
                setattr(node, attr, [self.transform(item) if isinstance(item, RosettaNode) else item for item in val])

        return node
