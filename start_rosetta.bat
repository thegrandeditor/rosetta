@echo off
echo Starting ROSETTA 32x32 Universal Transpiler Engine + Web Studio...
start "Rosetta FastAPI Engine (Port 8008)" cmd /k "cd /d %~dp0rosetta-web && %~dp0.venv\Scripts\python.exe -m uvicorn backend.main:app --host 127.0.0.1 --port 8008"
start "Rosetta Web Studio (Port 3000)" cmd /k "cd /d %~dp0rosetta-web && npm run dev"
echo Both services launched! Open http://localhost:3000 in your browser.
