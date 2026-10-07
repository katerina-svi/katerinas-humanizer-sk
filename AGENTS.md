# AGENTS.md

Pokyny pre AI agentov (Claude Code, Codex a pod.), ktorí pracujú v tomto repozitári.

## Čo tento repozitár je

Prenosný agent skill implementovaný čisto v Markdowne. Runtime artefakt je `SKILL.md`: YAML frontmatter (metadáta a povolené nástroje), za ktorým nasleduje redakčný prompt. Žiadny build, žiadny kód.

## Kľúčové súbory

- `SKILL.md`: samotný skill, zdroj pravdy. 35 číslovaných vzorcov s príkladmi pred/po, prísne pravidlá (časť ⛔) a pravidlá pýtania sa (časť ❓).
- `README.md`: pre ľudí. Inštalácia, použitie, prehľad vzorcov, história verzií.
- `.claude-plugin/`: voliteľné manifesty pre Claude Code plugin a marketplace z jedného repozitára.

## Kontrakt údržby

- `SKILL.md` a `README.md` musia zostať zosynchronizované: pri zmene vzorcov aktualizuj prehľad v README aj históriu verzií.
- Verzia sa udržiava v `.claude-plugin/plugin.json` a v README. Frontmatter `SKILL.md` pole `version` zámerne NEMÁ a smie obsahovať len `name`, `description`, `license` a `allowed-tools` (iné polia validátory skillov odmietajú).
- ⛔ PRÍSNE PRAVIDLÁ a časť ❓ o pýtaní sa sú jadrom tohto skillu. Nijaká úprava ich nesmie oslabiť ani obísť.
- Pravopis a slovná zásoba sa riadia kodifikačnými príručkami JÚĽŠ SAV, typografia normou STN 01 6910. Pri úpravách zachovaj obrátenú logiku voči anglickému originálu (úvodzovky „ ", limit pomlčiek, zákaz Title Case).
- Príklady „Po" musia samy spĺňať pravidlá skillu (žiadne em dashe, anglické úvodzovky, lepidlové pomlčky ani bohemizmy).
- Slovenská a česká verzia (katerina-svi/katerinas-humanizer-cz) sa udržiavajú spoločne: zmena spoločného vzorca patrí do oboch.
