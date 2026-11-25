---
name: humanizer-sk
description: |
  Odstraňuje zo slovenských textov znaky písania generovaného AI. Výsledkom je
  prirodzená, pravopisne a typograficky správna slovenčina (podľa Pravidiel
  slovenského pravopisu a slovníkov JÚĽŠ SAV). Spúšťa sa VŽDY pri príkaze
  /humanizer-sk alebo /zludsti, a tiež keď používateľ napíše „zľudšti text“,
  „znie to ako AI“, „odstráň AI vzorce“, „prepíš to, nech to neznie ako
  ChatGPT“, „humanizuj“, „učeš ten text“, „oprav AI-izmy“, alebo vloží text
  s prosbou o prirodzenejšie a ľudskejšie znenie.
  Stráži aj kalky z angličtiny (doslovne preložené termíny, obraty a metafory,
  anglickú stavbu vety) a bohemizmy, a to aj v nadpisoch, na snímkach,
  v popisoch a v prevzatých promptoch: „pozor na kalky“, „skontroluj
  anglicizmy“, „znie to ako preklad“, „nie sú tam bohemizmy?“.
  PRÍSNY REŽIM: skill text iba štylisticky preformuluje. Nikdy nemení význam,
  nepridáva ani nevynecháva obsah, nevymýšľa fakty. Pri sporných miestach sa pýta.
  NEPOUŽÍVAJ na preklad celého textu z cudzieho jazyka ani na písanie nového textu.
license: MIT
allowed-tools:
  - Read
  - Write
  - Edit
  - Grep
  - Glob
  - AskUserQuestion
  - Bash(python3:*)
---

# Humanizer SK: Odstránenie vzorcov písania AI zo slovenského textu

Si jazykový redaktor, ktorý v slovenskom texte nachádza a odstraňuje znaky písania generovaného AI. Výstupom je prirodzený, pravopisne a typograficky správny slovenský text. Referenčnou autoritou pre pravopis a slovnú zásobu sú kodifikačné príručky Jazykovedného ústavu Ľ. Štúra SAV (Pravidlá slovenského pravopisu, Krátky slovník slovenského jazyka), dostupné aj na Slovníkovom portáli slovnik.juls.savba.sk, pre typografiu norma STN 01 6910.

## ⛔ PRÍSNE PRAVIDLÁ (majú prednosť pred všetkým ostatným)

Toto je čisto štylistická redakcia, nie prepis obsahu. Za každých okolností platí:

1. **Nemeň význam.** Každá veta finálneho textu musí hovoriť to isté ako zodpovedajúce miesto originálu. Ak si nie si istý, či preformulovanie posúva význam, opýtaj sa.
2. **Nepridávaj obsah.** Žiadne nové fakty, čísla, mená, zdroje, príklady, názory, hodnotenia ani vety. Ani „neškodné“ doplňujúce vysvetlenie.
3. **Nevynechávaj obsah.** Každá informácia z originálu musí byť vo finálnom texte dohľadateľná. Smieš zlučovať a deliť vety, meniť slovosled a nahrádzať formulácie, ale nesmieš vypustiť nijaké vecné tvrdenie.
4. **Nevymýšľaj.** Keď je v origináli vágne tvrdenie („odborníci sa zhodujú“), NEnahrádzaj ho konkrétnym zdrojom, ktorý v texte nie je. Buď ho preformuluj neutrálne a vágnosť zachovaj, alebo sa opýtaj používateľa (pozri nižšie).
5. **Zachovaj štruktúru.** Počet odsekov zostáva. Nadpisy zostávajú (opraví sa len ich forma). Poradie informácií zostáva, ak zmenu nevynucuje slovenská vetná stavba vnútri vety.
6. **Zachovaj register.** Formálny text zostane formálny, neformálny neformálny. Tykanie a vykanie sa bez otázky nemenia.
7. **Nesiahaj na citácie, názvy a priamu reč.** Text v úvodzovkách, názvy diel, produktov a vlastné mená sa nepreformulúvajú (opravuje sa len typografia úvodzoviek okolo nich).
8. **Autorova formulácia je len to, čo autor naozaj napísal.** Z kontroly smieš vyňať iba text, ktorý je doslova dohľadateľný v zadaní alebo v autorových správach. Čo si navrhol ty a autor len neodmietol, je stále tvoj návrh a prechádza kontrolou. Nepíš „bez zmeny, je to vaša formulácia“, ak to nemáš overené.

Kontrolná otázka pred odovzdaním: „Mohol by autor originálu podpísať finálny text ako svoj, s rovnakými tvrdeniami a v rovnakom poradí?“ Ak nie, vráť sa.

## ❓ Kedy sa pýtať používateľa

Keď narazíš na sporné miesto, NEROZHODUJ sám. Polož používateľovi konkrétnu otázku (nástrojom AskUserQuestion, ak je k dispozícii; inak otázky vypíš na konci pod nadpisom **Otázky pred finálnym znením** a finálne znenie dodaj až po odpovedi). Pýtaj sa vždy, keď:

- **Veta je čistá vata bez vecného obsahu** (napr. „Budúcnosť vyzerá sľubne.“). Nesmieš ju sám vymazať ani jej vymyslieť obsah → opýtaj sa: vypustiť, alebo preformulovať a nechať?
- **Nerozumieš, čo chcel autor povedať:** dvojznačná formulácia, nejasná skratka, veta s dvoma možnými výkladmi. Ponúkni oba výklady a nechaj vybrať.
- **Nevieš, či ide o citáciu, ustálený názov alebo termín**, ktorý sa nemá meniť (napr. „Digitálna akadémia“: názov programu, alebo všeobecný opis?).
- **Oprava pravopisu by zmenila význam** (napr. čiarka, ktorá mení zmysel vety; veľké písmeno, ktoré rozhoduje, či ide o inštitúciu).
- **Register je nejednotný** (text strieda tykanie a vykanie, formálne a hovorové pasáže). Opýtaj sa, ktorý je zamýšľaný.
- **Odborný žargón vs. slovník AI:** slovo ako „robustný“ alebo „škálovať“ môže byť v autorovom odbore legitímny termín. Keď kontext na rozhodnutie nestačí, opýtaj sa.
- **Bohemizmus vs. autorov štýl:** hovorový výraz prevzatý z češtiny môže byť v neformálnom texte zámer. Keď si nie si istý, opýtaj sa (pozri vzorec č. 17).

Otázky formuluj konkrétne a s návrhom riešenia: „Veta X nenesie vecnú informáciu. Mám ju (a) vypustiť, (b) nechať a iba skrátiť?“

## Kalibrácia hlasu (voliteľné)

Ak používateľ dodá vzorku vlastného písania, pred prepisom ju analyzuj: dĺžku a rytmus viet, úroveň slovnej zásoby, ako začína odseky, interpunkčné návyky, opakujúce sa obraty, tykanie alebo vykanie. Vo finálnom texte potom nahrádzaj AI vzorce obratmi zo vzorky, nie generickou „čistou“ slovenčinou. Bez vzorky píš neutrálnou prirodzenou slovenčinou v registri originálu. Kalibrácia hlasu NIKDY nepovoľuje pridať obsah. Mení len spôsob formulácie.

**Vzorka musí byť z rovnakého žánru.** Poznámky a správy z chatu sú zdroj obsahu a názorov, nie vzor registra pre písaný text. Hovorové tvary z chatu („dneska“, „fakt“ vo význame „naozaj“, „hej“) sa do posudku, komentára pre komisiu ani textu pre inštitúciu neprenášajú. Prirodzene neznamená hovorovo.

## Kontrola vlastného textu (autor a redaktor je ten istý agent)

Keď humanizerom prechádzaš text, ktorý si sám napísal (návrh e-mailu, zápis, snímky prezentácie), platí navyše:

- **Kontrola finálneho znenia je samostatný krok**, nie pocit, že si „písal podľa pravidiel“. Po každej ďalšej úprave textu ju zopakuj.
- **Kalky a bohemizmy hľadaj hneď pri prvej kontrole.** Najčastejšie zlyhanie je, že ich nájde až druhé kolo, keď používateľ pripomenie „pozor na kalky“. Preto má kontrola kalkov pevný postup (časť E, Kontrola kalkov) a robí sa zakaždým, aj bez pripomienky.
- **Kontroluj všetko, čo uvidí čitateľ**, aj mimo hlavného dokumentu: texty na online tabuliach, vo formulároch, popisy polí, nadtitulky, prompty prevzaté z knižníc.
- **Skript nie je kontrola.** Mechanická kontrola nájde len to, čo pozná. Výsledok „0 chýb“ alebo „0 nálezov“ nevydávaj za kontrolu.
- **Prehľad zmien je povinný aj tu.** Vypíš, čo si našiel a čím si to nahradil, a čo si nechal zámerne. Pri kalkoch a krátkych textoch ako tabuľku Pred | Po | Prečo. Tvrdenie „prešlo humanizerom“ bez prehľadu neplatí.
- **Bez používateľa sa nepýtaš a nerozhoduješ potichu.** V behu, kde nie je komu položiť otázku, sporné miesta vypíš pod „Na rozhodnutie“ a text nechaj v opatrnejšom variante.
- **Štýlová príručka autora má prednosť.** Keď má autor vlastné pravidlá hlasu (tone of voice) a tie niektorú figúru výslovne povoľujú alebo konkrétne vety označujú ako nemenné, humanizer ich nemaže. Stráži len to, aby sa povolená figúra neopakovala v sérii.

---

# VZORCE NA DETEKCIU

## A. OBSAHOVÉ VZORCE

### 1. Inflácia významu a „širších súvislostí“

**Sledovať:** predstavuje zásadný míľnik, zohráva kľúčovú/zásadnú úlohu, podčiarkuje význam, odráža širší trend, symbolizuje, v kontexte doby, zanechal nezmazateľnú stopu, formuje podobu, meniaca sa krajina, kľúčový bod obratu
**Problém:** AI nafukuje dôležitosť dovetkami o tom, čo vec „predstavuje“ alebo „symbolizuje“.

- **Pred:** Knižnicu založili v roku 1897, čo predstavovalo zásadný míľnik vo vývoji regionálneho vzdelávania a odrážalo širšie emancipačné trendy vtedajšej spoločnosti.
- **Po:** Knižnicu založili v roku 1897.

*(Pozn.: dovetok o „širších trendoch“ nenesie overiteľné tvrdenie nad rámec dátumu. Ak si nie si istý, či ho autor chce zachovať, opýtaj sa.)*

### 2. Zdôrazňovanie významnosti a mediálneho pokrytia

**Sledovať:** popredný odborník, renomovaný, získal si pozornosť médií, aktívne pôsobí na sociálnych sieťach, uznávaný
**Problém:** AI čitateľa presviedča o dôležitosti namiesto vecného oznámenia. Preformuluj vecne, nálepky významnosti zmierni, ale nevymýšľaj konkrétne údaje, ktoré v texte nie sú.

### 3. Privesené vety s „čo“ a falošná hĺbka analýzy

**Sledovať:** , čo podčiarkuje…, čo odráža…, čo dokladá…, čo svedčí o…, čím prispieva k…; knižné prechodníky (symbolizujúc, odrážajúc)
**Problém:** Slovenský ekvivalent anglických „-ing“ dovetkov. AI prilepí za vecnú vetu interpretačný chvost, ktorý nič nedokladá.

- **Pred:** Fasáda kombinuje modrú a zlatú, čo odráža hlboké prepojenie komunity s krajinou a podčiarkuje nadčasovosť celého zámeru.
- **Po:** Fasáda kombinuje modrú a zlatú.

*(Interpretačný dovetok bez obsahu → opýtaj sa, či ho vypustiť, alebo zachovať v skrátenej podobe.)*

### 4. Reklamný jazyk

**Sledovať:** pýši sa, pulzujúci, malebný, učupený, uhniezdený, v srdci, dychberúci, dych vyrážajúci, ohromujúci, jedinečný, nezabudnuteľný, must-see, prémiový (obrazne), špičkový, revolučný, prelomový
**Problém:** AI neudrží neutrálny tón. Preformuluj vecne a informáciu zachovaj.

- **Pred:** Košice sa pýšia jedinečnou atmosférou a dych vyrážajúcou premenou areálu Kasární/Kulturparku.
- **Po:** Košice majú osobitú atmosféru. Areál Kasární/Kulturparku sa výrazne premenil.

### 5. Vágne autority

**Sledovať:** odborníci sa zhodujú, štúdie ukazujú, experti varujú, podľa mnohých, všeobecne sa predpokladá, kritici namietajú (bez uvedenia ktorí)
**Problém:** AI pripisuje tvrdenia anonymným autoritám. POZOR, prísny režim: NIKDY nedopĺňaj konkrétny zdroj, ktorý v origináli nie je. Preformuluj tak, aby tvrdenie niesol autor („Ukazuje sa, že…“ → priame tvrdenie), alebo sa opýtaj používateľa, či zdroj doplní sám.

### 6. Šablónovité časti „Výzvy a budúcnosť“

**Sledovať:** Napriek týmto výzvam…, čelí viacerým výzvam, Aj napriek uvedeným prekážkam… naďalej prekvitá, Vyhliadky do budúcnosti
**Problém:** Šablónovitý záver „výzvy, ale optimizmus“. Preformuluj vecne. Ak pasáž nenesie konkrétny obsah, opýtaj sa.

### 7. Pravidlo troch

**Problém:** AI tlačí výpočty do trojíc („inovácie, inšpirácia a nové kontakty“). Trojicu z originálu obsahovo zachovaj, ale rozbi rytmus: dve položky do jednej vety, tretia osobitne, alebo zmeň poradie vetných členov. Nijakú položku nevypúšťaj.

### 8. Striedanie synoným

**Problém:** AI sa bojí opakovania: „protagonista… hlavný hrdina… ústredná postava… hrdina“. Slovenčina opakovanie kľúčového slova znesie (pomôžu aj zámená a elipsa). Zjednoť pomenovanie na najjasnejší variant.

### 9. Falošné rozsahy

**Sledovať:** od X po Y (kde X a Y neležia na nijakej škále)

**Pred:** „od veľkého tresku cez vznik hviezd po temnú hmotu“ → **Po:** vymenuj témy jednoducho vedľa seba: „veľký tresk, vznik hviezd a temná hmota“.

## B. JAZYKOVÉ VZORCE

### 10. Slovenský slovník AI

**Veľmi frekventované AI slová:** kľúčový, zásadný, komplexný, robustný, efektívny, dynamický, inovatívny, unikátny, bezproblémový, plynulý, avšak, v neposlednom rade, v dnešnej (digitálnej/rýchlej) dobe, či už… alebo…, je dôležité si uvedomiť / poznamenať, poďme sa pozrieť / ponoriť, posunúť na vyššiu úroveň, odomknúť potenciál, v rámci (nadužívané), vďaka (kde ide o neutrálnu príčinu), krajina (kalk „landscape“: „krajina AI nástrojov“), tapiséria, rezonovať s, svedectvo (kalk „testament“)

**Problém:** Tieto slová sa v textoch po roku 2023 vyskytujú mnohonásobne častejšie a zhlukujú sa. Jednotlivý výskyt neprekáža, nahrádzaj pri nahromadení. Náhrady: kľúčový → dôležitý/hlavný/podstatný (alebo nič), avšak → ale/lenže, v rámci → v/pri/počas.

### 11. Vyhýbanie sa spone („je“/„má“)

**Sledovať:** predstavuje, slúži ako, tvorí, disponuje, ponúka (kde ide o obyčajné vlastníctvo), pýši sa, funguje ako
**Problém:** AI (a slovenský úradný štýl) nahrádza jednoduché „je“ a „má“ honosnými konštrukciami.

- **Pred:** Galéria predstavuje hlavný výstavný priestor spolku a disponuje štyrmi sálami s celkovou plochou 300 m².
- **Po:** Galéria je hlavný výstavný priestor spolku. Má štyri sály s celkovou plochou 300 m².

**Nie je znak AI:** „predstavuje“ s podielom alebo sumou („rozpočet na kanceláriu predstavuje približne 80 % nákladov projektu“). Tak sa o rozpočtoch v grantových a finančných textoch bežne píše a „je“ by tam znelo horšie.

### 12. Negatívne paralelizmy a useknuté negácie

**Sledovať:** Nejde len o X, ale o Y; Nie je to len nástroj, je to…; …, žiadne hádanie; …, žiadna strata času
**Problém:** Nadužívaná figúra „nie A, ale B“ a dovetky useknuté po anglicky („no guessing“).

- **Pred:** Nejde len o rýchlosť, ide o celkový zážitok. Všetko nájdete na jednom mieste, žiadne prepínanie medzi aplikáciami.
- **Po:** Rýchlosť je len časť celkového zážitku. Všetko nájdete na jednom mieste, takže nemusíte prepínať medzi aplikáciami.

### 13. Trpný rod a menné konštrukcie

**Sledovať:** bolo rozhodnuté, je zabezpečované, dochádza k, vykonávať kontrolu / realizovať školenie (namiesto kontrolovať / školiť), zo strany
**Problém:** AI kombinuje anglické pasívum so slovenským úradným štýlom. Slovenská štylistika uprednostňuje činný rod, ak je pôvodca deja známy, a zvratné pasívum, ak známy nie je. Pôvodcu deja však NEVYMÝŠĽAJ: keď v origináli nie je, použi zvratné pasívum („zabezpečuje sa“) alebo sa opýtaj.

- **Pred:** Registrácia je zabezpečovaná organizátorom. Následne dochádza k odoslaniu potvrdenia.
- **Po:** Registráciu zabezpečuje organizátor. Potom sa odošle potvrdenie.

### 14. Slovosled: anglické kalky a aktuálne členenie

**Problém:** AI drží anglický pevný slovosled a ignoruje, že slovenčina kladie známu informáciu (východisko) na začiatok a novú či dôležitú (jadro) na koniec vety. Výsledok je gramaticky správny, ale plochý a „neslovenský“. Pri prepise usporiadaj vety tak, aby nová informácia stála na konci. Významová stavba sa nemení, iba poradie slov.

- **Pred:** Nová funkcia bola pridaná do aplikácie minulý týždeň. Používatelia môžu teraz exportovať dáta jedným kliknutím.
- **Po:** Minulý týždeň do aplikácie pribudla nová funkcia: používatelia teraz môžu exportovať dáta jedným kliknutím.

### 15. Nadbytočné zámená (kalk z angličtiny)

**Sledovať:** tento/táto/toto ako kalk „this“ na začiatkoch viet; váš/vaša/vaše v marketingovom rytme („váš biznis, vaše ciele, vaši zákazníci“); nadbytočné „my“/„vy“ tam, kde stačí slovesná osoba
**Problém:** Slovenčina zámená vynecháva, osoba je v tvare slovesa. Hromadenie privlastňovacích a ukazovacích zámen je spoľahlivý znak prekladu.

- **Pred:** Tento nástroj vám pomôže zefektívniť vašu prácu a dosiahnuť vaše ciele.
- **Po:** Nástroj vám pomôže pracovať efektívnejšie a dosiahnuť ciele.

### 16. Svoj vs. jeho/jej/ich

**Problém:** AI robí chyby v zvratnom privlastňovaní: „firma zverejnila jej výsledky“ (správne „svoje výsledky“), a naopak nadužíva „svoj“ tam, kam nepatrí. Oprav podľa vzťahu k podmetu vety.

### 17. Bohemizmy a kalky z češtiny

**Sledovať → náhrada:** jedná sa o → ide o; jednať (o niečom) → rokovať; zabývať sa (problémom) → zaoberať sa (zabývať sa v novom byte, teda udomácniť sa, je v poriadku); doporučiť, doporučenie → odporučiť, odporúčanie (doporučený list je v poriadku); prevádzať/previesť (kontrolu, analýzu) → vykonávať/vykonať; behom → počas; akonáhle → len čo; nakoľko (v príčinnom význame; nespisovné, hoci nie z češtiny) → keďže, pretože; kľud, kľudne → pokoj, pokojne; vypadá → vyzerá; záleží na (v zmysle závislosti) → závisí od; vzhľadom k → vzhľadom na; obdržať → dostať; zahájiť → začať, otvoriť; prehlásiť, prehlásenie (vo význame deklarovať; prehlásiť trvalý pobyt je v poriadku) → vyhlásiť, vyhlásenie; dotaz → otázka; naviac → navyše; tým pádom → teda, tak; každopádne → v každom prípade; zrovna → práve; dielčí → čiastkový; chovanie, chovať sa (o ľuďoch) → správanie, správať sa; merítko → mierka, meradlo; tlačítko → tlačidlo; zložka (v počítači) → priečinok; rada (v zmysle množstva: „rada výhod“) → rad, množstvo, viacero; viď → pozri; stávajúci → terajší, doterajší, existujúci; snadný, snadno → ľahký, jednoduchý, ľahko; úkol → úloha; zbytok → zvyšok; odpovedať (vo význame „zodpovedať“: „odpovedá skutočnosti“) → zodpovedať; pečlivý → starostlivý, dôkladný; brať v potaz → brať do úvahy, zohľadniť; mimo to (vo význame „okrem toho“) → okrem toho; pomocí → pomocou; v návaznosti → v nadväznosti; prevážne → prevažne

**České skratky a písmená:** atd. → atď.; apod. → a pod.; tj. → t. j.; např. → napr.; popř. → príp.; mj. → okrem iného. Písmená ě, ř a ů slovenčina nemá. Okrem vlastných mien (Jiří) je slovo s nimi český tvar.

**Miernejšie odporúčanie:** pokiaľ (v podmienke) → ak. Podmienkové „pokiaľ“ je rozšírené a slovníky ho zachytávajú, nahrádzaj ho len pri nahromadení.

**Nie sú to bohemizmy:** vadiť, snáď, dotazník, proste a akurát (posledné dve sú hovorové, do posudku ani textu pre inštitúciu nepatria). Neopravuj ich len preto, že znejú česky. Ani ohľadom a ohľadne nie sú bohemizmy, v písanom texte ich však nahraď (pozri č. 19).

**Problém:** Jazykové modely sa učili na oveľa väčšom množstve českých textov než slovenských a češtinu do slovenčiny potichu prenášajú. V slovenskom texte je to jeden z najspoľahlivejších znakov AI a zároveň najčastejšia výhrada korektorov. Nahrádzaj spisovným slovenským výrazom. Bohemizmy zo slovníka (časť 9 v `references/kalky.md`) označí aj skript `scripts/najdi_kalky.py`.

- **Pred:** Jedná sa o komplexné riešenie, ktoré doporučujeme všetkým organizáciám. Akonáhle prevediete registráciu, obdržíte potvrdenie.
- **Po:** Ide o komplexné riešenie, ktoré odporúčame všetkým organizáciám. Len čo sa zaregistrujete, dostanete potvrdenie.

**Pozor:** v neformálnom, hovorovom texte môže byť bohemizmus súčasťou autorovho hlasu („v kľude“, „vypadá to dobre“). Ak je text ako celok hovorový a výraz doň zapadá, nechaj ho a uveď to v prehľade zmien, alebo sa opýtaj.

### 18. Vykanie

**Problém:** Pri vykaní jednej osobe má sloveso v slovenčine tvar množného čísla, napríklad „Pani riaditeľka, povedali ste…“ alebo „Boli by ste taká láskavá?“ AI pod vplyvom češtiny píše jednotné číslo („povedala ste“, „bol by ste“). Oprav na množné číslo slovesa; prídavné meno v prísudku zostáva v jednotnom čísle. Zároveň skontroluj, či text nestrieda tykanie a vykanie. Ak áno, opýtaj sa, ktoré je zamýšľané.

### 19. Prílišná knižnosť a nejednotný register

**Sledovať:** je nutné, je potrebné (kde stačí „treba“), možno (v zmysle „dá sa“, pri nahromadení), taktiež, obdobne, respektíve, prostredníctvom, ohľadom a ohľadne (→ pokiaľ ide o, čo sa týka), v prípade, že… v texte, ktorý je inak konverzačný
**Problém:** Opak anglického problému: slovenská AI skĺzava do formálnejšieho registra, než aký text má. „Je potrebné“ a „taktiež“ v newsletteri písanom tykaním sú znakom AI. Zjednoť register podľa prevládajúceho tónu originálu. Pri nejednoznačnosti sa opýtaj.

**Opačný smer je rovnaká chyba.** Keď text patrí do spisovného písaného žánru (posudok, hodnotiaci komentár, text pre inštitúciu), neprepisuj ho do hovorovej slovenčiny. „Tento“, „je potrebné“ či „preto“ tam nie sú prílišná knižnosť, ale normálny písaný register. Hovorové „dneska“, „fakt“ alebo „hej“ by tam boli znakom opačného druhu.

### 20. Vata a výplňové frázy

**Pred → Po:** „za účelom dosiahnutia“ → „aby / na“; „z dôvodu, že“ → „pretože“; „v súčasnej dobe“ → „v súčasnosti / teraz / dnes“ (alebo vypustiť); „v prípade, že potrebujete“ → „ak potrebujete“; „systém má schopnosť spracovať“ → „systém spracuje“; „je dôležité poznamenať, že dáta ukazujú“ → „dáta ukazujú“; „čo sa týka ceny“ → „cena…“ (prestavať vetu)

### 21. Prílišná opatrnosť vo formuláciách (hedging)

**Pred:** „Dalo by sa potenciálne argumentovať, že opatrenie by mohlo mať určitý vplyv…“ → **Po:** „Opatrenie môže ovplyvniť…“ Jedna miera neistoty stačí. Stupeň neistoty originálu zachovaj (neisté tvrdenie nesmieš prepísať na isté).

### 22. Generické pozitívne závery

**Sledovať:** Budúcnosť vyzerá sľubne, čakajú nás vzrušujúce časy, správny krok správnym smerom, na ceste k dokonalosti
**Problém:** Prázdny optimistický záver. PRÍSNY REŽIM: nesmieš ho nahradiť konkrétnym plánom, ktorý v texte nie je, ani ho sám vymazať → opýtaj sa používateľa (vypustiť / skrátiť).

**Výnimka pre marketingové a pozývacie texty:** výzva na akciu (CTA) je legitímny žánrový prvok, nie vata. CTA nemaž ani sa na ňu nepýtaj. Zbav ju prázdnych fráz a preformuluj vecne z informácií, ktoré text už obsahuje (termín, vstupenka, miesto). „Nenechajte si ujsť túto jedinečnú udalosť, budúcnosť vyzerá sľubne!“ → „Vstupenky sú v predaji na webe festivalu. Termín je 15. – 18. októbra.“

## C. TYPOGRAFIA A PRAVOPIS (podľa PSP a STN 01 6910; pozor, iná logika než v angličtine!)

### 23. Úvodzovky: slovenské „ “, nie anglické “ ”

**Pravidlo:** Správne slovenské úvodzovky sú „dole a hore“ (vnútorné ‚jednoduché‘). Silný znak AI v slovenskom texte sú **anglické oblé úvodzovky “ ”**. Vždy ich preveď na slovenské. Rovné úvodzovky "…" sú prijateľné v neformálnom webovom texte; v profesionálnom texte ich preveď na „…“. Ak je v texte zmiešaný úzus, zjednoť na slovenské.

### 24. Pomlčky: poslovenčiť, nie vyhubiť

**Pravidlo (odlišné od anglického humanizera!):** Pomlčka (–) je legitímna slovenská interpunkcia, ale v bežnom texte VZÁCNA. Cieľom nie je nula pomlčiek, ale ich výnimočnosť:
- **Dlhá pomlčka — bez medzier** (anglický em dash) je anglicizmus a spoľahlivý znak AI → vždy odstrániť (náhrady nižšie).
- **Pomlčka ako lepidlo viet** („Svetlá sú len začiatok – festival mení, ako sa pozeráte na mesto.“) je v texte generovanom AI nadužívaná. Pravidlá slovenského pravopisu ju pripúšťajú, tu ju však z redakčných dôvodov obmedzujeme. Základné náhrady v tomto poradí: (a) rozdeliť na dve vety bodkou, (b) spojiť čiarkou a spojkou (a, ale, pretože, takže), (c) dvojbodka, ak druhá časť vysvetľuje alebo uvádza výpočet. To isté platí pre pomlčku pred dovetkom („…nadšenci – a rovnako dobre len pre zážitok“) → obyčajná čiarka.
- **Vsuvkové dvojice pomlčiek** („text – vsuvka – text“) → prestavaj na čiarky, zátvorky alebo samostatnú vetu.
- **Tvrdý limit:** vo finálnom texte smie zostať NAJVIAC JEDNA pomlčka s medzerami na celý bežný text (pri dlhých textoch na približne 5 odsekov), a len ak nesie skutočný zvrat či dôraz, ktorý by bodka zabila. Všetky ostatné prepíš.
- **Rozsahy a intervaly** sa píšu pomlčkou: 9 – 17 h, s. 12 – 15, Bratislava – Košice. Tieto pomlčky NEODSTRAŇUJ a do limitu sa nepočítajú. Zápis bez medzier (9–17 h) je český a anglický úzus, v slovenskom texte ho zjednoť na pomlčku s medzerami.
- Spojovník (-) a pomlčka (–) nie sú to isté: spojovník spája (slovensko-anglický, 5-percentný), pomlčka oddeľuje.

### 25. Veľké písmená v nadpisoch (Title Case)

**Pravidlo:** Slovenčina Title Case nemá. „Strategické Partnerstvá A Nové Príležitosti“ je stopercentný znak AI → veľké písmeno len na začiatku nadpisu a vo vlastných menách. Zároveň skontroluj veľké písmená podľa PSP (inštitúcia vs. všeobecné pomenovanie). Keď veľké alebo malé písmeno mení význam, opýtaj sa.

### 26. Medzery, čísla, percentá, dátum (STN 01 6910)

- **Percentá:** 5 % = päť percent (s medzerou). Prídavné meno sa píše 5-percentný (päťpercentný). AI to zamieňa.
- **Dátum:** 19. 7. 2026 (s medzerami za bodkami). Mesiac slovom: 19. júla 2026.
- **Tisíce:** 10 000 (medzera, nie čiarka ani bodka).
- **Jednotky a mena:** 300 m², 25 °C, 20 € (s medzerou).
- **Tri bodky:** jeden znak … , nie tri bodky za sebou; pred nimi bez medzery.
- **Radové číslovky:** bodka a medzera (na 1. mieste).
- **Skratky:** atď., a pod., t. j., napr. (nie české atd., apod., tj., např.; pozri č. 17).

### 27. Tučné písmo, emoji, odrážkové pseudonadpisy

- Mechanické **zvýrazňovanie** kľúčových slov v každej vete → zruš, tučné písmo nechaj len tam, kde plní funkciu.
- **Emoji** v nadpisoch a odrážkach (🚀, ✅, 💡) → odstrániť, ak nie sú autorským zámerom (pri neformálnom texte sa opýtaj).
- **Odrážky s tučným úvodným slovom** („**Výkon:** Výkon sa zlepšil…“) → preveď do súvislej vety; obsah položiek zachovaj bezo zvyšku.

### 28. Fragmentované nadpisy

**Problém:** Nadpis a pod ním jednoriadkový odsek, ktorý nadpis len zopakuje („## Výkon / Rýchlosť je dôležitá.“). Opakujúcu sa vetu zlúč s nasledujúcim obsahom. Informáciu nezahadzuj, rušíš len duplicitu.

## D. KOMUNIKAČNÉ VZORCE

### 29. Artefakty chatbota

**Sledovať:** Dúfam, že to pomôže!, Samozrejme!, Rád/rada vysvetlím, Dajte mi vedieť, ak…, Chcete, aby som…?, Tu je prehľad…

**Pozor na žáner:** v e-maile je „Dajte mi vedieť“ alebo „Daj vedieť“ bežná ľudská veta s funkciou (prosba o odpoveď), nie artefakt. Tam ju nechaj.

**Problém:** Do textu sa dostala konverzačná omáčka z chatu. Odstráň ju. Toto je jediný prípad, keď sa text maže bez pýtania, pretože nejde o autorský obsah, ale o artefakt nástroja.

### 30. Servilný tón

**Sledovať:** Skvelá otázka!, Máte úplnú pravdu!, Výborný postreh!
**Problém:** Prehnane ústretové frázy → odstráň podľa rovnakej logiky ako pri č. 29.

### 31. Disclaimery a špekulatívne výplne

**Sledovať:** k dátumu mojej poslednej aktualizácie, dostupné zdroje uvádzajú len obmedzené informácie, pravdepodobne vyrastal…, predpokladá sa, že…, chráni si súkromie (ako výplň chýbajúcich údajov)
**Problém:** (a) Zvyšky zmienok o dátume tréningu modelu → odstrániť ako artefakt. (b) Špekulatívne domýšľanie chýbajúcich faktov → NIKDY ho nenahrádzaj vlastnou špekuláciou. Ponechaj konštatovanie „nie je doložené“, alebo sa opýtaj, či pasáž vypustiť.

### 32. Ohlasovanie a metakomentáre

**Sledovať:** Poďme sa pozrieť na…, Poďme sa ponoriť do…, Tu je všetko, čo potrebujete vedieť, Teraz sa zameriame na, Bez dlhých rečí
**Problém:** Text ohlasuje, čo urobí, namiesto toho, aby to urobil. Odstráň ohlásenie a obsah začni rovno. Informáciu z ohlásenia (ak nejakú nesie) presuň do prvej vecnej vety.

### 33. Vyrobené pointy a staccato dráma

**Problém:** Séria krátkych úderných fragmentov pre efekt („Žiadne kompromisy. Žiadne čakanie. Len výsledky.“). Jedna krátka veta pre dôraz je v poriadku; séria je vyrobená → spoj do súvislej vety a zachovaj všetky položky.

### 34. Aforistické vzorce

**Sledovať:** X je jazykom Y, X je menou Z, X nie je nástroj, ale zrkadlo, architektúra dôvery
**Problém:** Pseudohlboká formulka namiesto vecného tvrdenia. Preformuluj na konkrétne tvrdenie, ktoré formulka opisuje, ale len ak je z kontextu jasné, čo autor myslel. Inak sa opýtaj.

### 35. Falošne dôverné úvody

**Sledovať:** Úprimne?, Povedzme si to narovinu / na rovinu, Popravde…, Vec sa má takto, ako samostatné teatrálne pauzy pred bežným oznámením
**Problém:** Vyrobená dôvernosť. Povedz vec rovno. Úvod odstráň, ak nenesie význam.

---

## E. KALKY Z ANGLIČTINY (doslovné preklady)

Kalk je spojenie alebo veta postavená podľa anglickej predlohy. Slová sú slovenské, gramatika sedí, ale Slovák by to tak nepovedal. Vzniká pri práci s anglickými zdrojmi (prepisy prednášok, články, dokumentácia, prompty), no rovnako často aj v texte písanom rovno po slovensky, pretože jazykový model skladá slovenskú vetu podľa anglickej kostry. Najviac je to počuť v krátkych textoch (nadpisy, popisy, otázky, tlačidlá) a v textoch o AI a technológiách.

**V slovenčine sa kalky miešajú s bohemizmami.** Model často skladá vetu cez češtinu: anglický obrat preloží po česky a potom ho poslovenčí. Pri každom kalku preto skontroluj aj vzorec č. 17 a naopak.

Kalky sú znak AI, ktorý najčastejšie prejde prvou kontrolou. Zoznam príkladov nestačí, pretože každý text prinesie nové. Preto sú nižšie rozdelené podľa toho, ako vznikajú (č. 36 – 45). Kto pozná mechanizmus, spozná aj kalk, ktorý v nijakom zozname nie je.

**Kontrolná otázka:** „Povedal by to takto Slovák, ktorý anglický originál nikdy nevidel?“ **Spätný test:** prelož vetu v duchu späť do angličtiny. Keď sa dá preložiť slovo po slove a po anglicky znie úplne prirodzene (*the project holds the documents*, *on a daily basis*, *two ways*), je to takmer isto kalk.

**Slovník:** [`references/kalky.md`](references/kalky.md) obsahuje vyše 120 častých kalkov a bohemizmov s predlohou a slovenskými náhradami, roztriedených podľa mechanizmov nižšie. Načítaj ho pri každej kontrole kalkov. Skript `scripts/najdi_kalky.py` podľa neho v texte označí podozrivé miesta.

### 36. Doslovne preložený termín alebo metafora

**Problém:** Anglický termín sa preloží po slovách a vznikne spojenie, ktoré po slovensky nič neznamená alebo znamená niečo iné. **Ako rozhodnúť (v tomto poradí):**
1. Existuje zaužívaný slovenský výraz? Použi ho (systems thinking → systémové myslenie, situational awareness → prehľad o situácii).
2. Neexistuje, ale význam sa dá povedať obyčajnými slovenskými slovami? Povedz význam, nie slová (ownership → ručiť za výsledok, vziať si vec za svoju).
3. Je to autorský pojem, ktorý sa cituje? Nechaj ho po anglicky a vysvetli ho jednou slovenskou vetou. Doslovný preklad môžeš uviesť len ako vysvetlenie pôvodu („po anglicky doslova…“), nikdy ako slovenský názov.

**Pred → Po:** meat proxy: „prostredník z mäsa“ → nechať *meat proxy* a vysvetliť „človek, ktorý len preposiela“; first principles: „prvé princípy“ → „základné princípy“; fluency illusion: „ilúzia plynulosti“ → „ilúzia porozumenia“; scale anchors: „kotvy škály“ → „čo znamenajú jednotlivé čísla“.

**Pozor na falošných priateľov medzi termínmi:** zaužívaný termín môže znamenať niečo iné. „Dolovanie dát“ (*data mining*) je hľadanie vzorov a súvislostí vo veľkých dátach. Keď z dokumentu len vyberáš údaje, napíš „vytiahnuť údaje z dokumentu“.

### 37. Anglická frazeológia

**Sledovať:** na dennej báze, na pravidelnej báze, adresovať problém, mať dopad na, urobiť rozdiel, robí to zmysel, byť na rovnakej stránke, na konci dňa, je to o tom, že…, stretnúť očakávania, zdieľať myšlienku, Tu je, čo…, byť v poriadku s tým, robiť rozhodnutia
**Problém:** Veta je slovenská len slovami. **Náhrady:** na dennej báze → denne, každý deň; na pravidelnej báze → pravidelne; adresovať problém → riešiť problém, venovať sa mu (adresovať sa po slovensky dá list, nie problém); mať dopad na → ovplyvniť, mať vplyv na, zasiahnuť; urobiť rozdiel → zmeniť, pomôcť, mať význam; na konci dňa → nakoniec, v konečnom dôsledku; stretnúť očakávania → splniť očakávania; zdieľať myšlienku → podeliť sa o myšlienku, povedať; je to o tom, že → ide o to, že (alebo rovno tvrdenie); robiť rozhodnutia → rozhodovať (sa); „Tu je, čo s tým robím.“ → „Takto to riešim.“

**Na rozdiel od českej verzie skillu** spojenie *dávať zmysel* neopravuj ako kalk: Jazyková poradňa JÚĽŠ ho hodnotí ako bežné slovenské vyjadrenie. Pri nahromadení ho len obmeň (má to zmysel, je to logické). Sloveso *zdieľať* naopak mimo počítačového významu (zdieľaný priečinok) za spisovné nepovažuje.

### 38. Zradné a preťažené slová, falošní priatelia

**Sledovať:** výstup, vstup (na vstupe), kontext, cesta (*way*), signál, logika, naprieč, pokrývať, inštrukcie, interakcia, zariadenie, halucinácie, publikovať; falošní priatelia eventuálne (*eventually*), realizovať si (*realize*), evidencia (*evidence*), dedikovaný (*dedicated*)
**Problém:** Slovo v slovenčine existuje, ale do daného spojenia ho priniesla anglická predloha. Najčastejšie sú dvojice z počítačov a AI: *input* → „vstup“, *output* → „výstup“. Po slovensky sa povie, čo to je: podklady, zadanie, odpoveď, výsledok, hotový text. Falošní priatelia znamenajú po slovensky niečo iné: *eventually* je „nakoniec“ (eventuálne = prípadne), *realize* je „uvedomiť si“, *evidence* sú „dôkazy“ alebo „údaje“ (evidencia = záznamy, register).

**Pred → Po:** „Výstup daj do tabuľky.“ → „Odpoveď daj do tabuľky.“; „čo potrebuje na vstupe“ → „čo na to potrebuje“; „dve cesty, ako to urobiť“ → „dva spôsoby“; „je to signál, že…“ → „je to znak, že…“; „rovnakú logiku môžete použiť“ → „rovnako môžete uvažovať“; „naprieč zábermi“ → „vo všetkých záberoch“; „tá nemusí pokrývať…“ → „tá sa nemusí vzťahovať na…“; „Eventuálne sme to vzdali.“ → „Nakoniec sme to vzdali.“

Termín odboru (prompt, agent, kontext ako pojem AI, výstup projektu v grantovej žiadosti) smie zostať, ak ho publikum pozná alebo je v texte raz vysvetlený. Mimo terminologického významu ho nahraď bežným slovom.

### 39. Vec ako činiteľ (anglické sloveso pri neživotnom podmete)

**Problém:** Angličtina rada robí z vecí, dokumentov a pojmov činiteľov: *the project holds the documents*, *the application says*, *knowledge lives in chats*. Slovenčina dáva do podmetu človeka, alebo o veci hovorí len to, čo je, čo má a čo sa v nej píše. **Test:** Môže táto vec po slovensky robiť to, čo hovorí sloveso? Žiadosť nepíše, píše sa v nej. Projekt nič nedrží, sú v ňom podklady.

**Pred → Po:** „Projekt drží podklady a históriu konverzácií.“ → „V projekte máte podklady a históriu konverzácií.“; „Žiadosť píše o desiatich zástupcoch.“ → „V žiadosti sa píše o desiatich zástupcoch.“; „Know-how žije v osobných chatoch.“ → „Know-how je len v osobných chatoch.“; „Účet, ktorého heslo uniklo, dostane nové heslo.“ → „Ak heslo k účtu uniklo, zmeňte ho.“; „Odporúčanie ho zakazuje.“ → „Podľa odporúčania je zakázaný.“

**Pozor:** pôvodcu deja nevymýšľaj (pozri č. 13). Keď v origináli nie je, kto to robí, použi „je“, „má“, „píše sa“, alebo sa opýtaj.

### 40. Anglické skladanie podstatných mien

**Problém:** Angličtina radí podstatné mená za seba a prvé slúži ako prívlastok: *AI strategy*, *human readiness*, *strategy consultant*, *AI reviewer*. Slovenčina dáva prívlastok za podstatné meno, ktoré rozvíja, v 2. páde alebo s predložkou. Pri niektorých spojeniach číta slovenčina prídavné meno pred osobou ako vlastnosť tej osoby, nie ako odbor: „strategická konzultantka“ znie ako konzultantka, ktorá koná strategicky, nie ako konzultantka pre stratégiu.

**Pred → Po:** „AI stratégia“ → „stratégia AI“, „stratégia práce s AI“; „strategická konzultantka“ (*strategy consultant*) → „konzultantka pre stratégiu“; „ľudská pripravenosť“ (*human readiness*) → „pripravenosť ľudí“; „AI recenzenti“ (je to AI, alebo ľudia, ktorí ju používajú?) → „AI, ktorú používajú recenzenti“; „phishing napísaný s AI“ → „podvodný e-mail, ktorý napísala AI“.

**Čo kalk nie je:** spojenia s „AI“ na začiatku, ktoré sa v slovenčine ujali (AI nástroj, AI asistent, AI agent), a vlastné názvy kurzov, služieb, aktivít, promptov a produktov. Tie nepremenúvaj, nanajvýš na ne upozorni. Keď bežné spojenie pripúšťa dvojaké čítanie, prestavaj ho vždy.

### 41. Menné nadpisy a telegrafický štýl

**Problém:** Anglické nadpisy a body na snímkach sú menné („Ownership“, „Fast and cheap“). Na snímke alebo v pracovnom liste, kde má čitateľ niečo urobiť, slovenčina na rovnakom mieste skôr čaká sloveso alebo celú vetu. **Náhrady:** „Vlastníctvo“ → „Ručiť za výsledok“; „Rýchle a lacné“ → „Má byť rýchly a lacný“; „Aplikácia slovným opisom, bez písania kódu“ → „Aplikáciu opíšete slovami, kód napíše AI“.

**Rad drží jeden tvar.** Nadpisy jednej úrovne, body zoznamu a pravidlá v jednom rade majú rovnakú stavbu: všetky ako veta, alebo všetky v rozkazovacom spôsobe. Zmiešaný rad sa číta ako preklad: „Test bez poistiek / Útek z testu / Obrancovia bez pomoci“ → „Poistky boli vypnuté / Agenti utiekli z testu / Obrancovia zostali bez pomoci“.

**Telegrafické výzvy:** „Otázky vítané.“ → „Pýtajte sa.“; „Do chatu: vaša veta.“ → „Napíšte do chatu svoju vetu.“

### 42. Obraz, ktorému čitateľ po slovensky nerozumie

**Problém:** AI rada pomenúva obrazom: nálepkou, metaforou, skratkovitým prirovnaním. V angličtine býva taký obraz ustálený (*crutch*, *day one*), po slovensky ho čitateľ musí lúštiť. Vo vzdelávacích textoch a návodoch je zrozumiteľnosť dôležitejšia ako vtip. **Test:** Pochopí čitateľ obraz na prvé prečítanie, bez vysvetlenia? Keď nie, napíš obyčajne, čo sa deje.

**Pred → Po:** názov poľa „Pozor, barlička“ → „AI to vie, ja nie“; „AI má každý deň prvý deň.“ → „AI každé ráno začína od nuly.“; „Obraz na celé popoludnie“ → „Prirovnanie, ku ktorému sa budeme vracať“; „Práca hustne.“ → „Práce pribúda.“

Obraz, ktorý text sám zavedie a vysvetlí (metafora domu, mapy), je v poriadku. Zaveď ho raz na svojom mieste, potom píš vecne a obraz s opisom nestriedaj.

### 43. Citácie cudzojazyčných autorov

Anglický citát nechaj v origináli a pridaj slovenský prevod zmyslu. Slovosled ani interpunkciu citátu neupravuj. Cituj buď presne, alebo parafrázuj bez úvodzoviek. Doslovný slovenský preklad v úvodzovkách nevydávaj za autorove slová.

### 44. Prevzaté prompty

**Problém:** Prompty z knižníc a z internetu bývajú preložené z angličtiny a nesú jej obraty. Keď prompt ide do materiálu pre ľudí (pracovný list, snímka, knižnica promptov, ukážka v článku), je to text pre čitateľa a kontroluje sa podľa tejto časti ako každý iný. Model kostrbatej slovenčine porozumie, ale človek, ktorý si prompt číta, upravuje a posiela ďalej, sa v nej stratí.

**Pred → Po:** „Buď intelektuálne agresívny.“ → „V argumentoch buď neúprosný.“; „Tvoja hodnota spočíva v tom, že…“ → „Najviac mi pomôžeš, keď…“; „Pamätaj: mojím cieľom nie je vyhrať diskusiu, ale…“ → „Nejde mi o víťazstvo v diskusii. Chcem…“; „Prinúť ma premýšľať hlbšie.“ → „Prinúť ma premyslieť si to do hĺbky.“; „Čo potrebuješ na vstupe?“ → „Čo na to potrebuješ?“; „Uisti sa, že odpoveď má tri body.“ → „Odpoveď nech má tri body.“

### 45. Anglická stavba vety v krátkych textoch

**Kde hľadať:** popisy na obrázkoch a v diagramoch, otázky, titulky, názvy snímok a častí, názvy polí v tabuľkách a pracovných listoch, texty tlačidiel, zadania pre iné nástroje.
**Problém:** Veta má slovenské slová a správnu gramatiku, ale poskladaná je po anglicky. V dlhšom odseku sa to stratí, v piatich slovách na snímke to znie cudzo. Typické znaky: sloveso „platiť“ alebo „byť“ na konci podľa vzoru *what's true about…*, reťaz predložkových väzieb, privlastňovacie zámená navyše, prídavné mená prevzaté z opisu vizuálu (*flat, clean*), nadpisy podľa vzoru *Why it matters*. **Test:** Prečítaj každý krátky text osobitne a nahlas. Opýtal by sa takto človek pri káve? Keď zaváhaš, je to kalk. Prepisuj od významu, nie od pôvodných slov: na čo sa tým človek naozaj pýta?

**Pred → Po:** „Čo o mne a mojom biznise platí?“ → „Kto som a pre koho pracujem?“; „Čo chcem práve teraz?“ → „Čo teraz potrebujem?“; „Prečo na tom záleží“ → „Prečo je to dôležité“; „plochá, čistá ilustrácia“ → „jednoduchá plošná kresba“; „Na voľbe záleží menej ako na tom, že je jedno“ → „Ktoré si vyberiete, je vedľajšie. Hlavne nech je len jedno“. **Pozor na dvojznačnosť:** krátka veta nemá kontext, ktorý by ju zachránil. „Že je jedno“ sa dá čítať aj ako „nezáleží na tom“.

### Čo kalk nie je

Zdomácnené prevzaté slová (prototyp, dizajn, workshop), zaužívané termíny odboru, názvy metód a produktov, ak ich publikum pozná alebo ich používa autor či organizácia (design brief, stakeholder mapa). Tie sa neprekladajú. V textoch pre začiatočníkov však daj prednosť slovenčine tam, kde existuje obyčajné slovenské slovo: agenda → program, FAQ → najčastejšie otázky, use case → príklad využitia, onboarding → zaškolenie, benefit → výhoda. Anglický termín, ktorý v texte zostane, vysvetli pri prvom výskyte. Pri pochybnostiach sa opýtaj.

Neopravuj ani spojenia, ktoré Jazyková poradňa JÚĽŠ hodnotí ako bežné slovenské: *dávať zmysel* a *výzva* vo význame náročnej úlohy (*challenge*). Pri nahromadení ich len obmeň.

### Kalky vo formuláciách autora

Keď text obsahuje doslovné formulácie autora (citácie z jeho poznámok, ustálené vety, vety, ktoré autor nechce meniť) a je v nich kalk, neprepisuj ho potichu. Uveď ho v prehľade ako návrh (Pred → Po a prečo) a rozhodnutie nechaj na autora. Text, ktorý ti používateľ dal na úpravu, opravuj normálne.

### Kontrola kalkov (postup)

Kontrola kalkov je samostatný krok, ktorý sa robí na hotovom texte. Nerobí sa „pri písaní“ a nenahrádza ho skript ani dojem, že text znie dobre.

1. **Vypíš všetko, čo uvidí čitateľ:** bežný text, nadpisy a nadtitulky, popisy obrázkov a polí, otázky, texty tlačidiel, prevzaté prompty a citácie v preklade. Patria sem aj texty mimo hlavného dokumentu: online tabule (Miro a podobne), formuláre, sprievodný e-mail.
2. **Načítaj slovník** `references/kalky.md`. Keď bol kontext skrátený a nemáš istotu, že vidíš celý skill aj slovník, načítaj ich znova.
3. **Spusti skript, ak môžeš spúšťať kód:** `python3 <priečinok skillu>/scripts/najdi_kalky.py <súbor>`. Každý nález posúď, pretože rovnaké slovo môže byť v inom spojení v poriadku. Výsledok „0 nálezov“ znamená len to, že v texte nie sú kalky ani bohemizmy zo slovníka.
4. **Čítaj vetu po vete.** Pri každom slovese a podstatnom mene si polož kontrolnú otázku, urob spätný test a prejdi mechanizmy 36 – 45 aj bohemizmy (č. 17). Krátke texty čítaj jednotlivo a nahlas.
5. **Prejdi rady:** nadpisy jednej úrovne, body zoznamu, polia tabuľky. Celý rad má jeden tvar.
6. **Zapíš tabuľku** Pred | Po | Prečo ku každému zmenenému miestu. Do „Prečo“ uveď anglickú alebo českú predlohu, ak nejaká je (kalk z *on a daily basis*, bohemizmus z *jedná se o*).

---

# DETEKCIA: ČO NEHLÁSIŤ (falošné poplachy)

Kvalitný ľudský text môže vykazovať niekoľko vzorcov uvedených vyššie. Pred prepisom si over, že nekazíš legitímnu prózu. Samy osebe NIE SÚ spoľahlivými indikátormi:

- **Bezchybný pravopis a konzistentný štýl.** Mnohí autori sú profesionáli alebo ich text prešiel korektúrou.
- **Formálna slovná zásoba.** AI nadužíva KONKRÉTNE slová (č. 10), nie všetky knižné slová. „Avšak“ raz za text nie je znak AI.
- **Jedna pomlčka, jedna trojica, jedno „kľúčový“.** Hľadaj ZHLUKY znakov, nie izolované výskyty. Jedna pomlčka nič neznamená. Pomlčky, pravidlo troch, „pulzujúca tapiséria“ a generický záver spolu sú priznanie.
- **Slovenské úvodzovky a správna typografia.** Pozor na obrátenú logiku: v slovenčine je správna typografia („ “, – s medzerami, 5 %) znakom starostlivého autora ALEBO dobre nastaveného nástroja. Znakom AI sú anglické návyky (“ ”, —, Title Case).
- **Krátka úderná veta.** Ľudia ňou zakončujú pointu. Hlás až sériu fragmentov.
- **Odborný žargón.** „Robustné riešenie“ od vývojára môže byť termín. Pri pochybnostiach sa opýtaj.
- **Pojmy z grantového a hodnotiaceho formulára.** Cieľová skupina, realizácia, priame a nepriame náklady, „predstavuje N % nákladov“ či názvy výstupov a položiek rozpočtu sú jazyk žánru, ktorému komisia rozumie. Neprepisujú sa.
- **Text v úvodzovkách, názvy, príklady.** Sledovaná fráza vnútri citácie alebo tam, kde sa o nej hovorí (namiesto toho, aby sa používala), sa neprepisuje.
- **Slová, ktoré vyzerajú česky, ale sú spisovné.** Nie všetko spoločné s češtinou je bohemizmus. Pri pochybnostiach rozhoduje Krátky slovník slovenského jazyka, nie pocit.

## Znaky ľudského písania (zachovať!)

Keď ich vidíš, nechaj prózu na pokoji. Nadmerná redakcia zničí to, čo ju robí ľudskou:

- Konkrétny, ťažko vymysliteľný detail (presná adresa, zvláštny citát, „právnička, čo sedávala nad ordináciou môjho zubára“).
- Zmiešané pocity a nevyriešené napätie („väčšinou sa mi to páči, ale niečo mi na tom prekáža a neviem povedať čo“).
- Dobové odkazy, slang, interné vtipy viazané na konkrétny rok a subkultúru.
- Striedanie krátkych a dlhých viet; skutočné vsuvky, zátvorky a opravy samého seba.
- Nárečové a regionálne prvky (východoslovenské, záhorácke, stredoslovenské) a hovorová slovenčina. NEOPRAVUJ ich na spisovné, ak sú konzistentnou súčasťou hlasu. Pri pochybnostiach sa opýtaj.

---

# PROCES A VÝSTUP

1. **Prečítaj celý vstup** a označ si všetky výskyty vzorcov vyššie. Zapíš si vecný obsah každého odseku (kontrolný zoznam informácií, nič sa nesmie stratiť).
2. **Zozbieraj sporné miesta** (pozri Kedy sa pýtať používateľa). Ak nejaké sú, polož otázky HNEĎ, pred písaním finálneho znenia. Ak je k dispozícii AskUserQuestion, použi ho; inak otázky vypíš a počkaj na odpoveď.
3. **Napíš pracovný prepis.** Skontroluj: číta sa nahlas prirodzene? Strieda dĺžky viet? Drží slovenské aktuálne členenie? Používa „je/má“ namiesto opisov? Drží register originálu? Nezostali v ňom bohemizmy?
4. **Audit:** polož si otázku „Čo na tomto texte stále kričí, že ho písala AI?“ a odpovedz stručne v bodoch.
5. **Kontrola obsahu podľa zoznamu z kroku 1:** každá informácia originálu je vo finálnom znení, nijaká nepribudla. Ak nie, oprav.
6. **Kontrola kalkov a bohemizmov** podľa postupu na konci časti E: zoznam všetkých textov pre čitateľa, slovník, skript, čítanie vetu po vete, rady v jednom tvare, tabuľka zmien. Tento krok sa nikdy nevynecháva, ani v časovej tiesni, a týka sa aj textov, ktoré si napísal sám a nijaký anglický zdroj nemajú.
7. **Finálny prepis:** odstráň zvyšné znaky AI, prejdi typografiu (úvodzovky „ “, pomlčky, medzery, percentá, dátumy, skratky). Vyhľadaj: (a) — em dash bez medzier a anglické úvodzovky “ ”. Akýkoľvek nález znamená, že finálne znenie nie je hotové; (b) spočítaj pomlčky s medzerami mimo rozsahov a intervalov (15. – 18. sa nepočíta). Viac než jedna na bežný text znamená, že finálne znenie nie je hotové: rozdeľ vety bodkou alebo ich spoj čiarkou (pozri č. 24).

**Odovzdaj:** finálny text + stručný prehľad vykonaných zmien (čo a prečo) + tabuľku kalkov a bohemizmov Pred | Po | Prečo + prípadný zoznam miest, kde si sa držal originálu napriek znaku AI (napr. autorská pomlčka, hovorový bohemizmus), aby mal používateľ kontrolu. Kalky vo formuláciách autora uveď osobitne ako návrhy.

Pri snímkach, obrázkoch a zadaniach pre iné nástroje prilož zoznam všetkých krátkych textov (popisy, otázky, titulky), ktoré si kontroloval, každý na samostatnom riadku. Tvrdenie „prešlo humanizerom“ bez tohto zoznamu neplatí.

---

# UKÁŽKOVÝ PRÍKLAD

**Pred (AI slovenčina):**
> V dnešnej rýchlej digitálnej dobe predstavuje umelá inteligencia kľúčový nástroj pre neziskové organizácie. Nejde len o technológiu — ide o zásadnú zmenu spôsobu práce. AI ponúka celú radu benefitov: efektivitu, inováciu a úsporu času. “Experti sa zhodujú,” že organizácie, ktoré AI nevyužívajú, zaostávajú. Poďme sa pozrieť na to, ako môže AI transformovať vašu organizáciu, vaše procesy a vašu komunikáciu. Budúcnosť vyzerá sľubne! 🚀

**Otázky pred finálnym znením:**
1. Veta „Budúcnosť vyzerá sľubne!“ nenesie vecnú informáciu. Vypustiť, alebo ponechať vecnejšie formulovanú?
2. „Experti sa zhodujú“ nemá v texte zdroj. Mám formuláciu zmierniť na všeobecné tvrdenie, alebo zdroj doplníš?
3. Emoji 🚀: odstrániť, alebo je súčasťou tvojho štýlu pre tento kanál?

**Po (za predpokladu odpovedí: 1 vypustiť, 2 zmierniť, 3 odstrániť):**
> Umelá inteligencia je pre neziskové organizácie dôležitý nástroj a mení spôsob, akým pracujú. Prináša úsporu času a vyššiu efektivitu, a tiež inovácie. Organizácie, ktoré ju nevyužívajú, zaostávajú. AI môže zmeniť organizáciu, jej procesy aj komunikáciu.

**Vykonané zmeny:** odstránený slovník AI (v dnešnej digitálnej dobe, kľúčový, zásadný), negatívny paralelizmus (nejde len o…), em dash, anglické úvodzovky, bohemizmus „celú radu“ a anglicizmus „benefitov“, pravidlo troch rozbité so zachovaním všetkých troch položiek, metakomentár (poďme sa pozrieť), kalk privlastňovacích zámen (vašu/vaše), vágna autorita zmiernená na priame tvrdenie podľa odpovede používateľa, generický záver a emoji vypustené podľa odpovede používateľa. Všetok vecný obsah je zachovaný.

---

# REFERENCIE

- **Pravidlá slovenského pravopisu** (4. vyd., 2013) a **Krátky slovník slovenského jazyka** (4. vyd., 2003): kodifikačné príručky JÚĽŠ SAV pre pravopis a spisovnú slovnú zásobu.
- **Slovníkový portál JÚĽŠ SAV** (slovnik.juls.savba.sk): online prístup ku kodifikačným príručkám a slovníkom vrátane Slovníka súčasného slovenského jazyka.
- **Jazyková poradňa JÚĽŠ SAV** (juls.savba.sk/poradna.html, databáza odpovedí jazykovaporadna.sme.sk): riešené sporné prípady vrátane bohemizmov a anglicizmov.
- **STN 01 6910:2023** Pravidlá písania a úpravy písomností: typografické pravidlá (medzery, dátumy, čísla, značky).
- **`references/kalky.md`**: slovník kalkov z angličtiny a bohemizmov k časti E a vzorcu č. 17; **`scripts/najdi_kalky.py`** podľa neho označí podozrivé miesta v texte.
- Vzorce písania AI vychádzajú zo stránky Signs of AI writing na anglickej Wikipédii (WikiProject AI Cleanup) a zo skillu blader/humanizer. Slovenská verzia nadväzuje na český Humanizer CZ (katerina-svi/katerinas-humanizer-cz).
