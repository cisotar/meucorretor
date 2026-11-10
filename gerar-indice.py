#!/usr/bin/env python3
"""Gera index.json de correcoes/, agentes/ e propostas/ (GitHub Pages não lista diretórios).
Rode após adicionar correções, agentes ou propostas. Subpastas (ex.: agentes/bak) são ignoradas."""
import json, pathlib
raiz = pathlib.Path(__file__).parent
for pasta, padroes in (("correcoes", ["*.md"]), ("agentes", ["*.md"]), ("propostas", ["*.pdf", "*.jpg", "*.jpeg", "*.png"])):
    d = raiz / pasta
    nomes = sorted({p.name for pat in padroes for p in d.glob(pat) if p.is_file()})
    (d / "index.json").write_text(json.dumps(nomes, ensure_ascii=False, indent=1), encoding="utf-8")
    print(pasta, len(nomes), "arquivos indexados")
