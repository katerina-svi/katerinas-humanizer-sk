#!/usr/bin/env python3
"""Nájde v slovenskom texte miesta podozrivé z kalkov z angličtiny a bohemizmov.

Pomocník k časti E a vzorcu č. 17 skillu humanizer-sk. Prejde text podľa
slovníka references/kalky.md a pri každom náleze vypíše predlohu (anglickú
alebo českú) a návrh náhrady. Nič neopravuje. Každý nález je kandidát na
posúdenie, pretože rovnaké slovo môže byť v inom spojení v poriadku.

Skript pozná len kalky a bohemizmy zo slovníka. Výsledok „0 nálezov“ preto
neznamená, že text kalky nemá, a čítanie vetu po vete (časť E) nenahrádza.

Použitie:
    python3 najdi_kalky.py text.md
    cat text.txt | python3 najdi_kalky.py -
    python3 najdi_kalky.py text.md --slovnik moj-slovnik.md

Preskakuje sa YAML frontmatter, bloky kódu, kód v riadku a URL.
Návratový kód je vždy 0: nálezy sú na posúdenie, nie chyby.
"""
import argparse
import re
import sys
from pathlib import Path

VYCHODZI_SLOVNIK = Path(__file__).resolve().parent.parent / "references" / "kalky.md"
ODDELOVAC = re.compile(r"(?<!\\)\|")


def nacitaj_slovnik(cesta):
    """Vráti položky slovníka, ktoré majú v poslednom stĺpci vzor v `…`."""
    polozky = []
    sekcia = ""
    for cislo, riadok in enumerate(Path(cesta).read_text(encoding="utf-8").splitlines(), 1):
        if riadok.startswith("## "):
            sekcia = riadok[3:].strip()
            continue
        riadok = riadok.strip()
        if not (riadok.startswith("|") and riadok.endswith("|")):
            continue
        bunky = [b.strip() for b in ODDELOVAC.split(riadok[1:-1])]
        if len(bunky) < 4:
            continue
        vyraz, predloha, nahrada, hladat = bunky[:4]
        m = re.fullmatch(r"`(.+)`", hladat)
        if not m:
            continue  # záhlavie, oddeľovač alebo položka len na čítanie
        vzor = m.group(1).replace(r"\|", "|")
        try:
            rx = re.compile(vzor, re.IGNORECASE)
        except re.error as chyba:
            print(f"Slovník, r. {cislo}: neplatný vzor {vzor!r} ({chyba})", file=sys.stderr)
            continue
        polozky.append({
            "vyraz": vyraz,
            "predloha": predloha.replace("*", ""),
            "nahrada": nahrada.replace(r"\|", "|"),
            "typ": "bohemizmus" if "bohemizm" in sekcia.lower() else "kalk",
            "rx": rx,
        })
    return polozky


def priprav_text(surovy):
    """Nahradí časti, ktoré sa nekontrolujú, medzerami. Čísla riadkov zostanú."""
    def vymaz(m):
        return re.sub(r"[^\n]", " ", m.group(0))

    t = re.sub(r"\A---\n.*?\n---\n", vymaz, surovy, flags=re.S)
    t = re.sub(r"```.*?```", vymaz, t, flags=re.S)
    t = re.sub(r"`[^`\n]*`", vymaz, t)
    t = re.sub(r"https?://\S+", vymaz, t)
    return t


def najdi(text, polozky):
    nalezy = []
    for p in polozky:
        for m in p["rx"].finditer(text):
            riadok = text.count("\n", 0, m.start()) + 1
            zac = text.rfind("\n", 0, m.start()) + 1
            kon = text.find("\n", m.end())
            ukazka = " ".join(text[zac: kon if kon != -1 else len(text)].split())
            if len(ukazka) > 100:
                stred = m.start() - zac
                ukazka = "…" + ukazka[max(0, stred - 45): stred + 55] + "…"
            nalezy.append((riadok, m.group(0), p, ukazka))
    nalezy.sort(key=lambda n: (n[0], n[1]))
    return nalezy


def main():
    parser = argparse.ArgumentParser(description="Nájde miesta podozrivé z kalkov z angličtiny a bohemizmov.")
    parser.add_argument("subor", help="cesta k textu, alebo - pre štandardný vstup")
    parser.add_argument("--slovnik", default=str(VYCHODZI_SLOVNIK), help="cesta k slovníku kalkov (.md)")
    args = parser.parse_args()

    surovy = sys.stdin.read() if args.subor == "-" else Path(args.subor).read_text(encoding="utf-8")
    polozky = nacitaj_slovnik(args.slovnik)
    nalezy = najdi(priprav_text(surovy), polozky)

    kalky = sum(1 for n in nalezy if n[2]["typ"] == "kalk")
    print(f"Slovník: {len(polozky)} hľadaných výrazov. Nálezov na posúdenie: {len(nalezy)} "
          f"(kalky {kalky}, bohemizmy {len(nalezy) - kalky}).")
    for riadok, nalez, p, ukazka in nalezy:
        print(f"r. {riadok} | {p['typ']} | „{nalez}“ | {p['predloha']} → {p['nahrada']} | {ukazka}")
    print("Skript pozná len výrazy zo slovníka. 0 nálezov neznamená text bez kalkov: "
          "pokračuj čítaním vetu po vete (humanizer-sk, časť E a vzorec č. 17).")


if __name__ == "__main__":
    main()
