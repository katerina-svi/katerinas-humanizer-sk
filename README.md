# Katerinas Humanizer SK

Agent skill, ktorý odstraňuje zo **slovenských textov** znaky písania generovaného AI a prevádza ich do prirodzenej, pravopisne a typograficky správnej slovenčiny podľa Pravidiel slovenského pravopisu a slovníkov [JÚĽŠ SAV](https://slovnik.juls.savba.sk/).

Je to slovenská verzia skillu [Humanizer CZ](https://github.com/katerina-svi/katerinas-humanizer-cz), ktorý vychádza z anglického [blader/humanizer](https://github.com/blader/humanizer). Nie je to obyčajný preklad: vzorce sú prepracované pre slovenčinu a pribudli dva čisto slovenské (bohemizmy a vykanie). Celý skill je čistý Markdown (`SKILL.md`), takže beží v každom prostredí, ktoré podporuje skilly.

## Čím sa líši od anglického originálu

**1. Prísny režim.** Skill nikdy nemení význam, nepridáva ani neodoberá obsah a nevymýšľa fakty či zdroje. Text iba štylisticky preformuluje. Pred finálnym znením kontroluje, že každá informácia originálu je vo výstupe dohľadateľná a nijaká nepribudla.

**2. Pýta sa.** Pri sporných miestach (veta bez vecného obsahu, dvojznačnosť, možná citácia, nejednotné tykanie a vykanie, odborný žargón vs. slovník AI) skill nerozhoduje sám. Položí konkrétne otázky s návrhom riešenia a počká na odpoveď.

**3. Slovenská typografia s obrátenou logikou.** Anglický humanizer učí: oblé úvodzovky sú znak AI, pomlčky treba vyhubiť. V slovenčine je to inak:
- správne slovenské úvodzovky sú „dole a hore“, znakom AI sú naopak anglické “ ”
- pomlčka (–) je legitímna slovenská interpunkcia, ale vzácna: skill stráži „lepidlové“ pomlčky medzi vetami (kalk anglického em dashu) a drží tvrdý limit najviac jednej pomlčky s medzerami na text; rozsahy zostávajú
- Title Case v nadpisoch slovenčina nemá vôbec

**4. Čisto slovenské vzorce.** Bohemizmy a kalky z češtiny (jedná sa o, doporučiť, akonáhle, behom, nakoľko…), ktoré jazykové modely do slovenčiny potichu prenášajú. Vykanie s množným číslom slovesa. Slovosled a aktuálne členenie vety, kalky ukazovacích a privlastňovacích zámen, svoj vs. jeho/jej/ich, prílišná knižnosť v konverzačnom texte, trpný rod a menné konštrukcie, medzery pri percentách a dátumoch podľa STN 01 6910.

## Inštalácia

### Claude (web a aplikácia)

1. Stiahni `humanizer-sk.zip` z [Releases](https://github.com/katerina-svi/katerinas-humanizer-sk/releases/latest). Nerozbaľuj ho.
2. V Settings > Capabilities skontroluj, že je zapnuté **Code execution and file creation**.
3. Otvor **Customize > Skills**, klikni na **+**, zvoľ **Create skill** a potom **Upload a skill**.
4. Vyber stiahnutý ZIP.

### ChatGPT

1. Stiahni `humanizer-sk.zip` z [Releases](https://github.com/katerina-svi/katerinas-humanizer-sk/releases/latest).
2. V ľavom paneli otvor **Plugins** a prepni na kartu **Skills**.
3. Klikni na **Create** a zvoľ **Upload from your computer**.
4. Vyber stiahnutý ZIP.

Ak Skills v ChatGPT nevidíš, vytvor si Projekt, nahraj doň `SKILL.md` a do inštrukcií Projektu napíš, že sa má riadiť týmto súborom.

### Claude Code (plugin)

```
/plugin marketplace add katerina-svi/katerinas-humanizer-sk
/plugin install humanizer-sk@katerinas-humanizer-sk
```

### Skills CLI (pre rôznych agentov)

```
npx skills add katerina-svi/katerinas-humanizer-sk
```

## Použitie

```
Použi skill humanizer-sk a zľudšti tento text:

[vlož text]
```

Alebo jednoducho: „Zľudšti mi tento text: …“ či „Prepíš to, nech to neznie ako ChatGPT.“

Skill text najprv prejde, **položí otázky k sporným miestam** a až po odpovediach dodá finálne znenie s prehľadom zmien.

### Kalibrácia hlasu

Keď priložíš dva až tri odseky vlastného písania, skill analyzuje tvoj rytmus viet, slovník a návyky a prepíše text tvojím hlasom namiesto generickej „čistej“ slovenčiny.

## Čo skill deteguje (35 vzorcov v 4 blokoch)

**A. Obsahové:** inflácia významu („zásadný míľnik“), privesené vety „čo podčiarkuje“, reklamný jazyk, vágne autority („odborníci sa zhodujú“), šablónovité časti „výzvy a budúcnosť“, pravidlo troch, striedanie synoným, falošné rozsahy.

**B. Jazykové:** slovenský slovník AI (kľúčový, komplexný, avšak, v dnešnej digitálnej dobe…), „predstavuje/disponuje“ namiesto je/má, negatívne paralelizmy („nejde len o…“), trpný rod a menné konštrukcie, anglický slovosled, kalky zámen, svoj vs. jeho, **bohemizmy**, **vykanie**, prílišná knižnosť, vata, prílišná opatrnosť vo formuláciách, generické závery (s výnimkou pre CTA v marketingových textoch).

**C. Typografia a pravopis:** slovenské úvodzovky „ “, pomlčky (tvrdý limit), Title Case, medzery, percentá, dátumy a tisíce, tučné písmo, emoji, fragmentované nadpisy.

**D. Komunikačné:** artefakty chatbota („Dúfam, že to pomôže!“), servilný tón, disclaimery a špekulatívne výplne, ohlasovanie („Poďme sa pozrieť…“), staccato dráma, aforistické vzorce, falošne dôverné úvody.

Súčasťou je časť o falošných poplachoch (kedy NEzasahovať, napríklad nárečové a hovorové prvky sa neopravujú) a o znakoch ľudského písania, ktoré sa majú zachovať.

## História verzií

- **0.9.0** (október 2026): prvá verejná verzia. 35 vzorcov pre slovenčinu, prísny režim, povinné otázky pri sporných miestach, tvrdý limit pomlčiek, nové vzorce pre bohemizmy a vykanie.

## Pripomienky k slovenčine sú vítané

Skill vznikol adaptáciou českej verzie. Ak v ňom nájdeš formuláciu, ktorá neznie po slovensky, chýbajúci bohemizmus alebo pravidlo, ktoré nesedí s kodifikáciou, napíš to prosím do [Issues](https://github.com/katerina-svi/katerinas-humanizer-sk/issues).

## Autorka

[Kateřina Švidrnochová](https://svidrnochova.cz), konzultantka, learning designérka a lektorka AI vzdelávania.

## Poďakovanie a zdroje

- [blader/humanizer](https://github.com/blader/humanizer) (MIT): pôvodný anglický skill
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing): pôvodný katalóg vzorcov (WikiProject AI Cleanup)
- [Slovníkový portál JÚĽŠ SAV](https://slovnik.juls.savba.sk/): referencia pre slovenský pravopis a slovnú zásobu

## Licencia

MIT
