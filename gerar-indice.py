#!/usr/bin/env python3
"""Gera index.json de correcoes/, agentes/ e propostas/ (GitHub Pages não lista diretórios).
Rode após adicionar correções, agentes ou propostas. Subpastas (ex.: agentes/bak) são ignoradas."""
import json, pathlib
raiz = pathlib.Path(__file__).parent
for pasta, padroes in (("correcoes", ["*.md"]), ("agentes", ["*.md"]), ("propostas", ["*.pdf", "*.jpg", "*.jpeg", "*.png"])):
    d = raiz / pasta
    nomes = sorted({p.name for pat in padroes for p in d.glob(pat) if p.is_file()})
    novo = json.dumps(nomes, ensure_ascii=False, indent=1)
    arq = d / "index.json"
    # Só grava se mudou (evita recarregar o Live Server à toa)
    if not arq.exists() or arq.read_text(encoding="utf-8") != novo:
        arq.write_text(novo, encoding="utf-8")
    print(pasta, len(nomes), "arquivos indexados")
