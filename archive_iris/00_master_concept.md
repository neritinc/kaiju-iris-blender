# 00 – KREATÍV BIBLIA: „IRIS SOVEREIGN”
**Lebegő, szimmetrikus mechanikus koponya + két tükrözött kibernetikus kéz · gyöngyház-króm és sötét anodizált panelek · zöld lézerlegyezők, magenta kúpok, cián pásztázók · sűrű volumetrikus füst · fekete tükörpadló · Excision / Subtronics szintű festival-VJ vizuál**

> Szerző: 00-concept-visionary (Concept Visionary / CGI Art Director), 2026-11-12
> Címzettek: 02-art-director, 03-modeler, 04-lookdev-artist, 05-lighting-artist, 06-animator
> Forrás: `pipeline/01_analysis.md`, `pipeline/01_visual_breakdown.md`, `pipeline/frames/` (IMG_6422 0003/0015/0019/0035, IMG_7563 0052 külön megnézve)
> Státusz: **KÖTELEZŐ SORVEZETŐ.** A 6. fejezet („Kötelező paraméterek”) számai kötöttek, a 02–06 agentek nem térhetnek el tőlük. Minden korábbi koncepció érvénytelen, egyetlen eleme sem használható, csak az itt leírtak.
> Alkalmazott skill-módszertan: blender-director (production brief, reference analysis, geometria-tierek, per-object emisszió, AgX), reference-image-match + reference-analysis-template + visual-match-checklist (elemzés -> kamera -> sziluett -> anyag -> fény -> összevetés), camera-cinematography (szándékos optika, target-empty, kompozíciós checklista), sci-fi-punk-worlds (egy sáv: tiszta króm-kiberpunk, nincs sárgaréz/steampunk keverés), neon-retrofuturism (fekete króm + forró neonél), dark-gritty-mood (low-key alap), brutalist-mood (monumentális lépték, kevés anyag), naming-conventions (COL_/SM_/MAT_/LGT_/CAM_).

---

## 1. Mit mutatnak a referenciák (Reference Analysis)

A `referencia/` mappa 4 videót és 1 WAV-ot tartalmaz, képfájlt nem. VJ- és koncertvizuál-kollekció: nagy, szimmetrikus, 3D-ben renderelt mechanikus „boss” karakterek fekete térben, króm/gyöngyház/anodizált/üveg anyagokkal, emisszív neon élekkel; mellettük valódi aréna-felvételek ívelt LED-fallal, négyzetes truss-kerettel, füsttel, lézerlegyezőkkel. A zene ~143.55 BPM-es, nagy energiájú elektronikus szám.

Saját szemmel ellenőrzött kulcskockák:
- **IMG_6422 / 0003 (Render):** lebegő, gyöngyház-króm, vízszintes lemez-szegmensekből álló koponya-sisak középen, két oldalt ökölbe szorított, magenta-kék irizáló robotkéz, mögöttük fehérre izzó LED-fal, felül kockás LED-plafon, a koponya körül szétszóródó üvegszilánk-részecskék. Tökéletes bal-jobb szimmetria.
- **IMG_6422 / 0015 (Render):** a koponya felülnézetből, cián-zöld króm koronalemezzel; a kezek sárgászöld-króm ujjpercekkel, magenta élfény, mélylila-fekete háttér. Live részen lapos zöld lézer-fénysík terül szét a füstben.
- **IMG_6422 / 0019 (Render):** a koponya szemüveg-szerű, fehéren izzó visor-sávval, alatta vigyorgó mechanikus fogsor; a két kéz nyitott tenyérrel, széttárt ujjakkal a koponya magasságában lebeg, kifelé-felfelé fordítva. Lila füst-háttér.
- **IMG_6422 / 0035 (Live):** ~20+ vékony zöld nyaláb legyezőben és keresztben, egymásba ágyazott négyzetes keretek a LED-falon, teljes zöld füsttelítés. (A Viewport-részen a kezek és a koponya clay-ként: ujjpercenként szegmentált, vastag, hidraulikus kezek.)
- **IMG_7563 / 0052 (Render):** szimmetrikus mechanikus fej koncentrikus gyűrűs lencse-szemekkel (fogaskerék-perem, LED-pontsor, üveglencse), kék és piros-rózsaszín rim-light fekete háttér előtt.

**Tiltás (kreatív szinten):** semmilyen színpad, DJ-pult, ember, tömeg, közönség-sziluett, szöveg, logó, monogram, felirat, réteg-címke, profilikon. A referenciák feliratai csak azonosításra szolgáltak.

---

## 2. Vizuális DNS (a referenciákból levont jegyek)

| Jegy | Megfigyelés | Forrás |
|---|---|---|
| Sziluett | Középtengelyes, tökéletes bal-jobb szimmetria: kompakt koponya középen, két oldalt tükrözött kéz | 6422 (0003, 0019) |
| Koponya | Vízszintes lemez-szegmensekből épülő kranium, szemüveg-szerű szem-sáv, mechanikus fogsor, irizáló króm | 6422 |
| Szemek | Koncentrikus gyűrűs lencse: fogaskerék-perem, LED-pontsor, üveglencse, belső mag | 7563 (0052) |
| Kezek | Szegmentált ujjpercek, hengeres ízületek, hidraulikus inak, tenyér felénk vagy ökölben | 6422 (0003, 0019, 0035 clay) |
| Anyag | Gyöngyház-króm vékonyréteg-irizálással (magenta/zöld/cián átfordulás), sötét anodizált panelek, üveg | 6422, 7563 |
| Emisszió | Magenta/pink élvonalak, cián LED-pontsor, fehér-zöld izzó mag | 6422, 7563, 9135 |
| Lézer | Zöld vékony legyező, függőleges keret-nyalábok, vízszintes zöld sorok, lapos fénysík, nested square alagút | 6422 |
| Lézerháló | 30–50 nyaláb V-ben + széles puha füstkúpok (eredetiben piros, nálunk magenta) | 7563 |
| Sunburst | Széles fehér-kék nyalábok a tárgy mögül | 9135 |
| Környezet | Ívelt LED-fal, négyzetes box-truss portál, plafon-spotsor (színpad nélkül átültetve) | 6422, 7563, 9135 |
| Padló | Sötét tükröző víz / tükörpadló, 50–60%-os tükörkép | 0836, 9135 |
| LED-fal minta | Koncentrikus gyűrűk, négyzetek, háromszögrács, ütemre vált | 0836, 9135 |
| Kontraszt | Fekete <-> telített szín <-> fehér flash | 0836, 9135 |
| Clay-réteg | Szürke clay villanás mint stílusváltó akcentus | 6422, 7563 |

---

## 3. Három koncepció (mind koponya + két kéz alapú)

### 3.1 Koncepció A – „MIRROR RELIQUARY” (tükörvíz-kupola)
Az IMG_0836 hengeres, cián bordás kupolájába helyezi a koponya-kéz triádot. A kupolafal LED-panelei ütemre váltanak, alul hullámzó fekete víztükör. Hipnotikus, intim, de nem festival-lépték, és a kupola elnyeli a lézerlegyezőket.

> *Prompt:* `symmetrical floating mechanical skull of pearlescent iridescent chrome plates between two mirrored giant cybernetic robot hands, inside a cylindrical cyan-ribbed dome lined with LED panels showing concentric rings, black rippling water floor with mirror reflection, magenta neon edge lines, cyan LED dot rings around crystal lens eyes, volumetric haze, extreme contrast, centered vertical composition, octane render --ar 9:16 --style raw --s 400 --no text, logo, people, stage`

### 3.2 Koncepció B – „CLAY GHOST PROTOCOL” (réteg-váltó)
A 6422/7563 Render-Viewport rétegszerkezetéből és a 9135 inverz villanásaiból: a triád ütemre vált teljes render, szürke clay és inverz zöld negatív között, zoom-blur glitch-átmenetekkel. Grafikus és agresszív, de a 240 frame-es loopban széttöredezik, és kevés benne a fény-telítettség.

> *Prompt:* `symmetrical cybernetic skull with hinged jaw and iris lens eyes, two mirrored hydraulic robot hands, hard cut between pearlescent chrome render, grey clay viewport #535353 and inverted acid green negative #70F34A, zoom blur glitch, black void, frontal hero shot --ar 9:16 --s 300 --no text, logo, watermark, people`

### 3.3 Koncepció C – „IRIS SOVEREIGN” (AJÁNLOTT)
A négy referencia festival-léptékű szintézise. Végtelen sötét, sűrű füsttel telt tér, színpad nélkül: a fekete tükörpadlóból emelkedik hátul egy hatalmas ívelt LED-fal, előtte három egymásba ágyazott négyzetes truss-portál (6422). A portálok előtt lebeg a gyöngyház-króm mechanikus koponya, mozgó állkapoccsal és írisz-tágulásra képes kristálylencse-szemekkel (6422 koponya + 7563 lencse-szem), két oldalt két hatalmas kibernetikus kéz tükrös szimmetriában (6422). A koponya mögül és alól zöld lézerlegyezők, a plafonról vastag magenta kúpok, a sarkokból cián pásztázók, keresztező nyalábok és lapos fénysíkok; a dropon magenta lézerháló (7563) és fehér sunburst (9135). Minden a tükörpadlón duplán visszatükröződik.

> *Prompt:* `epic festival VJ visual, colossal floating symmetrical mechanical skull of pearlescent iridescent chrome and dark anodized panels, segmented cranial plates, hinged mechanical jaw with chrome teeth, crystal lens eyes with dilating iris blades and cyan LED dot rings, two giant mirrored cybernetic robot hands with hydraulic tendons, segmented knuckles and glowing magenta palm cores, dozens of green laser fans #35FF3A layered and crossing, thick magenta volumetric beam cones #E040FB from above, cyan scanner beams #37CDEE, giant curved LED wall and nested square box-truss portals behind, dense volumetric smoke, glossy black mirror floor with double reflections, hard rim lights, bloom, slight chromatic aberration, film grain, perfect bilateral symmetry, low angle, Excision Subtronics show visuals, unreal engine 5, octane, 8k --ar 9:16 --style raw --s 750 --no text, logo, letters, watermark, stage, dj booth, people, crowd, audience`

> *SD negatív:* `text, logo, watermark, letters, signature, stage, dj booth, dj desk, people, crowd, audience, faces, red lasers, yellow lasers, fire, daylight, flat lighting, flat materials, asymmetry, empty dark frame, primitive shapes, blurry, lowres, overexposed`

**Miért C:** ez adja egyszerre a megrendelt festival-telítettséget, mind a négy referencia stílusjegyét és stabil, loopolható térbeli rendet (statikus tér, periodikus fények). A-ból a tükörpadló és a LED-fal mintaváltása, B-ből a clay-villanás 2 frame-es akcentusként épül be.

---

## 4. Az ajánlott koncepció részletesen

### 4.1 A koponya (SM_Char_Skull_*)
- **Lánc (skill: sci-fi-punk-worlds):** egyetlen sáv, tiszta króm-kiberpunk. Nincs sárgaréz, rozsda, steampunk-elem. Kopás csak mikro-szinten (dark-gritty-mood: finom élkopás az anodizált paneleken, nincs piszok).
- **Tier 1 – sziluett:** kerekded, enyhén előreeső kranium; széles, vízszintes szem-sáv (két mélyített szemüreg egy közös homlok-pajzs alatt); hangsúlyos járomcsontok; felső fogsor a maxillán; külön objektumként mozgó állkapocs (mandibula). Nincs nyak, a koponya lebeg.
- **Tier 2 – panel-tagolás:** a kranium 7 vízszintes, előrefelé lépcsőző lemez-szegmensből áll (6422 / 0003), 8–12 mm-es panelrésekkel; a halántékon kétoldalt 2-2 hidraulikus dugattyú köti a kraniumot az állkapocs-csuklóhoz (látható mechanika); járomcsont-lemezek, homlok-pajzs, tarkó-bordázat.
- **Tier 3 – részletek:** csavarfejek a lemezek szélén, szellőzőrácsok a halántékon, 6 kábelköteg az állkapocs alól 0.8 m hosszan lelógva (végükön emisszív gyűrű), fogankénti barázdák, mikro-élletörések, amelyek elkapják az élfényt.
- **Szemek (hero feature):** szemüreg-átmérő 0.62 m. Rétegek kívülről befelé: fogaskerék-perem (anodizált), 24 pontos cián LED-pontsor, kristály-üveglencse kupola, 12 lamellás írisz (anodizált, tágul/szűkül), emisszív mag (#E8FFD0). Az írisz nyílása az animáció fő karakter-gesztusa.
- **Állkapocs:** csukló-pivot a fülcsuklóknál, X-tengely körüli forgás. Alsó fogsor króm, a fogak mögött magenta emisszív „torok-fény”.

### 4.2 A két kéz (SM_Char_Hand_R és X-tükre SM_Char_Hand_L)
- **Forma:** 5 ujj, ujjanként 3 ujjperc hengeres ízületekkel, a kézháton ujjanként 1 hidraulikus ín (krómrúd + anodizált henger), tenyér-lemez középen kör alakú magenta emisszív maggal, csukló-gallér cián emisszív gyűrűvel, alóla 4 kábel lelóg és sötétbe vész.
- **Póz (alap):** tenyér a kamera felé, ujjak 12°-ban széttárva, 15°-ban enyhén behajlítva (6422 / 0019), a kéz 12°-kal befelé fordul a koponya felé, 10°-kal hátradől.
- **Szimmetria:** a bal kéz minden frame-en a jobb pontos X-tükre (geometria és animáció). Kötelező a Mirror X.

### 4.3 Anyagok (kevés anyag, brutalist-mood elv; naming-conventions szerint)
- `MAT_Metal_PearlChrome` (kranium, kéz-lemezek): metallic 1.0, roughness 0.12, vékonyréteg-irizálás 250–450 nm; nézőszögtől függően magenta, zöld és cián felé fordul (6422 / 0003, 0015).
- `MAT_Metal_AnodizedDark` (belső panelek, írisz-lamellák, ujjperc-közök): #1A1426, metallic 1.0, roughness 0.35, enyhe anizotrópia, finom élkopás.
- `MAT_Metal_ChromeRod` (dugattyúk, inak, fogak): roughness 0.05.
- `MAT_Glass_EyeCrystal` (szemlencse): transmission 1.0, IOR 1.52, roughness 0.02, tint #15194A.
- `MAT_Rubber_CableDark` (kábelek): #0D0712, roughness 0.55.
- Emisszió kizárólag objektumonkénti `MAT_LightInst_*` anyagokon (szem-mag L/R, LED-pontsor L/R, élvonalak, torok, tenyér-mag L/R, csukló-gyűrű L/R). **Strukturális anyag (PearlChrome, AnodizedDark) emissziója soha nem animálható.**

### 4.4 Tér
- Végtelen, fekete, sűrű füsttel kitöltött tér. Nincs színpad, emelvény, DJ-pult, ember.
- Fekete tükörpadló a teljes alapsíkon. Hátul ívelt LED-fal a padlóból emelkedik. Előtte 3 egymásba ágyazott négyzetes box-truss portál, a legnagyobb a padlón áll.
- A plafon nem látszik: a truss-rács a kép fölött van, onnan érkeznek a kúpok.

### 4.5 Fénydramaturgia (festival-telítettség)
- Kemény kontraszt, de **nincs üres sötét felület**: a kép területének legalább 60%-án fény van (nyaláb, kúp, LED-fal, füstben szórt halo vagy tükörkép). Fekete csak a nyalábok közötti réseken és a padló sötét foltjain marad.
- Az eloszlás alapállapotban: kb. 25% mély fekete/lila-fekete, 50% telített lézer- és emissziós szín (zöld/magenta/cián), 15% fehér csúcsfény, 10% középtónusú füst-halo.
- A koponyát és a kezeket élfények rajzolják ki (rim : key = 4 : 1); a LED-fal ellenfényként glóriát ad mögöttük a füstben.
- A lézerek a füstben szilárd fényrudak és fénysíkok (6422 / 0015), a tükörpadlón duplán ismétlődnek.

### 4.6 Mozgáslogika
- A tér statikus; a fények, a füst, a koponya, a kezek és a kamera mozognak.
- Koponya: lassú lebegés, az állkapocs basszusra lenyílik, a szemek írisze basszusra kitágul, a drop előtt összeszűkül.
- Kezek: tükrös lebegés, basszusra az ujjak behajlanak, a 204-es csúcson szétnyílnak.
- Lézerek: a legyező beatre nyit/zár, a pásztázók periodikusan lengenek, a csúcsponton lézerháló.

### 4.7 Hangreakció dramaturgiája (8 s ablak, 4 blokk)
| Blokk | Frame | Hang (analízis) | Kép |
|---|---|---|---|
| I. PULSE | 1–62 | kick 13, 50; snare 20, 49 | Zöld domináns: kettős legyező (A+J), keret-nyalábok, LED-fal koncentrikus gyűrűk, az írisz beatre pulzál |
| II. BREATH | 63–124 | kick 63, basszus-szünet ~91–121; legerősebb snare 118 | Magenta domináns: plafon-kúpok, LED-fal egymásba ágyazott négyzetek, az írisz 30 frame-es lélegzése. 118-on teljes fehér flash, az állkapocs szélesre nyílik, a nested square zöld lézer-alagút a szájból „tör elő” |
| III. BUILD | 125–186 | bassz 136, 149, 161, 174, 180, 186 (sűrűsödik) | Cián + zöld: pásztázók gyorsulnak, LED-fal háromszögrács, a rázkódás és az állkapocs-mozgás erősödik |
| IV. PEAK | 187–240 | 187–203 feszültségépítés; bassz 192, 198, 204 (legerősebb), 211…235 | 187–203: szűkülő írisz, záródó legyezők, gyorsuló strobe, 203 sötétítés. 204: fehér flash, sunburst, magenta lézerháló, max. írisz és állkapocs, max. rázkódás. 225–240: lecsengés a frame-1 állapotba |

---

## 5. Konzisztencia-szabályok (röviden)
- Csak a 6.5 palettából. **Piros és sárga lézer, valamint tűz nincs.**
- Minden fényelem X-tükrözött párban jelenik meg, kivéve a középtengelyen állókat.
- Szöveg, logó, ember sehol, a LED-fal tartalmán sem.

---

## 6. KÖTELEZŐ PARAMÉTEREK

### 6.1 Téma és forrás-hozzárendelés
1. **Téma:** „Iris Sovereign”, Excision / Subtronics szintű festival-VJ vizuál. Középen lebegő, szimmetrikus mechanikus koponya (gyöngyház-króm + sötét anodizált panelek, mozgó állkapocs, írisz-tágulásra képes kristályszemek), két oldalt két hatalmas kibernetikus robotkéz tükrös szimmetriában. Tér: sűrű volumetrikus füst, fekete tükörpadló, hátul ívelt LED-fal és 3 egymásba ágyazott négyzetes truss-portál. Fények: zöld lézerlegyezők, magenta élfények/kúpok, cián pásztázók, tükröződés a padlón, AgX.
2. **Forrás-hozzárendelés:**
   | Jegy | Fájl |
   |---|---|
   | Koponya (lemez-szegmensek, szem-sáv, fogsor), két tükrözött kéz, gyöngyház-irizáló króm, magenta élfény, zöld lézerlegyező, függőleges keret-nyalábok, vízszintes zöld sorok, lapos fénysík, nested square truss-portál, LED-fal | referencia/IMG_6422.MP4 |
   | Tükörvíz-padló, LED-fal mintaváltás (gyűrű/négyzet), fekete-fehér kontraszt | referencia/IMG_0836.MP4 |
   | Lencse-szem koncentrikus gyűrűkkel + LED-pontsor (írisz alapja), V-lézerháló, füstkúpok, kék/rózsaszín rim, clay-villanás | referencia/IMG_7563.MP4 |
   | Sunburst nyalábok, fehér-zöld mag-emisszió, LED-fal háromszögrács | referencia/IMG_9135.MP4 |
   | BPM, beat-rács, basszus/snare csúcsok, loop-ablak | referencia/CIGARETTA MOLLYWOOD.wav |

### 6.2 Formátum
3. Felbontás: **1080 x 1920**, képarány **9:16** (álló).
4. FPS: **30**.
5. Frame range: **1–240** (240 frame = 8.000 s). Frame-konvenció: 1-alapú, **frame = s × 30 + 1**.
6. Hang: `referencia/CIGARETTA MOLLYWOOD.wav`, **kezdőpont 60.48 s**, ablak 60.48–68.48 s. Az ablak vége build-up, ezért a hang-loop seamnél 6–10 frame-es crossfade kötelező.

### 6.3 Loop-szabály (seamless)
7. **A frame 1 állapota azonos a (nem renderelt) frame 241 állapotával**, a 240-es frame NEM ismétli az 1-est.
8. Minden folyamatos periodikus mozgás periódusa 240 vagy annak osztója: **240, 120, 80, 60, 48, 40, 30, 24** frame. Más periódus tilos.
9. Eseményalapú lecsengések (rázkódás, flash, emisszió-pulzus, állkapocs, írisz, ujjak, skála) **modulo 240 körbefutnak**: a 235-ös basszus és a 238-as snare lecsengése az 1–6. frame-be átnyúlik, és ott meg kell jelennie.
10. A füst mozgása is periodikus (240 frame). Nem lehet folyamatosan sodródó, nem-ciklikus zaj.
11. A blokk-vágások (63, 125, 187) diszkrét váltások. A 240 -> 1 határon a IV. blokk lecsengett állapota megegyezik az I. blokk kezdőállapotával.

### 6.4 Ritmus (az analízisből, ablak 60.48 s-tól)
12. BPM **143.55**, beat = 0.418 s = **12.54 frame**. 8 s = 19.1 beat (nem egész szám, a seamet a 9. pont kezeli).
13. **Beat-frame-ek (19 db):** 13, 26, 38, 50, 63, 75, 88, 100, 112, 125, 137, 150, 162, 174, 187, 199, 212, 224, 237.
14. **Basszus-csúcsok (17 db):** 13, 50, 63 (kick), majd 136, 149, 161, 174, 180, 186, 192, 198, **204 (legerősebb)**, 211, 217, 223, 229, 235. Basszus-szünet: kb. **91–121**.
15. **Snare-csúcsok, erős (10 db):** 20, 49, 70, 76, **118 (legerősebb)**, 150, 156, 169, 210, 226. **Gyenge (13 db):** 14, 25, 43, 62, 82, 87, 101, 126, 144, 180, 201, 221, 238.
16. **LED-fal mintaváltás (egyetlen szabály):** vágás a 63., 125. és 187. frame-en, plusz a loop-határon. Minták: 1–62 koncentrikus gyűrűk, 63–124 egymásba ágyazott négyzetek, 125–186 háromszögrács, 187–240 lencse-írisz (koncentrikus gyűrű + 12 lamella, a koponya szemének visszhangja). Blokkon belül a minta lassan animál, 60 frame-es periódussal. A LED-fal tartalma csak geometrikus minta: nincs szöveg, logó, arc, kép a karakterről.

### 6.5 Színpaletta (HEX)
17.
| Szerep | HEX |
|---|---|
| Void fekete (alap, padló) | #040510 |
| Lila-fekete háttér, kábelek | #0D0712 |
| Mély éjkék (füst árnyék) | #0D1330 |
| Szemlencse-üveg tint | #15194A |
| Anodizált panel | #1A1426 |
| Lézer-zöld (fő) | #35FF3A |
| Lézer-zöld (mély) | #04D12C |
| Savzöld akcent | #70F34A |
| Magenta (kúpok, élvonal, háló, tenyér-mag, torok) | #E040FB |
| Neon lila (key tónus) | #8A4CD6 |
| Cián (pásztázók, LED-pontok, csukló-gyűrű) | #37CDEE |
| Mély cián | #34AED4 |
| Fehér flash / strobe | #FBF4FD |
| Szem-mag izzás | #E8FFD0 |
| Clay-szürke (2 frame villanás) | #535353 |
| Gyöngyház irizálás – rózsa / menta / jég (a króm vékonyréteg-színei, nem külön fény) | #FF8FD8 / #9BFFD6 / #9FD8FF |
| Tűz-narancs | #EF4E2C – **INAKTÍV** (tűz nincs: színpad tilos, és nincs a fénylistában) |

### 6.6 Méretarányok és kompozíció (világ-méter, 1 BU = 1 m; origó = a koponya alatti padlópont, a kamera −Y irányban áll, +Y a mélység)
18. Tér: nincs látható fal; a füst-domén 40 m széles × 40 m mély × 24 m magas, középen az origó. Tükörpadló: 60 × 60 m sík, z = 0.
19. **Színpad nincs.** Minden fényforrás a padlóba süllyesztett résben, a truss-portálokon vagy a kép fölötti plafon-truss-on ül.
20. **LED-fal:** 18 m széles × 12 m magas, ívelt (görbületi sugár 20 m, a kamera felé homorú), alsó éle a padlón (z = 0), középpontja y = +7.0 m. A széle a képen kívül esik (nincs él-érintés).
21. **Truss-portál:** 3 egymásba ágyazott négyzet, **11 / 9 / 7 m** oldalhossz, 0.5 m-es box-truss, y = **+2.5 / +4.0 / +5.5 m**, középpontjuk z = **5.5 m** (a legnagyobb a padlón áll). (Eltérés a korábbi paramétertől: 14/11.5/9 m @ 8.5 m -> 11/9/7 m @ 5.5 m; ok: színpad nélkül a padlón állnak, és a 28 mm-es 9:16 képben így férnek el élérintés nélkül.)
22. **Koponya:** 2.6 m széles × 3.4 m magas (állkapoccsal) × 2.8 m mély, középpontja **(0, 0, 4.5)**. Szemüreg Ø 0.62 m, a két szem középtávolsága 1.10 m. Állkapocs-csukló x = ±1.15, y = +0.35, z = 3.9.
23. **Kezek:** egyenként 3.0 m magas (csuklótól ujjhegyig) × 2.0 m széles, középpontjuk **(±3.3, −0.4, 5.0)**. A koponya és a kéz belső éle között 0.8 m rés. Az együttes teljes szélessége **8.6 m**, függőleges kiterjedése z = 2.8–6.6 m.
24. **Kamera:** `CAM_Main_Hero` a **(0, −16, 1.7)** pontban, fókusz **28 mm**, sensor fit vertical, sensor 36 mm (függőleges FOV ≈ 65.5°, vízszintes ≈ 39.7°). Célpont: `EMPTY_CamTarget_Hero` a **(0, 0, 2.43)** pontban (dőlés ≈ +2.6°, low-angle), így a koponya középpontja a kép alulról mért **60%**-ánál van.
25. **Képkompozíció (9:16), a fenti számokból levezetve:**
    - A koponya síkjában a látható szélesség 11.6 m: a koponya + kezek együttese a képszélesség **74%**-a (legközelebbi dolly-állásban, 14.8 m-en **80%**; +3% skála-pulzussal **83%**). Mindig a **90%-os safe-area-n belül**, orbit és rázkódás közben is.
    - Függőlegesen az együttes a képmagasság **kb. 18%**-a (a 9:16 keskeny szélessége a korlát), sávja a kép alulról mért ~51–69%-a között.
    - Alsó sáv: a padlón az együttes tükörképe a kép alulról mért ~10–22%-ában (dupla kép), a padló 0–50% között.
    - Felső sáv: a portálok teteje ~85%-on, a LED-fal teteje ~81%-on, felettük a C-sorok (90–96%) és a plafonról lelógó D/M-kúpok töltik ki a képet. Üres sötét sáv nincs.

### 6.7 Lézer- és fénycsóva-táblázat (minden csoport X-tükrözött)
26. A darabszám, szög, szín, vastagság és viselkedés a korábbi táblázatból változatlan; az A–I sorokban csak a forráspozíció került át a színpadról a padlóra/portálra. A J–M sorok a festival-telítettség miatt újak.

| Csoport | Darab | Forrás (pozíció) | Szög | Szín | Vastagság | Viselkedés |
|---|---|---|---|---|---|---|
| A – zöld fő legyező | 14 (7+7) | padlórés a koponya mögött, (0, +1.2, 0) | ±6, ±14, ±22, ±30, ±38, ±46, ±54° a függőlegestől, előre (kamera felé) 10° | #35FF3A | 2.5 cm (≈3–5 px) | Minden beat-frame-en +5° nyitás, 8 frame alatt vissza. I. és IV. blokkban 100%, II-ben 30%, III-ban 70%. A középső nyalábokat a koponya takarja (ellenfény-glória) |
| B – függőleges keret-nyalábok | 6 (3+3) | a középső (9 m-es) portál alja, y = +4.0, x = ±1.2 / ±2.4 / ±3.6 m | 0° (függőleges) | #04D12C | 2 cm | I. blokkban mind, II-ben csak a középső 2, III-ban mind 50%-on, IV-ben mind + villogás beatre |
| C – vízszintes zöld sorok | 4 | y = +4.0 síkban, z = 12.5 / 13.3 / 14.1 / 14.9 m | 0° (vízszintes), ±3° hullámzás | #70F34A | 1.5 cm | Lassú függőleges hullámzás, periódus 60 frame |
| D – magenta füstkúpok | 8 (4+4) | plafon-truss z = 18 m, y = +1.0, x = ±3 / ±6 / ±9 / ±12 m | lefelé, 15 / 22 / 28 / 35° befelé dőlve | #E040FB | kúp nyílás 4° (fényfolt 0.6–1.2 m) | II. blokk fő eleme, snare-re fényerő-csúcs, 120 frame-es pásztázás ±8° |
| E – cián pásztázók | 4 (2+2) | hátsó sarkok (±14, +9, 10) | pásztázás ±45° vízszintesen | #37CDEE | 2 cm | Periódus 80 frame (I–II), a III. blokkban 40 frame |
| F – nested square alagút | 5 koncentrikus négyzet | a száj előtti tengely, középpont z = 4.0, y = +5.5 -> +0.7, 1.2 m lépésköz, oldalhossz 6 / 5 / 4 / 3 / 2 m (a kamera felé csökken) | – | #35FF3A | 1.5 cm | Csak 118–130, a 118-as snare-re kinyílik, mintha a nyitott szájból törne elő |
| G – magenta lézerháló (drop) | 40 (20+20) | padlórés a koponya alatt, (0, +0.8, 0.05) | V-legyező ±5…±75° a függőlegestől egyenletesen, 2 síkban (0° és +8° dőlés a kamera felé) | #E040FB, mag #FBF4FD | 1 cm | Aktív 198–216, csúcs 204. Felfutás 2 frame, lecsengés 10 frame |
| H – fehér sunburst | 6 (3+3) | a koponya mögül, (0, +1.5, 4.5) | ±12, ±30, ±50° | #FBF4FD -> #37CDEE szél | 0.6–1 m (60–120 px) | 204–212, csúcs 204 |
| I – tűzgejzír | 2 | – | – | #EF4E2C | – | **INAKTÍV.** Színpad tilos, és a tűz nincs a fénylistában. A 204-es csúcson G + H + K-teljes fehér + M-maximum helyettesíti |
| J – zöld 2. szintű legyező (új) | 16 (8+8) | két padlórés, (±2.0, +2.0, 0) | ±4, ±12, ±20, ±28, ±36, ±44, ±52, ±60° a függőlegestől, előre 18° | #70F34A | 2 cm | I. és III. blokk 100%, II-ben ki, IV-ben 100%. Beatre +4° nyitás, 8 frame alatt vissza. Az A-val keresztező, többrétegű legyezőt ad |
| K – keresztező diagonálok (új) | 8 (4+4) | a legnagyobb portál felső sarkai (±5.5, +2.5, 11) és alsó sarkai (±5.5, +2.5, 0) | a túloldali sarok felé, X-keresztben a koponya mögött | felső pár #35FF3A, alsó pár #37CDEE | 2 cm | Mindig aktív (60%). Erős snare-re strobe-szerűen 100% (3 frame) |
| L – lapos cián fénysík (új) | 12 (6+6) | padlórés a kezek alatt, (±3.3, −0.4, 0.05) | majdnem vízszintes legyező, 3° emelkedés, ±10…±60° oldalra (10° lépés) | #37CDEE | 1.5 cm | Mindig aktív; a padlón végigfutó fénysík (6422 / 0015). Basszusra +50% × súly |
| M – vastag volumetrikus kúpok (új) | 6 (3+3) | plafon-truss z = 18 m, y = −2.0, x = ±2 / ±5 / ±8 m | lefelé, a koponya/kezek felé dőlve | belső pár #FBF4FD, középső #E040FB, külső #37CDEE | kúp nyílás 14°, blend 0.3 | Mindig aktív, 120 frame-es ±6° pásztázás. A legvastagabb fénytestek a füstben |

27. **Nyaláb-darabszám (telítettség-szabály):** minden renderelt frame-en legalább **40 látható vékony lézernyaláb** (kivétel csak a 118–120 fehér flash és a 203 sötétítés). Blokkonként: I. = A14 + B6 + C4 + E4 + J16 + K8 + L12 = **64** + D8 + M6 kúp; II. = A14 (30%) + B2 + C4 + E4 + K8 + L12 = **44** + D8 + M6; III. = A14 + B6 + C4 + E4 + J16 + K8 + L12 = **64** + D8 + M6; IV. = 64 + G40 (198–216) = **104** + H6 + D8 + M6.
28. **Emissziós erősség (renderer-relatív):** A–C 40–60, G 80, H 25, J 45, K 50, L 35. A nyalábok a füstben láthatók, a tükörpadlón visszaverődnek.
29. **Spot-teljesítmények:** D-kúpok 2500 W/db (spot 4°), M-kúpok 6000 W/db (spot 14°, blend 0.3), E-pásztázók 1500 W/db. LED-fal emisszió 3–6 (nem éghet ki). Koponya-élvonalak emisszió 8–15, szem-mag 25, LED-pontsor 12, tenyér-mag 10, csukló-gyűrű 8, torok 6.

### 6.8 Basszusreakciók
30. **Súlyok (w):** 204 = 1.00; 198 és 211 = 0.75; 235 = 0.60; 136, 149, 161, 174, 180, 186, 192, 217, 223, 229 = 0.55; 13, 50, 63 = 0.40.
31. **Csatornánkénti reakciótábla** (minden csatorna additív az alapállapotra; a lecsengés modulo 240 körbefut, a 235-ös basszusé a 241–242 = **1–2.** frame-be, a 6.9 snare-eké a 9. pont szerint):

| Csatorna | Trigger-frame-ek | Amplitúdó | Felfutás / lecsengés | Megjegyzés |
|---|---|---|---|---|
| Kamera-rázkódás | 13, 50, 63, 136, 149, 161, 174, 180, 186, 192, 198, 204, 211, 217, 223, 229, 235 | transzláció **6 cm** × w, pitch **0.6°** × w, yaw **0.4°** × w, roll **0.8°** × w | csillapított oszcilláció, 2 periódus **8 frame** alatt, a 8. frame-re < 5% | Determinisztikus, az irány peak-enként váltakozik (bal/jobb). Nincs zaj-alapú random |
| FOV-punch | ugyanazok | 204-en **−2°** fókusz-ekvivalens, a többin **−0.8° × w** | 6 frame alatt vissza | – |
| Skála-pulzus (koponya + kezek együtt, saját középpontjukból) | ugyanazok + minden beat-frame (13. pont) | basszus: **+3% × w**; beat: **+1%** | 2 frame be, 6 frame vissza | max. +4% |
| Írisz-tágulás | ugyanazok | nyílás-átmérő = 0.16 m alap + **0.20 m × w** (204-en 0.36 m); beat-frame-en +0.02 m | 2 frame be, 6 frame vissza | 6.10 feszültség-szakaszban az alap 0.10 m-re szűkül |
| Állkapocs | ugyanazok | nyitás = 3° alap + **14° × w** (204-en 17°) | 2 frame be, 6 frame vissza | felső korlát 24° (snare-rel összeadva) |
| Ujjak (mindkét kéz tükrösen) | ugyanazok, kivéve 204 | behajlás **+12° × w** ujjpercenként | 2 frame be, 6 frame vissza | 204-en fordítva: −10° (kinyílás) + 8° szétterülés, 10 frame alatt vissza |
| Lézer-emisszió (A, J, L, K) | ugyanazok | **+50% × w** | 1 frame be, 6 frame vissza | A beat-nyitással (26. sor) összeadódik |
| Karakter-emisszió (szem-mag, LED-pontsor, élvonalak, tenyér-mag) | ugyanazok | **+40% × w** | 1 frame be, 6 frame vissza | beat-frame-en +15%, 6 frame; összesen max. +60% |
| LED-fal és füst | ugyanazok | LED-fényerő +30% × w, alsó füstréteg fényessége +20% × w | 1 frame be, 6 frame vissza | – |

32. **Basszus-szünet (91–121):** az állkapocs zárva (3°), az írisz lélegzik: ±0.015 m, szinusz, periódus **30 frame**, fázis 0 a 91. frame-en (121-re visszaér 0-ra).

### 6.9 Snare-reakciók
33. **Erős snare** (20, 49, 70, 76, 118, 150, 156, 169, 210, 226): plafon-stroboszkóp, fehér #FBF4FD, 3 frame (100% / 50% / 15%). A D-kúpok fényereje +50%, a K-diagonálok 100%. Állkapocs-„harapás”: +6° 1 frame alatt, 3 frame alatt vissza. Szem LED-pontsor +80%, tenyér-mag +100%, 3 frame.
34. **Gyenge snare** (14, 25, 43, 62, 82, 87, 101, 126, 144, 180, 201, 221, 238): csak a D-kúpok +25%, 2 frame. A 238-as lecsengése a 239–240. frame-be esik; az erős snare-ek 3 frame-es strobe-ja egyik esetben sem fut át a loop-határon.
35. **118 (legerősebb snare):** teljes képes fehér flash 4 frame (118: 100%, 119: 60%, 120: 25%, 121: 0). Az állkapocs 22°-ra nyílik, 118–124 között tart, 130-ra visszazár 3°-ra. Az F-alagút a szájból kinyílik (118–130).
36. **204 (fő csúcs):** fekete -> fehér -> szín: 203 = 85% sötétítés, 204–205 fehér flash (100% / 70%), 206–210 telített szín + G + H + K 100% + M maximum (+50%). Írisz 0.36 m, állkapocs 17°, kezek kinyílnak (31. pont).
37. **Clay-villanás:** 196–197 (2 frame) a koponya és a kezek a #535353 clay-anyagot kapják (`MAT_Clay_Grey`), emisszió nélkül, majd 198-tól vissza a renderanyagra (7563 / 6422 viewport-réteg átültetve).

### 6.10 Drop-dramaturgia (feszültség és csúcs, frame-re kötve)
38. **Feszültségépítés 187–203:**
    - Az írisz alapnyílása lineárisan 0.16 -> 0.10 m-re szűkül (187 -> 203), a basszus-tágulás erre adódik.
    - Az A és J legyezők szögtartománya lineárisan 100% -> 60%-ra zárul (a szögek szorzója), a K-diagonálok 60% -> 100%-ra erősödnek.
    - Strobe-sűrítés: a 187, 192, 196, 199, 201 frame-eken 1 frame-es fehér strobe 40%-on (a 196–197 clay-villanással együtt).
    - Az M-kúpok fényereje 100% -> 70%, a LED-fal fényereje 100% -> 60%; a kamera dolly-ja a 39–40. ponton túl további −0.3 m-t közelít 187 -> 203 között, majd 204–216 között visszaáll.
    - 203: 85% sötétítés (csak a szem-magok és a C-sorok maradnak).
39. **Csúcs 204–216:** lásd 36. pont; G aktív 198–216 (204-en 100%), H 204–212, rázkódás és FOV-punch maximum.
40. **Lecsengés 217–240:** 217–235 a basszusreakciók súlyaival; 225-től minden paraméter a frame-1 állapot felé tart, 240 után (modulo) pontosan az 1. frame állapota.

### 6.11 Kamera (alap-mozgás)
41. Ciklikus orbit az `EMPTY_CamTarget_Hero` körül: yaw ±4°, szinusz, periódus 240 frame (frame 1 = 0°).
42. Dolly: 0 -> −1.2 m (közelebb) -> 0, koszinusz-alakú, periódus 240 frame.
43. Függőleges lebegés: ±0.08 m, periódus 120 frame.
44. A rázkódás (31. pont) erre adódik rá. Mélységélesség: f/4, fókusz a koponyán (a 28 mm-en a kezek is élesek). Lassú, ease-elt mozgás; nincs vad FOV-animáció a punch-on kívül.
45. Koponya lebegése: ±0.10 m függőlegesen, periódus 120 frame; kezek ugyanígy, azonos fázisban (szimmetria), plusz ±2° csukló-billegés, periódus 60 frame, tükrösen.

### 6.12 Volumetrikus füst
46. **Sűrű füst kötelező.** Globális térfogat-sűrűség **0.08**, anizotrópia **0.65** (előre szórás, a nyalábok a kamera felé izzanak).
47. Talajközeli réteg 0–2.5 m között, sűrűség **0.18**, lassan hömpölygő zajjal, periódus 240 frame.
48. A koponya középpontja körüli 5 m-es zónában (a kezeket is lefedi) a sűrűség max. **0.05**. A sziluett nem mosódhat ki, a kontrasztja a háttérhez képest ≥ 60% maradjon.
49. A füst színe a domináns fényé (zöld/magenta/cián). Saját színe semleges, #0D1330 árnyékkal.

### 6.13 Élfények (rim) és key
50. **Bal-hátsó rim** `LGT_Rim_Magenta`: #E040FB, 1500 W area, a kamerához képest 135°-ban, 30° magasan.
51. **Jobb-hátsó rim** `LGT_Rim_Cyan`: #37CDEE, 1500 W area, −135°-ban, 30° magasan.
52. **Felső élfény** `LGT_Rim_Top`: #FBF4FD, 800 W, keskeny softbox közvetlenül felülről; a kranium-lemezek és az ujjpercek élét rajzolja.
53. **Alsó zöld visszaverődés** `LGT_Bounce_Green`: #35FF3A, 300 W, a padlóról felfelé, gyenge (a lézerek bounce-a).
54. **Arány:** rim : key = **4 : 1**. `LGT_Key_Front` 375 W, hideg, frontális (#8A4CD6 tónus), csak a szemlencsék és a fogak csillanásáért.

### 6.14 Tükörpadló (dupla visszatükrözés)
55. Fekete (#040510), roughness **0.06**, finom hullám-normál (erősség 0.02, periódus 240 frame), a tükörkép fényereje **55%**.
56. Plusz clearcoat-réteg: weight 0.5, roughness 0.01. Így éles + lágy, kettős tükörkép keletkezik. A króm koponya a padló tükörképét is visszaveri (glossy bounce ≥ 4), ez adja a dupla visszatükrözést.

### 6.15 Render és utómunka
57. **Színkezelés:** AgX, look **High Contrast**, exposure 0.0 (±0.3 hangolható). Kontrasztos, élénk, nem kiégett: a flash-frame-eken (118–120, 204–205) kívül a kép max. 1%-a lehet clipelt fehér.
58. **Glare/bloom:** Fog Glow, threshold 1.0, size 7, mix 0; plusz Streaks 4 ággal, threshold 2.0, mix −0.7 (csak a lézer-forrásokon és a szem-magon).
59. **Kromatikus aberráció:** Lens Distortion, dispersion **0.012** (enyhe, csak a képszéleken látszik).
60. **Film grain:** finom, 2–3% intenzitás, frame-enként determinisztikus seed (frame-számmal), hogy a loop-seam ne villogjon.
61. Mintavétel: a végső renderen a füstben a nyalábok zajmentesek; a volumetrikus lépésköz legalább olyan finom, hogy az 1 cm-es G-nyalábok is folytonosak.

### 6.16 Minőségi mérce és tesztrender (kötelező)
62. A cél Excision / Subtronics szintű festival-VJ vizuál; lapos, üres vagy „demo” hatású kép nem fogadható el.
63. **Minden pipeline-lépés (02, 03, 04, 05, 06) után tesztrender készül a frame 1, 118 és 204 képkockáról**, a hero kamerából, 1080 x 1920-ban. A lépés csak akkor zárható, ha az önellenőrzés minden pontja teljesül:
    - [ ] Telítettség: a 27. pont szerinti nyaláb-darabszám látszik, többrétegű és keresztező legyezők, nincs üres sötét felület (6.6 / 25. pont).
    - [ ] Karakter: koponya + két kéz részletgazdag (Tier 1–3: lemez-szegmensek, dugattyúk, inak, kábelek, kristálylencse-szemek írisszel), gyöngyház-króm + sötét anodizált, erős emissziós élek; nincs lapos anyag és elnagyolt primitív.
    - [ ] Fény: kemény kontraszt, zöld/magenta/cián rim, vastag volumetrikus kúpok a füstben, dupla tükörkép a padlón.
    - [ ] Dinamika (06 után): rázkódás, FOV-punch, skála-pulzus, strobe, írisz, állkapocs frame-pontosan a 6.8–6.10 listák szerint; 118 és 204 csúcsként olvasható.
    - [ ] Utómunka: AgX High Contrast, bloom/glare, enyhe kromatikus aberráció, grain; élénk, nem kiégett.
    - [ ] Szimmetria: a bal és jobb oldal tükrös; a kezek a 90%-os safe-area-n belül.
    - [ ] Tiltások: nincs színpad, DJ-pult, ember, szöveg, logó.
    - [ ] Strukturális anyagon nincs emissziós keyframe (blender-director szabály).
64. Hibánál gap-lista (max. 5 tétel, prioritás: kamera -> sziluett -> mélység -> anyag -> fény), javítás, újrarenderelés, legfeljebb 3 kör (reference-image-match módszertan).

### 6.17 Elnevezés és szervezés
65. Kollekciók: `COL_Character` (koponya, állkapocs, kezek), `COL_Environment` (padló, LED-fal, truss), `COL_Lasers` (A–M csoportonként al-kollekció), `COL_Lights`, `COL_Cameras`, `COL_FX` (füst-domén). Mesh: `SM_`, anyag: `MAT_`, fény: `LGT_`, kamera: `CAM_`, target: `EMPTY_CamTarget_Hero`.

### 6.18 Tiltások
66. Semmilyen színpad, emelvény, DJ-pult, ember, tömeg, közönség-sziluett, szöveg, logó, monogram, felirat, UI-címke, vízjel.
67. Piros és sárga lézer, tűz nincs. Lapos (egyszínű, reflexió nélküli) anyag és elnagyolt, részletezetlen primitív a hero-elemeken nincs.
68. Kód nem része ennek a dokumentumnak. A 02–06 agentek a fenti számokat implementálják.
