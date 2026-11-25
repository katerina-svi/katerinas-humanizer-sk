# Slovník kalkov z angličtiny a bohemizmov

Pomocný slovník k časti E a vzorcu č. 17 skillu humanizer-sk. Zbiera kalky a české tvary, ktoré sa v slovenských textoch písaných pomocou AI opakujú najčastejšie, roztriedené podľa mechanizmov z časti E.

**Ako slovník používať**

- Náhrady sú ponuka, nie povinnosť. Vyber tú, ktorá zachováva význam originálu. Keď nesedí nijaká, prestavaj celú vetu od významu.
- Rovnaké slovo môže byť v inom spojení v poriadku („vstup do budovy“, „výstup projektu“ v grantovej žiadosti). Rozhoduje kontext a kontrolná otázka z časti E.
- Slovník nie je úplný. Kalk, ktorý v ňom nie je, spoznáš podľa mechanizmu (časť E, č. 36 – 45).
- Stĺpec **Predloha** uvádza anglický výraz, z ktorého kalk vznikol. V časti 9 je v ňom český tvar (čes.).
- Stĺpec **Hľadať** je regulárny výraz pre skript `scripts/najdi_kalky.py`. Zvislá čiara vnútri výrazu je kvôli tabuľke zapísaná ako `\|`. Položky s textom „ručne“ sa strojovo hľadať nedajú a hľadajú sa len čítaním.

**Obsah**

1. Frazeológia a slovesné väzby (č. 37)
2. Zradné a preťažené slová, falošní priatelia (č. 38)
3. Vec ako činiteľ (č. 39)
4. Skladanie podstatných mien (č. 40)
5. Doslovne preložené termíny a obrazy (č. 36, 42)
6. Prevzaté prompty (č. 44)
7. Krátke texty a výzvy (č. 41, 45)
8. Anglicizmy, ktoré začiatočníkom nič nepovedia
9. Bohemizmy a české tvary (č. 17)

## 1. Frazeológia a slovesné väzby

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| na dennej báze, na pravidelnej báze | *on a daily / regular basis* | denne, každý deň, pravidelne | `na (?:dennej\|týždennej\|mesačnej\|pravidelnej\|ročnej\|individuálnej\|dobrovoľnej) báze` |
| adresovať problém | *address an issue* | riešiť, zaoberať sa, venovať sa; adresovať sa dá list | `adres\w* (?:\w+ )?(?:problém\|otázk\|tém\|potreb\|výzv\|rizik\|nedostat\|obav)\w*` |
| mať dopad na | *have an impact on* | ovplyvniť, mať vplyv na, dosah, účinok | `\bdopad(?:u\|y\|om\|ov\|e\|mi\|och)?\b` |
| urobiť rozdiel | *make a difference* | zmeniť, pomôcť, mať význam; „robiť rozdiel medzi“ je v poriadku | `\b(?:urob\w*\|rob\w*) (?:veľký \|zásadný \|obrovský )?rozdiel\b(?! medzi)` |
| robí to zmysel | *makes sense* | má to zmysel, je to logické; „dáva zmysel“ je v slovenčine v poriadku | `\brob\w*(?: to)? zmysel\b\|zmysel rob\w*` |
| byť na rovnakej stránke | *be on the same page* | zhodnúť sa, mať rovnaké informácie | `na (?:rovnakej\|tej istej) stránke` |
| na konci dňa | *at the end of the day* | nakoniec, v konečnom dôsledku; v doslovnom význame (večer) je v poriadku | `na konci dňa` |
| je to o tom, že | *it's about* | ide o to, že; rovno tvrdenie | `je to o tom` |
| stretnúť očakávania | *meet expectations* | splniť očakávania | `stret\w* (?:\w+ )?očakávani\w*` |
| zdieľať myšlienku, postreh | *share a thought* (aj čes. *sdílet*) | podeliť sa o, povedať, vymeniť si; zdieľaný priečinok je termín | `\bzdieľ\w*` |
| byť v poriadku s tým | *be OK with* | neprekáža mi, súhlasím | `v poriadku s tým\b` |
| Tu je, čo…; Tu je, ako… | *Here's what / how…* | Takto…; rovno obsah | `\btu je,? (?:čo\|ako\|prečo\|kde)\b` |
| obsah žije v… | *lives in* | je uložený v, je len v | `(?:obsah\w*\|dáta\|dát\|údaj\w*\|know-how\|znalost\w*\|informáci\w*\|podklad\w*\|súbor\w*) (?:\w+ )?žij\w*` |
| drží podklady, kontext | *holds* | má, sú v ňom, uchováva | `drž\w* (?:\w+ )?(?:podklad\|kontext\|histór\|dát\|údaj\|informáci\|súbor\|dokument\|pamä)\w*` |
| pokrýva | *covers* | vzťahuje sa na, zahŕňa, rieši; „pokryť náklady“ je v poriadku | `\bpokrýv\w*\|\bpokry(?:je\|jú\|l\|la\|lo\|li\|ť)\b` |
| fungovalo na (téme) | *worked on* | osvedčilo sa pri, vyskúšané na | `fungoval\w* na\b` |
| robiť rozhodnutia | *make decisions* | rozhodovať (sa), rozhodnúť (sa) | `\b(?:urob\|rob)\w* (?:\w+ )?rozhodnut\w*` |
| premýšľať hlbšie | *think more deeply* | premyslieť do hĺbky | `(?:premýšľ\|rozmýšľ)\w* (?:\w+ )?hlbšie` |
| byť schopný + neurčitok | *be able to* | vie, dokáže, môže; posudzuj pri nahromadení | `\b(?:je\|sú\|bol\w*\|byť\|bude\w*) schopn\w+ \w+ť\b` |
| odprezentovať | *present* | predstaviť, ukázať, prezentovať | `odprezent\w*` |
| publikovať (na webe, na sieťach) | *publish, post* | zverejniť; publikovať článok v časopise je v poriadku | `publik(?:ova\|uj)\w*` |
| vziať si z toho | *take away* | odniesť si, naučiť sa; „vziať si z toho poučenie“ je v poriadku | ručne |
| konflikt beží | *is ongoing* | trvá, prebieha | ručne |

## 2. Zradné a preťažené slová, falošní priatelia

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| výstup | *output* | výsledok, odpoveď, hotový text; „výstup projektu“ v grante je termín | `\bvýstup(?:om\|och\|u\|y\|ov\|e)?\b` |
| vstup, na vstupe | *input* | podklady, zadanie, čo na to potrebuje | `\bna vstupe\b\|\bvstup(?:om\|y\|ov)\b` |
| kontext (mimo pojmu AI) | *context* | súvislosti, podklady, znalosť prostredia | `\bkontext\w*` |
| dve cesty, cesta, ako… | *two ways, a way to* | dva spôsoby, možnosť, variant | `(?:dve\|tri\|štyri\|päť\|iné\|ďalšie\|rôzne\|obe\|nové) cesty\b\|\bcest[au],? ako\b\|\b(?:iná\|ďalšia\|tretia\|druhá) cesta\b` |
| signál | *signal* | znak, náznak, varovanie | `\bsignál\w*` |
| rovnaká logika | *the same logic* | rovnaký princíp, rovnako uvažovať | `(?:rovnak\w*\|ist\w*\|túto\|táto\|inú\|iná) logik\w*` |
| naprieč | *across* | vo všetkých, v celej, medzi | `\bnaprieč\b` |
| inštrukcie | *instructions* | pokyny | `\binštrukci\w*` |
| interakcia | *interaction* | rozhovor, otázka, výmena | `\binterakci\w*` |
| zariadenie | *device* | notebook, telefón, počítač | ručne |
| existovať („čo po bloku existuje“) | *exist* | mať hotové, byť | ručne |
| halucinácie (v texte pre laikov) | *hallucination* | vymýšľanie, AI si vymýšľa | `halucin\w*` |
| rodina modelov | *model family* | modely jedného radu | `rodin\w* (?:\w+ )?model\w*` |
| agenda porady | *agenda* | program; úradná agenda je v poriadku | `\bagend\w*` |
| kotvy škály | *scale anchors* | čo znamenajú jednotlivé čísla | `kotv\w* (?:\w+ )?škál\w*` |
| krajina AI nástrojov | *landscape* | prehľad, ponuka, trh | `krajin\w* (?:\w+ )?(?:AI\|nástroj\|technológi\|startup\|trh)\w*` |
| rezonovať | *resonate* | osloviť, sadnúť, zaujať | `rezon\w*` |
| trenie v procese | *friction* | zdržanie, prekážka, spomaliť; fyzikálne trenie je v poriadku | `\btreni\w*` |
| je svedectvom | *is a testament to* | dokladá, ukazuje | `(?:je\|sú) svedectvom` |
| tapiséria | *tapestry* | vypustiť, povedať vecne | `tapiséri\w*` |
| eventuálne (vo význame „nakoniec“) | *eventually* | nakoniec, časom; eventuálne = prípadne | `\beventuáln\w*` |
| realizovať si (vo význame „uvedomiť si“) | *realize* | uvedomiť si, pochopiť | `\brealiz\w* si\b\|\brealizoval\w*,? že\b` |
| evidencia (vo význame „dôkazy“) | *evidence* | dôkazy, doklady, údaje; evidencia = záznamy, register | `\bevidenci\w*` |
| dedikovaný | *dedicated* | vyhradený, určený, venuje sa len tomu | `\bdedikovan\w*` |
| kontrolovať (vo význame „ovládať“) | *control* | ovládať, riadiť | ručne |
| aktuálne (vo význame „v skutočnosti“) | *actually* | v skutočnosti, vlastne | ručne |

## 3. Vec ako činiteľ

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| žiadosť píše, štúdia píše | *the application says* | v žiadosti sa píše, v štúdii sa uvádza; „kniha hovorí o…“ je v poriadku | `(?:žiadosť\w*\|štúdi[ae]\|dokument\w*\|správ[ay]\|článok\|text) píše\b` |
| odporúčanie zakazuje | *the guideline forbids* | podľa odporúčania je zakázaný | `(?<!vo )(?<! v )odporúčani\w* (?:\w+ ){0,2}(?:zakazuje\|hovorí\|chce)\b` |
| dáta nie sú pokyny | *data is not instructions* | prestavať: kto s dátami čo robí | ručne |
| účet dostane nové heslo | *the account gets* | pri účte si zmeňte heslo | ručne |
| know-how žije v chatoch | *lives in* | je len v chatoch | pozri časť 1, „obsah žije v“ |

## 4. Skladanie podstatných mien

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| AI stratégia | *AI strategy* | stratégia AI, stratégia práce s AI | `\bAI stratégi\w*` |
| AI transformácia | *AI transformation* | zavádzanie AI, premena práce s AI | `\bAI transformáci\w*` |
| AI vzdelávanie | *AI education* | vzdelávanie o AI, kurzy práce s AI; ak je to ustálený názov služby alebo kurzu, ponechaj | `\bAI vzdelávani\w*` |
| AI recenzent | *AI reviewer* | AI, ktorú používa recenzent (alebo naopak, podľa zmyslu) | `\bAI recenzent\w*` |
| strategický konzultant (ako odbor) | *strategy consultant* | konzultant pre stratégiu | `strategick\w+ konzultant\w*` |
| ľudská pripravenosť | *human readiness* | pripravenosť ľudí | `ľudsk\w+ pripravenos\w*` |
| dátovo riadený | *data-driven* | podložený dátami, rozhodovať sa podľa dát | `dátovo (?:riaden\|orientovan)\w*` |
| phishing napísaný s AI | *AI-written phishing* | podvodný e-mail, ktorý napísala AI | ručne |

## 5. Doslovne preložené termíny a obrazy

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| prvé princípy | *first principles* | základné princípy, premyslieť od základu | `\bprv\w+ princíp\w*` |
| intelektuálne agresívny | *intellectually aggressive* | v argumentoch neúprosný | `intelektuálne agresívn\w*` |
| ilúzia plynulosti | *fluency illusion* | ilúzia porozumenia | `ilúzi\w* plynulos\w*` |
| prostredník z mäsa | *meat proxy* | nechať *meat proxy* a vysvetliť | `prostredník\w* z mäsa` |
| vlastníctvo | *ownership* | ručiť za výsledok, vziať si vec za svoju; vlastníctvo majetku je v poriadku | `\bvlastníctv\w*` |
| polymat | *polymath* | všestrannosť, široký rozhľad, polyhistor | `\bpolymat\w*` |
| profil T | *T-shaped* | v jednom odbore do hĺbky a k tomu rozhľad | `profil\w* T\b` |
| balíček kontextu | *context pack* | podklady | `balíč\w* kontext\w*` |
| kognitívna technológia, technológia na myslenie | *cognitive technology* | opísať vetou, čo sa s myslením deje | `kognitívn\w* technológi\w*\|technológi\w* (?:pre\|na) myslenie` |
| holý ChatGPT | *vanilla, bare* | ChatGPT bez úprav, v základnom nastavení | `\bhol\w+ (?:ChatGPT\|Gemini\|Claude\w*\|Copilot\w*\|model\w*\|chatbot\w*)` |
| ťažba dát (o vytiahnutí údajov z dokumentu) | *data mining* | vytiahnuť údaje; dolovanie dát je hľadanie vzorov a súvislostí vo veľkých dátach | `ťažb\w* (?:dát\|údajov)` |
| človek v procese | *human in the loop* | kedy výsledok kontroluje človek | `človek\w* v (?:procese\|slučke)\|human in the loop` |
| barlička (ako nálepka) | *crutch* | opísať, čo sa deje („AI to vie, ja nie“) | `barličk\w*` |
| má každý deň prvý deň | *every day is day one* | každé ráno začína od nuly | `každý deň (?:prvý\|nový) deň` |
| práca hustne | *the work thickens* | práce pribúda | `\bhustn\w*\|\bhustne\b` |

## 6. Prevzaté prompty

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| Pamätaj: | *Remember:* | rovno pravidlo bez úvodu | `\bpamätaj(?:te)?\s*:` |
| Tvoja hodnota spočíva v tom | *Your value lies in* | Najviac mi pomôžeš, keď | `hodnota spočíva` |
| Uisti sa, že… | *Make sure that…* | Dbaj, aby…; Skontroluj, či…; mimo promptov je „uistiť sa“ v poriadku | `uisti(?:te)? sa,? že` |
| Buď intelektuálne agresívny | *Be intellectually aggressive* | pozri časť 5 | pozri časť 5 |
| na vstupe, výstup | *input, output* | pozri časť 2 | pozri časť 2 |

## 7. Krátke texty a výzvy

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| Otázky vítané. | *Questions welcome.* | Pýtajte sa. | `otázky (?:sú )?vítané` |
| Čo o mne platí? | *What's true about me?* | Kto som…?; prepísať od významu | `\bčo (?:o \w+ )?(?:\w+ ){0,3}platí\?` |
| Prečo na tom záleží | *Why it matters* | Prečo je to dôležité | `prečo na tom záleží` |
| Kľúčové poznatky | *Key takeaways* | Čo si odniesť, Zhrnutie | `kľúčov\w+ (?:poznatk\|zisten\|myšlienk)\w*` |
| Do chatu: vaša veta. | *In the chat: your sentence.* | Napíšte do chatu svoju vetu. | ručne |
| Celá cesta na jednej snímke | *The whole journey on one slide* | metakomentár, povedať rovno obsah | ručne |

## 8. Anglicizmy, ktoré začiatočníkom nič nepovedia

Odborníci ich bežne používajú. V textoch pre začiatočníkov a laikov daj prednosť slovenčine, v odbornom texte ich posúď podľa publika.

| Kalk | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| use case | *use case* | príklad využitia, riešený príklad, prípad použitia | `\buse[- ]?cas\w*` |
| onboarding | *onboarding* | zaškolenie, adaptácia nového zamestnanca, v aplikácii úvodný sprievodca | `\bonboarding\w*` |
| FAQ | *FAQ* | najčastejšie otázky | `\bFAQ\b` |
| tone of voice | *tone of voice* | tón, akým píšeme | `tone of voice` |
| workflow | *workflow* | pracovný postup | `\bworkflow\w*` |
| deadline | *deadline* | termín, uzávierka | `\bdeadlin\w*` |
| feedback | *feedback* | spätná väzba | `\bfeedback\w*` |
| insight | *insight* | zistenie, postreh | `\binsight\w*` |
| benefit | *benefit* | výhoda, prínos | `\bbenefit\w*` |
| meeting, míting | *meeting* | stretnutie, porada | `\bmeeting\w*\|\bmíting\w*` |
| event | *event* | podujatie | `\bevent(?:y\|ov\|u\|e\|om\|och\|mi)?\b` |
| content | *content* | obsah | `\bcontent\w*` |

## 9. Bohemizmy a české tvary

Jazykové modely do slovenčiny potichu prenášajú češtinu (vzorec č. 17). V hovorovom texte môže byť bohemizmus zámer autora; vtedy ho nechaj a uveď v prehľade zmien.

| Bohemizmus | Predloha | Po slovensky skôr | Hľadať |
|---|---|---|---|
| jedná sa o, o čo sa jedná | *čes. jedná se o* | ide o, o čo ide | `\b(?:ne)?jedn(?:á\|ajú\|al\|ala\|alo\|ali\|ať) sa\b\|\bsa (?:ne)?jedn(?:á\|alo)\b` |
| jednať (o niečom), jednanie | *čes. jednat, jednání* | rokovať, rokovanie | `\bjednan\w*\|\bjedna(?:ť\|l\|la\|li\|lo)\b` |
| zabývať sa (čím) | *čes. zabývat se* | zaoberať sa; „zabývať sa v byte“ (udomácniť sa) je v poriadku | `\bzabýv\w*` |
| doporučiť, doporučenie | *čes. doporučit* | odporučiť, odporúčanie; doporučený list je v poriadku | `\bdoporuč\w*` |
| previesť kontrolu, analýzu | *čes. provést* | vykonať, urobiť | `\bprev(?:ádz\|ied\|iesť\|edie\|edú\|eď)\w* (?:\w+ )?(?:kontrol\|analýz\|registráci\|test\|meran\|výskum\|prieskum\|úprav\|zmen\|školen\|audit)\w*` |
| behom | *čes. během* | počas; behom (od slova beh) je v poriadku | `\bbehom\b` |
| akonáhle | *čes. jakmile* | len čo | `\bakonáhle\b` |
| nakoľko (príčina) | nespisovné príčinné použitie, nie z češtiny | keďže, pretože; „nakoľko“ = do akej miery je v poriadku | `\bnakoľko\b` |
| kľud, kľudne | *čes. klid, klidně* | pokoj, pokojne | `\bkľud\w*` |
| vypadá, vypadal | *čes. vypadá* | vyzerá, vyzeral | `\bvypad(?:á\|ajú\|al\|ala\|alo\|ali\|ať\|áš\|ám\|áme\|áte)\b` |
| záleží na (závislosť) | *čes. záleží na* | závisí od; „záleží mi na tom“ je v poriadku | `\bzálež\w* na\b` |
| vzhľadom k | *čes. vzhledem k* | vzhľadom na | `\bvzhľadom k\b` |
| obdržať | *čes. obdržet* | dostať | `\bobdrž\w*` |
| zahájiť | *čes. zahájit* | začať, otvoriť | `\bzaháj\w*` |
| prehlásiť, prehlásenie | *čes. prohlásit* | vyhlásiť, vyhlásenie; prehlásiť trvalý pobyt je v poriadku | `\bprehlás\w*\|\bprehlas\w*` |
| dotaz | *čes. dotaz* | otázka; dotazník je v poriadku | `\bdotaz\b\|\bdotaz(?:u\|y\|om\|ov\|e\|mi\|och)\b` |
| naviac | *čes. navíc* | navyše | `\bnaviac\b` |
| tým pádom | *čes. tím pádem* | teda, tak | `\btým pádom\b` |
| každopádne | *čes. každopádně* | v každom prípade | `\bkaždopádne\b` |
| zrovna | *čes. zrovna* | práve | `\bzrovna\b` |
| dielčí | *čes. dílčí* | čiastkový | `\bdielč\w*` |
| chovanie, chovať sa (o ľuďoch) | *čes. chování* | správanie, správať sa; chov zvierat je v poriadku | `\bchovan\w*\|\bchov(?:á\|ajú\|al\|ala\|ali\|ať) sa\b` |
| merítko | *čes. měřítko* | mierka, meradlo | `\bmerít\w*` |
| tlačítko | *čes. tlačítko* | tlačidlo | `\btlačít\w*` |
| zložka (v počítači) | *čes. složka* | priečinok; zložka ako súčasť je v poriadku | `\bzlož(?:ka\|ky\|ke\|ku\|kou\|iek\|kách\|kami)\b` |
| rada výhod, celá rada | *čes. řada* | rad, množstvo, viacero | `\bcel(?:á\|ú\|ej\|ou) rad(?:a\|u\|y\|e\|ou)\b\|\brad(?:a\|u\|ou) (?:\w+ )?(?:výhod\|možnost\|funkci\|nástroj\|otáz\|problém\|projekt\|krok\|oblast)\w*` |
| viď | *čes. viz* | pozri | `\bviď\b` |
| pokiaľ (podmienka) | *čes. pokud* | ak; nahrádzaj len pri nahromadení | `\bpokiaľ\b` |
| stávajúci | *čes. stávající* | terajší, doterajší, existujúci | `\bstávajúc\w*` |
| snadný, snadno | *čes. snadný* | ľahký, jednoduchý, ľahko | `\bsnadn\w*` |
| úkol | *čes. úkol* | úloha | `\búkol\w*` |
| zbytok | *čes. zbytek* | zvyšok; zbytočný je v poriadku | `\bzbyt(?:ok\|ku\|kom\|ky\|kov\|koch\|kami)\b` |
| odpovedá skutočnosti, odpovedajúci | *čes. odpovídá* | zodpovedá, zodpovedajúci | `\bodpovedajúc\w*\|\bodpoved(?:á\|ajú\|al\|alo\|ala\|ali) (?:\w+ )?(?:očakávani\|skutočnost\|realit\|požiadavk\|norm\|predstav\|potreb\|kritéri\|zadani)\w*` |
| pečlivý, pečlivo | *čes. pečlivý* | starostlivý, dôkladný, dôkladne | `\bpečliv\w*` |
| brať v potaz | *čes. brát v potaz* | brať do úvahy, zohľadniť | `\bv potaz\b` |
| mimo to (okrem toho) | *čes. mimo to* | okrem toho | `\bmimo (?:to\|toho)\b` |
| pomocí, pomoci nástroja | *čes. pomocí* | pomocou | `\bpomocí\b\|(?<!bez )\bpomoci (?:AI\|nástroj\w*\|aplikáci\w*\|program\w*\|funkci\w*\|model\w*)` |
| v návaznosti | *čes. v návaznosti* | v nadväznosti, nadväzovať | `\bnávaz\w*` |
| výjimka | *čes. výjimka* | výnimka | `\bvýjim\w*` |
| prevážne | *čes. převážně* | prevažne | `\bprevážn\w*` |
| atd. | *čes. atd.* | atď. | `\batd\.` |
| apod. | *čes. apod.* | a pod. | `\bapod\.` |
| tj. | *čes. tj.* | t. j. | `\btj\.` |
| např. | *čes. např.* | napr. | `\bnapř\.` |
| popř. | *čes. popř.* | príp., prípadne | `\bpopř\.` |
| mj. | *čes. mj.* | okrem iného | `\bmj\.` |
| slovo s ě, ř alebo ů | *čeština* | slovenský tvar; vlastné mená (Jiří) nechaj | `\b\w*[ěřůĚŘŮ]\w*\b` |
