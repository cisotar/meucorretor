#!/usr/bin/env python3
"""Gera correcoes/index.json (GitHub Pages não lista diretórios). Rode após adicionar correções."""
import json, pathlib
d = pathlib.Path(__file__).parent / "correcoes"
nomes = sorted(p.name for p in d.glob("*.md"))
(d / "index.json").write_text(json.dumps(nomes, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(nomes), "correções indexadas")
