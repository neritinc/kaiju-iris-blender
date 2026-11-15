# 02 – MÉRNÖKI 3D SPECIFIKÁCIÓ: „IRIS SOVEREIGN”

> Szerző: 02-art-director (Technical Art Director), 2026-11-12. Ez a fájl teljesen felülírja a 20:09-es régi specet („Mercury Totem”), annak egyetlen eleme sem érvényes.
> Mérvadó bemenet: `pipeline/00_master_concept.md` (IRIS SOVEREIGN, **6. fejezet kötelező paraméterei**). Kiegészítő bemenetek: `pipeline/01_analysis.md`, `pipeline/01_visual_breakdown.md`, `audio_metrics.json` (ezt NEM használjuk, lásd 0.3), valamint a saját szemmel megnézett kockák: `pipeline/frames/IMG_6422/0003.png`, `0019.png`, `pipeline/frames/IMG_7563/0052.png`.
> Címzettek: 03-modeler, 04-lookdev-artist, 05-lighting-artist, 06-animator.
> Futtatókörnyezet: **Blender 5.2**, kizárólag `"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"`, háttérben (`-b`), bpy scripttel. MCP nincs.
> Alkalmazott skill-módszertan: blender-director (production brief, geometria-tierek, objektumonkénti emisszió, AgX), hard-surface (bevel-tierek, boolean-szabályok, weighted normal, instancelt greeble), procedural-modeling (seed, paramétertartományok), rigging + mechanical-rig (constraint-first, rigid parent, nincs súlyfestés), materials (master + instance, `MAT_` nevek), lighting (motivált fények, volumetrika), vfx-fx (domain-szabályok, timing brief), camera-cinematography (target-empty, szándékos optika), naming-conventions, polycount-budgets, reference-analysis-template, asset-pipeline.

**Precedencia:** 00/6. fejezet számai > ez a spec > az agent-fájlok (`.claude/agents/0x-*.md`) általános példái > skill-alapértékek. A `(feltételezés)` jelölésű értékeket a koncepció nem rögzíti. Ezeket ez a spec véglegesíti a koncepció keretein belül, és indokolja. A 03–06 agentek ezeket ne bírálják felül, csak a 11. fejezet nyitott kérdéseinek megválaszolása után.

---

## 0. Bemenet-ellenőrzés (frissesség, ütközések)

### 0.1 Leltár
`referencia/` (Glob, 2026-11-12): `IMG_0836.MP4`, `IMG_6422.MP4`, `IMG_7563.MP4`, `IMG_9135.MP4`, `CIGARETTA MOLLYWOOD.wav`. Képfájl nincs. Ez egyezik a 01_analysis és a 00 koncepció leltárával. A saját szemmel ellenőrzött kockák alapján a koncepció témája egyezik a referenciákkal:
- 6422/0003: irizáló, vízszintes sávokból álló koponya, két ökölbe szorított kéz, fehér LED-fal, kockás plafon.
- 6422/0019: fehér visorral izzó koponya és fogsor, két nyitott, felfelé álló kéz ujjpercekkel, lila háttér.
- 7563/0052: koncentrikus gyűrűs lencse-szem, fogaskerék-perem, LED-pontsor, kék és piros rim.

**A 0–1. lépést nem kell újrafuttatni.**

### 0.2 Régi fájlok
A `pipeline/01_model.blend`, a `pipeline/02_textured.blend` és a `pipeline/03_lit_scene.blend` (a `.blend1` mentésekkel együtt) a régi koncepcióból készült, ezért **érvénytelen**. A 03 üres jelenetből indul (`--factory-startup`), és nem nyithatja meg vagy importálhatja őket. A lánc a következő fájlokat felülírja.

### 0.3 Ütközés: `audio_metrics.json` ≠ koncepció (NYITOTT, a felhasználónak jelezve)
| | 00 koncepció + 01_analysis | `audio_metrics.json` |
|---|---|---|
| Ablak kezdete | **60.48 s** | 77.856 s |
| Beat-frame-ek | 13, 26, 38, 50, 63 … | 1, 14, 25, 37, 48, 62 … |
| Drop | az ablakban nincs drop (build); a csúcs a 204. frame-en | 48. frame |
| BPM | 143.55 | 143.555 (egyezik) |

A két forrás **másik 8 másodpercet** ír le. A felhasználó a koncepciót tette kötelezővé, ezért ez a spec **kizárólag a 00/6.4 és 6.8–6.10 frame-listáit és súlyait használja**. A JSON `sub_bass_curve` és `full_energy_curve` görbéje **tilos meghajtóforrásként** (rossz ablak). A `pipeline/audio_window.wav` eredetét (melyik ablakból vágták) a 06-nak ellenőriznie kell. Ha a 77.856 s-os kivágás, akkor a 60.48 s-os ablakot újra kell vágni a `referencia/CIGARETTA MOLLYWOOD.wav`-ból.

### 0.4 Ütközés: elnevezési előtagok
A 02-es szerepleírás `GEO_/RIG_/CTL_/EMP_` előtagokat javasol, a 00/6.17 (kötelező) viszont `SM_`, `MAT_`, `LGT_`, `CAM_`, `COL_`, `EMPTY_CamTarget_Hero` előtagokat ír elő. **A koncepció nyer.** A koncepció által nem szabályozott kategóriákban a felhasználói szerepleírás előtagjai érvényesek (`RIG_`, `CTL_`, `EMP_`), mert a felhasználói előírás erősebb a skillnél (`ARM_`/`CTRL_`). Kivétel az `Audio_Controller`: a 06-os agent-fájl betű szerint ezt a nevet írja elő.

| Szerepleírás | Ebben a projektben |
|---|---|
| `GEO_` | `SM_` |
| `RIG_` | `RIG_` (armature) |
| `CTL_` | `CTL_` (rig-vezérlő empty), plusz `Audio_Controller` (globális audio- és show-vezérlő) |
| `EMP_` | `EMP_` (segéd-empty), kivétel: `EMPTY_CamTarget_Hero` |
| `MAT_`, `LGT_`, `CAM_` | változatlan |

### 0.5 Belső számellenőrzés (a koncepció számaiból levezetve)
- Kamera: 28 mm, 36 mm-es függőleges szenzor esetén a függőleges FOV 2·atan(18/28) = **65.5°**, a vízszintes 2·atan(10.125/28) = **39.7°**. A dőlés atan(0.73/16) = 2.6°. A koponya középpontja (0, 0, 4.5) a kép alulról mért **60.0%**-ánál van. ✓
- LED-fal teteje: **80.6%**. Truss-portál (11 m) teteje: **85.7%**. Az ívelt fal széle (x ≈ ±8.7, y ≈ +5.0) kívül esik a látómezőn (21 m-en ±7.6 m látszik). ✓
- C-sorok a hero kamerából: **87.5–96.4%** (a 00/25 „90–96%”-ot ír). A különbség elfogadható, a koncepció z-értékei maradnak.
- **Eltérés:** a koponya félszélessége 1.3 m, a kéz belső éle 3.3 − 1.0 = 2.3 m, így a rés **1.0 m**, nem 0.8 m (00/23). A középpontok és a 8.6 m-es teljes szélesség a mérvadó. A rés kérdése nyitott (11. fejezet, Q3).
- **Eltérés:** a 238-as gyenge snare lecsengéséről a 9. pont szerint „az 1–6. frame-be átnyúlik”, a 34. pont szerint „a 239–240. frame-be esik”. **A 34. pont érvényes** (specifikusabb). A 238-as snare nem fut át a loop-határon.

---

## 1. Téma-összefoglaló és forrás-hozzárendelés

**Mi épül:** végtelen fekete, sűrű füsttel teli tér, színpad nélkül. A középtengelyen lebeg egy gyöngyház-króm, 7 vízszintes lemezből álló mechanikus koponya. Mozgó állkapcsa és 12 lamellás írisszel tágulni képes kristálylencse-szemei vannak. Két oldalt két 3 m-es kibernetikus kéz áll tükrös szimmetriában. Mögöttük 3 egymásba ágyazott box-truss portál és egy 18 × 12 m-es ívelt LED-fal látszik. A teret 12 aktív fény- és lézercsoport (A–M; az I inaktív) tölti ki, a fekete tükörpadló mindent duplán visszatükröz.

| Jegy | Megvalósítás | Forrás |
|---|---|---|
| Vízszintes lemezes kranium, szem-sáv, fogsor | `SM_Char_Skull_*` | 6422 (0003, 0019) |
| Lencse-szem: fogaskerék-perem, LED-pontsor, üveg, írisz | `SM_Char_Eye_*` | 7563 (0052) |
| Két tükrözött, ujjpercenként szegmentált kéz | `SM_Char_Hand_R/L_*` | 6422 (0003, 0019, 0035 clay) |
| Gyöngyház-irizáló króm, anodizált panel | `MAT_Metal_PearlChrome`, `MAT_Metal_AnodizedDark` | 6422, 7563 |
| Zöld legyező, keret-nyalábok, vízszintes sorok, fénysík, nested square | A, B, C, L, F csoport | 6422 |
| V-lézerháló, vastag füstkúpok | G, D, M csoport | 7563 |
| Sunburst | H csoport | 9135 |
| Tükörpadló, LED-fal gyűrű/négyzet minta | `SM_Env_Floor`, `SM_Env_LEDWall` | 0836 |
| LED-fal háromszögrács | LED-fal 3. minta | 9135 |
| Clay-villanás | `NG_ClayOverride` | 6422, 7563 viewport-réteg |
| BPM, beat, basszus, snare, ablak | 7. fejezet | `CIGARETTA MOLLYWOOD.wav` (60.48 s) |

**Tiltva:** színpad, emelvény, DJ-pult, ember, tömeg, szöveg, logó, monogram, vízjel, piros vagy sárga lézer, tűz (az I csoport inaktív).

---

## 2. Projekt-állandók és technikai keret

| Paraméter | Érték |
|---|---|
| Felbontás | 1080 × 1920 (9:16), `resolution_percentage=100` (teszt: 50) |
| FPS | 30 (`fps_base=1.0`) |
| Frame range | `frame_start=1`, `frame_end=240`. **A (nem renderelt) 241. frame állapota azonos az 1. frame-ével**, a 240. frame nem ismétli az 1.-t |
| Időkonvenció | frame = s × 30 + 1 (1-alapú) |
| Motor | **Cycles** (feltételezés: a 00/56 glossy bounce ≥ 4 előírás, a vékony emisszív nyalábok fénye a füstben és a tükörpadló csak path tracinggel adja a kért képet). GPU: OPTIX → CUDA → HIP → ONEAPI, egyébként CPU |
| Light paths | max bounces 8, diffuse 3, **glossy 4**, transmission 8, **volume 2**, transparent 16. Light tree be. Emission sampling: Auto |
| Volume | step rate: teszt 1.0, végső **0.25** (a 00/61 szerint az 1 cm-es G-nyalábok is folytonosak legyenek); max steps 1024 |
| Mintavétel | teszt 64 + OIDN; végső 512 + OIDN (albedo/normal passokkal) |
| Motion blur | **ki** (feltételezés: a strobe- és flash-frame-ek élesek maradjanak, a rázkódás képkockánként olvasható legyen) |
| Színkezelés | View Transform `AgX`, Look **High Contrast** (az 5.2-es enum-nevet a `view_settings.bl_rna.properties['look'].enum_items` listából kell kiolvasni, pl. `AgX - High Contrast`), exposure 0.0 (±0.3), gamma 1.0 |
| Mértékegység | Metric, 1 BU = 1 m. Tengelyek: X jobbra, **+Y a mélység (a kamera −Y-ban áll)**, Z fel. Origó: a koponya alatti padlópont |
| Kimenet | PNG 16 bit szekvencia `pipeline/renders/final/####.png`, utána H.264 MP4. A hang a 7.9 szerint kerül rá |

**Fájllánc:** `scripts/build_model.py` → `pipeline/01_model.blend` → `scripts/build_materials.py` → `pipeline/02_textured.blend` → `scripts/build_lighting.py` → `pipeline/03_lit_scene.blend` → `scripts/animate_scene.py` → `final_animated_scene.blend` (projektgyökér). Tesztrenderek: `pipeline/renders/`.

---

## 3. Elnevezési konvenciók és collection-struktúra

### 3.1 Előtagok és formátum
Formátum: `PREFIX_Kategória_Név_Variáns`, PascalCase, kétjegyű számozás (`_01`). **Oldaljelölés: `_R` / `.R` = +X (a képen jobbra), `_L` / `.L` = −X.** Ez képoldal, nem anatómiai oldal: a +X oldali kéz anatómiailag a karakter bal keze. **Tilos** a `.001` végű név és az elnevezetlen objektum. A mesh/curve/light/camera datablock neve egyezzen az objektum nevével. Minden lámpának saját datablockja van, mert a driverek az `energy`-re kerülnek.

| Előtag | Típus | Példa |
|---|---|---|
| `SM_` | mesh és curve geometria | `SM_Char_Skull_Plate_03`, `SM_Laser_A_R04` |
| `MAT_` | anyag | `MAT_Metal_PearlChrome`, `MAT_LightInst_EyeCore_R` |
| `NG_` | shader node group (feltételezés) | `NG_ClayOverride`, `NG_LaserBeam` |
| `RIG_` | armature objektum és data | `RIG_IrisSovereign` |
| `CTL_` | rig-vezérlő empty custom property-kkel | `CTL_Skull`, `CTL_Hands` |
| `Audio_Controller` | globális audio- és show-vezérlő empty (egyetlen kivétel, 06-os előírás) | – |
| `EMP_` | segéd-empty (pivot, aim, kamera-lánc) | `EMP_CamOrbit`, `EMP_Aim_M_Skull` |
| `EMPTY_CamTarget_Hero` | kamera-célpont (00/24, betű szerint) | – |
| `LGT_` | lámpa | `LGT_Rim_Magenta`, `LGT_Spot_D_R03` |
| `CAM_` | kamera | `CAM_Main_Hero` |
| `COL_` | collection | `COL_Lasers_A` |

**Modifier-nevek:** `MIR_X`, `SOL_Shell`, `BOOL_<Vágás>`, `BVL_Primary`, `BVL_Panel`, `TRI_Ngon`, `SUB_Main`, `WN_Main`, `ARR_<Név>`, `CRV_<Név>`.
**Node-nevek** (a `name` és a `label` azonos; a driver-célpontoknál kötelező): `EMIT_*` (Emission), `VOL_*`, `NOI_*`, `VOR_*`, `WAV_*`, `CR_*` (ColorRamp), `MR_*` (Map Range), `LW_*` (Layer Weight), `BVN_*` (Bevel node), `MIX_*`, `TC_*`, `GEO_*` (Geometry node), `VAL_*`.

### 3.2 Collection-hierarchia (00/6.17, kiegészítve)
```
Scene Collection
├── COL_Character
│   ├── COL_Character_Skull     SM_Char_Skull_*, SM_Char_Eye_R_*, SM_Char_Eye_L_*
│   ├── COL_Character_Hand_R    SM_Char_Hand_R_*
│   ├── COL_Character_Hand_L    SM_Char_Hand_L_*
│   ├── COL_Character_Rig       RIG_IrisSovereign, CTL_Skull, CTL_Hands
│   └── COL_Greebles            (rejtett, nem renderelt) SM_Greeble_Bolt_Hex, SM_Greeble_LEDDot, SM_Greeble_Vent
├── COL_Environment             SM_Env_Floor, SM_Env_LEDWall, SM_Env_Truss_Portal_11/09/07,
│                               SM_Env_Truss_Ceiling, SM_Env_FloorSlot_*, SM_Env_Fixture_*
├── COL_Lasers
│   ├── COL_Lasers_A … COL_Lasers_H, COL_Lasers_J … COL_Lasers_M   (I nincs: inaktív)
├── COL_Lights                  LGT_*, EMP_Aim_M_*
├── COL_Cameras                 CAM_Main_Hero, EMPTY_CamTarget_Hero, EMP_Cam*, EMP_Focus_Skull
├── COL_FX                      SM_FX_SmokeDomain, Audio_Controller
└── COL_Booleans                (rejtett, nem renderelt) SM_Cutter_*
```
(feltételezés) Az `Audio_Controller` a `COL_FX`-be kerül, mert a 6.17-es kötelező listában nincs külön vezérlő-collection, és a füst, a flash és a strobe is innen fut.

---

## 4. Modell (03-modeler)

### 4.1 Production brief
| | |
|---|---|
| Típus | hero karakter (hard-surface mechanikus) + statikus környezet + emisszív nyalábok |
| Cél | cinematic (nem game asset). LOD és export nincs |
| Stílus | fotoreál PBR + stilizált neon emisszió (sci-fi-punk: tiszta króm-kiberpunk, nincs sárgaréz vagy rozsda) |
| Poligonkeret (kiértékelt, modifierekkel) | koponya-összeállítás ≤ 600 k tri; kezenként ≤ 350 k tri; truss összesen ≤ 300 k (instancing); LED-fal ≤ 60 k; lézerek összesen ≤ 40 k; padló 1 quad; **a jelenet összesen ≤ 1.8 M tri** |
| Textúra | nincs bitmap: minden procedurális (Object/Generated koordináta vagy világ-pozíció). UV csak a LED-falon kötelező (4.6) |
| Pivot | funkcionális (csukló-, ízület-, forráspont), lásd alább |
| Animáció | rigid mechanikus rig (5. fejezet) + Audio_Controller (7. fejezet) |

### 4.2 Általános topológiai szabályok (minden `SM_`)
1. Quad-dominancia. **Végleges állapotban 0 db n-gon** (az 5+ csúcsú lapok száma = 0; a 03 validátora ezt számolja). Háromszög csak a boolean-vágások környékén és a csavarfejeken megengedett.
2. Kemény felület stack-je, ebben a sorrendben: `MIR_X` (Mirror X, clipping be, merge 0.0005) → `BOOL_*` (Exact solver, a vágók a `COL_Booleans`-ban, `SM_Cutter_<Feature>` néven) → `BVL_Primary` (limit: Angle 30°, a szélességeket lásd lent, harden normals be) → `TRI_Ngon` (Triangulate, **Minimum Vertices = 5**, vagyis csak az n-gonokat bontja) → `WN_Main` (Weighted Normal, Keep Sharp be). A boolean-t a 03 a mentés előtt alkalmazza (Apply), ezután a TRI_Ngon is alkalmazandó. A Bevel és a Weighted Normal élő marad.
3. Ívelt héjak (kranium-lemezek, állkapocs-héj, tenyér, ujjpercek) stack-je: `MIR_X` → `SUB_Main` (Catmull-Clark, viewport 1, render 2) → `SOL_Shell` (Solidify, a vastagságokat lásd lent, even thickness) → `BVL_Panel` (0.004 m, 2 segment, limit Angle 30°) → `WN_Main`. A SubSurf előtti alaphálóban az élek mentén támasztó élhurkok vannak, **boolean nincs**.
4. Bevel-tierek (hard-surface): elsődleges élek 0.008–0.015 m / 3 segment; panelélek 0.002–0.003 m / 2 segment; mikro-részletek 0.0008 m / 1 segment. Egyenletes, egész hálóra kiterjedő bevel tilos.
5. Panelrések: a lemezek között 8–12 mm-es valódi geometriai rés (külön objektumok vagy inset + 0.006 m-es befelé extrudálás).
6. Greeble-ek (csavar, LED-pont, szellőző): **instancing** (Geometry Nodes Instance on Points vagy collection instance) a `COL_Greebles` mintákból. Egyedi modellezésük tilos.
7. Minden mesh-en **Apply Scale és Apply Rotation** (scale = 1, rotation = 0), mielőtt a rig-be parentelődik. Kivétel: a lézernyalábok és a lámpák forgatása animált, ezeken csak az Apply Scale kötelező.
8. A bal oldal tükrözése: a `MIR_X` modifier a középtengelyes objektumokon (koponya-részek, F, G, H). A külön objektumként álló bal oldali elemek (kéz L, szem L, a lézerek L-párja, a D/M/E lámpák L-párja) a jobb oldali párból készülnek: duplikálás, majd **a mesh-adat tükrözése** (`bmesh` scale(−1, 1, 1) + normal flip), utána Apply. **Negatív objektum-skála tilos.**
9. Shade: Smooth by Angle 30°. Az origó a funkcionális pivotra kerül (alább, objektumonként).

### 4.3 Koponya (`COL_Character_Skull`) – befoglaló: 2.6 m széles (x ±1.30) × 3.4 m magas (z 2.80–6.20) × 2.8 m mély (y −1.40…+1.40), középpont (0, 0, 4.5)

**Tier 1 – sziluett** (blockout, a 03 először ezt rendereli le a hero kamerából):

| Objektum | Forma és méret | Pozíció / pivot | Anyag |
|---|---|---|---|
| `SM_Char_Skull_Plate_01…07` | **7 vízszintes, felfelé egymásra rakott lemez-szelet** egy ellipszoid-héjból. Az ellipszoid középpontja (0, +0.10, 4.75), félátmérői a_x 1.25, a_y 1.30, a_z 1.45. Szeletek z 4.62 és 6.20 között, a lemezmagasság alulról: 0.26 / 0.25 / 0.24 / 0.23 / 0.22 / 0.21 / 0.17 (sapka), a lemezek között **10 mm rés**. Solidify 0.06 befelé. „Előrefelé lépcsőzés”: az i. lemez (i = 0 alul) eltolása −Y irányba i × 0.015 m (a felső lemezek előrébb állnak). A páros indexű lemezek külső felülete +12 mm-rel kijjebb van (ritmus a 0003 kockán látott sávozás szerint, feltételezés) | origó: (0, 0, 4.5) mindegyiken | PearlChrome; a lemezek belső pereme AnodizedDark |
| `SM_Char_Skull_EyeBand` | vízszintes „szemüveg” sáv: z 3.98–4.72, szélesség 2.36, homlokfelülete y −1.25-ön, enyhén ívelt (R 2.2 m XY-ban). Két szemüreg-furat Ø 0.62 m, a középpontok (±0.55, −1.25, 4.35), mélység 0.25 m (boolean, `SM_Cutter_EyeSocket`) | origó (0, 0, 4.5) | PearlChrome, a furat fala AnodizedDark |
| `SM_Char_Skull_BrowShield` | homlok-pajzs: x ±1.25, z 4.62–4.86, előlap y −1.36, vastagság 0.08, előre ívelt | origó (0, 0, 4.5) | PearlChrome |
| `SM_Char_Skull_Zygoma` (Mirror) | járomcsont-lemez: x 0.85–1.30, z 3.95–4.30, előre-kifelé 25°-ban dőlve, vastagság 0.07 | origó (0, 0, 4.5) | PearlChrome |
| `SM_Char_Skull_Maxilla` | felső állcsont: szélesség 1.60, z 3.72–4.00, előlap y −1.30, XY-ban R 0.80-as íven | origó (0, 0, 4.5) | AnodizedDark + PearlChrome előlap |
| `SM_Char_Skull_TeethUpper` | **14 fog** (Mirror 7 + 7), egyenként 0.10 sz × 0.17 m × 0.10 mély, köztük 12 mm rés, R 0.75-ös íven, alsó élük z 3.58-on | origó (0, 0, 4.5) | ChromeRod |
| `SM_Char_Skull_Occipital` | tarkó-ház: z 3.70–4.62, y +0.2…+1.40, x ±1.15, lekerekített doboz | origó (0, 0, 4.5) | AnodizedDark |
| `SM_Char_Skull_Jaw` | mandibula: a csukló-tengely **x = ±1.15, y = +0.35, z = 3.90**. A test z 2.80–3.70 között van, az áll y −1.30-on. A szélesség a csuklónál 1.90, az állnál 1.30. Héj Solidify 0.06 | **origó a csukló-tengely közepén: (0, +0.35, 3.90)** | PearlChrome + AnodizedDark belső |
| `SM_Char_Skull_TeethLower` | 14 alsó fog (Mirror), felső élük z 3.70-en (3°-os alapnyitásnál ~0.12 m rés a felső fogsorhoz), a Jaw-val együtt mozog | origó = Jaw-pivot | ChromeRod |

**Tier 2 – panel-tagolás és mechanika:**
- `SM_Char_Skull_Piston_R_01/02_Cyl` és `_Rod` (+ `_L_`; összesen 4 henger + 4 rúd): a halántékon kétoldalt 2-2 hidraulikus dugattyú. A henger (Ø 0.09, hossz 0.45, AnodizedDark) a krániumon ül, a felső rögzítés (±1.22, +0.05, 4.62) és (±1.22, +0.55, 4.55). A rúd (Ø 0.05, ChromeRod) az állkapocs alsó rögzítéséhez fut: (±1.12, −0.10, 3.55) és (±1.12, +0.30, 3.45). Pivot: a henger a felső, a rúd az alsó rögzítési ponton. Rig: 5.2.
- Panelvágások (boolean, 2–3 mm): a Plate_01 és Plate_02 elején 3-3 függőleges szegmensvágás; a BrowShield közepén egy függőleges osztás; a Zygoma két részre osztva.
- `SM_Char_Skull_TempleVent` (Mirror): halántékrács, 6 lamella, 0.30 × 0.20 m, (±1.24, +0.20, 4.20), AnodizedDark.
- `SM_Char_Skull_OccipitalRib`: 5 függőleges borda a tarkón (Array), szélesség 0.06, z 4.0–5.6, PearlChrome.
- `SM_Char_Skull_NasalVent`: háromszög alakú mélyedés a szem-sáv alatt (x ±0.14, z 3.98–4.20), 4 vízszintes lamellával, AnodizedDark.

**Tier 3 – mikro-részletek:**
- Csavarok: `SM_Greeble_Bolt_Hex` (Ø 0.035, magasság 0.012) instancelve a lemezek alsó pereme mentén 0.18 m-enként (koponyán összesen ~120 db).
- `SM_Char_Skull_Cable_01…06`: 6 kábelköteg az állkapocs alól (a jaw csonthoz parentelve). Curve, bevel Ø 0.04–0.06, hossz 0.80 m, enyhe S-ív. A gyökerek x = ±0.25 / ±0.55 / ±0.85, y −0.30, z 2.85. Anyag RubberCable. A végükön `SM_Char_Skull_CableRing_01…06` (torus Ø 0.08) `MAT_LightInst_CableRing` anyaggal.
- Fogankénti barázdák: 2 vízszintes, 2 mm-es panelvágás fogankét (normal bump is elég).
- Élvonal-emisszió: `SM_Char_Skull_EdgeLines`. 12 mm széles, 4 mm-rel a felületből kiemelt sávok a BrowShield alsó élén, a szemüregek peremén (gyűrű R 0.33) és a Zygoma felső élén (Mirror). `MAT_LightInst_SkullEdge`.
- `SM_Char_Skull_ThroatCore`: magenta „torok-fény” korong a fogak mögött, Ø 0.9 × 0.4 m-es ellipszis, (0, −0.85, 3.65), a jaw csonthoz parentelve. `MAT_LightInst_Throat`.

### 4.4 Szemek (`SM_Char_Eye_R_*`, tükörpár `_L_`). Középpont (±0.55, −1.20, 4.35), az optikai tengely −Y. **Origó: a szem középpontja.** Rétegek kívülről befelé:

| Objektum | Geometria | Anyag |
|---|---|---|
| `SM_Char_Eye_R_GearRim` | fogaskerék-perem: külső Ø 0.62, belső Ø 0.50, mélység 0.06, **36 fog** (fogmagasság 0.018) | AnodizedDark |
| `SM_Char_Eye_R_LEDRing` | **24 db** `SM_Greeble_LEDDot` (gömb Ø 0.022) R 0.235 m-en, egyenletesen, y −1.215 | `MAT_LightInst_EyeLED_R` |
| `SM_Char_Eye_R_Lens` | kristálykupola: Ø 0.46, kupolamagasság 0.08, vastagság 0.02, a csúcs y −1.29-en | `MAT_Glass_EyeCrystal` |
| `SM_Char_Eye_R_IrisBlade_01…12` | **12 lamella**: ívelt, sarló alakú lemez, vastagság 0.004, húr 0.24, a pivot-kör R 0.21 m. A lamella saját origója a pivotpontja; a forgástengely az optikai tengellyel (világ Y) párhuzamos. A lamellák síkja y −1.15-ön van (a lencse mögött) | AnodizedDark |
| `SM_Char_Eye_R_IrisHousing` | gyűrű a lamellák mögött, Ø 0.50 / 0.40, mélység 0.04 | AnodizedDark |
| `SM_Char_Eye_R_Core` | emisszív mag: Ø 0.14-es lapított gömb, y −1.08 | `MAT_LightInst_EyeCore_R` |

**Írisz-mechanika:** a lamellák elfordulási szöge θ_blade a nyílás-átmérőből (`iris_ap`, m) számolva. Kalibrációs pontok: θ = 0° → nyílás 0.40 m (teljesen nyitva), θ = 42° → 0.08 m (feltételezés, a lamella alakjától függ). A 03 a geometria alapján 4 pontban (0.10 / 0.16 / 0.36 / 0.40 m) **megméri a tényleges nyílást**, és a θ(iris_ap) leképezést lineáris darabokból álló táblaként adja át (Q2). A lamella-objektumok a szem-csonthoz (`eye.R`/`eye.L`) vannak parentelve, a saját lokális forgatásukat driver hajtja (5.3).

### 4.5 Kezek (`COL_Character_Hand_R`; a `_L` a tükörpár)
Befoglaló: 3.0 m magas (csukló → középső ujjhegy) × 2.0 m széles. **Középpont: (±3.3, −0.4, 5.0)**; ez a csukló–ujjhegy tengely felezőpontja (feltételezés). Alappóz (a tükörpár ellentétes előjellel): hátradőlés X −10° (az ujjhegyek +Y felé), befordulás Z −12° (R) / +12° (L), így a tenyér −Y felé néz, 12°-kal a koponya felé fordulva. Ebből levezetve a **csukló-pivot: (±3.25, −0.65, 3.52)**, a csukló→ujjhegy irányvektor R oldalon (−0.036, +0.170, +0.985).

**Az ujjak sorrendje (képoldali definíció):** mindkét kézen a **hüvelykujj a belső, a koponya felőli oldalon** van (a +X kéz anatómiailag bal kéz, tenyérrel előre), utána index, middle, ring, és kívül a pinky.

Arányok (az emberi kéz ×15.8-as skálája, feltételezés): csukló-gallér 0.25 + tenyér 1.45 + középső ujj 1.30 = 3.00 m. A tenyér 1.25 m széles és 0.38 m vastag.

| Ujj | Perc 1 / 2 / 3 (m) | Ø (m) | Alap-szétterülés (a középsőhöz képest) |
|---|---|---|---|
| Thumb | 0.55 / 0.42 / 0.33 | 0.30 | a tenyér belső oldalán, a csuklótól 0.35 m-re indul, 40°-kal befelé és 30°-kal előre (−Y) |
| Index | 0.50 / 0.36 / 0.30 | 0.26 | 12° befelé (a hüvelykujj felé) |
| Middle | 0.55 / 0.42 / 0.33 | 0.26 | 0° |
| Ring | 0.52 / 0.40 / 0.32 | 0.25 | 12° kifelé |
| Pinky | 0.40 / 0.30 / 0.25 | 0.22 | 24° kifelé |

Objektumok (R oldal; L azonos `_L_`-lel):
- `SM_Char_Hand_R_Palm`: tenyér-lemez (PearlChrome) a kézháton, 3 panelre osztva, a tenyérfelület AnodizedDark. Origó: csukló-pivot.
- `SM_Char_Hand_R_PalmCore`: kör alakú magenta emisszív mag, Ø 0.36, a tenyér közepén, 0.02 m-rel bemélyítve, PearlChrome peremgyűrűvel (`SM_Char_Hand_R_PalmCoreRim`). `MAT_LightInst_PalmCore_R`.
- `SM_Char_Hand_R_<Finger>_01…03` (15 db): ujjpercenként egy objektum. Hengeres héj PearlChrome-ból, az ízületi oldalon AnodizedDark. Az ujjperc vége felé 8%-kal keskenyedik. **Origó: a proximális ízület középpontja.**
- `SM_Char_Hand_R_<Finger>_Joint_01…03` (15 db): hengeres ízület-dob, Ø = ujjátmérő × 0.9, hossza ujjátmérő × 1.05, a tengelye az ízület hajlítási tengelye, AnodizedDark, oldalt egy-egy csavarfej-instance.
- `SM_Char_Hand_R_<Finger>_KnuckleEdge` (5 db, az _01 perc háta): 10 mm-es emisszív élcsík. `MAT_LightInst_HandEdge_R` (feltételezés: a 00/4.3 „élvonalak” és a 63-as checklista „erős emissziós élek” pontja alapján).
- `SM_Char_Hand_R_Tendon_<Finger>_Cyl/_Rod` (5 + 5 db): hidraulikus ín a kézháton. A henger (Ø 0.07, AnodizedDark) a tenyér-lemezen ül, a rúd (Ø 0.035, ChromeRod) az _01 ujjperc hátán rögzül. Rig: 5.2.
- `SM_Char_Hand_R_WristCollar`: csukló-gallér, Ø 0.80, magasság 0.25, 8 radiális borda. AnodizedDark.
- `SM_Char_Hand_R_WristRing`: emisszív gyűrű a gallér felső peremén (torus, R 0.40, a keresztmetszet Ø 0.03). `MAT_LightInst_WristRing_R`.
- `SM_Char_Hand_R_Cable_01…04`: 4 kábel a gallér alól, 1.4 m hosszan lelógnak és sötétbe vesznek. Curve, bevel Ø 0.05, RubberCable.
- Csavarok: `SM_Greeble_Bolt_Hex` instance-ek a tenyér-lemez panelpereme mentén, 0.16 m-enként.

### 4.6 Környezet (`COL_Environment`)
| Objektum | Spec | Anyag |
|---|---|---|
| `SM_Env_Floor` | sík, 60 × 60 m, z = 0, 1 quad (a hullám csak normál-térkép), origó (0, 0, 0) | `MAT_Floor_BlackMirror` |
| `SM_Env_LEDWall` | hengerpalást-szelet: 18 m ív menti szélesség × 12 m magasság, sugár **20 m**, a kamera felé homorú, a görbületi tengely (0, −13) pontban függőleges, a fal csúcspontja y = **+7.0**, a szélei x ≈ ±8.70, y ≈ +5.0. Alsó él z = 0. Vastagság 0.15 m (hátlap AnodizedDark). Osztás: 180 × 120 quad. **UV kötelező:** U = ív menti hossz méterben (0…18), V = magasság méterben (0…12), aránytartó | előlap: `MAT_LightInst_LEDWall` |
| `SM_Env_Truss_Portal_11 / _09 / _07` | négyzetes keret, oldalhossz **11 / 9 / 7 m** (a box-truss középvonalán mérve), keresztmetszet 0.5 × 0.5 m. y = **+2.5 / +4.0 / +5.5**, középpont z = **5.5** (a 11-es a padlón áll, z 0…11; a 9-es z 1.0…10.0; a 7-es z 2.0…9.0, a kép fölötti plafon-truss-ról függesztve, a függesztés a képen kívül van). Box-truss: 4 főcső Ø 0.05, rácsrudak Ø 0.025 cikcakkban 0.5 m-enként. Technika: profil-curve + Array + Curve modifier vagy Geometry Nodes (`GN_BoxTruss`, a paraméterek: hossz, keresztmetszet, rácsosztás). A sarkokban 0.6 m-es kocka csomópont-elem van | `MAT_Metal_AnodizedTruss` |
| `SM_Env_Truss_Ceiling` | plafonrács z = 18 m-en, 30 × 8 m, ugyanilyen box-truss, a képen kívül esik (a D/M fények motiválása) | AnodizedTruss |
| `SM_Env_FloorSlot_A / _G / _J_R / _J_L / _L_R / _L_L` | padlóba süllyesztett rés: 1.2 × 0.3 m (A, G), 0.6 × 0.3 m (J, L). A pozíció a forráspont (8.3). Mélység 0.15, belül egy kis emisszív lencse | AnodizedDark + `MAT_LightInst_FixtureGlow` |
| `SM_Env_Fixture_Laser_*` / `SM_Env_Fixture_Spot_*` | lámpatestházak a portálon, a plafon-truss-on és a hátsó sarkokban: 0.35 × 0.30 × 0.25 m doboz + Ø 0.12 lencse; minden B, E és K forráson, minden D/M lámpán és mindkét C-sor végpontján. Instance | AnodizedDark + `MAT_LightInst_FixtureGlow` |

### 4.7 Lézer- és fénysugár-geometria (`COL_Lasers_*`) – technika
- Egy nyaláb = egy mesh-objektum. **Az origó a forráspontban van, a nyaláb a lokális +Z mentén fut.** A forgatás `rotation_mode='XYZ'`, `rotation_euler = (φ, θ, 0)`, ebből az irányvektor **d = (cos φ · sin θ, −sin φ, cos φ · cos θ)**. Itt θ az oldalszög a függőlegestől (+ = +X felé), φ az előredőlés a kamera felé (+ = −Y felé).
- Szerkezet: egy objektumon két koncentrikus, fedőlap nélküli henger, két anyag-slottal. (1) **Mag:** 8 oldalú henger, a sugár = vastagság / 2. (2) **Halo-héj:** 12 oldalú henger, a sugár = a mag sugara × 6, kifelé néző normálokkal. Az anyagot a `NG_LaserBeam` node group adja (6.4). A füstben a fényrúd megjelenése a Cycles emission sampling (a mag megvilágítja a füstöt) és a halo együttes eredménye.
- Hossz: A, J, G 35 m; B 9 m; C 2 × 10 m; E 40 m; H 30 m; K a célpontig; L 25 m. A domain széle levágja.
- **Objektumszám:** 104 vékony nyaláb (A 14, B 6, C 4, E 4, G 40, J 16, K 8, L 12) + 5 F-négyzet + 6 H-sunburst = **115 lézer-objektum**. Pozíciók és szögek: 8.3.

### 4.8 Füst-domain (`COL_FX`)
`SM_FX_SmokeDomain`: kocka, 40 (X) × 40 (Y) × 24 (Z) m. **Az objektum origója a világ origójában (0, 0, 0) van, a mesh z 0…24 között.** Így az Object és a világ koordináták egybeesnek; a shader ennek ellenére **világ-pozíciót** (`Geometry.Position`) használ (6.7). Megjelenítés: csak volume (az anyag csak Volume kimenetet kap). Anyaga `MAT_FX_Smoke`.

---

## 5. Rig (03 építi, 06 animálja)

### 5.1 Elvek (mechanical-rig)
Constraint-first, **rigid parenting**: minden mesh `parent_type='BONE'`, nincs súlyfestés, **nincs deformáló csont (DEF_ nincs)**. Minden csont vezérlőcsont, a mesh-részek merev testként követik. **A parentelés után a világ-mátrix nem változhat** (a bone-parent a csont tail-jéhez köt, ezért a `matrix_parent_inverse`-t be kell állítani; ellenőrzés: a parentelés előtti és utáni `matrix_world` eltérése < 1e-5).
A bal oldali csontok a jobb oldaliakból a **Symmetrize** paranccsal készülnek (`.R`/`.L` utótag, tükrös roll), ezért ugyanaz a lokális forgatás mindkét oldalon tükrösen hat. Az animátor kizárólag a `CTL_*` és az `Audio_Controller` custom property-ket keyeli; a csontokat driverek mozgatják. Minden csont `rotation_mode = 'XYZ'`.

### 5.2 Csontlista – `RIG_IrisSovereign` (az armature-objektum origója 0,0,0, rotation 0, scale 1)
A „lokális tengelyek” oszlop a rest pozícióra vonatkozik, roll = 0 mellett (Blender-konvenció: a csont lokális Y-ja a head→tail irány). **A driverek a pose-bone csatornákat a feltüntetett indexen hajtják.**

| Csont | Head → Tail (rest, világ) | Lokális tengelyek (rest) | Szülő | Hajtott csatorna |
|---|---|---|---|---|
| `root` | (0, 0, 0) → (0, 0, 1) | Y = világ +Z | – | – |
| `skull_float` | (0, 0, 4.5) → (0, 0, 5.0) | Y = +Z, X = +X, Z = −Y | root | `location[1]` = `float_z` (világ-emelés); `scale[0..2]` = `scale_pulse` |
| `jaw` | (0, 0.35, 3.90) → (0, −0.65, 3.90) | Y = −Y világ; a hajlítási tengely a lokális X (= világ ±X; az előjelet a teszt dönti el) | skull_float | `rotation_euler[0]` = ±radians(`jaw_deg`): **az előjelet úgy kell választani, hogy `jaw_deg` > 0 esetén az áll (a tail) világ-Z-je csökkenjen** (Blenderben a −Y irányú csont lokális X-e várhatóan világ −X, ekkor az előjel +; a 03 assertel). Limit Rotation a hajlítási tengelyen 0…24° |
| `eye.R` / `eye.L` | (±0.55, −1.20, 4.35) → (±0.55, −1.50, 4.35) | Y = −Y világ (optikai tengely) | skull_float | statikus |
| `piston_cyl_01.R`, `piston_cyl_02.R` (+ .L) | a felső rögzítés → a rúd felé | – | skull_float | **Damped Track** → a párja (`piston_rod_0x`), track axis Y |
| `piston_rod_01.R`, `piston_rod_02.R` (+ .L) | az alsó rögzítés → a henger felé | – | jaw | **Damped Track** → `piston_cyl_0x`, track axis Y |
| `hand_center.R` / `.L` | (±3.3, −0.4, 5.0) → (±3.3, −0.4, 5.5) | Y = +Z, X = +X, Z = −Y | root | `location[1]` = `float_z`; `scale[0..2]` = `scale_pulse` |
| `wrist.R` / `.L` | a csukló-pivot (±3.25, −0.65, 3.52) → a kéz-középpont | Y = a csukló→ujjhegy irány; roll úgy, hogy a lokális X a tenyér szélességi tengelyével párhuzamos legyen, és R oldalon a +X világ felé mutasson | hand_center | `rotation_euler[0]` = radians(`wrist_deg`) (előre-hátra billegés) |
| `palm.R` / `.L` | a csukló-pivot → a középső ujj tövének közepe | mint a wrist | wrist | statikus |
| `<finger>_01…03.R` (thumb, index, middle, ring, pinky) (+ .L) | a proximális ízület → a következő ízület (az _03 a hegyig) | Y = az ujj iránya; **roll: a lokális X az ízület hajlítási tengelye**, úgy, hogy a +X körüli pozitív forgatás az ujjhegyet a tenyér oldala (−Y világ) felé vigye | lánc: palm → _01 → _02 → _03 | hajlítás: `rotation_euler[0]` = radians(`curl_deg` × k_ujj); szétterülés (csak az _01-en): `rotation_euler[2]` = radians(alap_ujj + `spread_deg` × s_ujj) |
| `tendon_cyl_<finger>.R` / `tendon_rod_<finger>.R` (+ .L) | a kézhát / az _01 háta | – | palm / <finger>_01 | Damped Track egymásra |

Csontszám: root 1 + skull_float 1 + jaw 1 + eye 2 + piston 8 + hand_center 2 + wrist 2 + palm 2 + ujjpercek 30 + ín 20 = **69**.
Ujj-szorzók (k_ujj): mind 1.0, a hüvelykujj 0.7. Szétterülési szorzó (s_ujj, + = a hüvelykujj felé): index +1.0, middle 0, ring −1.0, pinky −2.0, thumb +1.5. Ezzel a `spread_deg` = 8 a 00/31-es „+8° szétterülést” arányosan nyitja (feltételezés). Az alap_ujj értékek a 4.5-ös táblából.
Limit Rotation (hajlítás, ujjpercenként): −25° (túlnyújtás, a 204-es kinyíláshoz) … +70°.

### 5.3 Vezérlők, driverek és kötelező előjel-tesztek
- `CTL_Skull` (empty, (0, 0, 7.0), a `COL_Character_Rig`-ben) custom property-k: `iris_ap` (m, alap 0.16, tartomány 0.08–0.40), `jaw_deg` (alap 3.0, tartomány 0–24), `float_z` (m, 0), `scale_pulse` (1.0, tartomány 1.0–1.04).
- `CTL_Hands` (empty, (0, 0, 7.5)): `curl_deg` (alap **5.0** ízületenként, vagyis 15° az egész ujjra; feltételezés a 00/4.2 „15°-ban enyhén behajlítva” alapján), `spread_deg` (alap 0, + = szétterül), `wrist_deg` (0), `float_z` (0), `scale_pulse` (1.0).
- A koponya és a kezek skála-pulzusa együtt mozog (00/31): a `CTL_Hands["scale_pulse"]` drivere = `CTL_Skull["scale_pulse"]`. A lebegés azonos fázisú: a `CTL_Hands["float_z"]` drivere = `CTL_Skull["float_z"]`.
- Írisz-lamellák: minden `SM_Char_Eye_*_IrisBlade_nn` objektum a pivotjában ül, a világ-Y-nal (optikai tengellyel) párhuzamos saját tengelye körüli forgatásának drivere `theta(CTL_Skull["iris_ap"])` (a 03 kalibrációs táblája, 4.4). A kifejezés egyszerű, lineárisan darabolt legyen, Python autoexec nélkül is fusson.
- Driver-szabály: csak egyszerű kifejezés (`var * 0.0174533` stb.), minden driver `is_valid`.
- **Kötelező assertek a 03 scriptjében (különben a lépés nem zárható):**
  1. `float_z = +0.1` → a `skull_float` és a `hand_center.R/L` head világ-Z-je +0.1-gyel nő (X és Y nem változik).
  2. `jaw_deg = 24` → az állkapocs-csont tail világ-Z-je csökken (a száj nyílik), az X változása < 1e-4.
  3. `curl_deg = 17` → az `index_03.R` tail-je a világ −Y felé mozdul (a tenyér felé zár). `curl_deg = −5` → a +Y felé.
  4. `spread_deg = 8` → az `index_01.R` tail-je a koponya felé (−X), a `pinky_01.R`-é kifelé (+X) mozdul.
  5. Tükör: minden fenti pózban az `.L` csontok világ-pozíciója az `.R` csontokénak (−x, y, z) tükre (eltérés < 1e-4).
  6. `iris_ap` = 0.10 / 0.16 / 0.36 / 0.40 → a mért nyílás-átmérő ±0.01 m-en belül.
  7. `scale_pulse = 1.04` → a koponya befoglalója a saját középpontjából 4%-kal nő, a kéz a (±3.3, −0.4, 5.0) pontból.

### 5.4 Shape Key-k
**Nincs.** Indok: a karakter rigid, panelekből álló gép (a 0019 és a 0035 clay-kockán is merev ujjpercek látszanak). Ami organikus deformációnak tűnne (állkapocs, írisz, ujjak), az csont- vagy objektumforgatás. A kábelek a szülőjüket merev testként követik (szimuláció nincs).

### 5.5 Kamera-rig (`COL_Cameras`; a 03 építi, a 06 animálja)
```
EMP_CamOrbit        (0, 0, 2.43)  – rot Z = yaw_orbit (±4°)
└── EMP_CamDolly    lokális (0, −16.0, −0.73) → világ (0, −16, 1.7); lokális Y = dolly
    └── EMP_CamAim  Track To → EMPTY_CamTarget_Hero (track axis −Z, up axis Y)
        └── EMP_CamShake   lokális loc/rot = rázkódás
            └── CAM_Main_Hero   (lokális 0; CAM data: 28 mm, sensor fit VERTICAL, sensor_height 36 mm)
EMPTY_CamTarget_Hero  (0, 0, 2.43), statikus
EMP_Focus_Skull       a skull_float csonthoz parentelve, világ (0, −1.25, 4.35) – a DoF fókusz-objektuma
```
DoF: be, f/4, a fókusz-objektum `EMP_Focus_Skull` (00/44). Megjegyzés: 28 mm-en f/4 mellett a hiperfokális távolság ≈ 6.5 m, így a ~15 m-re lévő teljes karakter éles.

---

## 6. Procedurális shader-fák (04-lookdev; a fény-anyagokat a 05 hangolja)

**Általános szabályok:**
1. A HEX értékek sRGB-ben értendők, a node-ba lineárisan konvertálva kerülnek.
2. Minden strukturális anyag kimenete előtt ott van a `NG_ClayOverride` (6.1).
3. **Strukturális anyag (PearlChrome, AnodizedDark, AnodizedTruss, ChromeRod, Glass, Rubber, Floor) emissziója nincs, és semmilyen paramétere nem keyelhető.** Animált emisszió csak a `MAT_LightInst_*` anyagokon van, mindegyikben egy `EMIT_*` nevű Emission node-dal, amelynek Strength bemenetét driver hajtja (7. fejezet).
4. Minden anyagban legalább 2 rétegű variáció van (szín és/vagy roughness).
5. **Koordináta-tér:** ha egy képlet világ-pozícióhoz hasonlít (magasság, távolság a koponyától), akkor `Geometry.Position`-t (világ) kell használni, nem Object koordinátát. Object/Generated koordináta csak a pozíciófüggetlen zajokhoz megengedett.

### 6.1 `NG_ClayOverride` (shader node group, minden hero-anyagban)
Bemenet: `Shader`, `Clay` (0/1). Belül: `MIX_Clay` (Mix Shader, a faktor = Clay) a bejövő shader és egy Principled BSDF között (Base #535353, Roughness 0.80, Metallic 0, Specular IOR Level 0.3). A `Clay` bemenet drivere az `Audio_Controller["clay"]` (constant). Ezen kívül létezik egy önálló `MAT_Clay_Grey` anyag ugyanezzel a Principleddel (00/37, a viewport-teszthez); a váltás azonban a node groupon keresztül történik, mert slot-csere nem keyelhető.
A karakter `MAT_LightInst_*` anyagaiban az `EMIT_*` Strength driver-kifejezése (1 − clay) szorzót kap (7.4).

### 6.2 Karakter-anyagok
**`MAT_Metal_PearlChrome`** (a kranium-lemezek, a BrowShield, a Zygoma, a kéz-lemezek és az ujjpercek):
```
TC_Obj(Object) → NOI_Film (Noise, scale 1.6, detail 3, roughness 0.5)
              → MR_FilmThk (0..1 → 250..450 nm) → Principled.Thin Film Thickness
LW_Facing (Layer Weight, blend 0.35).Facing → MR_FilmFacing (+0..+60 nm) → hozzáadva a thickness-hez   [2. réteg: nézőszög-függő színforgás]
Principled: Base #D9D6E3, Metallic 1.0, Roughness = MR_Rough(NOI_Micro scale 40 → 0.10..0.15), Thin Film IOR 1.38,
            Coat 0.0, Anisotropic 0
→ NG_ClayOverride → Material Output
```
Elvárt kép: a nézőszögtől függően rózsa (#FF8FD8), menta (#9BFFD6) és jég (#9FD8FF) irizálás a 0003 és a 0015 kocka szerint. Ha a teszten nem elég színes, a vastagság-tartomány felső végét 520 nm-ig lehet emelni (a 04 döntése, rögzítendő).

**`MAT_Metal_AnodizedDark`** (belső panelek, írisz-lamellák, ízület-dobok, perem, házak):
```
Principled: Base #1A1426, Metallic 1.0, Roughness 0.35 (± NOI_Rough scale 25 → 0.30..0.42), Anisotropic 0.3,
            Anisotropic Rotation 0 (Tangent: Radial Z)
Élkopás (2. réteg): Geometry.Pointiness → CR_Edge (0.50→0, 0.56→1) × NOI_Wear (scale 60) → MIX_Wear:
            a kopott élen Base #6B6478, Roughness 0.22
BVN_Edge (Bevel node, radius 0.004) → Normal
→ NG_ClayOverride
```
(dark-gritty: csak finom élkopás, piszok nincs.)

**`MAT_Metal_AnodizedTruss`**: a fenti példánya Roughness 0.28-cal, kopás nélkül, NOI_Rough scale 8 (a truss-hosszon látszó csíkozás).

**`MAT_Metal_ChromeRod`** (dugattyúk, inak, fogak): Principled Base #E6E6EA, Metallic 1.0, Roughness 0.05. 2. réteg: NOI_Scratch (Noise scale 200, nyújtott koordinátával: Mapping scale (1, 1, 30)) → Roughness 0.04..0.09. → NG_ClayOverride.

**`MAT_Glass_EyeCrystal`**: Principled Base #15194A, Transmission Weight 1.0, IOR 1.52, Roughness 0.02, Coat 0.3 (roughness 0.0). 2. réteg: NOI_Inclusion (scale 18) → Roughness 0.01..0.05 (belső zárványok). → NG_ClayOverride.

**`MAT_Rubber_CableDark`**: Principled Base #0D0712, Metallic 0, Roughness 0.55. 2. réteg: WAV_Ribs (Wave, Bands, scale 60, a kábel hossza mentén) → Bump 0.15 + Roughness 0.50..0.62. → NG_ClayOverride.

### 6.3 Karakter fény-anyagok (`MAT_LightInst_*`, objektumonként egy)
Közös szerkezet: `TC_Obj` → 2. réteg (gradiens és/vagy statikus zaj) → `EMIT_<Név>` (Emission: Color, Strength) → Mix Shader egy PearlChrome-szerű Principleddel (Roughness 0.2, a nem emisszív részeken) → `NG_ClayOverride` → Output. **A Strength kizárólag driverrel változik.**

| Anyag | Objektum | Szín | Alap-strength (00/29) | 2. réteg |
|---|---|---|---|---|
| `MAT_LightInst_EyeCore_R/_L` | Eye Core | #E8FFD0 | 25 | radiális gradiens: a közép #E8FFD0, a perem #9BFFD6, ×0.7 |
| `MAT_LightInst_EyeLED_R/_L` | LEDRing | #37CDEE | 12 | pontonként statikus ±8% (Object Info: Random) |
| `MAT_LightInst_SkullEdge` | Skull EdgeLines | #E040FB | 12 (tartomány 8–15) | a sáv mentén Noise ±10%, a szélein Layer Weight lágyítás |
| `MAT_LightInst_Throat` | ThroatCore | #E040FB | 6 | radiális gradiens a közép felé ×1.3 |
| `MAT_LightInst_PalmCore_R/_L` | PalmCore | #E040FB | 10 | koncentrikus gyűrűk (Wave Rings, scale 8) ±20% |
| `MAT_LightInst_WristRing_R/_L` | WristRing | #37CDEE | 8 | a kerület mentén 16 szegmens ±15% |
| `MAT_LightInst_HandEdge_R/_L` | KnuckleEdge | #E040FB | 10 (8–15) | Noise ±10% |
| `MAT_LightInst_CableRing` | CableRing 01–06 | #37CDEE (feltételezés: a 00 nem ad színt; a cián a „cián LED” szereppel egyezik) | 4 | – |
| `MAT_LightInst_FixtureGlow` | lámpatest-lencsék, padlórések | #35FF3A | 2 | – (nem animált, × (1 − 0.85·dim)) |

### 6.4 Lézer-anyagok (`NG_LaserBeam` + csoportonként egy példány)
`NG_LaserBeam` bemenetei: `Color`, `Strength`, `Is_Halo` (0/1).
- Mag (`Is_Halo` = 0): `EMIT_Core` = Emission(Color, Strength).
- Halo (`Is_Halo` = 1): `LW_Halo` (Layer Weight, blend 0.5).Facing → `CR_Halo` (0 → 1, 1 → 0, ease) → `MIX_Halo` (Transparent ↔ Emission(Color, Strength × 0.04)). A halo lágy szélű, a füstben szilárd fényrudat ad.
- A nyaláb-objektumok ne vessenek árnyékot (Object → Visibility → Shadow off).

| Anyag (a mag és a halo külön példány: `…_Core`, `…_Halo`) | Szín | Alap-strength (00/28) |
|---|---|---|
| `MAT_LightInst_Laser_A` | #35FF3A | 50 |
| `MAT_LightInst_Laser_B` | #04D12C | 45 |
| `MAT_LightInst_Laser_C` | #70F34A | 40 |
| `MAT_LightInst_Laser_E` | #37CDEE | 50 (feltételezés: a 00 csak a spot W-ot adja; a mag a K-val egyezik) |
| `MAT_LightInst_Laser_F` | #35FF3A | 50 |
| `MAT_LightInst_Laser_G` | mag #FBF4FD, halo #E040FB | 80 |
| `MAT_LightInst_Laser_H` | gradiens a hossz mentén: a forrásnál #FBF4FD, a végén #37CDEE (Generated Z → ColorRamp) | 25 |
| `MAT_LightInst_Laser_J` | #70F34A | 45 |
| `MAT_LightInst_Laser_K_Upper` / `_K_Lower` | #35FF3A / #37CDEE | 50 (az alapszint 60% = 30) |
| `MAT_LightInst_Laser_L` | #37CDEE | 35 |

A H-sunburst szélességét nem a halo adja: a nyaláb maga csonkakúp (8.3), anyaga Emission × LW_Facing² + Transparent, hogy lágy élű legyen; halo-héja nincs.

### 6.5 LED-fal: `MAT_LightInst_LEDWall`
```
UV (méterben) → [Minta-modul] → MASK (0..1)
  P1 Gyűrűk:     r = |UV − (9, 6)|;  MASK = smoothstep(0.82, 0.92, sin(2π(r/1.2 − phase))·0.5+0.5)
  P2 Négyzetek:  q = max(|u−9|, |v−6|);  ugyanez q/1.0-val
  P3 Háromszög:  3 vonalrács 0° / 60° / 120°-ban (Wave Bands vagy fract), osztás 1.5 m, vonalvastagság 0.08 m,
                 a rács phase × 1.5 m-rel csúszik
  P4 Lencse-írisz: P1 gyűrűk (osztás 0.9 m) + 12 szektor-lamella: fract(12·atan2(v−6, u−9)/2π + phase) < 0.12
  A váltás: Audio_Controller["block"] (1..4, constant) → 4 egymás utáni MIX_Pattern (Compare/Math)
phase = ((frame − 1) mod 60) / 60   (driver; 60 frame periódus, 00/16)
Pixelrács (2. réteg): fract(UV / 0.04) → kör alakú LED-pont maszk (0.85..1.0)
Szín = mix(Bg, Fg, MASK)
  blokk 1: Fg #35FF3A, Bg #0D1330 ×0.15
  blokk 2: Fg #E040FB, Bg #0D0712 ×0.15
  blokk 3: Fg #37CDEE a P3 vonalain, a csomópontokban #70F34A; Bg #0D1330 ×0.15
  blokk 4: Fg #E040FB (gyűrűk) + #FBF4FD (lamellaélek), a középső Ø 2 m-es mag #35FF3A
           (feltételezés: a 00 nem ad színt a IV. blokkra, a koponya szemének visszhangja a karakter színeiből)
EMIT_LEDWall.Strength = 4.5 × Audio_Controller["led_wall"] × (1 − 0.85·dim)
```
(00/29: 3–6, nem éghet ki; a sötét háttér is világít ×0.15-tel, így nincs teljesen üres felület.) A LED-fal tartalmán nem lehet szöveg, arc vagy a karakter képe.

### 6.6 `MAT_Floor_BlackMirror` (00/55–56)
```
TC_Obj (a padló origója a világ origója, így ez világ XY) → vektor + (0.6·cos 2πt, 0.6·sin 2πt, 0),
   ahol t = Audio_Controller["floor_t"] = (frame−1)/240   → periodikus hullám
  → NOI_Ripple (scale 0.8, detail 2) + WAV_Ripple (Rings, scale 0.25, distortion 2) → Bump strength 0.02
Principled: Base #C1C1C1 (lineárisan ≈ 0.54, így a tükörkép fényereje ≈ 55%), Metallic 1.0, Roughness 0.06,
            Coat Weight 0.5, Coat Roughness 0.01, Coat IOR 1.5, Normal = Bump
2. réteg: NOI_Smudge (scale 3) → Roughness 0.05..0.09 (a tükörkép enyhén foltos, a lágy és az éles kép ettől válik el)
```
Indoklás: a fekete (#040510) hatást a tükröződő fekete űr adja. Egy diffúz #040510 alap nem tudna 55%-os tükörképet adni, ezért fémes, 0.54-es reflektanciájú felület kell. A coat-réteg (0.01) adja az éles képet, az alapréteg (0.06) a lágyat: így áll elő a dupla tükörkép. A 04 a teszten ellenőrizze, hogy a koponya tükörképe 50–60%-os fényerejű-e.

### 6.7 `MAT_FX_Smoke` (Principled Volume a domain-kockán; 00/46–49)
```
p = GEO_Pos (Geometry node → Position, VILÁG-koordináta, méterben)
t = Audio_Controller["smoke_t"] = (frame−1)/240
n1 = NOI_Global(p·0.15 + 3.0·(cos 2πt, sin 2πt, 0)),  detail 3                → MR 0.7..1.3
n2 = NOI_Floor (p·0.35 + 4.0·(sin 2πt, cos 2πt, 0.3·sin 2πt)), detail 4       → MR 0.6..1.4   (hömpölygés)
floor = 1 − smoothstep(2.0, 2.5, p.z)                                         → padlóréteg 0–2.5 m
D = 0.08·n1 + 0.10·floor·n2·Audio_Controller["smoke_floor"]                   → a padlóközeli réteg ≈ 0.18
skull = smoothstep(4.5, 5.0, |p − (0, 0, 4.5)|)                                → az 5 m-es zóna (a kezeket is lefedi)
VOL_Density = mix(min(D, 0.05), D, skull)
Principled Volume: Density = VOL_Density, Color #E6E8F0 (semleges), Anisotropy 0.65, Absorption Color fekete (0)
```
A füst színét a fények adják. Az árnyék tónusa a világ hátteréből jön (World: #0D1330, strength 0.03). A periodicitás körpályás koordináta-eltolással biztosított, ezért a 241. frame azonos az 1.-vel. Ellenőrzés (04): a sűrűséget a (0, 0, 1.0), a (0, 6, 12) és a (0, 0, 4.5) pontban mintavételezve ~0.18 / ~0.08 / ≤ 0.05 jön ki.

### 6.8 Anyaglista összesen
Strukturális (7): PearlChrome, AnodizedDark, AnodizedTruss, ChromeRod, Glass_EyeCrystal, Rubber_CableDark, Floor_BlackMirror. Ezen felül: Clay_Grey, FX_Smoke. LightInst: 9 karakter-típus (L/R példányokkal 15 db) + LEDWall + 11 lézer-anyag (mag- és halo-példánnyal). Node groupok: `NG_ClayOverride`, `NG_LaserBeam`.

---

## 7. Mozgás és audio-reaktív animáció (06-animator)

### 7.1 Architektúra
- **`Audio_Controller`** (empty, (0, 0, 0), `COL_FX`) hordozza az összes csatornát custom property-ként. A 06 a csatornák értékét **frame-enként (1–240) determinisztikusan számolja** a 00/6.4 és 6.8–6.10 eseménylistáiból (7.2–7.7 képletei), és minden frame-re kulcsot tesz (LINEAR; a `block` és a `clay` CONSTANT). A **241. frame-re az 1. frame értéke** kerül, és minden F-curve-re `Cycles` modifier kerül.
- **A 06-os agent-fájl Sound Bake előírása (felhasználói követelmény) így teljesül:** az `Audio_Controller["Bass"]` (20–150 Hz) és `["Snare"]` (2–5 kHz) property-be a 06 `graph.sound_bake`-kel besüti a `CIGARETTA MOLLYWOOD.wav` **60.48 s-tól kezdődő** ablakát (a kulcsokat −1814.4 frame-mel eltolva, hogy a 60.48 s az 1. frame-re essen). Ezek a görbék **validációra** szolgálnak, **közvetlenül nem hajtanak paramétert**, mert a 00 frame-pontos, súlyozott értékeket ír elő (6.8–6.10).
- **Ablak-azonosító kapu (strukturális; ha bukik, meg kell állni és jelezni kell a 0.3 szerint):**
  1. A sütött `Bass` átlaga a 91–121. frame-en (basszus-szünet) legfeljebb 50%-a a 136–235. frame-en mért átlagnak.
  2. A `Bass` maximuma a 190–215. frame-ek közé esik.
  3. A 40–50. frame-en **nincs** csend → maximum ugrás (ez a 77.856 s-os ablak jellegzetessége lenne).
- Egyedi csúcsok: a sound bake attack/release simítása késleltet, ezért a 00/14–15 trigger-frame-ektől való **≤ 3 frame eltérés csak reportolandó**, nem hiba.
- Minden fizikai paramétert **driver** köt az `Audio_Controller` (vagy a `CTL_*`) property-jéhez. Közvetlenül csak a kamera-rig empty-ket és a `CTL_*` property-ket keyeli a 06.

### 7.2 Időrács (00/6.4; a JSON-t nem használjuk)
- BPM 143.55, 1 beat = 12.54 frame.
- **Beat (19):** 13, 26, 38, 50, 63, 75, 88, 100, 112, 125, 137, 150, 162, 174, 187, 199, 212, 224, 237.
- **Basszus (17) és súly w:** 13 (0.40), 50 (0.40), 63 (0.40), 136 (0.55), 149 (0.55), 161 (0.55), 174 (0.55), 180 (0.55), 186 (0.55), 192 (0.55), 198 (0.75), **204 (1.00)**, 211 (0.75), 217 (0.55), 223 (0.55), 229 (0.55), 235 (0.60).
- **Erős snare (10):** 20, 49, 70, 76, **118**, 150, 156, 169, 210, 226. **Gyenge snare (13):** 14, 25, 43, 62, 82, 87, 101, 126, 144, 180, 201, 221, 238.
- **Blokkok:** I 1–62, II 63–124, III 125–186, IV 187–240. A váltás diszkrét.

### 7.3 Burkológörbe-definíció (minden eseménycsatornára)
A körkörös eltérés: Δ = ((f − f₀ + 120) mod 240) − 120. Ez kezeli a loop-határon átfutó lecsengést és az 1. frame előtti felfutást is.
```
env(Δ; a, d) = (a + Δ)/a             ha −(a−1) ≤ Δ ≤ 0      (felfutás: a csúcs PONTOSAN a trigger-frame-en)
             = (1 − Δ/(d+1))²         ha 1 ≤ Δ ≤ d           (ease-out lecsengés, a d. frame még nem nulla)
             = 0                       egyébként
csatorna(f) = alap(f) + Σ_események A·w·env(Δ)                  → a végén clamp a csatorna korlátjára
```
**A konvenció indoka (definíció):** a 00 a csúcsértékeket frame-hez köti (pl. 204: írisz 0.36 m, állkapocs 17°, és a 204 a kötelező tesztframe). Ezért a csúcs a trigger-frame-re esik, a „2 frame be” felfutás az előtte lévő frame-et is érinti. A kép 1 frame-mel (33 ms) a hang előtt indul, ez a szinkron-tűrésen belül van.

**Rázkódás (külön alak):** shake(Δ) = e^(−3Δ/8) · cos(2π·Δ/4), ha 0 ≤ Δ ≤ 8, egyébként 0. Két periódus 8 frame alatt; Δ = 8-nál < 5%.

### 7.4 Csatornatábla (`Audio_Controller` property-k → mit hajtanak)
| Property | Alap | Események → amplitúdó; a, d | Korlát | Driver-cél |
|---|---|---|---|---|
| `shk_x`, `shk_pitch`, `shk_yaw`, `shk_roll` | 0 | basszus (17): x 0.06·w m, pitch 0.6·w°, yaw 0.4·w°, roll 0.8·w°; shake() alak. Előjel: s_i = (−1)^i az i. basszus-eseményre (i = 0 a 13-nál); az x, a yaw és a roll s_i-vel váltakozik, a pitch mindig + (lefelé ütés) (feltételezés) | – | `EMP_CamShake` location[0], rotation_euler[0/1/2] |
| `fov_punch` (fok) | 0 | basszus: −0.8·w°, a 204-en −2.0°; a = 1, d = 6 | ≥ −2.0 | `CAM_Main_Hero.data.lens = 18 / tan(radians(65.5 + fov_punch)/2)` |
| `scale_pulse` | 1.0 | basszus +0.03·w (a 2, d 6); beat +0.01 (a 2, d 6) | ≤ 1.04 | `CTL_Skull["scale_pulse"]` |
| `iris_ap` (m) | 0.16; 91–121: 0.16 + 0.015·sin(2π(f−91)/30); 187→203: lineárisan 0.16 → 0.10, a 204-től újra 0.16 | basszus +0.20·w (a 2, d 6); beat +0.02 (a 2, d 6) | 0.08–0.40 | `CTL_Skull["iris_ap"]` |
| `jaw_deg` | 3.0 | basszus +14·w (a 2, d 6); erős snare +6 (a 1, d 3); **felülírás:** 118–124 = 22°, 125→130 lineárisan 22 → 3 | ≤ 24 | `CTL_Skull["jaw_deg"]` |
| `curl_deg` | 5.0 | basszus (a 204 kivételével) +12·w (a 2, d 6); **204:** −10 (a 2, d **10**) | −5…+20 | `CTL_Hands["curl_deg"]` |
| `spread_deg` | 0 | 204: +8 (a 2, d 10) | 0–8 | `CTL_Hands["spread_deg"]` |
| `float_z`, `wrist_deg` | 7.6 szerint | – | – | `CTL_Skull["float_z"]`, `CTL_Hands["wrist_deg"]` |
| `em_char` (szorzó) | 1.0 | basszus +0.40·w (a 1, d 6); beat +0.15 (a 1, d 6) | ≤ 1.60 | EyeCore, SkullEdge, HandEdge, PalmCore, Throat, WristRing, CableRing `EMIT_*`: alap × em_char × (1 − clay) × (1 − 0.85·dim) [az EyeCore-on a dim-tag nincs] |
| `em_led_dots` (szorzó, az em_char-ra szorozva) | 1.0 | erős snare: +0.80 a trigger-frame-en, majd +0.48, +0.20 (3 frame) | – | EyeLED |
| `em_palm` (szorzó, az em_char-ra szorozva) | 1.0 | erős snare: +1.00 / +0.60 / +0.25 (3 frame) | – | PalmCore |
| `las_bass` (szorzó) | 1.0 | basszus +0.50·w (a 1, d 6) | – | A, J, L, K |
| `fan_open_A`, `fan_open_J` (fok) | 0 | beat: A +5°, J +4° (a 1, d 8) | – | az A és J nyalábok θ-ja (7.5) |
| `fan_mult` | 1.0; 187→203: lineárisan 1.0 → 0.6; 204-től 1.0 (feltételezés: a drop „kinyit”) | – | – | A és J |
| `led_wall` (szorzó) | 1.0 (187→203: 1.0 → 0.6, a 204-től 1.0) | basszus +0.30·w (a 1, d 6) | – | `EMIT_LEDWall` |
| `smoke_floor` | 1.0 | basszus +0.20·w (a 1, d 6) | – | a `MAT_FX_Smoke` padlóréteg-szorzója |
| `block` | 1 / 2 / 3 / 4 a 1., 63., 125., 187. frame-től (CONSTANT) | – | – | LED-fal minta, a lézerblokk-szorzók |
| `clay` | 0; **196–197 = 1** (CONSTANT) | – | – | `NG_ClayOverride.Clay`; a karakter `EMIT_*` × (1 − clay) |
| `strobe` (0–1) | 0 | erős snare: 1.0 / 0.5 / 0.15 (a trigger és az utána következő 2 frame); feszültség: 187, 192, 196, 199, 201 = 0.40 (1 frame); átfedésnél a nagyobb érték nyer | – | `LGT_Strobe_Ceiling_R/L.energy` |
| `flash` (0–1) | 0 | 118: 1.0, 119: 0.6, 120: 0.25, 121: 0; 204: 1.0, 205: 0.7, 206: 0 | – | kompozitor fehér flash (7.8) |
| `dim` (0–1) | 0; **203 = 1** | – | – | minden fény és LightInst × (1 − 0.85·dim), **kivéve** EyeCore L/R és C-sorok |
| `las_A … las_M` (csoport-szorzók) | 7.5 tábla | 7.5 tábla | – | a csoport `EMIT_Core` / halo Strength, a D/M/E spot energy |
| `smoke_t`, `floor_t`, `led_phase` | (f − 1)/240; (f − 1)/240; ((f − 1) mod 60)/60 | – | – | füst-, padló- és LED-zaj (keyelt, LINEAR; a led_phase CONSTANT-lépcső nélkül, frame-enként keyelve) |
| `Bass`, `Snare` | sound bake | – | – | **csak validáció** (7.1) |

**Átfutás a loop-határon (a Δ-szabályból számolva; a 06 ezekre assertel):**
| Esemény | Csatorna | Átnyúló frame-ek |
|---|---|---|
| basszus 235 (w 0.6) | shake (d 8) | **1, 2, 3** (Δ 6, 7, 8) |
| basszus 235 | d = 6 csatornák (fov, scale, iris, jaw, curl, em_char, las_bass, led_wall, smoke_floor) | **1** (Δ = 6, env = (1/7)² ≈ 0.02) |
| beat 237 | fan_open_A/J (d 8) | **1–5** (Δ 4…8) |
| beat 237 | scale, iris, em_char (d 6) | **1–3** (Δ 4…6) |
| gyenge snare 238 | D-kúp +25% (a 1, d 2: 238 = 1.0, 239 = 0.44, 240 = 0.11) | nincs (a 00/34 szerint, lásd 0.5) |
| erős snare 226 | strobe (226–228) | nincs |

A frame 1 renderelt értékei tehát **tartalmazzák** ezeket a maradékokat. A frame-1-es tesztrender referenciaértéke a Δ-szabály szerinti összeg, nem a nyers alapállapot.

### 7.5 Lézer- és fénycsoport-szorzók (`las_*`; a driver-kifejezés = alap-strength vagy alap-W × szorzó × (1 − 0.85·dim))
| Csoport | I (1–62) | II (63–124) | III (125–186) | IV (187–240) | Események, egyéb |
|---|---|---|---|---|---|
| A | 1.0 | 0.3 | 0.7 | 1.0 | × las_bass; θ = sign(θ₀)·(\|θ₀\|·fan_mult + fan_open_A) |
| B | mind 1.0 | csak a ±1.2 m-es pár 1.0, a többi 0 (objektumonként külön szorzó: `las_B_inner`, `las_B_outer`) | mind 0.5 | mind 0.4, a beat-frame-en és az utána következő 3 frame-en 1.0 („villogás beatre”, feltételezés) | – |
| C | 1.0 | 1.0 | 1.0 | 1.0 (a 203-on is, a dim alól kivéve) | hullámzás, 7.6 |
| D | 0.5 | 1.0 (a II. blokk fő eleme) | 0.5 | 0.5 | erős snare: +50% (1.0 / 0.5 / 0.15 alak, 3 frame); gyenge snare: +25%, a = 1, d = 2 (a trigger + 2 lecsengő frame). A blokk-alapszintek feltételezések |
| E | 1.0 | 1.0 | 1.0 | 1.0 | pásztázás, 7.6 |
| F | 0 | 118–130 aktív (7.7) | 0 | 0 | – |
| G | 0 | 0 | 0 | 198–216 (7.7) | – |
| H | 0 | 0 | 0 | 204–212 (7.7) | – |
| J | 1.0 | **0** | 1.0 | 1.0 | × las_bass; θ = sign(θ₀)·(\|θ₀\|·fan_mult + fan_open_J) |
| K | 0.6 | 0.6 | 0.6 | 187→203: 0.6 → 1.0; 204–216: 1.0; 217→222: 1.0 → 0.6 (feltételezés) | × las_bass; erős snare: 1.0, 3 frame-ig |
| L | 1.0 | 1.0 | 1.0 | 1.0 | × las_bass |
| M | 1.0 | 1.0 | 1.0 | 187→203: 1.0 → 0.7; 204–210: 1.5; 211→216: 1.5 → 1.0 (feltételezés) | – |

### 7.6 Folyamatos periodikus mozgások (fázis: frame 1 = 0; minden periódus a {240, 120, 80, 60, 48, 40, 30, 24} halmazból)
| Elem | Képlet | Periódus |
|---|---|---|
| Koponya és kezek lebegése | `float_z` = 0.10·sin(2π(f−1)/120) | 120 |
| Csukló-billegés (tükrösen, a Symmetrize miatt automatikusan) | `wrist_deg` = 2.0·sin(2π(f−1)/60) | 60 |
| Kamera-orbit | `EMP_CamOrbit` rotation_euler[2] = radians(4·sin(2π(f−1)/240)) | 240 |
| Kamera-dolly | `EMP_CamDolly` location[1] = −16.0 + 1.2·(1 − cos(2π(f−1)/240))/2 (a +Y közelebb visz); plusz 187→203: további +0.3 m lineárisan, 204→216: vissza 0-ra (smoothstep) | 240 |
| Kamera függőleges lebegése | `EMP_CamDolly` location[2] = −0.73 + 0.08·sin(2π(f−1)/120) | 120 |
| C-sorok hullámzása | sor i (0–3): a két félnyaláb dőlése ±3°·sin(2π(f−1)/60 + i·π/2), tükrösen (Λ/V forma) | 60 |
| D-kúpok pásztázása | a dőlés a világ Y-tengelye körül: alap ± 8°·sin(2π(f−1)/120), az L oldal tükrösen | 120 |
| M-kúpok pásztázása | az aim-empty-k X-elmozdulása: Δx = táv·tan(6°)·sin(2π(f−1)/120 + π/2), tükrösen | 120 |
| E-pásztázók | azimut a világ Z-tengelye körül: ±45°·sin(2π·Φ(f)), tükrösen. **Φ(f) = folytonosan összegzett fázis:** az 1–124. frame-en 1/80 ciklus/frame, a 125–186.-on 1/40, a **187–240.-en 1/60 (feltételezés: a 00 a IV. blokkra nem ad periódust)**. Összesen 124/80 + 62/40 + 54/60 = 1.55 + 1.55 + 0.90 = **4.00 ciklus**, így a 241. frame = az 1. frame | 80 / 40 / 60 (szakaszonként) |
| LED-fal minta | `led_phase` = ((f−1) mod 60)/60 | 60 |
| Füst, padló | `smoke_t`, `floor_t` = (f−1)/240 | 240 |
| Film grain seed | = frame | – |

### 7.7 Eseményszekvenciák (frame-pontos)
**118 (legerősebb snare, 00/35):** `flash` 1.0 / 0.6 / 0.25 / 0 (118–121); `strobe` 1/0.5/0.15; `jaw_deg` 22° (118–124), 130-ra 3°. **F-alagút** (`SM_Laser_F_01…05`, 01 = a legkisebb, a kamerához legközelebbi): a skála 0.2 → 1.0, négyzetenként 1 frame-es késleltetéssel (a 01 a 118-on indul, az 05 a 122-n éri el az 1.0-t), az emisszió 118–124 100%, 125→130 lineárisan 0-ra (feltételezés). A kép a 118–120. frame-en fehérbe fordul, mire a flash elmúlik, az alagút áll, mintha a szájból törne elő.

**187–203 (feszültség, 00/38):** `iris_ap` alapja 0.16 → 0.10; `fan_mult` 1.0 → 0.6; K 0.6 → 1.0; M 1.0 → 0.7; `led_wall` 1.0 → 0.6; dolly további +0.3 m; strobe 0.4 a 187., 192., 196., 199. és 201. frame-en; clay 196–197; **203: dim = 1** (csak a szem-magok és a C-sorok világítanak).

**204–216 (csúcs, 00/36, 39):** `flash` 1.0 / 0.7 (204, 205); a 206–210. frame-en telített szín; G, H, K 100%, M 1.5; `iris_ap` ≈ 0.36 (+ a 198-as maradék ≈ 0.003); `jaw_deg` 17°; `curl_deg` −5° (5 − 10), `spread_deg` +8, 10 frame alatt vissza; rázkódás és FOV-punch maximum.
- **G-háló** (`las_G`): 198–202: 0.30; 203: 0.65 (a dim miatt ténylegesen ×0.15); **204: 1.0**; 205→214: 0.30 + 0.70·(1 − Δ/11)²; 215: 0.15; 216: 0.05; 217-től 0 (feltételezés: a „felfutás 2 frame, lecsengés 10 frame” értelmezése az „aktív 198–216” kereten belül).
- **H-sunburst** (`las_H`): 204: 1.0, 205→212 lineárisan 0-ra (a 213-on 0).

**217–240 (lecsengés, 00/40):** a basszusreakciók a súlyokkal futnak; a 225-től az összes blokk-szintű érték az I. blokk kezdőállapotában van (a K 222-re 0.6, az M 216-ra 1.0, a `led_wall` 1.0). A 241. frame (az 1.) állapotát a 7.4-es átfutási tábla adja.

### 7.8 Kompozitor-vezérelt elemek (felelős: **05** építi a node-okat, **06** keyeli a property-ket)
- **Teljes képes fehér flash** (118–121, 204–205): a Render Layers után `MIX_Flash` (Mix Color, Mix): Color B = #FBF4FD, a Factor drivere `Audio_Controller["flash"]`. Ha a kompozitor node-bemenetére az 5.2-ben nem lehet drivert tenni, a 06 a Factor bemenetet a `flash` értékeivel közvetlenül keyeli.
- **85%-os sötétítés (203):** **nem** kompozitorban, hanem a `dim` driverrel a fényeken és az emissziókon (mert a szem-magoknak és a C-soroknak ki kell maradniuk).
- **Glare** (00/58): Fog Glow (threshold 1.0, size 7, mix 0), Streaks (4 ág, threshold 2.0, mix −0.7). **Lens Distortion** dispersion 0.012. **Grain** 2–3%: Noise Texture, W/seed = frame; ha a kompozitorban nincs procedurális zaj, akkor egy 1080 × 1920-as, frame-enként előgenerált determinisztikus grain-szekvencia (`pipeline/renders/grain/####.png`) Overlay 0.025-tel.
- Megjegyzés: a 00 a flash-frame-eken kívül max. 1% clipelt fehéret enged. A 05 ezt a 118-as és a 204-es tesztframe mellett egy normál frame-en (pl. 150) is ellenőrzi.

### 7.9 Hang (felelős: **06**, a végső MP4 összeállításánál)
Forrás: `referencia/CIGARETTA MOLLYWOOD.wav`, **60.48–68.48 s**. Loop-crossfade 8 frame (0.267 s): a kimenet utolsó 8 frame-jének hangja = a 68.213–68.48 s-os szakasz lineárisan lehalkítva + a 60.213–60.48 s-os szakasz (az ablak előtti 8 frame) lineárisan felhangosítva. Így a 240. → 1. ugrás hangilag folytonos. A `pipeline/audio_window.wav` csak akkor használható, ha bizonyítottan ebből az ablakból vágták (0.3).

---

## 8. Világítás, lézer-elrendezés és kamera (05-lighting; a lézer-geometriát a 03 építi)

### 8.1 Karakterfények (00/50–54). A szín HEX-ben mérvadó; a telített színes fényekre a Kelvin nem értelmezhető
| Lámpa | Típus, méret | Pozíció | Cél / irány | Szín | Teljesítmény | Kelvin |
|---|---|---|---|---|---|---|
| `LGT_Rim_Magenta` | Area, négyzet 2 × 2 m | (−3.67, +3.67, 7.5): 135°-ban a kamerához képest, 30°-kal fent, 6 m-re a koponyától (a távolság feltételezés) | → (0, 0, 4.5) | #E040FB | 1500 W | n/a |
| `LGT_Rim_Cyan` | Area 2 × 2 m | (+3.67, +3.67, 7.5) | → (0, 0, 4.5) | #37CDEE | 1500 W | n/a |
| `LGT_Rim_Top` | Area, téglalap 6 × 0.5 m (keskeny softbox, X irányban) | (0, +0.3, 10.5) | lefelé | #FBF4FD | 800 W | ~7500 K (feltételezés) |
| `LGT_Bounce_Green` | Area 4 × 2 m | (0, −1.5, 0.3) | felfelé | #35FF3A | 300 W | n/a |
| `LGT_Key_Front` | Area 3 × 3 m | (0, −10, 3.5) | → (0, 0, 4.5) | #8A4CD6 | 375 W (rim : key = 4 : 1) | n/a |

A 05 agent-fájljának „Key / Fill / Rim” szereposztása így felel meg ennek: Key = `LGT_Key_Front`, Fill = `LGT_Bounce_Green`, Rim = `LGT_Rim_Magenta/Cyan/Top`. Más nevek (`LGT_Key`, `LGT_Fill`, `CAM_Main`) **nem** jönnek létre. A karakterfények kamerának láthatatlanok (Visibility → Camera off), a füstöt viszont megvilágíthatják. Mindegyik × (1 − 0.85·dim).

### 8.2 Spot-fények a füstben
| Csoport | Lámpák | Pozíció | Irány | Szín | Teljesítmény | Spot size / blend |
|---|---|---|---|---|---|---|
| D – magenta füstkúp | `LGT_Spot_D_R01…R04`, `_L01…L04` | (±3 / ±6 / ±9 / ±12, +1.0, 18) | lefelé, befelé dőlve 15 / 22 / 28 / 35°-kal (a világ Y-tengelye körül) | #E040FB | 2500 W × las_D | 4° / 0.15 (a blend feltételezés) |
| M – vastag kúp | `LGT_Spot_M_R01…R03`, `_L01…L03` | (±2 / ±5 / ±8, −2.0, 18) | Track To: a belső pár → `EMP_Aim_M_Skull` (0, 0, 4.5); a középső → `EMP_Aim_M_Hand_R/L` (±3.3, −0.4, 5.0); a külső → `EMP_Aim_M_Floor_R/L` (±5.5, −1.0, 0) (feltételezés). A pásztázás 7.6 szerint | belső #FBF4FD, középső #E040FB, külső #37CDEE | 6000 W × las_M | 14° / 0.3 |
| E – cián pásztázó | `LGT_Scan_E_R01/R02`, `_L01/L02` | (±14, +9, 10) | az alapirány: R01 → (0, 0, 6.5), R02 → (0, −2, 1.0) (feltételezés); a pásztázás 7.6 szerint; az `SM_Laser_E_*` nyaláb ugyanígy forog | #37CDEE | 1500 W | 2° / 0.05 |
| Strobe | `LGT_Strobe_Ceiling_R/L` | (±4, 0, 16) | lefelé | #FBF4FD | csúcs 12000 W × `strobe` (feltételezés; a 00 nem ad W-ot) | Area 8 × 1 m |

A D, M és E spotok shadow soft size-a 0.05 m. Gobo / IES-szimuláció (a 05-ös agent-fájl kéri): az M-kúpok light node-fájában a Strength egy **statikus** Voronoi-maszkkal (scale 6, 0.8–1.0) szorzódik a sugárirány szerint, így a kúp a füstben nem tökéletesen homogén. A D-kúpokon nincs gobo.

### 8.3 Lézer-elrendezés (00/26; minden csoport X-tükrözött)
| Csoport | Objektumok | Forrás | Szögek (θ az oldalszög a függőlegestől, φ az előredőlés) | Vastagság (mag Ø) |
|---|---|---|---|---|
| A | `SM_Laser_A_R01…R07`, `_L01…L07` | (0, +1.2, 0), `SM_Env_FloorSlot_A` | θ = ±6, 14, 22, 30, 38, 46, 54°; φ = 10° | 2.5 cm |
| B | `SM_Laser_B_R01…R03`, `_L01…L03` | (±1.2 / ±2.4 / ±3.6, +4.0, 1.0), a 9 m-es portál alsó gerendáján | θ = 0, φ = 0, hossz 9 m (a felső gerendáig) | 2 cm |
| C | `SM_Laser_C_01…04` (soronként 1 objektum, 2 tükrös félnyalábbal) | a félnyalábok forrása (±10, +4.0, z), z = 12.5 / 13.3 / 14.1 / 14.9; mindkét félnyaláb befelé, x = 0-ig fut (feltételezés: tükrös Λ/V hullám, mert a 00/5 szerint minden fényelem tükrös) | vízszintes, ±3° hullámzás | 1.5 cm |
| D | spotok (8.2) | – | – | 4°-os kúp |
| E | `SM_Laser_E_R01/R02`, `_L01/L02` + spot | (±14, +9, 10) | 8.2 / 7.6 | 2 cm |
| F | `SM_Laser_F_01…05` (négyzetes keret curve-ből, bevel Ø 1.5 cm) | középpont (0, y, 4.0): y = 0.7 / 1.9 / 3.1 / 4.3 / 5.5, oldalhossz 2 / 3 / 4 / 5 / 6 m (01 → 05) | a keret síkja XZ | 1.5 cm |
| G | `SM_Laser_G_R01…R20`, `_L01…L20` | (0, +0.8, 0.05), `SM_Env_FloorSlot_G` | síkonként 10 nyaláb oldalanként: θ = 5 + k·70/9 (k = 0…9) → 5.0, 12.8, 20.6, 28.3, 36.1, 43.9, 51.7, 59.4, 67.2, 75.0°; R01–R10: φ = 0°, R11–R20: φ = 8° | 1 cm |
| H | `SM_Laser_H_R01…R03`, `_L01…L03` | (0, +1.5, 4.5) (a koponya mögött) | θ = ±12, 30, 50°, φ = 0 (az XZ síkban sugárirányban, feltételezés); csonkakúp: a forrásnál r 0.30, 30 m-nél r 0.50 | 0.6–1.0 m |
| J | `SM_Laser_J_R01…R08`, `_L01…L08` | (±2.0, +2.0, 0), `SM_Env_FloorSlot_J_R/L` | az R forrásból **befelé**: θ = −4, −12, −20, −28, −36, −44, −52, −60°; az L forrásból ennek tükre (+). φ = 18° (feltételezés: a „keresztező” jelleg miatt a nyalábok átmetszik az A-legyezőt) | 2 cm |
| K | `SM_Laser_K_R01…R04`, `_L01…L04` | a nagy portál sarkai: felső (±5.5, +2.5, 11), alsó (±5.5, +2.5, 0) | minden sarokból 2 nyaláb (feltételezés): (1) az átlósan szemközti sarokba (az X-kereszt), (2) a szemközti oldalél közepére (∓5.5, 2.5, 5.5). A felső sarkok nyalábjai `K_Upper` (#35FF3A), az alsóké `K_Lower` (#37CDEE) | 2 cm |
| L | `SM_Laser_L_R01…R06`, `_L01…L06` | (±3.3, −0.4, 0.05), `SM_Env_FloorSlot_L_R/L` | 3°-os emelkedés; az azimut a −Y (kamera) iránytól kifelé 10, 20, 30, 40, 50, 60° (feltételezés: a kamera felé terülő fénysík tölti ki a padló 0–50%-os képsávját) | 1.5 cm |
| M | spotok (8.2) | – | – | 14°-os kúp |

**Darabszám-ellenőrzés (00/27):** I. blokk: 14 + 6 + 4 + 4 + 16 + 8 + 12 = **64**; II.: 14 + 2 + 4 + 4 + 8 + 12 = **44**; III.: **64**; IV.: 64 + G 40 = **104** (198–216). Ehhez jön mindig D 8 + M 6 kúp. Objektumszám: **115** (4.7).

### 8.4 World
Szín #040510, strength 0.03 (a füst árnyékában a #0D1330-as tónust a domain szórása adja, lásd 6.7). A world-ben **nincs** volume (a füst a domainben van).

### 8.5 Kamera (00/24–25, 41–44)
`CAM_Main_Hero`: az 5.5-ös lánc végén, világ-pozíció az 1. frame-en (0, −16, 1.7), 28 mm, sensor fit VERTICAL, sensor_height 36 mm (a hozzá tartozó szélesség 20.25 mm), clip 0.1–200 m. Célpont: `EMPTY_CamTarget_Hero` (0, 0, 2.43). Kompozíció-ellenőrzés (05):
- a koponya középpontja a kép alulról mért 60%-ánál;
- a karakter-együttes a képszélesség ~74%-a (a legközelebbi dolly-állásban, +4%-os skálával ≤ 83%), **a 90%-os safe-area-n belül** minden frame-en;
- a tükörkép 10–22%-on; a portálok teteje ~86%-on; a C-sorok 87.5–96.4%-on (0.5);
- üres sötét sáv nincs.

---

## 9. Technikai keret – összefoglaló
8 s = **240 frame @ 30 FPS**, `frame_start = 1`, `frame_end = 240`, **seamless loop** (a 241. frame azonos az 1.-vel), **9:16, 1080 × 1920**, Cycles, AgX High Contrast. A 00 nem ír elő eltérést.

---

## 10. Átadási ellenőrzőlisták (Definition of Done)

**Minden lépésnél kötelező (00/63):** tesztrender a frame **1, 118 és 204** képkockáról, a `CAM_Main_Hero`-ból, 1080 × 1920-ban (a 03-nál clay/workbench vagy alacsony mintás Cycles is elég), mentés a `pipeline/renders/<lépés>_f0001.png`, `…_f0118.png`, `…_f0204.png` néven, a 00/63 önellenőrzési listájával és legfeljebb 3 javítási körrel (gap-lista, max. 5 tétel).

### 03-modeler → `pipeline/01_model.blend`
- [ ] A collection-hierarchia a 3.2 szerint; minden objektum neve a 3.1 szerint; nincs `.001`.
- [ ] A koponya 7 lemeze, a szem-sáv, a homlok-pajzs, a járomcsontok, a maxilla, a 2 × 14 fog, az állkapocs (pivot (0, 0.35, 3.9)), a 4 dugattyú, a szellőzők, a tarkó-bordák, a 6 kábel a gyűrűkkel, az élvonalak és a torok-mag elkészült; a befoglaló méret 2.6 × 3.4 × 2.8 m ±3%.
- [ ] Szemenként: perem 36 foggal, 24 LED-pont, lencse, 12 írisz-lamella a pivotjukon, mag. Az írisz kalibrációs táblája (4 pont) a report-ban szerepel.
- [ ] Kezenként: tenyér-lemez, PalmCore, 15 ujjperc, 15 ízület-dob, 5 élcsík, 5 ín, gallér, csukló-gyűrű, 4 kábel. A befoglaló 3.0 × 2.0 m, a középpont (±3.3, −0.4, 5.0) ±0.05 m, a hüvelykujj a belső oldalon. Az L a mesh-adatában tükrözött, a skálája pozitív.
- [ ] Környezet: padló, ívelt LED-fal UV-vel, 3 portál + plafon-truss, a padlórések és a lámpatestek, a füst-domain (origó 0,0,0).
- [ ] 115 lézer-objektum (origó a forrásban, +Z irány, a 8.3 szögei), a mag- és halo-geometria a 4.7 szerint.
- [ ] `RIG_IrisSovereign` 69 csonttal, rigid bone-parentinggel (a `matrix_world` változatlan), a Damped Track dugattyúkkal és inakkal; a `CTL_Skull`, `CTL_Hands` és az összes driver `is_valid`; az 5.3 mind a 7 assertje átmegy.
- [ ] A kamera-rig (5.5) a helyén, az 1. frame-en a kamera (0, −16, 1.7) pontban, a célpont (0, 0, 2.43).
- [ ] Validáció: 0 n-gon, minden mesh-en scale = 1 (a lézerek és a lámpák kivételével a rotation is 0), nincs nem-manifold él a zárt héjakon, a poligonkeret (4.1) betartva. A report tartalmazza az objektumszámot és a tri-számot.
- [ ] A tesztrender (clay) 1/118/204: a sziluett, a szimmetria és a safe-area rendben.

### 04-lookdev → `pipeline/02_textured.blend`
- [ ] Mind a 6. fejezetben felsorolt anyag és node group megvan, a nevek pontosak; minden `EMIT_*` node a megadott alap-strength-tel.
- [ ] Strukturális anyagon nincs emisszió és nincs keyelhető paraméter.
- [ ] A `NG_ClayOverride` minden hero-anyagban benne van; a `clay = 1` teszt egyetlen frame-en szürke clay-t ad emisszió nélkül.
- [ ] A PearlChrome irizálása (rózsa, menta, jég) a tesztrenderen látszik; az anodizált élkopás finom.
- [ ] A LED-fal 4 mintája a `block` 1–4 értékeivel ellenőrizve (4 képkocka), szöveg és arc nincs.
- [ ] Padló: a tükörkép ~55%, a dupla (éles és lágy) kép látszik.
- [ ] A füst-sűrűség a 3 zónában (0.18 / 0.08 / ≤ 0.05) a 6.7-es pontokban mintavételezve; a `smoke_t` 0 és 1 értékén azonos a kép.

### 05-lighting → `pipeline/03_lit_scene.blend`
- [ ] A 8.1–8.2 összes lámpája a megadott néven, pozícióban, színnel és W-tal; minden lámpának saját datablockja van.
- [ ] A render-beállítások (2. fejezet), az AgX High Contrast és a GPU-backend reportolva.
- [ ] A kompozitor: MIX_Flash (a `flash` driverrel vagy keyekkel), Glare × 2, Lens Distortion, grain.
- [ ] Tesztrender 1/118/204 (a 118 és a 204 a property-k kézi beállításával szimulálva): telítettség (≥ 40 látható nyaláb), rim : key = 4 : 1 olvasható, vastag kúpok a füstben, dupla tükörkép, a sziluett kontrasztja a háttérhez ≥ 60%, clipping ≤ 1% (a flash-frame-eken kívül).
- [ ] A render-idő per frame (1080 × 1920, végső minta) reportolva (Q5).

### 06-animator → `final_animated_scene.blend` (projektgyökér)
- [ ] `Audio_Controller` minden 7.4-es property-vel, frame-enkénti kulcsokkal (1–241) és Cycles modifierrel; a `Bass`/`Snare` sound bake a 60.48 s-os ablakra; az ablak-azonosító kapu (7.1) átmegy, az egyedi csúcs-eltérések reportolva.
- [ ] Minden driver `is_valid`; a strukturális anyagokon nincs keyframe.
- [ ] Frame-ellenőrzés kiírással: f204: iris_ap ≈ 0.36, jaw_deg ≈ 17, curl_deg ≈ −5, spread_deg = 8, flash = 1.0, fov_punch = −2.0; f118: flash = 1.0, jaw_deg = 22; f203: dim = 1; f196–197: clay = 1.
- [ ] Loop-ellenőrzés: minden csatornára \|érték(241) − érték(1)\| < 1e-4, és a 7.4-es átfutási tábla értékei az 1–5. frame-en megjelennek.
- [ ] Periódusok: minden folyamatos mozgás periódusa a {240, 120, 80, 60, 48, 40, 30, 24} halmazból való; az E-fázis 241-nél pontosan 4.00 ciklus.
- [ ] Tesztrender 1/118/204 a teljes animációval, a 00/63 minden pontja teljesül; a hang a 7.9 szerint (8 frame-es crossfade) kerül a végső MP4-re.

---

## 11. Nyitott kérdések

| # | Kérdés | Kinek | Átmeneti döntés |
|---|---|---|---|
| Q1 | Az `audio_metrics.json` (77.856 s, a drop a 48. frame-en) és a koncepció (60.48 s) más ablakot ír le; a `pipeline/audio_window.wav` eredete ismeretlen | **felhasználó** | A 00 érvényes (60.48 s). A JSON nem hajt semmit. A 06 a 7.1-es strukturális kapuval ellenőriz |
| Q2 | Az írisz θ(nyílás) leképezése a lamella-geometriától függ | **03** | 0° → 0.40 m, 42° → 0.08 m lineárisan; a 03 4 pontban kalibrál és reportol |
| Q3 | A koponya–kéz rés a megadott középpontokból 1.0 m, a koncepció 0.8 m-et ír | **03 → felhasználó** | A középpontok (±3.3) és a 8.6 m-es szélesség maradnak, a rés 1.0 m. Ha a 0.8 m kötelező, a kéz 2.4 m-es szélességet kapna (az ujjak szétterülése miatt), ez a 03 döntése, reportolandó |
| Q4 | A kéz alappóza: a „15°-ban behajlítva” egész ujjra vagy ízületenként értendő? A kéz „középpontja” a csukló–ujjhegy tengely felezőpontja? A hüvelykujj a belső oldalon van? | 03 | 5° ízületenként (15° összesen); a felezőpont; a hüvelykujj belül |
| Q5 | A render-idő: 240 frame, sűrű volume, step rate 0.25, 512 minta, 1080 × 1920; valószínűleg több perc/frame | 05 → felhasználó | Ha > 4 perc/frame, a step rate 0.5-re, a minta 256-ra csökkenhet, ha az 1 cm-es G-nyalábok folytonosak maradnak |
| Q6 | A K-diagonálok második nyalábja, a J-legyező iránya, az L-fénysík azimut-referenciája és a C-sorok tükrös félnyalábjai feltételezések (a 00 nem rögzíti) | 03 / 05 | A 8.3 szerint; a tesztrenderen a telítettség és a keresztezés a döntő |
| Q7 | A 02-es lépés kötelező tesztrenderét (00/63) ez az agent nem tudta elkészíteni (nincs Bash/Blender-hozzáférése) | felhasználó / 03 | A 03 első tesztrendere (clay blockout, 1/118/204) pótolja a kompozíció- és safe-area-ellenőrzést |
| Q8 | Az állkapocs-csont hajlítási előjele (a −Y irányú csont lokális X-e) Blender-konvenciófüggő | 03 | Az 5.3/2. assert dönti el; a driver előjele ehhez igazodik |
