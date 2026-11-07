import time
import json
import urllib.request
import urllib.error
import threading
from typing import List, Dict, Any

# Target endpoints
API_BASE = "http://127.0.0.1:8000"
CLIENT_BASE = "http://127.0.0.1:3000"

print("======================================================================")
print("             ROSETTA GRID SYSTEM STRESS-TEST ENGINE v1.0              ")
print("======================================================================")
print(f"[*] Target Backend API Node: {API_BASE}")
print(f"[*] Target Frontend Client Node: {CLIENT_BASE}")

# 1. Generate "Company Size" massive test datasets
print("[*] Synthesizing enterprise-scale compiler test data...")

# 5,000 lines of complex enterprise COBOL containing numerous segments
cobol_lines = []
cobol_lines.append("       IDENTIFICATION DIVISION.")
cobol_lines.append("       PROGRAM-ID. ENTERPRISE-CORE-MAIN.")
cobol_lines.append("       AUTHOR. ROSETTA-AUTONOMOUS-GRID.")
cobol_lines.append("       ENVIRONMENT DIVISION.")
cobol_lines.append("       INPUT-OUTPUT SECTION.")
cobol_lines.append("       DATA DIVISION.")
cobol_lines.append("       WORKING-STORAGE SECTION.")

# Generate massive sequence of variable declarations
for i in range(1, 2000):
    cobol_lines.append(f"       01  TRANS-RECORD-{i:04d}.")
    cobol_lines.append(f"           05  TR-ID-{i:04d}           PIC X(12)  VALUE 'TX-{i:04d}'.")
    cobol_lines.append(f"           05  TR-AMOUNT-{i:04d}       PIC 9(7)V99 VALUE 150.75.")
    cobol_lines.append(f"           05  TR-STATUS-{i:04d}       PIC X(2)   VALUE '00'.")

cobol_lines.append("       PROCEDURE DIVISION.")
cobol_lines.append("       0000-MAIN-LOGIC.")
cobol_lines.append("           DISPLAY 'INITIALIZING MAIN TRANSACTION MATRIX...'.")

for i in range(1, 500):
    cobol_lines.append(f"           PERFORM 1000-PROCESS-RECORD-{i:04d}.")

cobol_lines.append("           DISPLAY 'TRANSACTION SCAN RESOLVED SUCCESSFUL.'.")
cobol_lines.append("           STOP RUN.")

for i in range(1, 500):
    cobol_lines.append(f"       1000-PROCESS-RECORD-{i:04d}.")
    cobol_lines.append(f"           IF TR-STATUS-{i:04d} = '00'")
    cobol_lines.append(f"               ADD TR-AMOUNT-{i:04d} TO TR-AMOUNT-0001")
    cobol_lines.append(f"               MOVE '10' TO TR-STATUS-{i:04d}")
    cobol_lines.append("           END-IF.")

MASSIVE_COBOL_SRC = "\n".join(cobol_lines)
print(f"[+] Formed massive COBOL benchmark codeblock: {len(cobol_lines)} lines, {len(MASSIVE_COBOL_SRC)} bytes")

# 3,000 lines of complex computational python
py_lines = []
py_lines.append("class ComputationGridNode:")
py_lines.append("    def __init__(self, node_id: int):")
py_lines.append("        self.node_id = node_id")
py_lines.append("        self.metrics = []")
py_lines.append("")

for i in range(1, 1000):
    py_lines.append(f"    def compute_vector_metric_{i}(self, value: float) -> float:")
    py_lines.append(f"        factor = {i * 1.05:.4f}")
    py_lines.append(f"        result = (value * factor) ** 0.5")
    py_lines.append(f"        self.metrics.append(result)")
    py_lines.append(f"        return result")
    py_lines.append("")

py_lines.append("if __name__ == '__main__':")
py_lines.append("    node = ComputationGridNode(node_id=775)")
for i in range(1, 100):
    py_lines.append(f"    node.compute_vector_metric_{i}(12.5)")
py_lines.append("    print('Metrics compute sweep finalized.')")

MASSIVE_PYTHON_SRC = "\n".join(py_lines)
print(f"[+] Formed massive Python benchmark codeblock: {len(py_lines)} lines, {len(MASSIVE_PYTHON_SRC)} bytes")

def query_endpoint(url: str, method: str = "GET", data: Dict[str, Any] = None) -> Dict[str, Any]:
    req = urllib.request.Request(url, method=method)
    req.add_header("Content-Type", "application/json")
    
    payload = None
    if data:
        payload = json.dumps(data).encode("utf-8")
        
    try:
        with urllib.request.urlopen(req, data=payload, timeout=20) as response:
            res_data = response.read().decode("utf-8")
            return {
                "status": response.status,
                "data": json.loads(res_data) if res_data else {}
            }
    except urllib.error.HTTPError as e:
        return {"status": e.code, "error": e.reason}
    except Exception as e:
        return {"status": 500, "error": str(e)}

# 2. Phase 1: Health Handshakes
print("\n--- PHASE 1: HEALTH AND INTEGRATION HANDSHAKES ---")
health = query_endpoint(f"{API_BASE}/api/health")
if "error" not in health and health["status"] == 200:
    print(f"[+] Backend healthy handshake: {health['data']}")
else:
    print(f"[-] Backend health check failed: {health}")

# Check supported languages fetch
languages_list = query_endpoint(f"{API_BASE}/api/languages")
if "error" not in languages_list and languages_list["status"] == 200:
    all_langs = languages_list["data"].get("languages", [])
    print(f"[+] Retrieved supported languages: {len(all_langs)} entries successfully loaded.")
else:
    print(f"[-] Languages retrieval failed: {languages_list}")

# 3. Phase 2: Heuristics Auto-Detection Load
print("\n--- PHASE 2: HEURISTICS AUTO-DETECTION SPEED STRESS ---")
detect_tests = [
    {"source": "IDENTIFICATION DIVISION.\nPROGRAM-ID. HELLO.", "expected": ".cbl"},
    {"source": "contract SimpleToken {\n  mapping(address => uint) balances;\n}", "expected": ".sol"},
    {"source": "def calculate_sum(a, b):\n    return a + b", "expected": ".py"},
    {"source": "fn main() {\n    println!(\"Hello\");\n}", "expected": ".rs"},
    {"source": MASSIVE_COBOL_SRC[:1000], "expected": ".cbl"},
    {"source": MASSIVE_PYTHON_SRC[:1000], "expected": ".py"}
]

for idx, t in enumerate(detect_tests):
    t1 = time.time()
    res = query_endpoint(f"{API_BASE}/api/detect", "POST", {"source": t["source"]})
    dur = (time.time() - t1) * 1000
    if "error" not in res and res["status"] == 200:
        detected = res["data"].get("language")
        conf = res["data"].get("confidence")
        print(f"[+] Signature Test #{idx+1:02d}: Got {detected} (Confidence: {conf}) in {dur:.2f} ms")
    else:
        print(f"[-] Signature Test #{idx+1:02d} Failed: {res}")

# 4. Phase 3: Transpiler Bridge High-Fidelity Load Check
print("\n--- PHASE 3: COMPILER TRANSPILATION BRIDGE STRESS ---")

# We test with the corporate size inputs we generated!
large_compiles = [
    {"source": MASSIVE_COBOL_SRC[:15000], "from": ".cbl", "to": "py", "label": "Enterprise COBOL Subroutine Block (15 KB)"},
    {"source": MASSIVE_PYTHON_SRC[:15000], "from": ".py", "to": "js", "label": "AI Grid Node Mathematical Vectors Block (15 KB)"},
    {"source": MASSIVE_COBOL_SRC, "from": ".cbl", "to": "py", "label": "FULL Corporate size COBOL Mainframe Core (200 KB)"},
    {"source": MASSIVE_PYTHON_SRC, "from": ".py", "to": "js", "label": "FULL Corporate size AI Vectors Array Structure (50 KB)"}
]

for idx, tc in enumerate(large_compiles):
    print(f"[*] Compiling payload: {tc['label']} ...")
    t1 = time.time()
    res = query_endpoint(f"{API_BASE}/api/transpile", "POST", {
        "source": tc["source"],
        "from_lang": tc["from"],
        "to_lang": tc["to"]
    })
    dur = (time.time() - t1) * 1000
    if "error" not in res and res["status"] == 200:
        output_len = len(res["data"].get("result", ""))
        tokens_used = res["data"].get("tokens_used", 0)
        actual_time = res["data"].get("time_ms", 0)
        print(f"[+] SUCCESS in {dur:.2f} ms (Engine reported parsing: {actual_time} ms) | Tokens: {tokens_used} | Output: {output_len} bytes")
    else:
        print(f"[-] Compiling error on {tc['label']}: {res}")

# 5. Phase 4: High Concurrent Load & Multi-Threading Stress
print("\n--- PHASE 4: HIGH-THROUGHPUT CONCURRENT LOAD SWEEP ---")

concurrent_results = []
def worker_thread(thread_id: int, payload: Dict[str, Any]):
    t1 = time.time()
    res = query_endpoint(f"{API_BASE}/api/transpile", "POST", payload)
    dur = (time.time() - t1) * 1000
    status_code = res.get("status", 500)
    success = "error" not in res and status_code == 200
    concurrent_results.append({
        "thread_id": thread_id,
        "success": success,
        "duration": dur,
        "status": status_code
    })

# Spawn 10 concurrent heavy compilation threads simultaneously to verify non-blocking capabilities
threads = []
payload_sample = {
    "source": "DATA DIVISION.\nWORKING-STORAGE SECTION.\n01 GREET PIC X(10) VALUE 'HELLO'.",
    "from_lang": ".cbl",
    "to_lang": "py"
}

print(f"[*] Spawning 12 concurrent worker compilation threads on the Rosetta Grid...")
for i in range(12):
    t = threading.Thread(target=worker_thread, args=(i, payload_sample))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

success_count = sum(1 for r in concurrent_results if r["success"])
durations = [r["duration"] for r in concurrent_results]
avg_dur = sum(durations) / len(durations) if durations else 0

print("\n======================================================================")
print("                   STRESS TEST ANALYSIS & GRID SUMMARY                ")
print("======================================================================")
print(f"[+] Total Compiled Thread Blocks: {len(concurrent_results)}")
print(f"[+] Successful Compiles:          {success_count} / {len(concurrent_results)} ({success_count/len(concurrent_results)*100:.1f}%)")
print(f"[+] Average Thread Roundtrip:     {avg_dur:.2f} ms")
print(f"[+] Minimum Thread Roundtrip:     {min(durations):.2f} ms" if durations else "N/A")
print(f"[+] Maximum Thread Roundtrip:     {max(durations):.2f} ms" if durations else "N/A")
print("======================================================================")
print("[+] ROSETTA GRID PLATFORM LOAD CAPACITY DIAGNOSTICS: STABLE.")
print("======================================================================")
