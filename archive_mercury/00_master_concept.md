# 00 – KREATÍV BIBLIA: „CIGARETTA MOLLYWOOD”
**Spotify Canvas · Dark Y2K · Liquid Chrome · Brutalist Type · Volumetric Smoke · Neon Rim**

> Szerző: 00-concept-visionary (Concept Visionary / CGI Art Director)
> Címzettek: 01-ref-analyzer, 02-art-director, 03-modeler, 04-lookdev-artist, 05-lighting-artist, 06-animator
> Státusz: **KÖTELEZŐ SORVEZETŐ.** A 7. fejezet („Kötelező paraméterek”) számai kötöttek, a 02–06 agentek nem térhetnek el tőlük.

---

## 0. Forrásanyag és ami még nincs elemezve

A `referencia/` mappa tartalma (Glob-bal ellenőrizve):

| Fájl | Típus | Állapot |
|---|---|---|
| `referencia/CIGARETTA MOLLYWOOD.wav` | zene (sötét underground riddim/hardstyle, súlyos basszusok) | **nincs elemezve** |
| `referencia/IMG_0836.MP4` | videó referencia | **nincs elemezve** |
| `referencia/IMG_6422.MP4` | videó referencia | **nincs elemezve** |
| `referencia/IMG_7563.MP4` | videó referencia | **nincs elemezve** |
| `referencia/IMG_9135.MP4` | videó referencia | **nincs elemezve** |

**Fontos:** ez az agent a videókat nem tudja megnézni, a hangot pedig nem tudja meghallgatni. A biblia ezért **csak a kötött projekttematikára épül**. A fájlnevekből nem vezettem le tartalmat. A videók és a hang tényleges elemzését (képkockák, mozgásjelleg, BPM, ütemrács, a legjobban loopoló 8 másodperces ablak, basszus- és snare-csúcsok frame-re átszámolva) a **01-ref-analyzer** végzi el, az eredményt a `pipeline/01_analysis.md` tartalmazza.

**Mit módosíthat a 01-es elemzés ebben a bibliában, és mit nem:**
- **Módosíthatja:** az audio ablak kezdőpontját, a BPM-et (információ), a basszus- és snare-csúcsok helyét, és a 7.6-os normalizálási csúcsértékeket (mérés alapján).
- **Szűk tűréssel finomíthatja:** a színpalettát. HEX-enként legfeljebb ±10° hue, ±10% saturation és ±10% value eltérés megengedett, és ezt a 02-esnek dokumentálnia kell. Új szín nem jöhet be.
- **Nem módosíthatja:** a formátumot, a loop-szabályt, a kiválasztott koncepciót, a méretarányokat és a reakció-tartományokat.
- **Konfliktus esetén** a 02-art-director jelez a felhasználónak, és nem talál ki saját megoldást.

---

## 1. Kreatív esszencia (logline)

> *Egy füstös, föld alatti betonszentélyben folyékony higanyszív lebeg. Minden basszusütésre összerándul, felizzik és hullámzik. Fölötte és alatta két nehéz, krómozott brutalista felirat áll, mint egy totem. A neon élfények a dobbal együtt lélegeznek. 8 másodperc, aminek nincs eleje és nincs vége.*

Hangulati kulcsszavak: *underground rave bunker, 3 AM, cigarette smoke haze, mercury, toxic Y2K chrome, brutal weight, bass pressure, hypnotic loop.*

---

## 2. Három koncepció (Midjourney / Stable Diffusion prompt stílusban)

> A promptok angolul vannak (MJ/SD szintaxis), a leírások magyarul. **Csak az 3. fejezetben kiválasztott koncepció kerül megvalósításra. A másik kettő kizárólag hangulati referencia.** A 03–06 agentek nem keverhetnek elemeket a nem kiválasztott koncepciókból.

### KONCEPCIÓ A: „MERCURY TOTEM” (AJÁNLOTT, lásd 3. fejezet)

**Logline:** Függőleges totem-kompozíció. Felül a `MOLLY` felirat, középen egy lebegő, folyékony higanygömb (Mercury Heart) hat keringő higanycseppel, alul a `WOOD` felirat. A tér egy fekete tükör-higany padlójú brutalista betonakna, két oldalt neon élcsíkos monolitokkal, sűrű, lassan kavargó füsttel és felülről a ködbe vágó fehér fénypászmával.

**Midjourney prompt:**
```
vertical totem composition, a levitating sphere of liquid chrome mercury at the center, its surface rippling with slow viscous waves, six small mercury droplets orbiting it in a tilted ring, massive extruded brutalist typography "MOLLY" above and "WOOD" below, ultra-bold uppercase sans-serif letters made of mirror-polished liquid chrome with thin hot magenta and electric cyan neon rim light tracing every edge, standing between two raw black concrete monoliths with glowing neon edge strips, black mirror floor of still mercury reflecting everything, dense volumetric cigarette smoke haze filling an underground concrete bunker, a single cold white god-ray spotlight cutting down through the fog with striped gobo shadows, dark Y2K aesthetic, aggressive riddim aesthetic, hardstyle rave energy, deep blacks, high contrast, rim lighting, volumetric fog, caustic reflections, octane render, unreal engine 5, cycles path tracing, 8k, ultra detailed, cinematic, hypnotic seamless loop, spotify canvas --ar 9:16 --style raw --v 6.1 --chaos 8 --stylize 350
```
**Negative prompt (SD):** `daylight, sunlight, pastel colors, cartoon, low poly, flat shading, matte plastic chrome, rust, people, faces, hands, lens dirt, watermark, logo, blurry text, misspelled text, cluttered background, warm orange grading`

**Anyagok:** A higany és a króm `Metallic 1`, roughness 0.02–0.08 között, így szinte tökéletes tükör. A beton matt, majdnem fekete, finom porózus roughness-variációval. A padló fekete tükör-higany, alig látható, lassan kúszó fodrozódással.
**Fény:** felülről hideg fehér spot gobo-csíkokkal a ködben, hátulról balról magenta, jobbról cián rim. Az ultraviola fill nagyon halk.
**Mozgás:** A gömb egy teljes fordulatot tesz 8 másodperc alatt, a cseppek ellentétes irányban keringenek. A felület hullámzása körpályás zajmintavétellel loopol. A kamera lassan, ingaszerűen lebeg.
**Basszus-reakció:** A gömb összenyomódik (squash), felülete erősebben hullámzik, a neon felizzik, a kamera lefelé „bólint”. Snare-re a feliratok éle villan, és a feliratok egy hajszálnyit megugranak.
**Blender-megvalósíthatóság:** Teljesen procedurális. UV-gömb + Subdivision + Displace modifier beépített procedurális textúrával, `Text` objektumok a beépített fonttal, primitív kockák és síkok, Principled Volume. Szimuláció nincs.

---

### KONCEPCIÓ B: „CHROME CIGARETTE RITUAL” (csak hangulati referencia)

**Logline:** Óriási, folyékony krómból öntött cigaretta lebeg átlósan a képben. A parazsa izzó neon-magenta gyűrű, a belőle felszálló füst a teljes 9:16-os keretet kitölti. Függőlegesen, a kép bal szélén, felfelé olvasva fut a `CIGARETTA` felirat nyers, vastag betűkkel.

**Midjourney prompt:**
```
a giant cigarette sculpted from liquid chrome floating diagonally in a pitch black void, the ember is a ring of pulsing hot magenta neon, thick volumetric smoke rising and curling to fill the vertical frame, smoke lit from behind by electric cyan rim light, huge brutalist vertical typography "CIGARETTA" running bottom to top along the left edge, heavy extruded chrome letters with neon edge glow, dark Y2K aesthetic, aggressive riddim aesthetic, underground club atmosphere, mercury reflections, rim lighting, volumetric fog, octane render, unreal engine 5, ultra detailed macro product shot, high contrast, seamless loop, spotify canvas --ar 9:16 --style raw --v 6.1 --stylize 300
```
**Negative prompt (SD):** `realistic tobacco texture, paper, ash mess, people, hands, mouth, daylight, warm cozy lighting, cartoon, low poly, watermark`

**Miért nem ez:** A hitelesen kavargó füst loopolva (Mantaflow nélkül) nehezen hozható. A cigaretta-motívum platformszabályozási kockázatot is hordozhat. Az átlós főtárgy a keskeny 9:16-os keretben sok üres sarkot hagy.

---

### KONCEPCIÓ C: „SUBWOOFER CATHEDRAL” (csak hangulati referencia)

**Logline:** Végtelen brutalista betonfolyosó, a falakban egymás fölé rakott, folyékony krómból öntött hangszórómembránok, amelyek a basszusra kidomborodnak. A padlón neon-cián élcsíkok futnak a fókuszpont felé, a mélyben a `MOLLYWOOD` felirat lebeg. A kamera lassú, végtelenített dolly-val halad előre (moduláris ismétlődés).

**Midjourney prompt:**
```
endless brutalist concrete corridor seen in one-point perspective, walls built from stacked speaker cones made of liquid chrome, the cones bulging outward with bass pressure, glowing electric cyan and hot magenta neon edge strips running along floor and ceiling toward a vanishing point, floating extruded brutalist typography "MOLLYWOOD" deep in the haze, dense volumetric fog with light shafts, wet black reflective floor, dark Y2K aesthetic, aggressive riddim aesthetic, hardstyle warehouse rave, rim lighting, volumetric fog, octane render, unreal engine 5, ultra detailed, symmetrical, cinematic, infinite seamless loop, spotify canvas --ar 9:16 --style raw --v 6.1 --stylize 400
```
**Negative prompt (SD):** `people, crowd, daylight, colorful, cartoon, cluttered, warm tones, low poly, watermark`

**Miért nem ez:** A végtelen folyosó-dolly elveszi a fókuszt egyetlen hősobjektumról. A 9-betűs felirat a távolban apró és olvashatatlan. A sok hangszóró sok drivert és sok renderidőt jelent, kisebb vizuális hatással.

---

## 3. KIVÁLASZTOTT KONCEPCIÓ: **A – „MERCURY TOTEM”**

**Döntés:** A megvalósítás kizárólag az **A – Mercury Totem** koncepcióra épül. A modell, az anyagok, a fények és az animáció is erre készül.

**Indoklás:**
1. **9:16-ra született.** A függőleges totem (felirat, gömb, felirat) kitölti a portré keretet, és nincsenek üres sarkok.
2. **Egyetlen hős-fókuszpont,** a higanyszív. Erre a basszus-reakció tisztán, olvashatóan ül rá.
3. **Matematikailag tiszta loop.** Minden mozgás egész fordulatú forgás, illetve a 240 osztójára periodikus mozgás. A „folyékony” felület körpályán mintavételezett zajjal loopol. Nincs szimuláció.
4. **100%-ban procedurális Blenderben.** Primitívek, `Text` objektumok a beépített fonttal, modifierek és Principled shaderek. Külső modell, textúra, HDRI és font nincs.
5. **Rövid, olvasható tipográfia.** `MOLLY` és `WOOD`: két rövid, csupa nagybetűs ASCII szó, amelyek együtt a dal nevének második szavát adják.

---

## 4. Vizuális biblia: Mercury Totem részletesen

### 4.1 A tér
- **Az akna:** Zárt, föld alatti brutalista betonbunker. Hátul egy masszív betonfal van, rajta egyetlen vízszintes, bemélyített neon-rés a gömb magasságában. Két oldalt egy-egy hatalmas, négyzetes keresztmetszetű betonmonolit áll, amelyek csak részben lógnak be a képbe. A belső függőleges élükön vékony neoncsík fut (balra magenta, jobbra cián).
- **A padló:** Fekete tükör-higany felület, amely mindent visszatükröz. Ettől a totem „kétszer” látszik, lefelé elmosódva.
- **A levegő:** Sűrű, nehéz, cigarettafüst-szerű volumetrikus köd. Nem egyenletes, hanem lassan kavargó, foltos sűrűségű, és a fény benne pászmákra törik.

### 4.2 A hősök
- **Mercury Heart (higanyszív):** Lebegő gömb, amelynek felülete viszkózus, lassú, nagy hullámhosszú hullámokban mozog, mint a higany a súlytalanságban. Nem fröcsköl és nem bomlik szét: egyben marad, csak lélegzik.
- **Higanycseppek:** Hat kisebb, tökéletes tükörgömb ferde gyűrűben kering a szív körül, eltérő méretben.
- **Tipográfia:** A felső `MOLLY` és az alsó `WOOD` vastag, mélyen extrudált, csupa nagybetűs, szoros betűközű, nehéz tömbbetű. Az anyag folyékony króm. Az éleken vékony neon élfény fut (fresnel- és facing-maszk), mögöttük egy halvány neon kontúr-glow lebeg. A betűk nem dőlnek, nem forognak, nem torzulnak. **Brutálisan stabilak, olvashatók.** Csak a snare-re ugranak meg minimálisan.

### 4.3 Anyagviselkedés
| Felület | Viselkedés |
|---|---|
| Liquid chrome (szív, cseppek, betűk) | Hidegszürke, szinte tökéletes tükör. Roughness 0.02–0.08 között, nagyon finom, alacsony frekvenciájú procedurális variációval (ujjlenyomat-szerű foltok). Halvány, hideg anizotróp-jellegű csillogás. Mindent a neonból és a reflexiós kártyákból kap, maga nem világít. |
| Mercury floor | Fekete-szürke tükör, roughness 0.02–0.05. Lassú, sekély procedurális bump-fodrozódás, amely a basszusra erősödik. |
| Beton (monolitok, fal) | Matt, majdnem fekete. Roughness 0.75–0.95, kétrétegű Noise/Voronoi pórus- és foltvariáció, élkopás (Bevel node maszk) halványabb szürkével. |
| Neon csíkok, rés, reflexiós kártyák | Tiszta emisszió, enyhe túlégés AgX alatt. Erősségük audio-driven. |
| Füst | Principled Volume. Sűrűsége procedurális Noise-mintázat, színe füstös grafit, gyenge ultraviola árnyalattal. Erős előreszórás (anisotropy), hogy a fénypászmák látszódjanak. |

**Kritikus:** Sötét világban HDRI nélkül a króm feketét tükrözne. Ezért **a 7.4-ben felsorolt reflexiós kártyák és neoncsíkok kötelező geometriák**. Ezek adják a króm fényét.

### 4.4 Fény dramaturgia
- **Key:** Felülről, kissé elölről lefelé vágó hideg-fehér spot, procedurális csík-gobóval. A ködben látható fénykúpot rajzol, és a szív tetején éles highlightot ad.
- **Rim (magenta) és Accent (cián):** Hátul balra és hátul jobbra elhelyezett keskeny area fények, amelyek a szív és a betűk kontúrját vágják ki a sötétből. A két oldal színben szétválik: bal oldal magenta, jobb oldal cián (Y2K split-tone).
- **Fill:** Nagyon halk, ultraviola, nagy area fény elölről. Csak annyi, hogy a fekete ne legyen digitálisan halott.
- **Kontraszt:** A kép kb. 70%-a mélyfekete vagy grafit. A fény az élekben, a ködben és a tükröződésekben él.

### 4.5 Kompozíció (9:16)
- Szimmetrikus, centrális totem. A függőleges tengely a kép közepe.
- Felül a `MOLLY` (a képmagasság kb. 74–86%-a között), középen a szív (kb. 45–63%), alul a `WOOD` (kb. 29–37%). A pontos koordinátákat a 7.4 tartalmazza.
- **Spotify UI-biztos sáv:** A Spotify felülete a Canvas alsó és felső részére UI-t rajzol, ezért fontos elem csak a képmagasság **20%–85%** közötti sávjában és a vízszintes **8–92%** között lehet. A Spotify általában nem javasolja a szöveget a Canvasban. A projekt kifejezetten kéri, ezért a felirat **grafikai elemként**, középen, az UI-sávoktól távol áll.

### 4.6 Mozgás dinamikája
- **Alap (zenétől független), nyugodt, hipnotikus réteg:**
  - A szív lassan forog (1 fordulat / 240 frame).
  - A cseppgyűrű ellentétesen kering (1 fordulat / 240 frame).
  - A szív lebeg (Z, periódus 240), a két felirat finoman lebeg eltérő fázissal (periódus 120).
  - A kamera ingaszerűen ível (yaw, periódus 240) és lélegzik (Z, periódus 120).
  - A füst körpályán kavarog (periódus 240).
  - Több, a 240 osztóival megadott periódus egymásra rétegzése adja a nem-mechanikus, organikus érzetet úgy, hogy közben a loop zárt marad.
- **Audio réteg, agresszív és impulzusszerű:** A basszus „nyomást” ad: a szív összenyomódik, a felület felkorbácsolódik, a neonok felrobbannak, a kamera lefelé bólint, a köd sűrűsödik. A snare „ostorcsapás”: a betűk élfénye villan, a betűk hajszálnyit megugranak, a key spot felvillan, a kamera oldalra rándul.
- A **ritmust kizárólag a sütött audio görbék adják** (`Audio_Controller`). Kulcskockázott, ütemre szinkronizált mozgás nincs, így a koncepció BPM-független.

---

## 5. Blender-megvalósíthatósági elvek (mindenre érvényes)

1. **Minden procedurális, `bpy`-ból építve:** primitívek (UV Sphere, Cube, Plane), modifierek (Subdivision, Displace, Bevel), `Text` objektumok, Principled BSDF / Emission / Principled Volume, és beépített procedurális textúrák (Noise, Voronoi, Wave; a Displace modifierhez a beépített `CLOUDS` vagy `VORONOI` textúratípus).
2. **Tilos:** külső modell, külső kép- vagy textúrafájl, HDRI, külső font (Windows TTF, pl. Arial Black, nem tölthető be), Mantaflow füst vagy folyadék, részecske- és fizikai szimuláció, Python autoexec-et igénylő driver.
3. **Font:** kizárólag a Blender beépített fontja (`bpy.data.fonts` közül a `<builtin>` filepath-ú „Bfont”, amit a `Text` objektum alapból kap). `bpy.data.fonts.load()` nem hívható. A brutalista karaktert az extrude, a bevel, a „faux bold” `offset`, a szoros betűköz és a csupa nagybetű adja.
4. **Neon él a `Text` objektumon** (görbe, nem mesh, ezért a Pointiness nem használható):
   - (a) Shaderben `Layer Weight` (Facing és/vagy Fresnel) maszk → ColorRamp → Emission keverése a krómra (`EMIT_TypeRim` node).
   - (b) Külön kontúr-glow objektum: a betű duplikátuma nagyobb `offset`-tel, a betű mögé tolva, csak emisszióval (`EMIT_TypeGlow` node).
   - A szöveget mesh-é konvertálni nem kötelező. Ha a 03-as quad-validáció miatt mégis konvertálja, a fenti shader-módszer változatlanul működik.
5. **Loopoló zaj:** Animált zaj (szív-displacement, füst, padlófodor) **csak zárt körpályán mozgó koordinátarendszerből** mintavételezhető. Egy Empty kering egy 240 frame alatt egy teljes fordulatot tevő pivot körül, és ez a textúra-koordináta objektum. Lineárisan sodródó W- vagy offset-érték **tilos**, mert nem zár.
6. **Rig:** egy egyszerű Armature (`RIG_Main`) a kulcskockázott alapmozgásokhoz (csontlista: 7.9). Az audio-driverek az objektumok **delta-transzformjaira** vagy a shader- és lámpaértékekre kerülnek, így nem ütköznek a kulcskockákkal.

---

## 6. Prioritási és precedencia-szabályok

1. A **7. fejezet számai** felülírnak minden más leírást (a prózát, a promptot és a 01-es palettát is a 0. fejezet tűrésén túl).
2. Csak az **A koncepció** valósul meg. B és C hangulati referencia.
3. Ha a 01-es mérés olyan adatot hoz, ami ütközik a 7. fejezettel (pl. a dal legjobb 8 másodperce nem a dropban van), a 02-es jelez a felhasználónak, és nem dönt önállóan.
4. A 02-es az elnevezést véglegesítheti. Az itt javasolt nevek (`GEO_`, `MAT_`, `LGT_`, `CAM_`, `EMP_`, `RIG_`, `CTL_`) a kiindulópontok, a számértékek viszont kötöttek.

---

## 7. KÖTELEZŐ PARAMÉTEREK (a 02–06 agentek szigorúan követik)

### 7.1 Formátum és render
| Paraméter | Érték |
|---|---|
| Felbontás | **1080 × 1920 px** (`resolution_x=1080`, `resolution_y=1920`, `resolution_percentage=100`; tesztrendernél 50% megengedett) |
| Képarány | **9:16** portré, pixel aspect 1:1 |
| FPS | **30** (`fps=30`, `fps_base=1.0`) |
| Hossz | **8.000 s = 240 frame** |
| Frame range | **`frame_start=1`, `frame_end=240`** |
| Render motor | Cycles (GPU, ha elérhető), `view_transform='AgX'`, look: `AgX - Punchy` vagy `AgX - Base Contrast` |
| Mintavétel | Végső: 256–512 sample + denoise (OpenImageDenoise). Teszt: 32–64. |
| Motion blur | Be, shutter **0.5** frame |
| Kimenet | PNG szekvencia (16 bit) → H.264 MP4, **hang nélkül** (a Spotify Canvas néma), 1080×1920, 30 fps |
| Volume | Step rate 1.0 (teszt: 2.0), max steps ≥ 512 |

### 7.2 Loop-szabály (SEAMLESS)
1. **Periódus = 240 frame.** A **241. frame állapota ≡ az 1. frame állapotával**. Renderelni csak az 1–240 tartományt kell.
2. **Tilos** ugyanazt az értéket az 1. és a 240. frame-re is kulcsolni, mert ez duplikált képkockát, vagyis akadást okoz a varratnál.
3. Minden kulcskockázott periodikus görbe: kulcs az **1.** és a **241.** frame-en azonos értékkel, a görbén **`Cycles` F-Curve modifier**.
4. Folyamatos forgás: **lineáris** interpoláció, 1. frame = 0°, 241. frame = ±360° (vagy ennek egész többszöröse), `Cycles` modifier.
5. **Megengedett periódusok** (a 240 osztói): **240, 120, 80, 60, 48, 40, 30, 24** frame. Minden más periódus tilos.
6. Animált procedurális zaj: kizárólag körpályás koordinátából (5. fejezet 5. pont), a pálya periódusa 240 frame.
7. **Audio görbék:** a 8 másodperces ablak az 1–240 frame-re képeződik le (a kezdőpontot a `01_analysis.md` adja). Az ablak elejére és végére **8 frame-es crossfade** kell (a 233–240. frame az 1. frame értéke felé simul). Tűrés: **|v(1) − v(240)| ≤ 0.05** (normalizált értéken). A 06-os ezt kiírja.
8. Alapállapot-ellenőrzés: minden kulcsolt vagy driverrel hajtott paraméterre **|érték(241) − érték(1)| < 0.001** (az audio görbék kivételével, azokra a 7. pont vonatkozik).

### 7.3 Színpaletta (HEX, sRGB; shaderben lineárisra konvertálva)
| Szerep | Név | HEX | Képarány cél |
|---|---|---|---|
| Háttér / világ | VOID | **#040406** | ~45% |
| Füst / köd szín | SMOKE | **#15141B** | ~20% |
| Beton (matt) | CONCRETE | **#1C1C21** (variáció: **#26262C**) | ~10% |
| Króm alapszín (fém F0) | CHROME | **#D7DBE3** | ~15% |
| Króm / sötét fém variáció | GUNMETAL | **#3A3E48** | ~2% |
| Elsődleges neon (bal rim, `MOLLY` él) | NEON MAGENTA | **#FF1F8F** | ~4% |
| Másodlagos neon (jobb accent, `WOOD` él) | NEON CYAN | **#00E8FF** | ~3% |
| Fill / köd árnyalat | ULTRAVIOLET | **#6A00FF** | ~1% |
| Key spot | WHITE HOT | **#F2F6FF** (≈ 7000 K) | highlightok |

Tilos: meleg narancs vagy sárga tónus, telített zöld, és tiszta #FFFFFF felületszín. A palettán kívüli szín nem jöhet be (a 01-es tűrése: 0. fejezet).

### 7.4 Méretarányok és pozíciók (méter, valós skála; X = jobbra, Y = a kamerától befelé, Z = fel)
| Elem (javasolt név) | Geometria | Méret | Pozíció (közép) |
|---|---|---|---|
| `GEO_Floor_Mercury` | Plane | 16 × 16 m | (0, +3.0, 0.0) |
| `GEO_Core_Mercury` (higanyszív) | UV Sphere 64×32 + Subdiv 2 (render 3) + Displace | sugár **0.75 m** | (0, 0, **3.20**) |
| `GEO_Droplet_01…06` | UV Sphere + Subdiv | sugár **0.06 / 0.08 / 0.10 / 0.12 / 0.09 / 0.14 m** | a szív körül, pálya sugara **1.15–1.35 m**, a pályasík X tengely körüli dőlése **18°**, egyenletes 60°-os kiosztás |
| `GEO_Text_Top` | Text: `MOLLY` | teljes szélesség **3.0–3.4 m**, sapkamagasság ≈ **0.65 m**, extrude **0.14 m**, bevel depth **0.015 m** (resolution 4), `offset` **0.008 m**, `space_character` **0.90** | középre igazítva (align X/Y = CENTER), (0, **+0.60**, **5.00**) |
| `GEO_Text_Bottom` | Text: `WOOD` | ugyanazok a beállítások és font size, mint a `MOLLY`-nál (szélesség ≈ 2.6–3.0 m) | (0, **+0.60**, **1.50**) |
| `GEO_TextGlow_Top / _Bottom` | Text duplikátum, csak emisszió | `offset` **0.025 m**, extrude **0.02 m** | a betű mögött **+0.18 m** Y-ban |
| `GEO_Slab_L / _R` (monolitok) | Cube + Bevel (0.02 m) | **0.9 × 0.9 × 9.0 m** | (**∓2.55**, +1.5, 4.5) |
| `GEO_NeonStrip_L / _R` | Cube | **0.03 × 0.03 × 8.0 m** | a monolitok belső, kamera felőli függőleges élén (X = ∓2.09, Y = +1.04, Z = 4.5) |
| `GEO_Wall_Back` | Cube | **12 × 0.5 × 12 m** | (0, **+7.0**, 6.0) |
| `GEO_NeonSlit_Back` | Cube (a falba süllyesztve) | **6.0 × 0.05 × 0.06 m** | (0, +6.74, **3.20**) |
| `GEO_ReflCard_Top_01…03` (kötelező reflexió-forrás) | Plane, emisszió, kamerának láthatatlan (`visible_camera=False`) | **6.0 × 0.08 m**, egymástól 0.6 m-re | Z = **8.5**, Y = −1.0 … +0.2, lefelé néz |
| `GEO_ReflCard_Back_01…03` (kötelező reflexió-forrás) | Plane, emisszió, kamerának láthatatlan | **4.0 × 0.10 m**, vízszintesen, egymás fölött 0.5 m-re | Y = **−11.0**, Z = 2.4 / 2.9 / 3.4, a szív felé néz |
| `GEO_Fog_Volume` | Cube (volume domain, a kamerát is tartalmazza) | **12 × 22 × 11 m** | (0, −2.0, 5.5) |
| `CAM_Main` | Kamera | lásd 7.5 | (0, **−8.00**, **2.90**) |
| `EMP_Cam_Target` | Empty | – | (0, 0, **2.90**) |

Kompozíció-ellenőrzés (35 mm, szenzor 36 mm, VERTICAL fit, 8 m távolság): látható magasság ≈ 8.23 m (Z ≈ −1.21 … 7.01), szélesség ≈ 4.63 m (X ≈ ±2.31). Az UI-biztos sáv az Y=0 síkban: **Z 0.44 … 5.79, X ±1.94**. A `MOLLY` teteje (≈ 5.33) és a `WOOD` alja (≈ 1.17) ezen belül van.

### 7.5 Kamera
| Paraméter | Érték |
|---|---|
| Objektív | **35 mm**, szenzor **36 mm**, `sensor_fit='VERTICAL'` |
| DoF | Be, fókusz: `EMP_Cam_Target`, **f/4.0** |
| Felépítés | `EMP_Cam_Pivot` (0, 0, 2.90) → gyereke a `CAM_Main`, Track To constraint az `EMP_Cam_Target`-re (vagy fix rotáció 90°, 0, 0) |
| Alapmozgás 1: ingaív | `EMP_Cam_Pivot` rot Z = **±4.0°** szinuszosan, periódus **240** (kulcsok: 1 → 0°, 61 → +4°, 121 → 0°, 181 → −4°, 241 → 0°; Bezier, `Cycles` modifier) |
| Alapmozgás 2: lélegzés | `CAM_Main` lokáció Z = **±0.06 m**, periódus **120** |
| Alapmozgás 3: dolly | `CAM_Main` lokáció Y = **±0.20 m**, periódus **240**, 60 frame fáziseltolással az ívhez képest |
| Tilos | Vágás, zoom (fókusztávolság-animáció), 6°-nál nagyobb ív |

### 7.6 Audio vezérlés (a 06-animator szerint)
- **Vezérlő:** `Audio_Controller` (Empty), custom propertyk: `["Bass"]`, `["Snare"]`.
- **Sávok:**
  - Bass: `sound_bake(low=20.0, high=150.0)`, `attack=0.005`, `release=0.18`
  - Snare: `sound_bake(low=2000.0, high=5000.0)`, `attack=0.002`, `release=0.08`
- **Normalizálás (kötelező, a sütött F-Curve-ön, nem a driver-kifejezésben):**
  - Mérd ki a sütött görbe maximumát az 1–240 ablakban (`peak`).
  - Adj a görbére `Generator` modifiert (Expanded polinom, együtthatók `[0.0, 1/peak]`), utána `Limits` modifiert (min 0.0, max 1.0).
  - Eredmény: **bass_n, snare_n ∈ [0, 1]**.
  - Ha a snare-sáv zajos: tegyél elé `Smooth`-ot, és a Generatorban egy küszöb-offsetet (`[-0.15/peak … ]`), majd újra Limits 0–1.
- **Driver-kifejezések:** kizárólag egyszerű, autoexec nélkül futó alak (`base + k*bass`, illetve `base - k*bass`), változó: `SINGLE_PROP`, target `Audio_Controller`.
- **Crossfade és tűrés:** 7.2 / 7.

### 7.7 Reakciók számszerűen (bass_n, snare_n ∈ [0,1]; „alapérték” = a választott konstans; a min–max a megengedett tartomány; a „hard cap” átléphetetlen)

**Kamera shake (a `CAM_Main` delta transzformjain, a kulcskockák fölött):**
| Trigger | Paraméter | Képlet (alapérték) | Megengedett k | Hard cap |
|---|---|---|---|---|
| Bass | `delta_location.z` (lefelé bólintás) | **−0.010 · bass_n** m | 0.006–0.014 m | 0.020 m |
| Bass | `delta_rotation_euler.y` (roll, a kamera nézeti tengelye körül) | **0.35° · bass_n = 0.00611 rad · bass_n** | 0.20–0.50° (0.00349–0.00873 rad) | 0.80° (0.01396 rad) |
| Snare | `delta_location.x` (oldalrándulás) | **+0.004 · snare_n** m | 0.002–0.006 m | 0.010 m |

**Emisszió (Emission Strength, Cycles):**
| Trigger | Node / anyag | Képlet (alapérték) | Megengedett k | Hard cap |
|---|---|---|---|---|
| Bass | `EMIT_Neon` (monolit-csíkok, `MAT_Neon_Magenta` / `MAT_Neon_Cyan`) | **6.0 + 24.0 · bass_n** | k = 14–34 | 40 |
| Bass | `EMIT_Slit` (hátsó rés) | **5.0 + 15.0 · bass_n** | k = 10–20 | 25 |
| Bass | `EMIT_TypeGlow` (kontúr-glow) | **3.0 + 9.0 · bass_n** | k = 6–12 | 15 |
| Snare | `EMIT_TypeRim` (betű-él fresnel) | **2.5 + 15.0 · snare_n** | k = 10–20 | 25 |
| (nincs) | `EMIT_ReflCard` (reflexiós kártyák) | **8.0** konstans (opcionálisan + 4.0 · bass_n) | 0–6 | 14 |

**Lámpák (Power, W):**
| Trigger | Lámpa | Képlet | Megengedett k | Hard cap |
|---|---|---|---|---|
| Bass | `LGT_Rim` (magenta), `LGT_Accent_Cyan` | **350 + 650 · bass_n** | k = 400–900 | 1300 |
| Snare | `LGT_Key` (spot) | **1200 + 400 · snare_n** | k = 200–600 | 1800 |

**Scale (squash and stretch):**
| Trigger | Objektum | Képlet (alapérték) | Megengedett k | Hard cap |
|---|---|---|---|---|
| Bass | `GEO_Core_Mercury` `delta_scale.x` és `.y` | **1.0 + 0.10 · bass_n** | k = 0.06–0.14 | 1.18 |
| Bass | `GEO_Core_Mercury` `delta_scale.z` (összenyomás) | **1.0 − 0.08 · bass_n** | k = 0.05–0.11 | ≥ 0.86 |
| Bass | Szív Displace modifier `strength` | **0.15 + 0.12 · bass_n** | k = 0.08–0.15 | 0.30 |
| Snare | `GEO_Text_Top/Bottom` (+ glow) `delta_scale` (x, y, z egyformán) | **1.0 + 0.025 · snare_n** | k = 0.015–0.035 | 1.045 |
| Bass | `GEO_Droplet_*` `delta_scale` (egyformán) | **1.0 + 0.15 · bass_n** | k = 0.08–0.20 | 1.25 |

**Atmoszféra és padló:**
| Trigger | Paraméter | Képlet | Megengedett k | Hard cap |
|---|---|---|---|---|
| Bass | `GEO_Fog_Volume` Principled Volume `Density` | **0.035 + 0.015 · bass_n** | k = 0.008–0.020 | 0.060 |
| Bass | Padló bump `Strength` | **0.05 + 0.15 · bass_n** | k = 0.08–0.20 | 0.30 |

A betűk Z-pozíciója, forgása és alakja a basszusra **nem** reagál (olvashatóság).

### 7.8 Alap (nem audio) mozgások
| Elem | Mozgás | Érték | Periódus | Interpoláció |
|---|---|---|---|---|
| Szív | rot Z | 0° → **+360°** | 240 | lineáris + `Cycles` |
| Szív | lebegés Z | **±0.05 m** | 240 | Bezier + `Cycles` |
| Cseppgyűrű (`EMP_Droplet_Orbit`) | rot Z | 0° → **−360°** | 240 | lineáris + `Cycles` |
| Cseppek egyenként | saját lebegés Z | **±0.03 m**, fázis: n × 40 frame | 120 | Bezier + `Cycles` |
| `GEO_Text_Top` | lebegés Z | **±0.025 m** | 120 | Bezier + `Cycles` |
| `GEO_Text_Bottom` | lebegés Z | **±0.025 m**, **60 frame** fáziseltolással | 120 | Bezier + `Cycles` |
| `EMP_Noise_Pivot` (szív-displacement) | rot Z, gyereke `EMP_Noise_Orbit` X = **0.60 m**-en | 0° → 360° | 240 | lineáris + `Cycles` |
| `EMP_Fog_Pivot` (füst-zaj) | rot Z, gyereke `EMP_Fog_Orbit` X = **1.50 m**-en | 0° → −360° | 240 | lineáris + `Cycles` |
| `EMP_Floor_Pivot` (padló-fodor) | rot Z, gyereke `EMP_Floor_Orbit` X = **0.80 m**-en | 0° → 360° | 240 | lineáris + `Cycles` |
| Kamera | 7.5 szerint | – | 240 / 120 | – |

### 7.9 Rig (minimál)
`RIG_Main` Armature, csontok: `root` → `core` (szív + `EMP_Droplet_Orbit`), `type_top`, `type_bottom`, `cam_pivot` (opcionális). A kulcskockák a csontokra vagy a pivot Empty-kre kerülnek, az audio-driverek a **delta** csatornákra. A kettő soha nem ugyanazt a csatornát írja.

### 7.10 Fények (alapértékek; az audio-moduláció a 7.7 szerint)
| Lámpa | Típus | Pozíció | Szín | Power / méret |
|---|---|---|---|---|
| `LGT_Key` | Spot, procedurális csík-gobo (Wave/Brick textúra a lámpa node-fájában) | (0, −1.5, **9.0**), a szívre irányítva | #F2F6FF (≈ 7000 K) | **1200 W**, spot size **28°**, blend 0.35, radius 0.05 m |
| `LGT_Rim` | Area, Rectangle | (**−2.0, +2.2, 3.4**), a szív és a kamera felé | #FF1F8F | **350 W**, 1.5 × 0.15 m |
| `LGT_Accent_Cyan` | Area, Rectangle | (**+2.0, +2.2, 3.4**), szimmetrikusan | #00E8FF | **350 W**, 1.5 × 0.15 m |
| `LGT_Fill` | Area, Square | (0, **−6.0**, 4.0), a totem felé | #6A00FF | **60 W**, 4 × 4 m |
| IES-szimuláció | a `LGT_Key` falloff ColorRamp-pel (05-ös fallback) | – | – | – |

### 7.11 Anyag-paraméterek (kötött tartományok)
| Anyag | Base Color | Metallic | Roughness | Egyéb |
|---|---|---|---|---|
| `MAT_Chrome_Liquid` (szív, cseppek, betűk) | #D7DBE3 → #3A3E48 variáció (≤ 15%) | **1.0** | **0.02–0.08** (Noise scale 2–6) | Bump strength ≤ 0.05 |
| `MAT_Mercury_Floor` | #3A3E48 → #040406 | **1.0** | **0.02–0.05** | Bump: Noise/Wave a padló orbit-empty koordinátáiból |
| `MAT_Concrete_Dark` | #1C1C21 / #26262C | 0.0 | **0.75–0.95** | Kétrétegű Noise + Voronoi, Bevel-maszkos élkopás |
| `MAT_Neon_Magenta` / `MAT_Neon_Cyan` | – | – | – | Emission node neve: `EMIT_Neon`, alapérték 6.0 |
| `MAT_Type_Rim` réteg | – | – | – | `Layer Weight` Facing blend **0.15–0.30** → ColorRamp → `EMIT_TypeRim` (`MOLLY`: magenta, `WOOD`: cián) |
| `MAT_Type_Glow` | – | – | – | `EMIT_TypeGlow`, alapérték 3.0 |
| `MAT_Fog` | Principled Volume, szín #15141B, árnyalat #6A00FF ≤ 10% | – | – | Density 0.035, Anisotropy **0.55–0.70**, a Density Noise-maszkkal (scale 0.3–0.6, `EMP_Fog_Orbit` koordinátából) |

---

## 8. Tilos-lista (gyors ellenőrzéshez)
- Külső asset: modell, kép, textúra, HDRI, font.
- Szimuláció: Mantaflow, részecske, cloth, rigid body.
- Lineárisan sodródó zaj (W vagy offset), 240-et nem osztó periódus, azonos kulcs az 1. és a 240. frame-en.
- Szöveg torzítása, forgatása, a basszusra mozgó betűk, 5 betűnél hosszabb sor, nem ASCII karakter.
- Palettán kívüli szín, meleg tónus.
- Python autoexec-et igénylő driver-kifejezés.
- Elemek elhelyezése az UI-biztos sávon (7.4) kívül, kivéve a háttér-környezetet (padló, monolitok, fal, köd).

---

## 9. Átadás és ellenőrzés agentenként
| Agent | Mit vegyen át innen | Kész, ha… |
|---|---|---|
| 01-ref-analyzer | 0. fejezet: a videók és a hang tényleges elemzése, a legjobb 8 s-os ablak, a bass/snare csúcsok frame-ben (1–240), BPM | a `01_analysis.md` megadja az ablak kezdőpontját, és jelzi a palettától való eltéréseket |
| 02-art-director | 7. fejezet szó szerint + elnevezés véglegesítése | minden szám a 7. fejezetből származik, nincs ellentmondás |
| 03-modeler | 7.4, 7.9, 5.3–5.4 | minden objektum a megadott pozíción és méretben van, beépített font, nincs külső asset |
| 04-lookdev-artist | 4.3, 7.3, 7.11 | a node-nevek (`EMIT_*`) léteznek, a reflexiós kártyák világítanak, a króm nem fekete |
| 05-lighting-artist | 4.4, 7.1, 7.5, 7.10 | AgX, 1080×1920, 30 fps, 1–240, a fénykúp látszik a ködben |
| 06-animator | 7.2, 7.6, 7.7, 7.8 | \|v(241)−v(1)\| < 0.001 (alap), \|v(1)−v(240)\| ≤ 0.05 (audio), minden reakció a tartományon belül |

---

## 10. Nyitott kérdések (a 01-ref-analyzernek)
1. Melyik 8 s-os ablak loopol a legjobban (javasolt: a drop utáni első teljes ütemcsoport)? Kezdő időbélyeg másodpercben.
2. BPM és ütemrács. Ez csak tájékoztató: a koncepció BPM-független, a ritmust a sütött görbék adják.
3. Van-e a 4 videóban olyan mozgás-, kamera- vagy színjellemző, ami a 0. fejezet tűrésén belül finomíthatja a palettát vagy a kamera-ív amplitúdóját (max. a 7.5-ös tartományban)?
