#!/usr/bin/env python3
"""Repo kontrolleri (yerelde ve CI'da): python3 scripts/kontrol.py

- Her bölüm klasöründe README.md, tek PDF ve onizleme.png var.
- PDF'ler 50 MB'ı geçmiyor ve içlerinde yerel dosya yolu (/Users/, C:\\Users\\, /home/) gömülü değil.
- Markdown dosyalarındaki göreli linkler var olan dosyalara gidiyor; Markdown dosyaları 500 satırın altında.
"""
import re
import sys
from pathlib import Path

KOK = Path(__file__).resolve().parents[1]
SINIR = 50 * 1024 * 1024
YEREL_YOL = re.compile(rb"(/Users/|/home/|[A-Za-z]:\\\\Users\\\\)")
LINK = re.compile(r"\]\(([^)\s]+)\)")


def main():
    sorun = []
    bolumler = sorted(p for p in (KOK / "bolumler").iterdir() if p.is_dir())
    if not bolumler:
        sorun.append("bolumler/ altında bölüm yok")
    for b in bolumler:
        if not re.fullmatch(r"\d{2}-[a-z0-9-]+", b.name):
            sorun.append(f"{b.name}: klasör adı <iki haneli no>-<dönem> biçiminde değil")
        pdfler = list(b.glob("*.pdf"))
        for gerekli in ("README.md", "onizleme.png"):
            if not (b / gerekli).exists():
                sorun.append(f"{b.name}: {gerekli} yok")
        if len(pdfler) != 1:
            sorun.append(f"{b.name}: tek PDF olmalı, {len(pdfler)} var")
        for p in pdfler:
            veri = p.read_bytes()
            if len(veri) > SINIR:
                sorun.append(f"{p.relative_to(KOK)}: {len(veri) / 1048576:.1f} MB, sınır 50 MB")
            if YEREL_YOL.search(veri):
                sorun.append(f"{p.relative_to(KOK)}: içinde yerel dosya yolu var")
    for md in KOK.rglob("*.md"):
        if ".git" in md.parts:
            continue
        metin = md.read_text(encoding="utf-8")
        if metin.count("\n") >= 500:
            sorun.append(f"{md.relative_to(KOK)}: 500 satırı geçiyor")
        for hedef in LINK.findall(metin):
            if re.match(r"[a-z]+:", hedef) or hedef.startswith("#"):
                continue
            yol = (md.parent / hedef.split("#")[0]).resolve()
            if not yol.exists():
                sorun.append(f"{md.relative_to(KOK)}: kırık link {hedef}")
    for s in sorun:
        print(f"HATA: {s}")
    print(f"{len(bolumler)} bölüm, {len(sorun)} sorun")
    return 1 if sorun else 0


if __name__ == "__main__":
    sys.exit(main())
