# Zoznam zmien

Všetky podstatné zmeny skillu Humanizer SK. Verzie sa číslujú podľa [sémantického verziovania](https://semver.org/).

## 1.0.0

Obsahovo zosúladené s českou verziou Humanizer CZ 2.0.0 a doplnené o slovenské špecifiká.

### Pridané

- **Blok E: kalky z angličtiny** (vzorce 36 – 45). Kalky sú roztriedené podľa mechanizmu, ako vznikajú: doslovne preložené termíny a metafory, anglická frazeológia („na dennej báze“, „adresovať problém“, „mať dopad na“), zradné a preťažené slová vrátane falošných priateľov („výstup“, „vstup“, „eventuálne“ za *eventually*, „evidencia“ za *evidence*), vec ako činiteľ („Projekt drží podklady“), anglické skladanie podstatných mien („AI stratégia“), menné nadpisy a nejednotné rady, obrazy bez slovenskej opory, citácie, prevzaté prompty („Pamätaj:“) a anglická stavba vety v krátkych textoch. Každý mechanizmus má testovaciu otázku a príklady Pred → Po.
- Upozornenie, že v slovenčine sa kalky miešajú s bohemizmami, pretože model často skladá vetu cez češtinu.
- Časť „Čo kalk nie je“ vrátane spojení, ktoré Jazyková poradňa JÚĽŠ hodnotí ako bežné slovenské (*dávať zmysel*, *výzva* vo význame *challenge*).
- Pevný postup kontroly kalkov so zoznamom všetkých textov pre čitateľa (aj mimo hlavného dokumentu) a tabuľkou Pred | Po | Prečo.
- Slovník `references/kalky.md`: vyše 120 kalkov a bohemizmov s predlohou, náhradou a regulárnym výrazom, v deviatich častiach podľa mechanizmov.
- Skript `scripts/najdi_kalky.py` (Python 3, bez závislostí): podľa slovníka vypíše podozrivé miesta s číslom riadka a typom (kalk alebo bohemizmus). Nič neopravuje.
- Prísne pravidlo č. 8: autorova formulácia je len to, čo autor naozaj napísal.
- Časť „Kontrola vlastného textu“ pre prípad, keď text napísal ten istý agent: samostatná kontrola finálneho znenia, kalky hneď pri prvej kontrole, skript nie je kontrola, povinný prehľad zmien, žiadne tiché rozhodovanie bez používateľa, prednosť štýlovej príručky autora.
- Kalibrácia hlasu: vzorka musí byť z rovnakého žánru.
- Výnimky: „predstavuje“ s podielom alebo sumou (č. 11), „Dajte mi vedieť“ v e-maile (č. 29), pojmy grantových a hodnotiacich formulárov (falošné poplachy).
- Č. 19: opačný smer chyby, teda hovorové tvary v spisovnom žánri (posudok, komentár pre komisiu).

### Zmenené

- Vzorec č. 17 (bohemizmy) rozšírený o nové výrazy (stávajúci, snadný, úkol, zbytok, zabývať sa, odpovedať vo význame zodpovedať, pečlivý, brať v potaz, mimo to, pomocí, návaznosť, prevážne), české skratky (atd., apod., tj., např., popř., mj.) a písmená ě, ř, ů. Medzi slová, ktoré nie sú bohemizmy, pribudli proste, akurát (hovorové) a dotazník.
- Z bohemizmov vyradené „pojednávať o“ (kniha pojednáva o… je bežná slovenčina). „Ohľadom“ a „ohľadne“ už nie sú medzi slovami, ktoré sa neopravujú: nie sú bohemizmy, ale v písanom texte sa nahrádzajú (č. 19). Pri „nakoľko“ je doplnené, že ide o nespisovné príčinné použitie, nie o tvar z češtiny.
- Č. 26: pribudlo pravidlo o slovenských skratkách (atď., a pod., t. j., napr.).
- Opis skillu (description) spomína kalky, bohemizmy a vymedzenie, kedy skill nepoužívať. V `allowed-tools` pribudlo spúšťanie skriptu (`Bash(python3:*)`).
- Krátke príklady v častiach A a B zhustené, aby telo `SKILL.md` zostalo do 500 riadkov.
- Jazyková redakcia celého skillu (napr. „nevynecháva obsah“ namiesto „neodoberá“, „finálne znenie“ namiesto „finále“, „Kontrola kalkov“). Príklad v č. 4 bez obratu „prešiel premenou“.
- Referencie: pribudol odkaz na Jazykovú poradňu JÚĽŠ SAV, slovník a skript; Wikipédia je uvedená so skloňovaným názvom.
- README: inštalácia pre Claude, Gemini, ChatGPT, Copilot, Claude Code, Skills CLI a ručne; odkaz na českú verziu.
- Šablóny issues: nové prostredia (Gemini, Copilot, Skills CLI).

### Na overenie rodenými hovoriacimi

Slovenčinu tejto verzie napísal jazykový model a skontroloval ju iný model, nie človek. Pripomienky prosím do [Issues](https://github.com/katerina-svi/katerinas-humanizer-sk/issues).

Opora nových pravidiel v Jazykovej poradni JÚĽŠ (databáza jazykovaporadna.sme.sk; overené len cez úryvky vo vyhľadávači, stránky sú za bezpečnostným overením prehliadača):

- *dávať zmysel* ako bežné spojenie: [q/10187](https://jazykovaporadna.sme.sk/q/10187/)
- *výzva* vo význame *challenge*: [q/5861](https://jazykovaporadna.sme.sk/q/5861/)
- *zdieľať* mimo IT nespisovné: [q/2334](https://jazykovaporadna.sme.sk/q/2334/), [q/8901](https://jazykovaporadna.sme.sk/q/8901/)
- *stávajúci* nespisovné: [q/8397](https://jazykovaporadna.sme.sk/q/8397/)
- *snadný* ako bohemizmus: [q/8394](https://jazykovaporadna.sme.sk/q/8394/)
- *proste*, *akurát* nie sú bohemizmy: [q/3347](https://jazykovaporadna.sme.sk/q/3347/)
- *dopad* vo význame vplyv, účinok: [q/9504](https://jazykovaporadna.sme.sk/q/9504/), [q/6430](https://jazykovaporadna.sme.sk/q/6430/)
- pomlčka v rozsahu s medzerami: [q/9931](https://jazykovaporadna.sme.sk/q/9931/) a PSP 2000, kap. Pomlčka
- *adresovať* tému či problém ako anglicizmus: [jazykové okienko TASR](https://www.teraz.sk/import/slovencina-aky-problem-adresuje-tent/398118-clanok.html)

## 0.9.0 (7. 10. 2026)

Prvá verejná verzia. 35 vzorcov pre slovenčinu, prísny režim, povinné otázky pri sporných miestach, tvrdý limit pomlčiek, výnimka pre výzvu na akciu v marketingových textoch, nové vzorce pre bohemizmy a vykanie.
