#!/usr/bin/env python3
"""Hook PostToolUse: depois de criar/editar/apagar arquivos em correcoes/, agentes/ ou propostas/,
roda gerar-indice.py para o site (index.json) listar a novidade."""
import json, re, subprocess, sys, pathlib
raiz = pathlib.Path(__file__).resolve().parents[2]
try:
    d = json.load(sys.stdin)
except Exception:
    sys.exit(0)
ti = d.get("tool_input") or {}
alvo = ti.get("file_path") or ti.get("command") or ""
if re.search(r"(correcoes|agentes|propostas)/", alvo):
    subprocess.run([sys.executable, str(raiz / "gerar-indice.py")], stdout=subprocess.DEVNULL, check=False)
