# Katerinas Humanizer SK

Agent skill, ktorý odstraňuje zo **slovenských textov** znaky písania generovaného AI. Výsledkom je prirodzená, pravopisne a typograficky správna slovenčina podľa Pravidiel slovenského pravopisu a slovníkov [JÚĽŠ SAV](https://slovnik.juls.savba.sk/). Od verzie 1.0 systematicky stráži aj **kalky z angličtiny** a na **bohemizmy** má navyše slovník a skript.

Je to slovenská verzia skillu [Humanizer CZ](https://github.com/katerina-svi/katerinas-humanizer-cz), ktorý vychádza z anglického [blader/humanizer](https://github.com/blader/humanizer). Nie je to obyčajný preklad: vzorce sú prepracované pre slovenčinu a pribudli dva čisto slovenské (bohemizmy a vykanie). Jadro skillu je Markdown (`SKILL.md`), takže beží v každom prostredí, ktoré podporuje skilly. Slovník kalkov a pomocný skript sú voliteľné doplnky.

**Česká verzia:** [katerina-svi/katerinas-humanizer-cz](https://github.com/katerina-svi/katerinas-humanizer-cz)

## Čím sa líši od anglického originálu

**1. Prísny režim.** Skill nikdy nemení význam, nepridáva ani nevynecháva obsah a nevymýšľa fakty či zdroje. Text iba štylisticky preformuluje. Pred finálnym znením kontroluje, že každá informácia originálu je vo výslednom texte dohľadateľná a nijaká nepribudla.

**2. Pýta sa.** Pri sporných miestach (veta bez vecného obsahu, dvojznačnosť, možná citácia, nejednotné tykanie a vykanie, odborný žargón vs. slovník AI) skill nerozhoduje sám. Položí konkrétne otázky s návrhom riešenia a počká na odpoveď.

**3. Slovenská typografia s obrátenou logikou.** Anglický humanizer učí: oblé úvodzovky sú znak AI, pomlčky treba vyhubiť. V slovenčine je to inak:
- správne slovenské úvodzovky sú „dole a hore“, znakom AI sú naopak anglické “ ”
- pomlčka (–) je legitímna slovenská interpunkcia, ale vzácna: skill stráži „lepidlové“ pomlčky medzi vetami (kalk anglického em dashu) a drží tvrdý limit najviac jednej pomlčky s medzerami na text; rozsahy (15. – 18. 10.) zostávajú
- Title Case v nadpisoch slovenčina nemá vôbec

**4. Čisto slovenské vzorce.** Bohemizmy a kalky z češtiny (jedná sa o, doporučiť, akonáhle, stávajúci, úkol, české skratky atd. a tj.), ktoré jazykové modely do slovenčiny potichu prenášajú. Vykanie s množným číslom slovesa. Slovosled a aktuálne členenie vety, kalky ukazovacích a privlastňovacích zámen, svoj vs. jeho/jej/ich, prílišná knižnosť v konverzačnom texte aj opačná chyba (hovorové tvary v posudku), trpný rod a menné konštrukcie, medzery pri percentách a dátumoch podľa STN 01 6910.

**5. Kalky z angličtiny.** Znak AI, ktorý najčastejšie prejde prvou kontrolou: slovenské slová poskladané podľa anglickej predlohy („na dennej báze“, „Projekt drží podklady“, „AI stratégia“, „Pamätaj:“ v prevzatom prompte). Skill ich netriedi len podľa príkladov, ale podľa **desiatich mechanizmov**, ako kalk vzniká. Kto pozná mechanizmus, spozná aj kalk, ktorý v nijakom zozname nie je. V slovenčine sa kalky často miešajú s bohemizmami, lebo model skladá vetu cez češtinu. K tomu:
- **slovník** [`references/kalky.md`](references/kalky.md) s vyše 120 častými kalkami a bohemizmami, ich predlohou a slovenskými náhradami,
- **skript** [`scripts/najdi_kalky.py`](scripts/najdi_kalky.py), ktorý podľa slovníka označí podozrivé miesta (len kandidátov na posúdenie, nič neopravuje),
- **pevný postup kontroly kalkov** vrátane nadpisov, popisov, polí formulárov, textov na online tabuliach a prevzatých promptov, s tabuľkou Pred | Po | Prečo.

## Inštalácia

Najprv si stiahni `humanizer-sk.zip` z [najnovšieho vydania](https://github.com/katerina-svi/katerinas-humanizer-sk/releases/latest) (časť Assets). Účet na GitHube nepotrebuješ. ZIP obsahuje `SKILL.md`, slovník kalkov, skript a licenciu.

Názvy tlačidiel píšem po anglicky, tak ako ich uvádzajú návody výrobcov. Ak máš aplikáciu v slovenčine, nájdeš ich na rovnakom mieste.

### Claude (web a aplikácia)

1. ZIP nerozbaľuj.
2. V ľavom paneli klikni na **Plugins**.
3. Vpravo hore klikni na **Add** a zvoľ **Upload plugin**.
4. Do rámčeka pretiahni `humanizer-sk.zip` (alebo ho vyber cez **browse**) a klikni na **Upload**.
5. Skill nájdeš v Plugins pod filtrom **Skills**. Skontroluj, že je zapnutý.

Ak skill nefunguje, v **Settings → Capabilities** zapni **Create and edit files** (staršie nastavenie: **Code execution and file creation**). V tarifách Team a Enterprise môže nahrávanie vypnúť správca.

### Gemini

Gemini ZIP neberie. Chce rozbalený priečinok alebo súbory .md, .txt, .py a .csv.

1. ZIP rozbaľ. Vznikne priečinok `humanizer-sk` so súborom `SKILL.md`.
2. V ľavom paneli klikni na **Customize** a hore zvoľ **Skills**.
3. Klikni na **Create** → **Upload** a do rámčeka pretiahni celý priečinok `humanizer-sk`.

Ak namiesto Skills vidíš Gems, tvoj účet ešte neprešiel na skilly (pracovné účty Google Workspace prechádzajú v roku 2027). Vytvor nový Gem a do jeho pokynov vlož celý text súboru `SKILL.md`.

### ChatGPT

Ak v ľavom paneli vidíš **Plugins** a v nich kartu **Skills**:

1. Klikni na **Create** a zvoľ **Upload from your computer**.
2. Vyber stiahnutý `humanizer-sk.zip`.

Ak Skills nevidíš (závisí od tarify a od nastavení pracovného priestoru), vytvor si projekt, nahraj `SKILL.md` medzi súbory projektu a do pokynov projektu napíš: „Keď ťa požiadam o zľudštenie textu, riaď sa súborom SKILL.md.“ Samotný text `SKILL.md` do pokynov nekopíruj, je na ne pridlhý.

### Microsoft Copilot a ďalší chatboti

Prilož `SKILL.md` do chatu a použi tento prompt:

```
Prikladám súbor SKILL.md. Je to návod, ako upraviť slovenský text,
aby neznel ako z AI. Riaď sa ním a zľudšti tento text:
[vlož text]
```

### Claude Code (plugin)

```
/plugin marketplace add katerina-svi/katerinas-humanizer-sk
/plugin install humanizer-sk@katerinas-humanizer-sk
```

### Skills CLI (pre rôznych agentov)

```
npx skills add katerina-svi/katerinas-humanizer-sk
```

### Ručne

Naklonuj repozitár do priečinka, kde tvoj agent očakáva skilly:

```
git clone https://github.com/katerina-svi/katerinas-humanizer-sk.git /cesta/k/skillom/humanizer-sk
```

## Použitie

```
Použi skill humanizer-sk a zľudšti tento text:

[vlož text]
```

Alebo jednoducho: „Zľudšti mi tento text: …“, „Prepíš to, nech to neznie ako ChatGPT.“, „Prejdi to, pozor na kalky.“

Skill text najprv prejde, vypíše nájdené vzorce, **položí otázky k sporným miestam** a až po odpovediach dodá finálne znenie s prehľadom zmien. Kalky a bohemizmy vypíše v tabuľke Pred | Po | Prečo.

### Samotné hľadanie kalkov a bohemizmov

Skript beží bez závislostí, stačí Python 3:

```
python3 scripts/najdi_kalky.py moj-text.md
```

Vypíše každý nález s predlohou (anglickou alebo českou) a návrhom náhrady. Nálezy sú kandidáti na posúdenie: rovnaké slovo môže byť v inom spojení v poriadku. Výsledok „0 nálezov“ neznamená text bez kalkov, skript pozná len tie zo slovníka.

### Kalibrácia hlasu

Keď priložíš dva až tri odseky vlastného písania z rovnakého žánru, skill analyzuje tvoj rytmus viet, slovník a návyky a prepíše text tvojím hlasom namiesto generickej „čistej“ slovenčiny:

```
Použi skill humanizer-sk.

Vzorka môjho písania na zladenie hlasu:
[vlož vzorku]

Zľudšti tento text:
[vlož text]
```

## Čo skill deteguje (45 vzorcov v 5 blokoch)

**A. Obsahové:** inflácia významu („zásadný míľnik“), privesené vety „čo podčiarkuje“, reklamný jazyk, vágne autority („odborníci sa zhodujú“), šablónovité časti „výzvy a budúcnosť“, pravidlo troch, striedanie synoným, falošné rozsahy.

**B. Jazykové:** slovenský slovník AI (kľúčový, komplexný, avšak, v dnešnej digitálnej dobe…), „predstavuje/disponuje“ namiesto je/má, negatívne paralelizmy („nejde len o…“), trpný rod a menné konštrukcie, anglický slovosled, kalky zámen, svoj vs. jeho, **bohemizmy** (vrátane českých skratiek a písmen), **vykanie**, prílišná knižnosť aj opačná chyba, vata, prílišná opatrnosť vo formuláciách, generické závery (s výnimkou pre výzvu na akciu v marketingových textoch).

**C. Typografia a pravopis:** slovenské úvodzovky „ “, pomlčky (tvrdý limit, rozsahy s medzerami), Title Case, medzery, percentá, dátumy, tisíce a skratky, tučné písmo, emoji, fragmentované nadpisy.

**D. Komunikačné:** artefakty chatbota („Dúfam, že to pomôže!“), servilný tón, disclaimery a špekulatívne výplne, ohlasovanie („Poďme sa pozrieť…“), staccato dráma, aforistické vzorce, falošne dôverné úvody.

**E. Kalky z angličtiny:** doslovne preložené termíny a metafory („prvé princípy“, „prostredník z mäsa“), anglická frazeológia („na dennej báze“, „adresovať problém“, „mať dopad na“), zradné a preťažené slová a falošní priatelia („výstup“, „vstup“, „cesta“ za *way*, „eventuálne“ za *eventually*), vec ako činiteľ („Žiadosť píše“, „Projekt drží podklady“), anglické skladanie podstatných mien („AI stratégia“, „ľudská pripravenosť“), menné nadpisy a rady v nejednotnom tvare, obrazy, ktorým čitateľ po slovensky nerozumie, citácie, prevzaté prompty („Pamätaj:“, „Tvoja hodnota spočíva v tom…“) a anglická stavba vety v krátkych textoch.

Súčasťou je časť o falošných poplachoch (kedy NEzasahovať, napríklad nárečové a hovorové prvky, pojmy grantových formulárov, zaužívané anglicizmy odboru a spojenia, ktoré slovenčina prijala, ako *dávať zmysel*) a o znakoch ľudského písania, ktoré sa majú zachovať. Skill má aj pravidlá pre prípad, keď agent kontroluje text, ktorý sám napísal.

## História verzií

- **1.0.0**: nový blok E o kalkoch z angličtiny (vzorce 36 – 45, desať mechanizmov s testovacími otázkami a príkladmi), slovník kalkov a bohemizmov `references/kalky.md`, skript `scripts/najdi_kalky.py` a pevný postup kontroly kalkov. Rozšírený vzorec č. 17 o bohemizmoch (nové výrazy, české skratky a písmená). Ďalej pravidlá pre kontrolu vlastného textu, autorova formulácia len doslova doložená, vzorka hlasu z rovnakého žánru, ochrana spisovného registra posudkov, výnimky pre „Dajte mi vedieť“ v e-maile a pre pojmy grantových formulárov. Podrobnosti sú v [CHANGELOG.md](CHANGELOG.md).
- **0.9.0** (október 2026): prvá verejná verzia. 35 vzorcov pre slovenčinu, prísny režim, povinné otázky pri sporných miestach, tvrdý limit pomlčiek, nové vzorce pre bohemizmy a vykanie.

## Pripomienky k slovenčine sú vítané

Skill vznikol adaptáciou českej verzie a slovenčinu v ňom zatiaľ nečítal rodený hovoriaci. Ak nájdeš formuláciu, ktorá neznie po slovensky, chýbajúci kalk či bohemizmus alebo pravidlo, ktoré nie je v súlade s kodifikáciou, napíš to prosím do [Issues](https://github.com/katerina-svi/katerinas-humanizer-sk/issues).

## Autorka

[Kateřina Švidrnochová](https://svidrnochova.cz), konzultantka pre stratégiu AI vo firmách, service a learning dizajnérka a výskumníčka na Masarykovej univerzite.

## Poďakovanie a zdroje

- [blader/humanizer](https://github.com/blader/humanizer) (MIT): pôvodný anglický skill
- [Humanizer CZ](https://github.com/katerina-svi/katerinas-humanizer-cz) (MIT): česká verzia, z ktorej slovenská vychádza
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing): pôvodný katalóg vzorcov (WikiProject AI Cleanup)
- [Slovníkový portál JÚĽŠ SAV](https://slovnik.juls.savba.sk/) a [Jazyková poradňa JÚĽŠ SAV](https://www.juls.savba.sk/poradna.html): referencia pre slovenský pravopis a slovnú zásobu

## Licencia

MIT
