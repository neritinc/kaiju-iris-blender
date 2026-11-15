# 01 – REFERENCIA-ELEMZES: „CIGARETTA MOLLYWOOD”
Szerzo: 01-ref-analyzer. Kiegesziti a `pipeline/00_master_concept.md`-t (7. fejezet kotott szamai valtozatlanok). Mert adat = merve; ami nem merheto: `ismeretlen`.

## 0. Osszefoglalo
- **BPM ~ 143.6** (negyedes, 4/4; ugyanez half-time erzettel ~71.8). Beat-hossz 0.4179 s, uteme 1.671 s. 8.000 s = **19.14 beat = 4.79 utem** (nem egesz szam; lasd 4.3).
- **Javasolt 8 s ablak: kezdo = 38.78 s, veg = 46.78 s** (a 2. drop kozepe). Itt a basszus- es snare-gorbe eleje/vege majdnem azonos (|v1-v240| bass 0.012, snare 0.011 a csucshoz norm.; a 7.2/7. pont tuerese 0.05).
- A 4 videó **nem** a Canvas-stilus kozvetlen mintaja: VJ/visual-show reelek (render / viewport-drotkeret / live koncert valtogatva), kozepso hos-objektum, krom/uveg anyag, neon, tukros viz-padlo (IMG_0836). A palettat NEM modositom (lasd 3.4).

## 1. Bemenet es eszkozok
| Eszkoz | Allapot |
|---|---|
| ffmpeg (teljes utvonal) | elerheto, frame-kinyeres, scene-detekcio, nyers RGB pipe |
| ffprobe | **nincs** (a Spotify Downloader mappaban nem volt) – tartalek: `ffmpeg -i` fejlec |
| Python 3 + numpy 2.5.4 + scipy 1.18.1 + librosa 1.0.0 | elerheto |
| PIL/Pillow | **hianyzik** – tartalek: ffmpeg rawvideo pipe + numpy (szinelemzes) |
| Scriptek | `scripts/audio_analysis.py`, `audio_window.py`, `audio_sections.py`, `audio_final.py`, `video_colors.py` |
| Frame-ek | `pipeline/frames/IMG_<id>/%04d.png` (2 fps, 640 px magas) + `pipeline/frames/IMG_<id>_sheet.png` (16 egyenletesen elosztott frame 4x4 tile-on; a vizualis ellenorzes ezeken tortent) |

Fajlok (mert): `CIGARETTA MOLLYWOOD.wav` PCM 24 bit, 44.1 kHz, sztereo, 134.40 s (2:14.4); a hasznos zene ~0–108 s, utana csend/lecsengo. Videok:

| Fajl | Felbontas | Arany | FPS | Hossz | Hang |
|---|---|---|---|---|---|
| IMG_0836.MP4 | 720x1280 | **9:16** (0.5625) | 25 | 28.40 s | AAC (nem elemezve) |
| IMG_6422.MP4 | 1024x1280 | 4:5 (0.8) | 30 | 27.30 s | AAC (nem elemezve) |
| IMG_7563.MP4 | 1024x1280 | 4:5 (0.8) | 25.01 | 31.67 s | AAC (nem elemezve) |
| IMG_9135.MP4 | 1280x704 | 1.818:1 (~16:8.8) | 29.56 | 35.35 s | AAC (nem elemezve) |

Stilluskep-referencia a mappaban nincs (csak videok).

## 2. Hang: ritmikai DNS
### 2.1 Tempo
| Modszer | Eredmeny |
|---|---|
| librosa beat_track | 143.55 BPM, 257 beat, median IBI 0.4180 s |
| Onset-autokorrelacio (32–100 s) | 0.4180 s, 0.8243 s, 1.6486 s, 3.3088 s, 6.6177 s -> **143.58 BPM**, minden szorzonal konzisztens |
| Beat-idopontok linearis regresszioja | 145.0 BPM (a tracker zajos, szoras 28 ms) – nem hasznalom |
| Lokalis tempo percentilisek | 5%: 105, 50%: 143.6, 95%: 147.7 (a nyujtott/half-time szakaszok miatt) |
- **Vegleges: 143.6 BPM +-0.5**; beat 0.4179 s = 12.54 frame @30 fps; utem 1.671 s = 50.1 frame.
- Beat-racs horgony: **33.348 s** (alacsony biztossag: onset-illesztes pontszama 0.20; a 3. drop racs-eltolasa 0.016 beat, ez tamogatja). A **downbeat (utem 1. uteme) ismeretlen** – csak beat-racs van.

### 2.2 Szerkezet (merve, 0.5 s-os basszus-atlag alapjan)
| Idoszak (s) | Tartalom |
|---|---|
| 0–12.5 | intro: nincs 20–150 Hz energia, kozep/snare sav van |
| 12.6–23.7 | **drop 1** (basszus ~230–510 egyseg) |
| 24–32.5 | break: basszus ~0, 2 egyedi basszus-utes (26.5 s, 29.5 s) |
| ~32.8–60 | **drop 2** (basszus ~480–690, a legerosebb) |
| 60–71 | alacsonyabb basszus (~130–280) |
| 71.5–79 | rovid utesek (72.5, 76 s), kozben csend |
| 79.3–101.8 | **drop 3** (basszus ~430–650) |
| 102–~108 | outro, basszus nelkul, ~110 s-tol gyakorlatilag csend |

Savok atlaga 4 s-onkent (STFT magnitudo-osszeg, librosa, 22.05 kHz, n_fft 2048; csak relativ ertek): drop 2 alatt (36–60 s) bass ~360–550, mid ~1500–1700, snare ~1000–1200, hi(5–11 kHz) ~1350–1620.

### 2.3 Javasolt 8 s ablak (7. fejezet 3. szabaly: nem ugyanaz, mint „drop utani elso ut-csoport” – jelezni kell)
- A master szerinti javaslat („a drop utani elso teljes utemcsoport”, azaz kb. 32.9–40.9 s) **rosszul loopol**: itt az ablak elejen a basszus meg csend (v1/csucs ~0.10), a vegen magas (~0.70) -> |v1-v240| = 0.60 (snare 0.26), a 0.05-os tuerest nem teljesiti 8 frame crossfade-del sem.
- **Javasolt: start 38.78 s (38.781), end 46.78 s.** A 38.363 s (-0.42 s) es a 39.198 s (+0.42 s) kezdopontok is merve: |diff| bass 0.32 ill. 0.12 -> rosszabbak. A 38.85 s kornyeke (kb. +0.07 s) hasonloan jo (cont. 0.054).
- Ez a 2. drop kozepe, ~6 s-ra a drop elejetol; nincs benne breakdown vagy csend. A 7. fejezettel nincs utkozes a kotott szamokkal, de a 02-esnek jeleznie kell a felhasznalonak, hogy az ablak **nem a drop eleje**.
- Frame-lekepezes: `frame = 1 + round((t - 38.781) * 30)`, 1-alapu, 1..240.
- A 8 s nem egesz szamu beat: a vege 0.14 beattel (kb. 1.8 frame) a racs utan van – a zene nem loopol hallhatoan, de a Canvas nema, ezert csak a sutott gorbek 8 frame-es crossfade-e szamit.

### 2.4 Basszus (20–150 Hz) csucsok az ablakban (nyers sav, csucs-normalizalt 0–1, a csucs = 1.0 az ablak maximuma)
Minden detektalt csucs (relativ amplitudo >= 0.45), `t_ablak s -> frame (1..240) : amp`:

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

A basszus a riddim-re jellemzoen **szinkopalt/wobble** jellegu: csucsok nem a beat-racson, hanem 5–15 frame-es (0.17–0.5 s) koztekkel. Beat-racs frame-ek az ablakban (negyed-hang): 1.0, 13.5, 26.1, 38.6, 51.1, 63.7, 76.2, 88.8, 101.3, 113.8, 126.4, 138.9, 151.4, 164.0, 176.5, 189.0, 201.6, 214.1, 226.7, 239.2 (alacsony biztossag, 2.1).

### 2.5 Snare / kozepmagas (2–5 kHz) csucsok
| t_ablak (s) | abs (s) | frame | amp |
|---|---|---|---|
| 3.867 | 42.647 | 117 | 0.64 |
| 4.133 | 42.914 | **125** | **1.00** |
| 7.400 | 46.181 | 223 | 0.54 |
- Az ablakban csak 3 ketsegtelen csucs van (>=0.5), 2 a 4. mp korul (frame 117–125). A 2–5 kHz sav nem tiszta snare: szintetizator/hi-hat/vokal-jeleg is van benne, ezert a snare-gorbe „zajos” (7.6 szerint: Smooth + kuszob-offset javasolt). Tiszta snare-szeparacio nem tortent: `ismeretlen`, hogy a hallhato snare hany ponton van.
- Az ablak teljes, sima 2–5 kHz-es energiaszintje nagyjabol allando (~0.29 a csucs hanyadaban az 1. es a 240. frame-en).

### 2.6 Sutesi normalizalas (7.6) – merve
Az `Audio_Controller` sutott gorbe csucsat a 06-osnak kell Blenderben ujra megmerni, mert a Blender sound_bake mas egyseg. Referenciaul az en meresem (STFT-magnitudo-osszeg, simitott attack/release kovetovel, ablak 38.781–46.781): `bass_peak ~ 1288`, `snare_peak ~ 3507` (**nem Blender-egyseg**). Ertekes csak a relativ gorbe-alak.

### 2.7 Energiasavok osszegezve
| Sav | Megjegyzes |
|---|---|
| Basszus 20–150 Hz | drop-okban folyamatos, 5–15 frame koztes csucsok; a legnagyobb csucs frame 130 |
| Kozep 150–2000 Hz | folyamatos, drop-okban ~1500–1700 |
| Snare 2–5 kHz | ritka, kiemelkedo csucs: frame 125; frame 117 es 223 gyengebb |
| Magas 5–11 kHz | drop-okban magas (~1350–1620), intro/break ~15–880 |

## 3. Vizualis elemzes (video referenciak)
Megjegyzes: minden videot egyenletes 2 fps-es, 16 db-os mintan neztem meg (4x4 tile). Pontos fenyiranyt/szamszeru perspektivat (FOV) a mintakbol nem lehet kiolvasni: `ismeretlen`.

### 3.1 IMG_0836.MP4 – „sci-fi/ketelezo lenyek a kupola-szinpadon” (9:16, 25 fps, 28.4 s)
- **Stilus:** stilizalt-realisztikus 3D, sotet Y2K/rave; ultraviola-kek neon, uvegszeru/tukros fem teremtmeny (szarvak, hosszu lepkes labak), vizszerű fekete tukor-padlo hullamzo tukrozessel, kupolat ivek cian neon-keretekkel, LED-kupola kepernyokkel (felirat, kor-mintak, sakktabla, macska-kepek: ezek tartalomreferencia nem kellenek).
- **Kompozicio:** szimmetrikus kozepso hos, a kepmagassag kb. 25–95%-at foglalja; alacsony kameraallas (labtol felfele), erosen szeles latoszogu / halszem-jellegu torzitas, fuggoleges iv-vonalak vezetnek a kozeppontra.
- **Sziluett:** magas, keskeny (labak ~60% magassag), 2 hegyes szarv a fejen.
- **Mozgas / kamera:** lassu-kozepes „orbit” + belepes/kihuzas, dutch-tilt (ferdites) egyes kepekben; a hos folyamatosan mozog (jarasciklus). A hatter-LED-ek villognak, kozte feher-kek „flash” kepek.
- **Vagasi ritmus:** a ffmpeg scene>0.35 21 vagast talalt 28.4 s alatt (kb. 1 vagas/1.35 s); 2 fps-es frame-kulonbseg atlaga 62.8 (nagy), 56-bol 41 lepes >40 -> **nagyon gyors, flash-intenziv**.
- **Fenyiranyt:** elsodleges forras a hatulso/oldalso neon es a kupola LED-fal (hatulrol/foloeld), az elolap sotet; a tukorpadlo erosen visszaadja a hatterfalat.
- **Kontraszt:** magas; atlagos luma 0.317, sotet (<0.1) pixelek 22.8%, vilagos (>0.8) 12.0% (feher LED-villanok).
- **Szinek (merve, 4 bites kvantalas kozepei, +-16 ertek):** `#0D1330` (20.9%, mely ejkek), `#040510` (15.0%, mely fekete), `#FCF4FD` (8.7%, LED-feher), `#15184B` (7.8%), `#112451`, `#162A6C`, `#2C2970`, `#261351` ... ultraviola-kek, `#4E2F8F` (ultraviola), a cian ivek (pontos HEX nem merve: `ismeretlen`).

### 3.2 IMG_6422.MP4 – „szinpad-VJ breakdown: render / viewport / live” (4:5, 30 fps, 27.3 s)
- **Tartalom:** ismetlodo hármas-ciklus: `Render` (szineskrom, magenta-ultraviola kopasz fej + ket kez), `Viewport` (szurke drotkeret/clay), `Live` (koncert-felvetel zold lezerekkel, tuzlangok). Sarokban kerek logo + HUD-felirat.
- **Stilus:** realisztikus krom/uveg anyag, iridescens (zold-narancs-kek) beszurodo, feher kristaly-szilankokkal; a koncerten kek/ultraviola/zold lezer es **meleg narancs/tuz** (a master tiltja a meleg tonust: **nem veszem at**).
- **Mozgas:** a hos-fej lassan forog, a kezek kozeledni/szetnyilni latszanak; a sarok-flash kepek hirtelen valtanak. 2 fps kulonbseg 41.8 (kozepes-magas), >40: 25/54.
- **Szinek:** `#0D0712` (18.5%), `#130D2A` (6.1%), `#302F32` (6.1% szurke Viewport-hatter), `#535353`/`#6F6F6F`/`#8E8E8E`/`#AFAFAF` (Viewport szurkek), `#2C1110` (3.0%, tuz-fekete), `#F5F9FB` (1.7%, feher). Zold lezer ~`#04CC2C`, narancs-tuz ~`#F04E2C`, kek ~`#3350AD` (kvantalt kozepek).
- **Kontraszt:** atlagos luma 0.302; sotet 23.9%, vilagos 3.7%.

### 3.3 IMG_7563.MP4 – „piros-feher kaiju-fej, 2 szemszeru motorral” (4:5, 25.01 fps, 31.67 s)
- **Tartalom:** a Render/Viewport/Live harmas-ciklus ismet; kozepso kaiju/szornyfej fogakkal, ket oldalon kerek, gyuruzott „motor/lencse” egysegekkel; HUD jelolo „d_o”.
- **Stilus:** brutalista-gepies, fekete-piros krom, kozepes polygon-reszletesseg; Viewport = szurke clay.
- **Mozgas:** egyenletes, lassu-kozepes forgás/bokes; a ffmpeg csak 1 vagast talalt (0.03 s), 2 fps kulonbseg atlag 24.4 (**legnyugodtabb**), >40 csak 3/62.
- **Szinek:** `#323232` (34.7%, szurke Viewport), `#060103` (24.8%, fekete), `#4D4C4D`, `#6F6E6F`, `#8E8E8E`, `#2D080B` (5.5%), `#4D0609`, `#6E040A`, piros akcent ~`#F30106` / `#AD030C`, feher `#F7F5F7` (2.2%), kek-sotet `#11112A`.
- **Kontraszt:** atlagos luma 0.217 (legsotetebb), sotet 29.6%, vilagos 3.3%.
- A piros-narancs-sarga lezer/tuz a master szerint tiltott tonus: nem alkalmazhato.

### 3.4 IMG_9135.MP4 – „zold-ultraviola mammut / elefant robotfej” (16:9-szeru, 29.56 fps, 35.35 s)
- **Stilus:** hipertelitett, sotet, zold-pink-kek szinkaosz; fenylo elefantagyar-csovek (feher-sarga neon), meccha-fem; gyors szin-invertalo villanok (zold<->magenta<->kek, negativ-szeru frame-ek).
- **Mozgas:** extrem gyors vagas: ffmpeg scene>0.35 ~100 vagas-pontot (30-60 / 0.2 s kozokkel); a vagasok az elejen **0.4–0.43 s-onkent** (0.215, 0.648, 1.048, 1.482, 1.882, 2.315, 2.748), ami az audio-BPM (0.418 s) kornyeke, tehat valoszinuleg beat-re vagott; ennek zenei kapcsolatat a video hangja nem bizonyitja (nem elemezve: `ismeretlen`).
- **Kamera:** frontalis kozelkep, kb. szimmetrikus, lassu zoom/orbit az objektum koruli ket tengelyen, kozte bumm-zoom.
- **Kontraszt:** a legszelsosegesebb; mean luma 0.251, sotet 53.0% (`#060B05`, 38.6%), vilagos 12.2% (`#F9FAF9` 8.7%), kozte zold `#102906` (15.2%), `#144C08`, `#294F12`, `#2A6F14`; pink/ultraviola `#270A2D` / `#120D28` / `#30104B`.
- **Telitett zold:** `#4EAD31`, `#13B82D`, `#71F24D` – **a master tiltja** (telitett zold) -> nem veszem at.

### 3.5 Kozos tanulsagok a Canvas-hoz (mert/megfigyelt, a master szamait nem irjak felul)
1. Mind a 4 videóban a **kozepso hos, kozeli szimmetrikus kompozicio**; a hatter **sotet (45–55% fekete/tabla-sotet)**, mint a master VOID/SMOKE aranya (~65%).
2. Tukros viz-padlo megjelenik az IMG_0836-ban: hullamzo tukorkep, a hos alatt kb. 30% magassagban – a master `GEO_Floor_Mercury` irany helyes; a fodrok finom, nagy hullamhosszuak.
3. A neon a **kontur/iv** mentén jelenik meg (cian ivek, feher-sarga agyar), nem teljes felulet – egyezik a master „neon el” koncepcioval.
4. Kamera: alacsony szog + dutch-tilt a 0836-ban; a master 7.5 (+-4 fok iv, nincs vagas, nincs zoom) **szandekosan nyugodtabb** (Canvas-loop). A referencia vagasi ritmusat (0.4–1.4 s) **nem** kell atvenni (a master tiltja a vagast).
5. Hamar villanó feher flash frame-ek (8–12% fenyes pixel) a referenciaban; a masterben a snare-re villan a key spot/betu el (7.7), ugyanez az ertelem, a hard cap-ek valtozatlanok.

### 3.6 Szinpaletta (HEX): a master 7.3 es a meres osszevetese
A master palettat **nem modositom** (a meresek nem indokolnak 0. fejezeti tures-modositast, mert a videok palettaja (ultraviola/kek/piros/zold) es a master (magenta/cian/ultraviola) nem azonos; a kozeli rokon a 0836: ultraviola-kek-cian neon).

| Szerep | HEX (master, valtozatlan) | Mert megfelelo a referenciakban |
|---|---|---|
| Alap / VOID (hatter) | #040406 | #040510, #060103, #060B05 (a refek legsotetebb meletei; ~15–39%) |
| Fust / SMOKE | #15141B | #0D1330, #0D0712, #130D2A (sotet kek-ibolya) |
| Beton / CONCRETE | #1C1C21 / #26262C | #2D2D32 ~ #323232 (Viewport szurke, nem beton) |
| Krom / CHROME | #D7DBE3 | #AFAFAF–#F5F9FB (a refek feher/szurke krom-felei) |
| Gunmetal | #3A3E48 | #302F32, #4D4C4D |
| NEON MAGENTA (emisszio) | #FF1F8F | a refekben ultraviola-pink: ~#8A4CD5–#CE062D (erosen kulonbozo hue) |
| NEON CYAN (emisszio) | #00E8FF | 0836 cian ivek: pontos HEX `ismeretlen` (nem merve) |
| ULTRAVIOLET (fill) | #6A00FF | #4E2F8F, #2E318D, #6A35AF, #8A4CD5 |
| WHITE HOT (key) | #F2F6FF | #FCF4FD, #F9FAF9, #F7F5F7 |

Eltérés: **nincs** (nem modositok HEX-et). A referencia-szinek, amelyek a masterben tiltottak (piros/narancs tuz, telitett zold) **nem kerulnek be**.

## 4. Mozgas-osszefoglalo (idozites)
| Video | FPS | Hossz | Vagas (scene>0.35) | 2 fps atlag-diff | Kamera / hos mozgas |
|---|---|---|---|---|---|
| 0836 | 25 | 28.4 s | 21 vagas, kb. 1/1.35 s | 62.8 | alacsony szogu orbit + dutch, mozgo hos |
| 6422 | 30 | 27.3 s | 40+ (a harmas-ciklus kepei kozt) | 41.8 | lassu forgas, ciklikus mod-valtas |
| 7563 | 25.01 | 31.67 s | 1 (a ciklus-valtast a kuszob nem fogta) | 24.4 | lassu forgas, nyugodt |
| 9135 | 29.56 | 35.35 s | ~100 (0.03–0.43 s kozok, sok flash) | 76.8 | gyors zoom/orbit, szin-invertalas |

A masteri Canvas-mozgas (nincs vagas, 240-frame ciklus) lassabb, ezert a referencia-vagasi ritmus nem felel meg; csak a „beat-szintu intenzitas-impulzus” (flash) atvehetõ, ahogy a 7.7 irja.

## 5. Nyitott kerdesek
1. **A drop-elejet (32.9 s) a master „elso ut-csoportja” javaslattal ellentetben nem hasznalom** – 02-es jelezzen a felhasznalonak (3. szabaly: ugy dont a felhasznalo). A javasolt ablak: 38.78–46.78 s.
2. Downbeat/utem 1. uteme: `ismeretlen` (csak beat-racs; a horgony 33.348 s alacsony biztossagu).
3. A tiszta snare nem szeparalhato a 2–5 kHz savban (szintetizator/hi-hat atfedes): lehet, hogy a sutott snare-gorbe csak 3 jelentos csucsot ad.
4. A videok sajat audiosavja (AAC) **nem** lett elemezve: `ismeretlen`, hogy a videok vagasi ritmusa a CIGARETTA MOLLYWOOD ritmusahoz tartozik-e.
5. A 0836 cian neon pontos HEX-e nem merve (a kvantalt kozep osszemosott); ha szukseges, 02-es kert Blender-teszt utan finomitja a 0. fejezeti +-10% tureseben.
6. Spotify UI-szolnyom/aspect: a 4 video kozul csak a 0836 9:16; a többi nem hasznalhato kozvetlen kompozicio-mintanak (4:5, 16:9).
7. Legnagyobb basszus-csucs frame 130 (4.30 s); ha a felhasznalo masik ablakot valaszt, `audio_final.py` ujrafuttathato (`scripts/audio_final.py`).
