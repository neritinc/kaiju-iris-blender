# 02 – MÉRNÖKI 3D SPECIFIKÁCIÓ: „CIGARETTA MOLLYWOOD” / MERCURY TOTEM

> Szerző: 02-art-director (Technical Art Director)
> Bemenet: `pipeline/00_master_concept.md` (Kreatív Biblia, **mérvadó**), `pipeline/01_analysis.md` (mérések), `.claude/skills/blender-animation/SKILL.md`
> Címzettek: 03-modeler, 04-lookdev-artist, 05-lighting-artist, 06-animator
> Futtatókörnyezet: **Blender 5.2**, kizárólag `"C:\Program Files\Blender Foundation\Blender 5.2\blender.exe"` (Bash alatt: `"/c/Program Files/Blender Foundation/Blender 5.2/blender.exe"`), mindig külön, `--background` folyamatban.

**Precedencia (master 6. fejezet):** 00/7. fejezet számai > ez a spec > az agent-fájlok (`.claude/agents/0x-*.md`) általános példái. Ahol egy agent-fájl példája (pl. `bass * 0.05`, roughness 0.02–0.15, `frame_end` a hang hosszához) eltér, **a master és ez a spec érvényes**. A listát lásd a 10. fejezet K7 pontjában. A „(02 döntés)” jelölésű értékek olyan paraméterek, amelyeket a master nem rögzít, ezért ez a spec véglegesíti őket a master keretein belül.

---

## 0. Projekt-állandók (master 7.1)

| Paraméter | Érték |
|---|---|
| Felbontás | 1080 × 1920, `resolution_percentage=100` (teszt: 50) |
| FPS | 30 (`fps=30`, `fps_base=1.0`) |
| Frame range | `frame_start=1`, `frame_end=240` (8.000 s). A periódus 240 frame, a **241. frame ≡ az 1.** |
| Motor | Cycles, GPU ha elérhető (OPTIX → CUDA → HIP → ONEAPI, egyébként CPU) |
| Színkezelés | `view_transform='AgX'`, look `AgX - Punchy` (vagy `AgX - Base Contrast`). Az 5.2-es enum-nevet a 05 ellenőrzi: `scene.view_settings.bl_rna.properties['look'].enum_items` |
| Mintavétel | végső 256–512 + OpenImageDenoise; teszt 32–64 |
| Motion blur | be, `motion_blur_shutter=0.5` |
| Volume | step rate 1.0 (teszt 2.0), max steps ≥ 512 |
| Kimenet | PNG 16 bit szekvencia → H.264 MP4, **hang nélkül** |
| Mértékegység | Metric, `unit_settings.scale_length=1.0`, 1 BU = 1 m |
| Tengelyek | X = jobbra, Y = a kamerától befelé, Z = fel |

**Fájlláncolat (az agent-fájlok szerint):**
`scripts/build_model.py` → `pipeline/01_model.blend` → `scripts/build_materials.py` → `pipeline/02_textured.blend` → `scripts/build_lighting.py` → `pipeline/03_lit_scene.blend` → `scripts/animate_scene.py` → `final_animated_scene.blend` (projektgyökér). Renderek: `pipeline/renders/`.

---

## 1. Elnevezési konvenciók (szigorú)

### 1.1 Előtagok
Formátum: `PREFIX_Név_Variáns`, PascalCase nevek, számozás kétjegyű (`_01`). Ponttal végződő Blender-duplikátumnév (`.001`) **tilos**.

| Előtag | Típus | Példa |
|---|---|---|
| `GEO_` | mesh / text geometria | `GEO_Core_Mercury`, `GEO_Text_Top` |
| `RIG_` | armature objektum és armature data | `RIG_Main` |
| `MAT_` | anyag | `MAT_Chrome_Liquid` |
| `LGT_` | lámpa objektum **és** lámpa data (azonos név) | `LGT_Key` |
| `CAM_` | kamera objektum és kamera data | `CAM_Main` |
| `CTL_` | vezérlő (custom property hordozó) | *(lásd kivétel lent)* |
| `EMP_` | segéd-Empty (pivot, orbit, target) | `EMP_Noise_Orbit` |
| `COL_` | collection (02 döntés) | `COL_Hero` |
| `TEX_` | beépített (legacy) textúra-datablock a Displace-hez (02 döntés) | `TEX_Core_Clouds` |

**Egyetlen kivétel:** az audio-vezérlő Empty neve **`Audio_Controller`**. A master (4.6, 7.6) és a 06-os agent-fájl betű szerint ezt a nevet rögzíti, ezért nem kap `CTL_` előtagot (Nyitott kérdések, K2).

**Datablock-nevek:** a mesh, curve, armature, camera és light datablock neve megegyezik az objektum nevével. Minden lámpa saját datablockot kap, megosztott light data tilos, mert a driverek a `energy`-re kerülnek.

**Modifier-nevek (02 döntés):** `SUB_Main` (Subdivision), `DSP_Core` (Displace), `BVL_Slab` (Bevel).

**Node-nevek (a driver-célpontok kötelezőek, a többi ajánlott):** `EMIT_*` (Emission), `VOL_*` (volume / sűrűség), `VAL_*` (Value), `BUMP_*` (Bump), `NOI_*` (Noise), `VOR_*` (Voronoi), `WAV_*` (Wave), `CR_*` (ColorRamp), `MR_*` (Map Range), `LW_*` (Layer Weight), `BVN_*` (Bevel node), `MIX_*`, `TC_*` (Texture Coordinate). A node `name` és `label` mezője ugyanaz legyen.

### 1.2 Collection-struktúra

```
Scene Collection
├── COL_Control       RIG_Main, Audio_Controller (06 hozza létre),
│                     EMP_Noise_Pivot > EMP_Noise_Orbit,
│                     EMP_Fog_Pivot > EMP_Fog_Orbit,
│                     EMP_Floor_Pivot > EMP_Floor_Orbit,
│                     EMP_Droplet_Tilt > EMP_Droplet_Orbit
├── COL_Hero          GEO_Core_Mercury, GEO_Droplet_01 … GEO_Droplet_06
├── COL_Type          GEO_Text_Top, GEO_Text_Bottom, GEO_TextGlow_Top, GEO_TextGlow_Bottom
├── COL_Environment   GEO_Floor_Mercury, GEO_Slab_L, GEO_Slab_R, GEO_NeonStrip_L, GEO_NeonStrip_R,
│                     GEO_Wall_Back, GEO_NeonSlit_Back
├── COL_ReflCards     GEO_ReflCard_Top_01…03, GEO_ReflCard_Back_01…03
├── COL_Atmosphere    GEO_Fog_Volume
├── COL_Lights        LGT_Key, LGT_Rim, LGT_Accent_Cyan, LGT_Fill   (05 hozza létre)
└── COL_Camera        EMP_Cam_Pivot > CAM_Main, EMP_Cam_Target
```

A factory-startup `Cube`, `Camera` és `Light` objektumot a 03 törli. A `Collection` alapcollection sem maradhat meg.

### 1.3 Tulajdonjog: ki hoz létre, ki csak módosít
Duplikált létrehozás (`CAM_Main.001`) eltöri a drivereket. A „módosít” azt jelenti: név szerint megkeresi, és ha nem létezik, **hibával leáll**, nem hozza létre.

| Elem | Létrehozza | Módosítja |
|---|---|---|
| Minden `GEO_*`, `EMP_*`, `RIG_Main`, `TEX_Core_Clouds`, collectionök | 03 | 04 (anyag-hozzárendelés, ray-visibility) |
| `CAM_Main` (objektum + data, pozíció, parent), `EMP_Cam_Pivot`, `EMP_Cam_Target` | 03 | 05 (objektív, DoF, clip), 06 (kulcsok, delta-driverek) |
| Minden `MAT_*` és node | 04 | 06 (csak driverek) |
| `LGT_*` (objektum + data), World, render- és színkezelési beállítások | 05 | 06 (csak `energy` driverek) |
| `Audio_Controller`, minden kulcskocka és driver | 06 | – |

---

## 2. Modell (03-modeler)

### 2.1 Objektumlista, méretek (master 7.4, méter)

| Objektum | Geometria / felépítés | Méret | Pozíció (világ, közép) | Megjegyzés |
|---|---|---|---|---|
| `GEO_Floor_Mercury` | Plane | 16 × 16 | (0, 3.0, 0.0) | 1 quad elég (csak bump, nincs displacement) |
| `GEO_Core_Mercury` | UV Sphere 64 seg × 32 ring, `SUB_Main` (viewport 2, render 3) → `DSP_Core` | r = 0.75 | (0, 0, 3.20) | shade smooth; modifier-sorrend kötött: SUB → DSP |
| `GEO_Droplet_01…06` | UV Sphere 32 × 16 + `SUB_Main` (viewport 1, render 2) (02 döntés) | r lásd 2.2 | lásd 2.2 | gyerek: `EMP_Droplet_Orbit` |
| `GEO_Text_Top` | Text `MOLLY`, beépített Bfont | sapkamagasság ≈ 0.65, szélesség 3.0–3.4, `extrude=0.14`, `bevel_depth=0.015`, `bevel_resolution=4`, `offset=0.008`, `space_character=0.90`, `align_x='CENTER'`, `align_y='CENTER'` | (0, 0.60, 5.00) | rotation (90°, 0, 0), lásd 2.4 |
| `GEO_Text_Bottom` | Text `WOOD` | ugyanaz a `size` és minden beállítás, szélesség ≈ 2.6–3.0 | (0, 0.60, 1.50) | rotation (90°, 0, 0) |
| `GEO_TextGlow_Top` / `_Bottom` | Text duplikátum (azonos szöveg, size, betűköz) | `offset=0.025`, `extrude=0.02`, `bevel_depth=0` | (0, 0.78, 5.00) / (0, 0.78, 1.50) | Y = szöveg + 0.18 |
| `GEO_Slab_L` / `_R` | Cube, alkalmazott scale, `BVL_Slab` (width 0.02, segments 3, limit ANGLE 30°, harden normals) | 0.9 × 0.9 × 9.0 | (−2.55, 1.5, 4.5) / (+2.55, 1.5, 4.5) | a belső lap X = ∓2.10, az első lap Y = 1.05 |
| `GEO_NeonStrip_L` / `_R` | Cube | 0.03 × 0.03 × 8.0 | (−2.09, 1.04, 4.5) / (+2.09, 1.04, 4.5) | a monolit belső, kamera felőli élén |
| `GEO_Wall_Back` | Cube | 12 × 0.5 × 12 | (0, 7.0, 6.0) | az első lap Y = 6.75 |
| `GEO_NeonSlit_Back` | Cube (a falba süllyesztve, boolean nem kell) | 6.0 × 0.05 × 0.06 | (0, 6.74, 3.20) | |
| `GEO_ReflCard_Top_01/02/03` | Plane, normál −Z (lefelé) | 6.0 (X) × 0.08 (Y) | Z = 8.5; Y = −1.0 / −0.4 / +0.2; X = 0 | `visible_camera=False` (04 állítja) |
| `GEO_ReflCard_Back_01/02/03` | Plane, normál +Y (a szív felé), vízszintes | 4.0 (X) × 0.10 (Z) | Y = −11.0; Z = 2.4 / 2.9 / 3.4; X = 0 | `visible_camera=False` |
| `GEO_Fog_Volume` | Cube (volume domain) | 12 × 22 × 11 | (0, −2.0, 5.5) | a kamerát is tartalmazza (Y −13 … +9, Z 0 … 11) |
| `CAM_Main` | Camera | lásd 5.3 | világ (0, −8.00, 2.90); lokális a pivotban (0, −8.0, 0) | rotation (90°, 0, 0), **nincs Track To** |
| `EMP_Cam_Pivot` | Empty (Plain Axes, 0.3) | – | (0, 0, 2.90) | `CAM_Main` szülője |
| `EMP_Cam_Target` | Empty (Sphere, 0.1) | – | (0, 0, 2.90) | DoF fókusz, statikus, nincs szülője |
| `EMP_Noise_Pivot` → `EMP_Noise_Orbit` | Empty → Empty | orbit lokális X = 0.60 | pivot (0, 0, 3.20) (02 döntés) | a szív-displacement koordinátája |
| `EMP_Fog_Pivot` → `EMP_Fog_Orbit` | Empty → Empty | orbit lokális X = 1.50 | pivot (0, 0, 5.50) (02 döntés) | a füstzaj koordinátája |
| `EMP_Floor_Pivot` → `EMP_Floor_Orbit` | Empty → Empty | orbit lokális X = 0.80 | pivot (0, 3.0, 0.0) (02 döntés) | a padlófodor koordinátája |
| `EMP_Droplet_Tilt` → `EMP_Droplet_Orbit` | Empty → Empty | Tilt: rot X = **18°** (statikus); Orbit: rot Z animált | mindkettő (0, 0, 3.20) | lásd 2.2 |

**Szöveg extrude-értelmezés:** a Blender curve-extrude szimmetrikus, ezért `extrude=0.14` teljes mélysége 0.28 m (+ 2 × 0.015 bevel). A betű hátlapja Y ≈ 0.755-nél van, a glow eleje Y = 0.78 − 0.02 = 0.76-nál, így 5 mm a rés. Ez konzisztens a master „+0.18 m” értékével (K11).

### 2.2 Cseppgyűrű (master 7.4 / 7.8)
- **Hierarchia:** `RIG_Main:core` (csont) → `EMP_Droplet_Tilt` (rot X 18°, statikus) → `EMP_Droplet_Orbit` (rot Z kulcsolt 0 → −360°) → `GEO_Droplet_0n`.
- **Ok:** ha az X = 18° dőlés és az animált Z ugyanazon az objektumon van (XYZ Euler), a gyűrű síkja precesszál, és a gyűrű nem kering egy fix ferde síkban. A szétválasztás ezt kizárja.
- A cseppek **soha** nem gyerekei a `GEO_Core_Mercury`-nak, mert örökölnék a squash-t.
- Kiosztás az orbit lokális XY-síkjában, egyenletes 60°-os szögekkel. A nagyobb cseppek a külső pályára kerülnek (ütközés-tűrés, lásd 2.6).

| Csepp | Sugár (m) | Pálya sugara (m) (02 döntés, 1.15–1.35 tartományon belül) | Szög | Lokális pozíció (x, y, 0) |
|---|---|---|---|---|
| `GEO_Droplet_01` | 0.06 | 1.15 | 0° | (1.1500, 0.0000, 0) |
| `GEO_Droplet_02` | 0.08 | 1.20 | 60° | (0.6000, 1.0392, 0) |
| `GEO_Droplet_03` | 0.10 | 1.25 | 120° | (−0.6250, 1.0825, 0) |
| `GEO_Droplet_04` | 0.12 | 1.30 | 180° | (−1.3000, 0.0000, 0) |
| `GEO_Droplet_05` | 0.09 | 1.20 | 240° | (−0.6000, −1.0392, 0) |
| `GEO_Droplet_06` | 0.14 | 1.35 | 300° | (0.6750, −1.1691, 0) |

### 2.3 Displace (szív)
- `DSP_Core`: `texture = TEX_Core_Clouds` (`bpy.data.textures.new(type='CLOUDS')`, `noise_scale` 0.65, tartomány 0.5–0.9, `noise_depth` 1, `noise_basis='ORIGINAL_PERLIN'`; 02 döntés).
- `texture_coords='OBJECT'`, `texture_coords_object=EMP_Noise_Orbit`, `direction='NORMAL'`, `mid_level=0.5`.
- `strength=0.15`: ez az alapérték, a 06 drivere `0.15 + 0.12·bass` (hard cap 0.30).
- Lineárisan sodródó offset vagy W **tilos**. A zaj csak az orbit-empty körpályája miatt mozog.

### 2.4 Topológia, transzform, origó
- **Quad-dominancia:** minden mesh quad. Kivételek: a UV-gömbök pólus-háromszögei (megengedett), a síkok határ-élei (floor, kártyák, nem-manifold kivétel). **N-gon (>4 csúcs) = 0** minden MESH objektumon.
- **Text:** `FONT` típusú curve marad (master 5.4 megengedi). A FONT objektumokat a validáció az n-gon és a manifold teszt alól kihagyja. Ha a 03 mégis mesh-é konvertál, az n-gon-szabály érvényes, ezért trianguláció vagy quad-remesh kell, és ezt jelenti.
- **Apply Scale/Rotation** (`transform_apply(location=False, rotation=True, scale=True)`) minden MESH-en, a modifierek (Bevel, Subdiv) hozzáadása **előtt**. Utána scale = (1,1,1), rotation = (0,0,0).
- **Kivételek, ahol a rotation nincs alkalmazva:** `GEO_Text_*`, `GEO_TextGlow_*` (90°, 0, 0; FONT, lásd K5), `CAM_Main` (90°, 0, 0), `EMP_Droplet_Tilt` (18°, 0, 0), lámpák és az animált pivot-empty-k.
- **Origó:** minden mesh origója a geometriai középpont, ami megegyezik a 2.1 „Pozíció” oszlopával. A szöveg origója a szövegdoboz közepe (`align_x/y='CENTER'`). Ha a nagybetűk bbox-közepe nem esik ±0.02 m-en belül a célra, a 03 a curve `offset_y` értékével korrigál (az objektum `location` nem változik).
- **Shading:** a gömbök (szív, cseppek) smooth. A betonelemeknél a Bevel `harden_normals` mellett auto smooth nem kell.
- **Szöveg-méretezés:** a 03 a `size` értéket úgy állítja be, hogy az evaluált `MOLLY` bbox-magassága 0.65 ± 0.02 m legyen, majd megméri a szélességeket (`MOLLY` 3.0–3.4, `WOOD` 2.6–3.0). Ha a két feltétel `space_character=0.90` mellett egyszerre nem teljesül, **nem hangol saját értékre**, hanem a mért számokkal jelent (K5).

### 2.5 Kompozíció-ellenőrzés (master 7.4)
35 mm, 36 mm-es szenzor, VERTICAL fit, 8 m távolság: a látható tartomány az Y = 0 síkban Z −1.21 … 7.01, X ±2.31. Az UI-biztos sáv: **Z 0.44 … 5.79, X ±1.94**. A `MOLLY` teteje ≈ 5.33, a `WOOD` alja ≈ 1.17, a szív 2.45 … 3.95: mind a sávon belül van.

### 2.6 Ütközés-tűrés (hard cap mellett)
- A szív maximális sugara: 0.75 · 1.18 (scale cap) + 0.5 · 0.30 · 1.18 (displace cap, mid 0.5) ≈ **1.062 m**.
- A cseppek belső széle a cap mellett (pálya − r · 1.25): 01: 1.075, 02: 1.100, 05: 1.088, 03: 1.125, 04: 1.150, 06: 1.175. Mind > 1.062, tehát nincs ütközés.
- Alapértékekkel (k = 0.10 / 0.27) a szív sugara ≈ 0.97 m, ami bőséges tartalék.

---

## 3. Rig (03 építi, 06 animálja)

### 3.1 `RIG_Main` (master 7.9)
Armature az origóban, rotation/scale alkalmazva. **Minden csont `use_deform=False`.** Súlyozás nincs: az objektumok merev bone-parenttel lógnak rajta. A csontok függőlegesek (head → tail +Z), ezért a **pose-csont lokális Y tengelye = világ Z**.

| Csont | Head | Tail | Szülő | Típus | Gyerek-objektumok (`parent_type='BONE'`) |
|---|---|---|---|---|---|
| `root` | (0, 0, 0) | (0, 0, 0.5) | – | vezérlő | – |
| `core` | (0, 0, 3.20) | (0, 0, 3.50) | `root` (nem connected) | vezérlő | `GEO_Core_Mercury`, `EMP_Droplet_Tilt`, `EMP_Noise_Pivot` (02 döntés: a displace-zaj együtt lebeg a szívvel) |
| `type_top` | (0, 0.60, 5.00) | (0, 0.60, 5.30) | `root` | vezérlő | `GEO_Text_Top`, `GEO_TextGlow_Top` |
| `type_bottom` | (0, 0.60, 1.50) | (0, 0.60, 1.80) | `root` | vezérlő | `GEO_Text_Bottom`, `GEO_TextGlow_Bottom` |
| `cam_pivot` | – | – | – | **nem készül** (a master szerint opcionális). A kamera alapmozgása az `EMP_Cam_Pivot`-on van (master 7.5). | – |

- **Bone-parent:** a Blender a csont *tail*-jéhez köt. A `matrix_parent_inverse` legyen a csont rest-mátrixának inverze (vagy `bpy.ops.object.parent_set(type='BONE', keep_transform=True)` helyes context-tel). Utána **minden gyerek világpozíciója ≤ 1 mm-re egyezik a 2.1-gyel**. Ez a 03 checklistájának része.
- A `GEO_TextGlow_*` **nem** gyereke a `GEO_Text_*`-nak, hanem közvetlenül a type-csontnak. Így mindkettő saját snare `delta_scale` drivert kap, dupla skálázás nélkül.
- **Constraintek:** a rigben nincs. A kamerán sincs (Track To tilos, lásd 5.3). A lámpák fix rotációval céloznak.
- **Shape Key-k: NINCSENEK.** A master a deformációt Displace modifierrel és delta-scale-lel oldja meg. A 06 nem hoz létre Shape Key-t.

### 3.2 Csatorna-kiosztás (kulcs vs. driver, master 5.6 / 7.9)
A kulcskockák és a driverek **soha** nem írják ugyanazt a csatornát.

| Mozgás | Csatorna | Forrás |
|---|---|---|
| Szív lebegés Z | `RIG_Main` `pose.bones["core"].location[1]` (csont-lokális Y = világ Z) | kulcs |
| Szív forgás Z | `GEO_Core_Mercury.rotation_euler[2]` (saját objektum-csatorna, **nem** a `core` csont; különben a cseppgyűrű −360°-a kioltódna) | kulcs |
| Cseppgyűrű keringés | `EMP_Droplet_Orbit.rotation_euler[2]` | kulcs |
| Cseppek lebegése | `GEO_Droplet_0n.location[2]` (orbit-lokális) | kulcs |
| Felirat-lebegés | `pose.bones["type_top" / "type_bottom"].location[1]` | kulcs |
| Zaj-pályák | `EMP_Noise_Pivot`, `EMP_Fog_Pivot`, `EMP_Floor_Pivot` `.rotation_euler[2]` | kulcs |
| Kamera | `EMP_Cam_Pivot.rotation_euler[2]`, `CAM_Main.location[1]`, `CAM_Main.location[2]` | kulcs |
| Minden audio-reakció | `delta_*`, node-inputok, `energy`, `modifiers[...]` | driver |

---

## 4. Procedurális shader-fák (04-lookdev-artist)

### 4.1 Paletta (master 7.3, változatlan; 01 3.6: nincs eltérés)
Node- és lámpaszínhez a konverzió kötelezően: `mathutils.Color(hex_to_srgb).from_srgb_to_scene_linear()`. Kézi számolás tilos. A lineáris érték csak tájékoztató.

| Szerep | HEX | ≈ lineáris RGB |
|---|---|---|
| VOID | #040406 | (0.0012, 0.0012, 0.0018) |
| SMOKE | #15141B | (0.0075, 0.0070, 0.0109) |
| CONCRETE | #1C1C21 | (0.0116, 0.0116, 0.0152) |
| CONCRETE var. | #26262C | (0.0194, 0.0194, 0.0252) |
| CHROME | #D7DBE3 | (0.680, 0.708, 0.768) |
| GUNMETAL | #3A3E48 | (0.042, 0.048, 0.065) |
| NEON MAGENTA | #FF1F8F | (1.000, 0.014, 0.275) |
| NEON CYAN | #00E8FF | (0.000, 0.807, 1.000) |
| ULTRAVIOLET | #6A00FF | (0.144, 0.000, 1.000) |
| WHITE HOT | #F2F6FF | (0.888, 0.922, 1.000) |

Tilos: meleg narancs vagy sárga, telített zöld, tiszta #FFFFFF felületszín.

### 4.2 Driver-kompatibilitási szabály (kötelező)
Minden driverrel hajtott socket **link nélküli** (`is_linked == False`), különben a driver hatástalan. A socketet **név szerint** kell elérni (`node.inputs["Strength"]`), index szerint nem. Ha a driven értéknek maszkon kell átmennie, egy nevesített `VAL_*` Value-node a driven skalár, és ez Math Multiply-on át megy tovább (lásd fog).

### 4.3 Anyagok és hozzárendelés

| Anyag | Objektumok |
|---|---|
| `MAT_Chrome_Liquid` | `GEO_Core_Mercury`, `GEO_Droplet_01…06` |
| `MAT_Chrome_TypeRim_Magenta` | `GEO_Text_Top` |
| `MAT_Chrome_TypeRim_Cyan` | `GEO_Text_Bottom` |
| `MAT_Type_Glow_Magenta` | `GEO_TextGlow_Top` |
| `MAT_Type_Glow_Cyan` | `GEO_TextGlow_Bottom` |
| `MAT_Mercury_Floor` | `GEO_Floor_Mercury` |
| `MAT_Concrete_Dark` | `GEO_Slab_L`, `GEO_Slab_R`, `GEO_Wall_Back` |
| `MAT_Neon_Magenta` | `GEO_NeonStrip_L` |
| `MAT_Neon_Cyan` | `GEO_NeonStrip_R` |
| `MAT_Neon_Slit` | `GEO_NeonSlit_Back` |
| `MAT_ReflCard` | `GEO_ReflCard_Top_01…03`, `GEO_ReflCard_Back_01…03` |
| `MAT_Fog` | `GEO_Fog_Volume` (csak Volume output, Surface üres) |

*Névvéglegesítés (master 6.4):* a master `MAT_Type_Rim` „rétege” két anyagként valósul meg (`MAT_Chrome_TypeRim_Magenta/_Cyan`), mert szavanként eltér a rim színe, a szív és a cseppek pedig nem világíthatnak. A `MAT_Type_Glow` is két anyag (`_Magenta/_Cyan`). Mindkét változatban azonos a node-név (`EMIT_TypeRim`, `EMIT_TypeGlow`). (K4)

### 4.4 `MAT_Chrome_Liquid` (master 4.3, 7.11)
```
TC_Chrome (Object, saját objektum) ─┬─> NOI_Rough (3D, Scale 4.0 [2–6], Detail 2, Rough 0.5)
                                    │      └─> CR_Rough (fekete@0.35 → fehér@0.65)
                                    ├─> NOI_Smudge (Scale 2.0, Detail 1)  [ujjlenyomat-foltok]
                                    │      └─> CR_Smudge (0.45 → 0.60)
                                    │   MIX_Rough (Lighten: CR_Rough, CR_Smudge)
                                    │      └─> MR_Rough (0..1 → 0.02..0.08, clamp) ──> Principled.Roughness
                                    ├─> NOI_Tint (Scale 1.5) → CR_Tint (0 → 0.15 max)
                                    │      └─> MIX_Base (Factor; A=#D7DBE3, B=#3A3E48) ──> Principled.Base Color
                                    └─> NOI_Bump (Scale 9 [6–12], Detail 3)
                                           └─> BUMP_Chrome (Strength 0.02 [≤ 0.05], Distance 0.005) ──> Principled.Normal
Principled BSDF: Metallic 1.0, Anisotropic 0.15 (02 döntés, „halvány anizotróp-jellegű”), Coat 0
```
- A roughness a végső kimeneten **0.02–0.08**.
- A Base Color variáció a GUNMETAL felé ≤ 15%.
- A szív forgása a sziluetten alig látszik, mert a Displace-zaj az orbit-térben van. A forgást a saját Object-koordinátás roughness- és tint-foltok teszik olvashatóvá (K9).

### 4.5 `MAT_Chrome_TypeRim_Magenta` / `_Cyan` (master 5.4a, 7.11)
- A teljes `MAT_Chrome_Liquid` fa másolata, plusz a rim-réteg:
```
LW_Rim (Layer Weight, Blend 0.22 [0.15–0.30]) .Facing
   └─> CR_Rim (fekete@0.55 → fehér@0.90)
         └─> MIX_RimColor (Multiply: A = rim szín, B = CR_Rim)  ──> EMIT_TypeRim.Color
EMIT_TypeRim (Emission, Strength = 2.5, LINK NÉLKÜL → driver)
ADD_Rim (Add Shader: Principled + EMIT_TypeRim) ──> Material Output.Surface
```
- Rim szín: `MOLLY` = NEON MAGENTA #FF1F8F, `WOOD` = NEON CYAN #00E8FF.
- A betű elölnézeti lapja (Facing ≈ 0) nem világít. A bevel és az oldalfal (Facing → 1) izzik.

### 4.6 `MAT_Type_Glow_Magenta` / `_Cyan` (master 5.4b)
- `EMIT_TypeGlow` (Emission, Color #FF1F8F / #00E8FF, Strength **3.0**, link nélkül) → Material Output.
- Tiszta emisszió (master 4.3), nincs további réteg.

### 4.7 `MAT_Neon_Magenta` / `MAT_Neon_Cyan` / `MAT_Neon_Slit` / `MAT_ReflCard`
| Anyag | Node | Color | Strength alap | Driver |
|---|---|---|---|---|
| `MAT_Neon_Magenta` | `EMIT_Neon` | #FF1F8F | 6.0 | `6.0 + 24.0*bass` |
| `MAT_Neon_Cyan` | `EMIT_Neon` | #00E8FF | 6.0 | `6.0 + 24.0*bass` |
| `MAT_Neon_Slit` | `EMIT_Slit` | **NYITOTT (K3)**. Ideiglenes munkaérték a felhasználói döntésig: WHITE HOT #F2F6FF | 5.0 | `5.0 + 15.0*bass` |
| `MAT_ReflCard` | `EMIT_ReflCard` | **NYITOTT (K3)**. Ideiglenes munkaérték: WHITE HOT #F2F6FF | 8.0 | nincs (konstans; a master opcionális `+4.0·bass`-át nem használjuk) |

- Ezek tiszta emissziók (master 4.3). A 04 agent-fájl „legalább kétrétegű variáció” szabálya az emissziós anyagokra **nem** vonatkozik (master-precedencia).
- **Reflexiós kártyák ray visibility:** `visible_camera=False`. A glossy, diffuse és transmission láthatóság marad True. A `visible_volume_scatter` alapértéken marad, ha a 05 tesztrenderen túl erős a köd felülről, jelzi.

### 4.8 `MAT_Mercury_Floor` (master 7.11)
```
TC_Floor (Object = EMP_Floor_Orbit)
   ├─> NOI_FloorRipple (Scale 0.9 [0.6–1.2], Detail 1, Rough 0.4)
   ├─> WAV_Floor (Rings, Scale 0.45 [0.3–0.6], Distortion 2.0, Detail 1)
   │   MIX_FloorH (Mix 0.5) ──> BUMP_Floor.Height
BUMP_Floor (Strength 0.05, LINK NÉLKÜL → driver; Distance 0.02) ──> Principled.Normal
NOI_FloorTint (Scale 0.3) → CR_FloorTint ──> MIX_FloorBase (A=#040406, B=#3A3E48, Factor 0–0.35) ──> Base Color
NOI_FloorRough → MR_FloorRough (0..1 → 0.02..0.05) ──> Roughness
Principled: Metallic 1.0
```

### 4.9 `MAT_Concrete_Dark` (master 4.3, 7.11)
```
TC_Concrete (Object)
   ├─> NOI_Concrete (Scale 4.0 [3–6], Detail 8, Rough 0.6)   [foltok]
   ├─> VOR_Pores (F1, Scale 60 [40–80])                       [pórusok]
   │   MIX_ConcreteMask (Overlay 0.5)
   │      ├─> CR_ConcreteCol (#1C1C21 → #26262C) ──> MIX_Wear.A
   │      └─> MR_ConcreteRough (0..1 → 0.75..0.95) ──> Roughness
   │   VOR_Pores → BUMP_Concrete (Strength 0.15 [0.1–0.2], Distance 0.01, Invert) ──> Normal
Élkopás:
BVN_Wear (Bevel node, Radius 0.02, Samples 8) .Normal ─┐
Geometry.Normal ───────────────────────────────────────┴─> VM_Dot (Dot Product)
   └─> MR_Wear (1.0 → 0, 0.92 → 1, clamp) → CR_Wear ──> MIX_Wear.Factor (B = #26262C)
MIX_Wear ──> Base Color.  Metallic 0.0
```
- A Pointiness itt nem használható (alacsony csúcsszámú kocka), ezért a Bevel-node maszk kötelező (master 4.3).
- A roughness végső tartománya 0.75–0.95.

### 4.10 `MAT_Fog` (master 4.3, 7.11)
```
TC_Fog (Object = EMP_Fog_Orbit)
   └─> NOI_Fog (3D, Scale 0.45 [0.3–0.6], Detail 3, Rough 0.55)
         └─> CR_FogMask (0.35 → 0.5, 0.70 → 1.0)            [maszk ∈ 0.5 … 1.0]
VAL_FogDensity (Value = 0.035, driver: 0.035 + 0.015*bass)
VOL_Density (Math Multiply: VAL_FogDensity × CR_FogMask) ──> VOL_Fog.Density
MIX_FogColor (A=#15141B, B=#6A00FF, Factor 0.08 [≤ 0.10]) ──> VOL_Fog.Color
VOL_Fog (Principled Volume): Anisotropy 0.62 [0.55–0.70], Absorption Color #040406 (02 döntés), Emission 0
```
- A maszk maximuma 1.0, így a lokális sűrűség sosem lépi át a driven értéket, és a hard cap (0.060) tartható. Ennek ára, hogy az **átlagos** nyugalmi sűrűség ≈ 0.026, nem 0.035 (K13).
- A World-ben **nincs** volume (a 05 agent-fájl opcióját a master fog-kockája felülírja).

### 4.11 World (05 állítja)
Background #040406, Strength 1.0, külső HDRI vagy kép nincs.

---

## 5. Világítás és kamera (05-lighting-artist)

### 5.1 Lámpák (master 4.4, 7.10)
A lámpák fix rotációval céloznak: `rot = (target − loc).to_track_quat('-Z', 'Y')`, constraint nincs. Minden lámpának saját light datablockja van.

| Lámpa | Szerep | Típus | Pozíció | Célpont | Szín (HEX / K) | Power alap | Méret | Driver (06) |
|---|---|---|---|---|---|---|---|---|
| `LGT_Key` | key, felülről | Spot | (0, −1.5, 9.0) | (0, 0, 3.20) | #F2F6FF (≈ 7000 K) | **1200 W** | `spot_size = math.radians(28)` (= 0.4887 rad; **nem** `28`), `spot_blend=0.35`, `shadow_soft_size=0.05` | `1200.0 + 400.0*snare` |
| `LGT_Rim` | rim, hátul balra | Area RECTANGLE | (−2.0, 2.2, 3.4) | (0, 0, 3.20) | #FF1F8F (nem feketetest) | **350 W** | 1.5 × 0.15 (`size`, `size_y`) | `350.0 + 650.0*bass` |
| `LGT_Accent_Cyan` | accent, hátul jobbra | Area RECTANGLE | (+2.0, 2.2, 3.4) | (0, 0, 3.20) | #00E8FF (nem feketetest) | **350 W** | 1.5 × 0.15 | `350.0 + 650.0*bass` |
| `LGT_Fill` | fill, elölről | Area SQUARE | (0, −6.0, 4.0) | (0, 0, 3.20) | #6A00FF (nem feketetest) | **60 W** | 4 × 4 | nincs |

- A színt `light.color`-ral kell megadni (sRGB → scene linear konverzióval). A `use_temperature`/`temperature` nem használható, mert palettán kívüli tónust adhat. A „7000 K” csak leíró.
- **Gobo (key):** a `LGT_Key` lámpa node-fája: `TC_Gobo` (Normal) → Mapping → `WAV_Gobo` (Wave, Bands, Sine profile, Scale 6–10) → `CR_Gobo` (kemény csíkok: fekete@0.45 → fehér@0.55, a fekete érték 0.15, nem 0) → Emission.Strength szorzó. Ha a Blender 5.2-ben a lámpa node-fa nem érhető el, a 05 **nem** helyettesít más módszerrel, hanem jelez (K8).
- **IES-szimuláció (master fallback):** a key fényében radiális falloff: a `TC_Gobo` Normal Z komponense → `CR_IES` (széle 0.6, közepe 1.0). IES fájl **tilos** (külső asset).
- **Volumetrika:** a fénykúpot a `GEO_Fog_Volume` + `MAT_Fog` adja. Kész, ha a key kúp és a gobo-csíkok látszanak a ködben.
- **Kontraszt-cél:** a kép kb. 70%-a mélyfekete vagy grafit (master 4.4). Az expozíció nem állítható ennek érdekében +0.5 EV fölé.

### 5.2 Render-beállítás (05)
`engine='CYCLES'`, a GPU-választás a 05 agent-fájl szerint. `cycles.samples` teszt 32–64, végső 256–512, `use_denoising=True`, `denoiser='OPENIMAGEDENOISE'`. `volume_step_rate` 1.0 (teszt 2.0), `volume_max_steps` ≥ 512: ha az 5.2-ben a property nem létezik, naplózza és jelzi (K8). `render.use_motion_blur=True`, `motion_blur_shutter=0.5`. Kimenet: `image_settings.file_format='PNG'`, `color_depth='16'`, `filepath = //pipeline/renders/frames/MW_####.png`.

### 5.3 Kamera (master 7.5)
| Paraméter | Érték |
|---|---|
| `CAM_Main.data.lens` | **35 mm** |
| `sensor_width` / `sensor_fit` | 36 mm / `'VERTICAL'` (`sensor_height` 36 is) |
| DoF | `dof.use_dof=True`, `dof.focus_object=EMP_Cam_Target`, `aperture_fstop=4.0` |
| Clip | `clip_start` 0.1, `clip_end` 40 (02 döntés) |
| Felépítés | `EMP_Cam_Pivot` (0, 0, 2.90) → `CAM_Main` lokális (0, −8.0, 0), **fix rotáció (90°, 0, 0)** |
| Track To | **NEM** használható. A master megengedi a fix rotációt alternatívaként. A Track To a delta-forgatás után a teljes rotációt felülírja, így kioltaná a basszus-roll (`delta_rotation_euler.y`) reakciót. |
| Kompozíció | szimmetrikus centrális totem, a függőleges tengely a képközép. Arányok: `MOLLY` 74–86%, szív 45–63%, `WOOD` 29–37% képmagasság |
| Tilos | vágás, fókusztávolság-animáció, 6°-nál nagyobb ív |

---

## 6. Alap (nem audio) animáció: kulcstáblák (06-animator; master 7.5, 7.8)

**Általános szabályok (master 7.2 + varrat-sebesség):**
- Minden periodikus görbe: kulcs az **1.** és a **periódus+1.** frame-en azonos értékkel. **Soha ne legyen azonos érték az 1. és a 240. frame-en.**
- `Cycles` F-modifier (`mode_before = mode_after = 'REPEAT'`), a stack **első** helyén. A `mode_before` a motion blur miatt is kell (a 1. frame a 0.75…1.25 időt mintavételezi).
- **Sorrend (kötelező, varrat-sebesség):** (1) kulcsok felvitele, (2) a `CYCLES` modifier hozzáadása az első helyre, (3) `interpolation='BEZIER'`, `handle_left_type = handle_right_type = 'AUTO_CLAMPED'` minden kulcson, (4) **`fcurve.update()`** a modifier után. Ciklikus görbén a Blender az első és utolsó kulcs handle-jét a szomszédos ciklus figyelembevételével számolja. Enélkül a nulla-átmenetes végkulcsok (A2, A4, A5, A6, A10, A11) laposak maradnak, és a mozgás a varratnál minden loopban megáll.
- Forgásnál `'LINEAR'` (A1, A3, A7–A9), ott a handle nem számít.
- Megengedett periódusok: 240, 120, 80, 60, 48, 40, 30, 24.

| # | Csatorna | Kulcsok (frame → érték) | Interp. | Periódus |
|---|---|---|---|---|
| A1 | `GEO_Core_Mercury.rotation_euler[2]` | 1 → 0; 241 → **+2π (6.283185)** | LINEAR | 240 |
| A2 | `RIG_Main pose.bones["core"].location[1]` | 1 → 0; 61 → +0.05; 121 → 0; 181 → −0.05; 241 → 0 | BEZIER | 240 |
| A3 | `EMP_Droplet_Orbit.rotation_euler[2]` | 1 → 0; 241 → **−2π** | LINEAR | 240 |
| A4 | `GEO_Droplet_0n.location[2]` (n = 1…6, k = n−1, s = 1 + 40k) | s → 0; s+30 → +0.03; s+60 → 0; s+90 → −0.03; s+120 → 0 | BEZIER | 120 (fázis k·40) |
| A5 | `pose.bones["type_top"].location[1]` | 1 → 0; 31 → +0.025; 61 → 0; 91 → −0.025; 121 → 0 | BEZIER | 120 |
| A6 | `pose.bones["type_bottom"].location[1]` (60 frame-es eltolás = ellenfázis) | 1 → 0; 31 → −0.025; 61 → 0; 91 → +0.025; 121 → 0 | BEZIER | 120 |
| A7 | `EMP_Noise_Pivot.rotation_euler[2]` | 1 → 0; 241 → +2π | LINEAR | 240 |
| A8 | `EMP_Fog_Pivot.rotation_euler[2]` | 1 → 0; 241 → −2π | LINEAR | 240 |
| A9 | `EMP_Floor_Pivot.rotation_euler[2]` | 1 → 0; 241 → +2π | LINEAR | 240 |
| A10 | `EMP_Cam_Pivot.rotation_euler[2]` (ingaív ±4°) | 1 → 0; 61 → +0.069813; 121 → 0; 181 → −0.069813; 241 → 0 | BEZIER | 240 |
| A11 | `CAM_Main.location[2]` (lélegzés ±0.06, lokális alap 0) | 1 → 0; 31 → +0.06; 61 → 0; 91 → −0.06; 121 → 0 | BEZIER | 120 |
| A12 | `CAM_Main.location[1]` (dolly ±0.20, alap −8.0, +Y = befelé; 60 frame késés az ívhez) | 1 → −8.20; 61 → −8.00; 121 → −7.80; 181 → −8.00; 241 → −8.20 | BEZIER | 240 |

- A4 kulcsai túlnyúlhatnak a 241. frame-en. Ez helyes, a Cycles modifier a kulcstartományt ismétli. Ugyanazt a fázist kapja a 01 és a 04, a 02 és a 05, valamint a 03 és a 06 csepp (master: n × 40 frame, periódus 120).
- Pose-csont kulcsolásakor a skill szabálya: `rotation_mode='XYZ'` a csonton (itt csak location kulcs van, de állítsd be), Pose módban, `keyframe_insert(data_path="location", index=1, frame=…)`. Utána vissza Object módba.
- **BPM (csak tájékoztató):** 143.6 BPM, beat = 12.54 frame, ütem = 50.1 frame. 8 s = 19.14 beat, nem egész. A master szerint a koncepció **BPM-független**: ütemre kulcsolt mozgás nincs, a ritmust kizárólag a sütött audio-görbék adják (master 4.6). A beat-rács frame-jei az ablakban (alacsony biztosság, 01 2.4): 1.0, 13.5, 26.1, 38.6, 51.1, 63.7, 76.2, 88.8, 101.3, 113.8, 126.4, 138.9, 151.4, 164.0, 176.5, 189.0, 201.6, 214.1, 226.7, 239.2.

---

## 7. Audio-reaktív animáció (06-animator; master 7.2/7, 7.6, 7.7; 01 2.3–2.6)

### 7.1 Ablak
- **Forrás:** `referencia/CIGARETTA MOLLYWOOD.wav` (abszolút útvonallal).
- **Ablak: 38.781 s … 46.781 s** (01 javaslata, a 2. drop közepe). **Ez eltér a master „drop utáni első ütemcsoport” (~32.9 s) javaslatától**, lásd K1.
- **Leképezés:** `frame = 1 + round((t − 38.781) · 30)`. Fordítva: `t(f) = 38.781 + (f − 1)/30`, f = 1…240.

### 7.2 Vezérlő
- `Audio_Controller`: Empty, (0, 0, 0), `COL_Control`. Custom propertyk: `["Bass"] = 0.0`, `["Snare"] = 0.0`.
- Kezdő kulcs az 1. frame-en mindkettőre (`keyframe_insert(data_path='["Bass"]', frame=1)`), hogy legyen F-Curve.
- F-Curve-elérés **kizárólag** channelbagen át: `anim_utils.action_get_channelbag_for_slot(anim.action, anim.action_slot).fcurves.find('["Bass"]')`. Az `action.fcurves`, `action.groups` és `action.id_root` **nem létezik** 5.x-ben (skill).

### 7.3 Sütési eljárás (lépésről lépésre)
1. **Ideiglenes tartomány:** `frame_start=1`, `frame_end=1500`, `frame_current=1`. Ez lefedi a 46.8 s-ot (≈ 1404 frame). A végén vissza kell állítani **1…240**-re (a 06 agent-fájl „frame_end a hang hosszához” utasítása a végső állapotra nem érvényes).
2. **Operátor:** az 5.2-ben a név valószínűleg `bpy.ops.graph.sound_to_samples` (régi neve `graph.sound_bake`). A 06 `hasattr`-ral dönt, és a használt nevet naplózza.
   - Bass: `low=20.0, high=150.0, attack=0.005, release=0.18`
   - Snare: `low=2000.0, high=5000.0, attack=0.002, release=0.08`
   - Egyszerre csak a cél F-Curve legyen `select=True`. Graph Editor context kell: `bpy.context.temp_override(window=…, area=…, region=…)`, egy area `ui_type`-ját `'GRAPH_EDITOR'`-ra állítva.
   - Ha `--background` alatt nincs window, ezért az override nem lehetséges, akkor UI-val induló, de **külön** Blender-folyamatban fusson a script (soha nem a felhasználó nyitott sessionjében), és a 06 jelezze (K12).
3. **Minták vagy kulcsok:** a sütés eredménye lehet sampled points (`fcurve.sampled_points`) vagy kulcs. A 06 ellenőrzi. Ha minták jöttek, `fcurve.convert_to_keyframes(start, end)` következik.
4. **Ablak-kivágás:** legyen `F0` az a forrás-frame, ahol az audio t = 0 van (várhatóan a sütéskori `frame_current`/`frame_start` = 1). Minden f = 1…240-ra `v[f] = fcurve.evaluate(F0 + 38.781·30 + (f − 1))` (tört frame, lineáris kiértékelés). Utána a görbe kulcsai törlődnek, a 240 érték LINEAR kulcsként visszaíródik az 1…240 frame-re.
5. **Időeltolás-ellenőrzés (kötelező, pass/fail):** a Blender sávszűrője és envelope-ja eltér a 01 STFT-mérésétől, ezért **nem** egyetlen argmax-ot kell vizsgálni, hanem az időeltolást.
   - A 01 erős basszuscsúcsaihoz (frame **31, 104, 116, 130**) keresd meg a sütött bass-görbe legközelebbi lokális maximumát (±6 frame-es keresőablakban).
   - A négy eltérés **mediánja** legyen **|Δ| ≤ 3 frame**.
   - Snare: a 117 és 125 körüli csúcspár legközelebbi lokális maximumai ±3 frame-en belül legyenek (gyenge kontroll, mert a sáv zajos).
   - Ha nem teljesül, a 06 egyszer megpróbálja `F0 = 0`-val (off-by-one), és ha úgy sem, **jelent**. Kézzel tologatni tilos.
   - Kiírandó a négy Δ, a medián, valamint a sütött görbe abszolút argmax-a is (tájékoztató; nem kell, hogy pont a 130 legyen).
6. **Csúcs:** `peak_bass`, `peak_snare` = max(v[1…240]) Blender-egységben, a crossfade előtt. A 01 számai (1288 / 3507) nem Blender-egységek, csak a görbe alakja hasonlítható. A 06 kiírja a mért csúcsokat.
7. **Snare-simítás (master 7.6, „ha zajos”):** a 01 szerint a 2–5 kHz-es sáv zajos (szinti / hi-hat). A 06 legfeljebb egy kulcs-szintű simítást végezhet ([0.25, 0.5, 0.25] 3-tap, a Graph „Smooth Keys” megfelelője), utána újraméri a `peak_snare`-t. Ezt jelenti. A küszöb-offset a K6 döntéséig **nem** alkalmazható.
8. **Crossfade (master 7.2/7):** f = 233…240-re `w = (f − 232)/9`, `v'(f) = (1 − w)·v(f) + w·v(1)`. Plusz egy kulcs: **241 → v(1)**. Így a 240. frame nem azonos az 1.-vel (w = 8/9), a 241. viszont igen.
9. **Modifier-stack (sorrend kötött):** `CYCLES` (REPEAT/REPEAT) → `GENERATOR` (`mode='POLYNOMIAL'`, `poly_order=1`, `coefficients=(0.0, 1/peak)`) → `LIMITS` (`use_min_y=True, min_y=0.0, use_max_y=True, max_y=1.0`). Eredmény: `bass_n`, `snare_n ∈ [0, 1]`.
10. **Kiírandó:** `|n(1) − n(240)|` mindkét sávra (≤ 0.05), `|n(241) − n(1)|` (< 0.001), az 5. pont eltolás-adatai és a csúcsértékek.

### 7.4 Referencia-csúcsok (01 2.4 / 2.5, szó szerint; csúcs-normalizált, nem Blender-egység)
**Basszus (20–150 Hz), amp ≥ 0.45:**

| t_ablak (s) | abs (s) | frame | amp |
|---|---|---|---|
| 0.067 | 38.847 | 3 | 0.51 |
| 1.000 | 39.781 | **31** | 0.74 |
| 1.767 | 40.547 | 54 | 0.68 |
| 2.167 | 40.947 | 66 | 0.67 |
| 2.633 | 41.414 | 80 | 0.68 |
| 2.967 | 41.747 | 90 | 0.64 |
| 3.200 | 41.981 | 97 | 0.53 |
| 3.433 | 42.214 | **104** | 0.75 |
| 3.833 | 42.614 | 116 | 0.73 |
| 4.300 | 43.081 | **130** | **1.00** (ablak-maximum) |
| 4.633 | 43.414 | 140 | 0.49 |
| 5.033 | 43.814 | 152 | 0.60 |
| 5.367 | 44.147 | 162 | 0.57 |
| 5.933 | 44.714 | 179 | 0.59 |
| 6.300 | 45.081 | 190 | 0.50 |
| 6.700 | 45.481 | 202 | 0.60 |
| 7.033 | 45.814 | 212 | 0.50 |
| 7.633 | 46.414 | 230 | 0.53 |

**Snare (2–5 kHz), amp ≥ 0.5:**

| t_ablak (s) | abs (s) | frame | amp |
|---|---|---|---|
| 3.867 | 42.647 | 117 | 0.64 |
| 4.133 | 42.914 | **125** | **1.00** |
| 7.400 | 46.181 | 223 | 0.54 |

Megjegyzések:
- A snare alapszintje az 1. és a 240. frame-en ≈ 0.29 · csúcs. Ezért nyugalomban is ≈ 0.29 `snare_n` lesz (pl. `EMIT_TypeRim` ≈ 6.85). Ez mért tény, nem hiba.
- A basszus szinkópált / wobble jellegű, a csúcsok 5–15 frame-enként jönnek.

### 7.5 Driverek (master 7.6 / 7.7, alapértékek)
Driver-szabályok (skill + master):
- `driver.type='SCRIPTED'`, egy változó: `bass` vagy `snare`, `type='SINGLE_PROP'`, `targets[0].id_type='OBJECT'`, `targets[0].id = Audio_Controller`, `data_path='["Bass"]'` vagy `'["Snare"]'`.
- Csak egyszerű kifejezés (`base + k*bass`), amely autoexec nélkül fut. Ellenőrzés: `driver.is_valid == True`. Az autoexec bekapcsolása tilos.
- Node-socketnél: `sock = mat.node_tree.nodes["EMIT_Neon"].inputs["Strength"]; fc = sock.driver_add("default_value")`.

| # | Cél (ID → data path) | Kifejezés | Megengedett k | Hard cap | Érték bass_n / snare_n = 1-nél |
|---|---|---|---|---|---|
| D1 | `CAM_Main` → `delta_location[2]` | `-0.010*bass` | 0.006–0.014 | −0.020 | −0.010 |
| D2 | `CAM_Main` → `delta_rotation_euler[1]` (roll a nézeti tengely körül) | `0.00611*bass` | 0.00349–0.00873 rad | 0.01396 | 0.00611 |
| D3 | `CAM_Main` → `delta_location[0]` | `0.004*snare` | 0.002–0.006 | 0.010 | 0.004 |
| D4 | `MAT_Neon_Magenta` `EMIT_Neon.inputs["Strength"]` | `6.0 + 24.0*bass` | 14–34 | 40 | 30.0 |
| D5 | `MAT_Neon_Cyan` `EMIT_Neon.inputs["Strength"]` | `6.0 + 24.0*bass` | 14–34 | 40 | 30.0 |
| D6 | `MAT_Neon_Slit` `EMIT_Slit.inputs["Strength"]` | `5.0 + 15.0*bass` | 10–20 | 25 | 20.0 |
| D7 | `MAT_Type_Glow_Magenta` / `_Cyan` `EMIT_TypeGlow.inputs["Strength"]` | `3.0 + 9.0*bass` | 6–12 | 15 | 12.0 |
| D8 | `MAT_Chrome_TypeRim_Magenta` / `_Cyan` `EMIT_TypeRim.inputs["Strength"]` | `2.5 + 15.0*snare` | 10–20 | 25 | 17.5 |
| D9 | `LGT_Rim` data → `energy` | `350.0 + 650.0*bass` | 400–900 | 1300 | 1000 |
| D10 | `LGT_Accent_Cyan` data → `energy` | `350.0 + 650.0*bass` | 400–900 | 1300 | 1000 |
| D11 | `LGT_Key` data → `energy` | `1200.0 + 400.0*snare` | 200–600 | 1800 | 1600 |
| D12 | `GEO_Core_Mercury` → `delta_scale[0]`, `delta_scale[1]` | `1.0 + 0.10*bass` | 0.06–0.14 | 1.18 | 1.10 |
| D13 | `GEO_Core_Mercury` → `delta_scale[2]` | `1.0 - 0.08*bass` | 0.05–0.11 | ≥ 0.86 | 0.92 |
| D14 | `GEO_Core_Mercury` → `modifiers["DSP_Core"].strength` | `0.15 + 0.12*bass` | 0.08–0.15 | 0.30 | 0.27 |
| D15 | `GEO_Text_Top`, `GEO_Text_Bottom`, `GEO_TextGlow_Top`, `GEO_TextGlow_Bottom` → `delta_scale[0..2]` (4 objektum × 3 tengely) | `1.0 + 0.025*snare` | 0.015–0.035 | 1.045 | 1.025 |
| D16 | `GEO_Droplet_01…06` → `delta_scale[0..2]` (6 × 3) | `1.0 + 0.15*bass` | 0.08–0.20 | 1.25 | 1.15 |
| D17 | `MAT_Fog` `VAL_FogDensity.outputs[0]` → `default_value` | `0.035 + 0.015*bass` | 0.008–0.020 | 0.060 | 0.050 |
| D18 | `MAT_Mercury_Floor` `BUMP_Floor.inputs["Strength"]` | `0.05 + 0.15*bass` | 0.08–0.20 | 0.30 | 0.20 |

- **Tilos:** a betűk Z-pozíciója, forgása és alakja a basszusra nem reagál. A `EMIT_ReflCard` konstans 8.0.
- **Roll-ellenőrzés (D2):** `delta_rotation_euler.y = 0.1` próbaértéknél a kép a középpontja körül billenjen (horizont-dőlés), ne pásztázzon. Ha pásztáz, a 06 jelent. A tengely nem cserélhető önkényesen.

### 7.6 Seamless loop szabályok (összefoglaló)
1. 240 frame-es periódus, renderelés 1–240. A 241. frame ≡ az 1.
2. Az 1. és a 240. frame-en azonos kulcs tilos.
3. Periodikus kulcsok az 1. és a periódus+1. frame-en, `Cycles` modifier a stack elején, utána `fcurve.update()` (ciklikus handle-ek).
4. Forgás LINEAR, 0 → ±2π. Az ellenőrzésnél a forgást mod 2π kell összevetni.
5. Csak a 240 osztói használhatók periódusnak.
6. Animált zaj csak az orbit-empty-kből (Noise, Fog, Floor, és a Displace az `EMP_Noise_Orbit`-ből). W- vagy offset-animáció tilos.
7. Audio: 8 frame-es crossfade (233–240), `|n(1) − n(240)| ≤ 0.05`, 241 = 1.
8. Nem-audio csatornák: `|v(241) − v(1)| < 0.001` **és** varrat-sebesség: `|(v(2) − v(1)) − (v(241) − v(240))| ≤ 0.1 · max|Δv|` (max|Δv| = a ciklus legnagyobb frame-enkénti változása).

---

## 8. Átadási ellenőrzőlisták

### 8.1 03-modeler → `pipeline/01_model.blend`
- [ ] A factory objektumok törölve. Minden objektum a 1.2 szerinti collectionben van, és nincs `.001`-es vagy névtelen objektum, datablock vagy collection.
- [ ] A 2.1 összes objektuma létezik. A világpozíciók (a bone-parent után is) ≤ 1 mm-re, a méretek (evaluált bbox) ≤ 1 mm-re egyeznek a táblával.
- [ ] `GEO_Core_Mercury`: 64 × 32 UV-gömb, `SUB_Main` (2/3) → `DSP_Core` sorrend, `TEX_Core_Clouds` CLOUDS, OBJECT coords = `EMP_Noise_Orbit`, mid 0.5, strength 0.15.
- [ ] Cseppek: méretek és pályák a 2.2 szerint, hierarchia `core` → `EMP_Droplet_Tilt` (18°) → `EMP_Droplet_Orbit` → csepp. Egyik csepp sem gyereke a szívnek.
- [ ] Szöveg: beépített Bfont (`<builtin>`), `fonts.load()` nincs. `MOLLY`/`WOOD` csupa nagybetűs ASCII, a 2.1-es paraméterek beállítva. A mért bbox-magasság és -szélesség kiírva, eltérés esetén jelentés (K5).
- [ ] `RIG_Main`: 4 csont (`root`, `core`, `type_top`, `type_bottom`), mind `use_deform=False`. A gyerekek a 3.1 szerint vannak bone-parentelve, a `TextGlow` a csonthoz és nem a szöveghez kötve.
- [ ] Shape Key: 0. Constraint: 0.
- [ ] MESH n-gon = 0. Scale (1,1,1) és rotation (0,0,0) minden MESH-en (a kivételek a 2.4 szerint). A nem-manifold élek csak a síkokon vannak.
- [ ] `CAM_Main` létezik (rotation 90°, 0, 0, parent `EMP_Cam_Pivot`), lámpa nincs (azokat az 05 hozza létre).
- [ ] Kompozíció-ellenőrzés (2.5) és ütközés-tűrés (2.6) kiírva.
- [ ] Scene: 1080 × 1920, 30 fps, 1–240 (előbeállítás).

### 8.2 04-lookdev-artist → `pipeline/02_textured.blend`
- [ ] A 4.3 tábla minden anyaga létezik, a hozzárendelés pontos, nincs üres slot.
- [ ] Minden driver-cél node létezik a pontos névvel, és a cél-socket **nem linkelt**: `EMIT_Neon` (×2), `EMIT_Slit`, `EMIT_TypeGlow` (×2), `EMIT_TypeRim` (×2), `EMIT_ReflCard`, `VAL_FogDensity`, `BUMP_Floor`. Az alapértékek: 6.0 / 5.0 / 3.0 / 2.5 / 8.0 / 0.035 / 0.05.
- [ ] A színek a 4.1 HEX-ből `from_srgb_to_scene_linear()`-rel készültek. Palettán kívüli szín nincs. A K3-as ideiglenes színek a jelentésben meg vannak jelölve.
- [ ] Króm: Metallic 1, a roughness kimenet 0.02–0.08, a bump ≤ 0.05. Padló: 0.02–0.05. Beton: 0.75–0.95, Bevel-node élkopás. Fog: anisotropy 0.55–0.70, a szín-keverés ≤ 10%, maszk ∈ 0.5…1.0.
- [ ] Az animált zajok textúra-koordinátái az orbit-empty-k (`EMP_Floor_Orbit`, `EMP_Fog_Orbit`). Animált W vagy offset nincs.
- [ ] A reflexiós kártyák `visible_camera=False`. Gyors próbarenderen (Workbench helyett Cycles, 16 sample) **a króm nem fekete**, a kártyák és a neon tükröződnek benne.
- [ ] Külső kép, textúra vagy HDRI nincs (`bpy.data.images` üres, a Render Result kivételével).

### 8.3 05-lighting-artist → `pipeline/03_lit_scene.blend`
- [ ] 4 lámpa (`LGT_Key`, `LGT_Rim`, `LGT_Accent_Cyan`, `LGT_Fill`) az 5.1 szerinti pozícióval, típussal, színnel, teljesítménnyel és mérettel (`spot_size` radiánban), saját datablockkal, constraint nélkül.
- [ ] Key gobo és IES-szimuláció a lámpa node-fájában. Ha ez nem lehetséges, jelentés (K8).
- [ ] World #040406, nincs World-volume, nincs HDRI.
- [ ] Kamera: 35 mm, 36 mm VERTICAL, DoF az `EMP_Cam_Target`-re f/4.0, **nincs Track To**.
- [ ] Render: Cycles, a GPU-backend naplózva, AgX + look (a pontos enum-név naplózva), 1080 × 1920, 30 fps, 1–240, motion blur 0.5, PNG 16 bit, volume-beállítások (vagy jelentés a hiányukról).
- [ ] Tesztrender (50%, 32–64 sample, denoise) a `pipeline/renders/test_v01.png`-be. Ellenőrizni kell: a fénykúp és a gobo-csíkok látszanak a ködben; a magenta (bal) és cián (jobb) rim kivágja a szívet és a betűket; kb. 70% mélyfekete vagy grafit; a `MOLLY`/`WOOD` olvasható és az UI-biztos sávon belül van.
- [ ] Meglévő objektumot nem hozott létre újra (nincs `.001`).

### 8.4 06-animator → `final_animated_scene.blend`
- [ ] Az A1–A12 kulcsok a 6. fejezet táblája szerint, a 6. fejezet sorrendjével (kulcsok → Cycles első helyen → AUTO_CLAMPED → `fcurve.update()`), és a 240. kulcs nem duplikált.
- [ ] Minden nem-audio csatornán **kiírva**: `|v(241) − v(1)| < 0.001` (forgásnál mod 2π) **és** a varrat-sebesség-teszt (7.6/8). Az ingaív és a lebegés nem állhat meg a varratnál.
- [ ] Csak channelbag API van használva (nincs `action.fcurves`). A pose-csontok kulcsai Pose módban kerültek fel, a végén Object mód.
- [ ] `Audio_Controller` `["Bass"]`, `["Snare"]`: a sütés a 7.3 szerint történt, a használt operátornév naplózva. Időeltolás-ellenőrzés (7.3/5): a 31/104/116/130 csúcsok Δ-mediánja ≤ 3 frame, kiírva. A `peak_bass` és `peak_snare` (Blender-egység) kiírva.
- [ ] Crossfade 233–240, kulcs a 241-en = v(1). Modifier-stack: Cycles → Generator (0, 1/peak) → Limits 0–1. `|n(1) − n(240)|` ≤ 0.05 mindkét sávra **kiírva**.
- [ ] D1–D18 driverek léteznek, mind `is_valid`, egyszerű kifejezésűek (autoexec nélkül). Mintavétel a 1, 31, 104, 125, 130 és 240 frame-en: minden driven érték a hard capen belül van, és követi a `bass_n`/`snare_n`-t (kiírva).
- [ ] A D2 roll-ellenőrzés elvégezve. Shape Key nincs. Kulcs és driver egyetlen csatornán sem ütközik.
- [ ] A scene a végén `frame_start=1`, `frame_end=240`, `fps=30`.
- [ ] Opcionális preview: néhány frame (1, 125, 130, 240) alacsony mintával a `pipeline/renders/`-be. A 240 → 1 varrat vizuálisan nem ugrik.

---

## 9. Validációs összefoglaló (bármely agent lefuttathatja)
- Névellenőrzés: minden objektum `GEO_|RIG_|LGT_|CAM_|EMP_` előtagú vagy `Audio_Controller`. Minden anyag `MAT_` előtagú. Nincs `.\d{3}` végződés.
- Külső asset: `bpy.data.images` (Render Result és Viewer Node kivételével), `bpy.data.fonts` (csak `<builtin>`), `bpy.data.sounds` (a sütés után eltávolítható) ellenőrizve.
- Loop: a 7.6 és a 8.4 kiírásai.

---

## 10. Nyitott kérdések / ütközések (felhasználói döntésre vár; a spec nem talál ki saját megoldást)

| # | Téma | Leírás | A spec jelenlegi kezelése |
|---|---|---|---|
| **K1** | **Audio-ablak eltér a mastertől** | A master (10.1) „a drop utáni első teljes ütemcsoportot” javasolja (~32.9–40.9 s). A 01 mérése szerint ez nem loopol: `|v1 − v240|` basszus ≈ 0.60, snare ≈ 0.26, ami 8 frame-es crossfade-del sem fér a 0.05-ös tűrésbe. A 01 javaslata **38.781–46.781 s** (a 2. drop közepe, ~6 s-ra a drop elejétől), `|diff|` bass 0.012, snare 0.011. A master 0. fejezete megengedi, hogy a 01 módosítsa a kezdőpontot, de a 6.3 szerint a felhasználót értesíteni kell. | A spec a **38.781 s**-os ablakot használja. A felhasználó jóváhagyása szükséges. Más ablaknál a 7.4 csúcstáblát a `scripts/audio_final.py`-vel újra kell generálni. |
| K2 | `Audio_Controller` névkonvenció | A `CTL_` előtag-szabályt sérti, de a master és a 06 agent-fájl ezt a nevet rögzíti. | Kivételként megtartva. |
| **K3** | Nem specifikált színek | A master nem adja meg: (a) a hátsó neon-rés (`EMIT_Slit`) színét, (b) a reflexiós kártyák (`EMIT_ReflCard`) színét. A (c) TextGlow szavankénti színe (MOLLY magenta, WOOD cián) a 7.3 „MOLLY él / WOOD él” sorából következtetett. | (a), (b): **ideiglenesen WHITE HOT #F2F6FF** (palettán belüli), ez **nem végleges döntés**. (c): a következtetés megerősítendő. |
| K4 | `MAT_Type_Rim` anyag-szerkezet | A master „rétegként” írja le. Szavanként eltérő színnel, és mivel a szív nem izzhat, ez két külön anyagot jelent. | `MAT_Chrome_TypeRim_Magenta/_Cyan`, `MAT_Type_Glow_Magenta/_Cyan` (névvéglegesítés a master 6.4 alapján). |
| K5 | Tipográfia-megvalósíthatóság | (a) A Bfont-tal a 0.65 m-es sapkamagasság és a 3.0–3.4 m-es `MOLLY`-szélesség `space_character=0.90` mellett nem biztos, hogy egyszerre teljesül. (b) A FONT objektumon az 5.2-ben az Apply Rotation nem garantált, ezért a 90°-os X-rotáció alkalmazatlan marad. | A 03 mér és jelent, nem hangol. A FONT rotation-kivétel rögzítve. |
| K6 | Snare küszöb-offset képlete | A master 7.6 `[-0.15/peak … ]` alakja dimenzionálisan kétértelmű (nyers egységben a 0.15/peak elhanyagolható). | Küszöb nincs. Csak Smooth + Generator (0, 1/peak) + Limits, ami a master kötelező alapja. |
| K7 | Agent-fájl vs. master eltérések | 06: „frame_end a hang hosszához”, példa `bass*0.05`, Shape Key, „variáció/overlap” (a master szerint csak a 240 osztói). 04: króm roughness 0.02–0.15 (master: 0.02–0.08), „kétrétegű variáció” a neonokon (master: tiszta emisszió). 05: IES Texture node (a külső IES fájl tilos), World-volume (master: fog-kocka), „színhőmérséklet” (master: HEX). | A master érvényes (6. fejezet), a spec ennek megfelelően rendelkezik. |
| K8 | Blender 5.2 API-bizonytalanság | A lámpa node-fa (gobo/IES) elérhetősége, a `volume_step_rate`/`volume_max_steps` léte, az AgX look-enum neve és a hang-sütő operátor neve (`sound_to_samples` vs. `sound_bake`) az 5.2-ben. | Az agent ellenőrzi, és hiány esetén jelent. Csendes helyettesítés tilos. |
| K9 | A szív forgásának láthatósága | Mivel a Displace-zaj az orbit-empty terében van, a szív sziluettje a forgást nem mutatja, csak a shader Object-koordinátás foltjai. | Tájékoztató. Ha a felhasználó látható forgást kér, ez architekturális döntés. |
| K10 | 01 bizonytalanságok | A downbeat ismeretlen, a beat-rács horgonya alacsony biztosságú, a tiszta snare nem szeparálható (lehet, hogy csak 3 jelentős snare-csúcs lesz). | Tájékoztató. A koncepció BPM-független. |
| K11 | Szöveg-extrude értelmezése | A master `extrude 0.14` értékét a spec Blender-paraméterként kezeli (szimmetrikus, teljes mélység 0.28 m). Ez konzisztens a +0.18 m-es glow-távolsággal. | A paraméter = 0.14. |
| K12 | Sütés `--background` módban | A skill szerint a scriptek `--background` folyamatban futnak, de a Graph-operátor window/area contextet igényel, ami háttérmódban hiányozhat. | Ha nem megy, a script külön, UI-s Blender-folyamatban fut, és a 06 jelzi. |
| K13 | Köd-sűrűség maszk-értelmezése | A master „Density 0.035 + 0.015·bass, Noise-maszkkal, hard cap 0.060”. Ha a maszk átlaga 1.0 (pl. 0.5…1.5), az átlag 0.035 marad, de lokálisan átlépi a 0.060-as capet. A spec a capet tartja: maszk ∈ 0.5…1.0, ezért a nyugalmi **átlagsűrűség ≈ 0.026**. | Cap-tartó változat (02 döntés). Ha a felhasználó az átlagos 0.035-öt preferálja, a maszk-tartományt kell módosítani. |
