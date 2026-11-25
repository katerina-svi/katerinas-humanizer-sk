# AGENTS.md

Pokyny pre AI agentov (Claude Code, Codex a pod.), ktorí pracujú v tomto repozitári.

## Čo tento repozitár je

Prenosný agent skill. Runtime artefakt je `SKILL.md`: YAML frontmatter (metadáta a povolené nástroje), za ktorým nasleduje redakčný prompt. K nemu patrí slovník kalkov a bohemizmov v Markdowne a jeden voliteľný skript v Pythone bez závislostí. Žiadny build.

## Kľúčové súbory

- `SKILL.md`: samotný skill; keď sa iné súbory s ním rozchádzajú, platí jeho znenie. 45 číslovaných vzorcov s príkladmi pred/po, prísne pravidlá (časť ⛔), pravidlá pýtania sa (časť ❓) a postup kontroly kalkov (časť E).
- `references/kalky.md`: slovník kalkov z angličtiny (časti 1 – 8) a bohemizmov (časť 9) k časti E a vzorcu č. 17. Posledný stĺpec tabuľky (Hľadať) je regulárny výraz pre skript; zvislá čiara vnútri výrazu sa píše ako `\|`.
- `scripts/najdi_kalky.py`: podľa slovníka vypíše miesta podozrivé z kalkov a bohemizmov. Len kandidátov na posúdenie, nič neopravuje, návratový kód je vždy 0.
- `README.md`: pre ľudí. Inštalácia, použitie, prehľad vzorcov, história verzií.
- `CHANGELOG.md`: podrobný zoznam zmien po verziách.
- `.claude-plugin/`: voliteľné manifesty pre Claude Code plugin a marketplace z jedného repozitára.

## Pravidlá údržby

- `SKILL.md`, `README.md` a `CHANGELOG.md` musia zostať zosynchronizované: pri zmene vzorcov aktualizuj prehľad v README, históriu verzií aj CHANGELOG.
- Verzia sa udržiava v `.claude-plugin/plugin.json`, v README a v CHANGELOG. Frontmatter `SKILL.md` pole `version` zámerne NEMÁ a obsahuje len `name`, `description`, `license` a `allowed-tools`. Pole `description` drž do 1 024 znakov, inak ho validátor skillov v Claude odmietne.
- Telo `SKILL.md` drž do 500 riadkov. Dlhé zoznamy patria do `references/`.
- ⛔ PRÍSNE PRAVIDLÁ a časť ❓ o pýtaní sa sú jadrom tohto skillu. Nijaká úprava ich nesmie oslabiť ani obísť.
- Pravopis a slovná zásoba sa riadia kodifikačnými príručkami JÚĽŠ SAV, typografia normou STN 01 6910. Pri úpravách zachovaj obrátenú logiku voči anglickému originálu (úvodzovky „ “, limit pomlčiek, zákaz Title Case).
- Príklady „Po“ musia samy spĺňať pravidlá skillu (žiadne em dashe, anglické úvodzovky, lepidlové pomlčky, kalky ani bohemizmy). Po zmene príkladov spusti na nich skript.
- Slovník sa rozširuje pridaním riadka do príslušnej časti `references/kalky.md`. Bohemizmy patria do časti 9 (skript ich podľa názvu časti označí ako bohemizmus). Po zmene spusti skript na krátkom testovacom texte, aby bolo isté, že sa vzor dá preložiť (neplatný vzor skript ohlási na stderr a preskočí).
- Položky v slovníku sú kandidáti, nie zákazy. K slovám s legitímnym významom (výstup projektu, vstup do budovy, doporučený list) patrí poznámka do stĺpca Po slovensky skôr.
- Nové pravidlo o slovenčine pridávaj len s oporou v kodifikačnej príručke alebo v odpovedi Jazykovej poradne JÚĽŠ. Čo nie je overené, označ v CHANGELOG alebo v issue ako „na overenie“.
- Slovenská a česká verzia (katerina-svi/katerinas-humanizer-cz) sa udržiavajú spoločne: zmena spoločného vzorca patrí do oboch. Čísla vzorcov sa líšia (slovenská verzia má navyše bohemizmy a vykanie), časť E je v CZ č. 34 – 43, v SK č. 36 – 45.
- Pri vydaní verzie prilož k GitHub release `humanizer-sk.zip`, ktorý sa dá nahrať do Claude: priečinok `humanizer-sk/` so súbormi SKILL.md, references/, scripts/ a LICENSE, bez skrytých súborov a bez `__pycache__`.
