<div align="center">
  <img src="rosetta-web/public/logo.svg" alt="Rosetta" width="240" />
  <h3>Universal 32 &times; 32 Multi-Paradigm Source-to-Source Transpiler</h3>
</div>

Rosetta is an industrial-strength, multi-paradigm source-to-source transpiler capable of bidirectional translation across **32 programming languages** spanning classical imperative, object-oriented, functional, concurrent, logic, stack-based, and modern emerging systems languages.

```
       ┌────────────────┐
       │ BABEL Frontend │   (32 Source Parsers)
       └───────┬────────┘
               │  [Rosetta IR AST]
               ▼
       ┌────────────────┐
       │ HERMES Passes  │   (Type Inference, Idiom & Stdlib Normalization)
       └───────┬────────┘
               │  [Canonical & Optimized IR]
               ▼
       ┌────────────────┐
       │ CIPHER Backend │   (32 Target Code Emitters)
       └────────────────┘
```

---

## 🚀 Key Features

- **Full $32 \times 32$ Bidirectional Symmetrical Matrix**: Any of the 32 languages can be used as both an input source and an output target.
- **Canonical Rosetta IR**: Unified, language-agnostic intermediate representation handling OOP, functional patterns, logic programming, stack operations, contracts, and memory models.
- **HERMES Optimization Passes**:
  - `StdlibNormalizationPass`: Maps cross-language I/O, string, and collection intrinsics (`console.log`, `fmt.Println`, `System.out.println`, `std::cout`, `println!`, `puts`, `echo`, `.len()`, `.size()`) to canonical IR.
  - `LibraryMappingPass`: Translates ecosystem APIs (`fetch` $\leftrightarrow$ `requests.get` $\leftrightarrow$ `http.Get`, `JSON.stringify` $\leftrightarrow$ `json.dumps` $\leftrightarrow$ `json.Marshal`, `Math.*` $\leftrightarrow$ `math.*`, `Date.now` $\leftrightarrow$ `time.time`).
  - `MemorySafetyNormalizationPass`: Adapts C/C++ pointers, `malloc`, and `free` to target memory models (typed buffers in Python/JS/Go/Rust and automatic GC cleanup).
  - `TypeInferencePass`: Infers static types for dynamically typed constructs.
  - `IdiomNormalizationPass`: Converts list comprehensions into map/filter chains and handles static method/decorator metadata.
  - `LegacyIndexingPass`: Normalizes 1-based indexing (Fortran, PL/I, etc.) to 0-based.
  - `RedundantDeclarationPass`: Cleans up redundant parameter re-declarations.
- **Next.js Web Studio & Workbench**: Interactive UI with real-time heuristics-based auto-detection, interactive quick-apply badge, AST tree inspector, and Hermes optimizer pass controls.
- **MCP Server Ready**: Built-in Model Context Protocol server exposing `transpile`, `inspect_ir`, and `get_supported_languages`.

---

## 📊 Supported 32-Language Matrix

| Phase | Paradigm | Languages |
|---|---|---|
| **Phase 1: Foundation & Modern** | Multi-paradigm, OOP, Systems | Python (`.py`), JavaScript (`.js`), TypeScript (`.ts`), Java (`.java`), C++ (`.cpp`), C (`.c`), Rust (`.rs`), Go (`.go`), Swift (`.swift`), Kotlin (`.kt`), Ruby (`.rb`), PHP (`.php`) |
| **Phase 2: Enterprise Business** | Legacy Records & Business | COBOL (`.cbl`, `.cob`) |
| **Phase 3: Classic & Foundational** | Numeric, Symbolic, Logic, OOP | Fortran (`.f90`), BASIC (`.bas`), Pascal (`.pas`), Ada (`.adb`), LISP (`.lisp`), Algol (`.alg`), Smalltalk (`.st`), Prolog (`.pl`) |
| **Phase 4: Declarative & Modular** | Concatenative, Functional, Contracts | SNOBOL4 (`.sno`), PL/I (`.pli`), Modula-2 (`.mod`), RPG (`.rpg`), Eiffel (`.e`), Forth (`.fs`), Standard ML (`.ml`) |
| **Phase 5: Emerging & Future** | Blockchain, AI, Systems Evolutions | Solidity (`.sol`), Mojo (`.mojo`, `.🔥`), Zig (`.zig`), Carbon (`.carbon`) |

---

## ⚡ Quickstart

### 1. One-Click Launch (Windows)
Double-click `start_rosetta.bat` or run:
```cmd
start_rosetta.bat
```
This boots both the **Rosetta FastAPI Engine** on port `8008` and the **Web Studio** on port `3000`.

### 2. CLI Usage
Transpile any file directly using the CLI:
```bash
# Python to Rust
python -m rosetta.cli.main input.py --to rs

# COBOL to Solidity
python -m rosetta.cli.main payroll.cbl --to solidity

# JavaScript to C++
python -m rosetta.cli.main app.js --to cpp --show-ir
```

### 3. Docker Deployment
```bash
docker-compose up --build
```
- API Engine: `http://localhost:8008`
- Web Studio: `http://localhost:3000`

---

## 🧪 Verification & Test Suite

Run the full $32 \times 32$ cross-language matrix test runner:
```bash
python cross_matrix_runner.py
```
**Current Status**: 269 / 269 test cases passing with **100.0%** success rate.

---

## 🛠️ Architecture

```
rosetta/
├── babel/            # Phase 1: Language-specific frontends & AST parsers
│   ├── base/         # Abstract frontend and universal structural parser
│   ├── cobol/        # COBOL column-aware parser
│   ├── python/       # Python AST & ANTLR parser
│   └── ...           # (All 32 language frontends)
├── hermes/           # Phase 2: Intermediate Representation & Transform Pipeline
│   ├── pipeline.py   # Multi-pass execution harness
│   └── passes/       # Semantic lowering, stdlib normalization, type inference
├── cipher/           # Phase 3: Language-specific target code generators
│   └── ...           # (All 32 language emitters)
├── cli/              # Unified CLI, resolver registry, and MCP server
│   ├── resolver.py   # Centralised frontend & backend registry
│   ├── mcp_server.py # FastMCP server
│   └── main.py       # Command-line entrypoint
└── rosetta-web/      # Next.js 16 Web Studio & FastAPI bridge
```

---

## 📜 License
MIT License.
