# 01 Analysis (referencia/ aktualis tartalom alapjan, 2026-11-12, frissitett vizualis elemzes)

## 1. Leltar
| Fajl | Tipus | Meret | Adat | Allapot |
|---|---|---|---|---|
| referencia/IMG_6422.MP4 | video | 10.4 MB | 1024x1280 (4:5), 30 fps, 27.30 s; felso fel Render/Viewport, also fel Live | pipeline/frames/IMG_6422/ (2 fps, 0001-0055); egyenkent atneztem 1 fps-es csempe-lapokon (27 kocka, 4 lap) |
| referencia/IMG_0836.MP4 | video | 10.9 MB | 720x1280 (9:16), 25 fps, 28.40 s | frames/IMG_0836/ (2 fps, 57 db); ~minden 3. kocka egyenkent megnezve (t=0..28 s) |
| referencia/IMG_7563.MP4 | video | 12.1 MB | 1024x1280 (4:5), 25 fps, 31.67 s; felso Render/Live, also Viewport | frames/IMG_7563/ (2 fps, 63 db); ~minden 3. kocka egyenkent megnezve |
| referencia/IMG_9135.MP4 | video | 13.0 MB | 1280x704 (vizszintes), 29.56 fps, 35.35 s | frames/IMG_9135/ (2 fps, 71 db); ~minden 4. kocka egyenkent megnezve |
| referencia/CIGARETTA MOLLYWOOD.wav | hang | 35.6 MB | 44.1 kHz, 24 bit, sztereo, 134.40 s | librosa-val merve (korabbi futas, adatok megtartva) |

Megjegyzes: nincs kep-fajl, csak 4 videó + 1 WAV. Idobelyeg = (kockaszam-1)/2 s. A videók saját hangsavja nem elemezve (ismeretlen). A frames/ mappakban a regi f_XX.png (0.5 fps) es sheet.png fajlok is vannak.

## 2. Osszefoglalo
A referenciak egy kiborg-/mech-karakter VJ- es koncertvizual-kollekcio: nagy, 3D-renderelt, fém/krom/uveg-panelos, emisszios neon-elu "boss" objektumok (kiborg-koponya + ket kez, lila szarvas ragadozo, Godzilla-kiborg ket lencse-turbina szemmel, zold-lila mech-mamut) szimmetrikus, kozeptengelyes kompozicioban, fekete teren, ritmusra valto szinvilaggal. Ket videoban (6422, 7563) ugyanaz a jelenet harom rétegben latszik: Render (a 3D vilag), Viewport (szurke clay/drotvaz nezet), Live (valodi koncert-aréna: ívelt LED-fal, truss-keret, fust, zold/voros lezerek, tuzgejzirek, tomeg-sziluett). A hang egy ~143.55 BPM elektronikus szam (nagy energia kb. 24-104 s kozott). Kozos cel: grandiozus, fustos, lezer-eros koncertaréna-látvány, szimmetrikus kozponti 3D-objektummal.

## 3. Vizualis DNS
- **Fo formak es sziluett:** kozeptengelyes szimmetria, karakterek fuggoleges/kompakt sziluettje (szarvak, szarv-parok, tüske-sor, lencse-turbinak oldalt); a hatter a keret szeleit vezeti kozep fele (kupola-bordak, truss-keret, LED-fal).
- **Karakter-reszletgazdagsag:** hard-surface panelek (hidraulikus dugattyuk, csavarok, lencse-gyuruk koncentrikus fogaskerek-peremmel, LED-pontsor a lencse korul, vezetek-kotegek, fogsor); krom/gyongyhaz felulet (6422 koponya), pikkelyes lila borszeru felulet (0836), koszos anodizalt fem + borpikkely (7563), fekete-zold fem es agyar-emisszio, ormany-bordak (9135).
- **Stilus:** hibrid: fotorealisztikus anyagok (krom, uveg, fem) stilizalt neon-emissziv szinekkel; szurreális, nem realisztikus.
- **Anyagok:** tukrozo viz-padlo (0836), tukrozo szinpadpadlo (9135), krom-visor (6422), kristaly-/uveg-lencse (7563), emissziv LED-panelek, volumetrikus fust (6422 Live, 7563 Live).
- **Kompozicio:** kozep-fokusz, frontalis vagy low-angle kamera, 3 melysegreteg (tomeg-sziluett elol, szinpad kozepen, LED-fal hatul), bal-jobb tukrozott legyezok; extrem kontraszt (fekete <-> telitett szin <-> feher flash).
- **Fenyirany:** hatulrol/oldalrol (rim-light, magenta/kek), a LED-fal mint nagy hatso fenyforras, lezerek a szinpad kozepebol felfele.
- **Lezer / fenycsova (Live-retegek reszletesen):**
  - IMG_6422 Live: zold lezerek (#04D12C - #35FF3A), 1-3 px vekony; (a) szimmetrikus legyezo a szinpadrol, 8-15 nyalab, ~+-10/25/40 fok, (b) 4-6 parhuzamos fuggoleges nyalab egy negyzetes truss-keretben, (c) vizszintes zold sorok a keret folott, (d) koncentrikus negyzet-alagut. Narancs tuzgejzirek a szelen, narancs-voros fust.
  - IMG_7563 Live: voros (#F30106) lezer-hallo 30-50 vekony nyalab V-ben szimmetrikusan + 6-10 szeles puha fustben terjedo kup + 4-6 sarga (#E8C81C) keresztezett nyalab; fent narancs vizszintes LED-sorok.
  - IMG_9135: feher-kek vastag (60-120 px) nyalabok sunburst-ben (Render), feher-zold nyalab a fejbe.
  - IMG_7563 Render: rozsaszin/feher fuggoleges nyalabok a lencsekbol, rozsaszin villam-gyuru.
- **Fust:** kozepesen suru, a lezerek es nyalabok jol lathatok, a LED-fal halo-t hoz letre; szinterek (fust) a fenyt viszi: zold, voros, narancs, lila.
- **Szinpad / LED-fal / padlo:** ivelt, nagy LED-fal (a tartalma a Render-jelenet), kozepen DJ-pult, truss (racs) keret, szinpad-szelen tuzgejzir, tomeg-sziluett elol; 0836: tukrozo vizpadlo, 9135: fekete-zold aramkor-padlo.
- **Tipografia:** logok/feliratok (RENDER/VIEWPORT/LIVE, kis logo, monogram) - nem atveendo.
- **Kozos DNS:** szimmetrikus kozponti karakter, fekete ter, emisszios neon-elek, krom/fem, tukrozo padlo, ritmusra valto monokrom/neon, szurke clay-nezet mint stilusvaltas, lezer-legyezo.
- **Elterok:** 0836 lila/cian + geometrikus fal-minta + viz-padlo; 6422 pop-neon + kezek + zold lezer + tuz + kanyon-taj; 7563 voros/feher agressziv + lezer-hallo + lencse-szemek; 9135 zold + inverz flash + aramkor.

## 4. Szinpaletta (HEX, pixelmintavetel: PIL, a kinyert 2 fps-es kockak ~14 kvantalt szinklasztere, a gyakoriak es a telitettek szerint)
| Szerep | HEX | Forras / megjegyzes |
|---|---|---|
| Alap hatter / fekete ter | #060B05 / #040510 / #060103 / #0D0712 | 9135 / 0836 / 7563 / 6422 (a kep 15-39%-a) |
| Mely ejkek / sotet kupola | #0D1330, #15194A | 0836 |
| Lila karakter / neon lila | #8A4CD6, #7946CF | 0836 (telitett pixelek) |
| Cian vezetoel / ivek | #37CDEE, #34AED4 | 0836 |
| Feher emisszio (flash, agyar) | #FBF4FD, #F9FAF9 | 0836, 9135 |
| Lezer-zold | #04D12C (Live), #70F34A, #56F02E | 6422, 9135 |
| Sotetzold hatter | #112906 | 9135 |
| Voros lezer | #F30106, #D30209 | 7563 |
| Sotet voros fust | #2D080B, #4D0609 | 7563 |
| Magenta / rozsaszin akcent | #E040FB (szemmel, 6422 kezek) | 6422, 0836 (becsult) |
| Narancs tuz / mennyezet-LED | #EF4E2C, #D5462A | 6422, 7563 |
| Sarga lezer | #E8C81C (becsult) | 7563 |
| Viewport szurke | #323232, #535353, #6F6F6F | 7563, 6422 |
| Kek LED / jeg | #52B0EB, #4F8EF1 | 6422 |

## 5. Mozgas
- **IMG_6422:** Render/Viewport/Live atvaltas 1-3 s-onkent (3 s Render, 3 s Viewport, ... Live folyamatosan alul); kozel -> tavol, koponya forog, kezek szettarulnak; Live: fix kamera, vilagitas-valtas beatenkent. Kanyon-tajban (t=15-27 s) a koponya lebeg, vizpermet, villam. A Viewport a Render-nel szinkronban kiegyenesiti.
- **IMG_0836:** extrem kameraszog-valtas (low, top-down, fisheye, roll 180, push-in); hatterminta kb. 1.5-3 s-onkent valt (gyuruk -> keresztek -> negyzetek -> sakktabla -> feher villanas -> nagy szemek -> videofal -> sotet); 18 s-nal fehér villanas = csucspont; a leny meg-megall, ugrik, lábait terpesztve.
- **IMG_7563:** Render 0-7 s, Live 7.5-10.5 s, Render 12-17, Live 18-26, Render 27-31; kamera lassu push-in, roll, kozelikkel; fej-ugyes (szajnyitas), lencse-kisules (energia-nyalab) a 28-31 s-ban.
- **IMG_9135:** nyers vagas + 4-6 frame-es zoom-blur/glitch, 1-2 s-os blokkok, szinvaltas zold -> lila -> inverz zold -> kek/feher -> lila -> inverz zold; kamera lassu push-in frontalis, fejjel lefele, vegen logo-sting.
- **Ciklikussag:** beatre (143.55 BPM): kb. 4-8 beat-os blokkok; ismetlodo Render -> Viewport -> Live (6422/7563); szinvaltas es flash 8 beatenkent.

## 6. Ritmikai DNS (CIGARETTA MOLLYWOOD.wav) - valtozatlanul az elozo meresbol
- Hossz 134.40 s; BPM ~143.55 (librosa), beat-periodus 0.418 s (= 12.54 frame @30 fps). Tehat 8 s ~ 19.1 beat: nem egesz szam, a loop vege nem esik pontosan beatre (ismert kompromisszum; 20 beat = 8.36 s lenne).
- Energia (8 s-os atlagok): intro 0-8 s halk; basszus nagy 32-56 s es 80-100 s; kozepso break ~64-72 s (basszus alacsony); 104 s utan outro, 112 s-tol csend.
- Legerosebb pontok (1 s simitas): basszus ~33.9, 42.2, 58.7, 88.2, 100.9 s; kozep 29.5, 46.0, 59.6, 72.6, 85.6 s; magas 31.7, 46.0, 54.1, 78.6, 98.6 s.
- **Javasolt loop-ablak: kezdet 60.48 s (60.48-68.48 s)**, a nagy energiaju tartomanyban (30-95 s) a legjobb kezdet/veg-spektrum es basszusritmus-egyezes (r=0.59). Az ablak vege 16-odos basszus-felfutas (build-up), ezert a loop vege hangosabb; teljesen zokkenomentes hanghurok nem garantalt (crossfade ajanlott). Hasznalat: ffmpeg -ss 60.48 -t 8.
- Beatek az ablakon belul (s / frame, frame = s*30+1): 0.403/13, 0.821/26, 1.227/38, 1.633/50, 2.051/63, 2.469/75, 2.887/88, 3.294/100, 3.700/112, 4.130/125, 4.536/137, 4.954/150, 5.360/162, 5.778/174, 6.196/187, 6.602/199, 7.020/212, 7.438/224, 7.856/237.
- Basszus-csucsok (onset, frame): 136, 149, 161, 174, 180, 186, 192, 198, 204 (legerosebb), 211, 217, 223, 229, 235. A 0-4 s kozott a basszus level-csucs: 13, 50, 63 (jel. kick); kb. 3-4 s kozt basszus onset nincs.
- Snare/magas-sav onsetek (frame, erosebbek): 20, 49, 70, 76, 118 (legerosebb), 150, 156, 169, 210, 226 (gyengebbek: 14, 25, 43, 62, 82, 87, 101, 126, 144, 180, 201, 221, 238).
- Onset-detekcio frekvenciasavokon (basszus 30-120 Hz, snare 1.5-6 kHz), nem tiszta kick/snare szeparacio; becsles.

## 7. Forras-hozzarendeles
- Zold lezer-legyezo, negyzetes keret-fuggoleges sugarak, nested negyzet-alagut, tuzgejzirek, narancs fust, Render/Viewport/Live szerkezet, kez+koponya, kanyon-taj, viz-permet: IMG_6422
- Kupola (cian ivek nyilhegyekkel), tukrozo viz-padlo, mintavaltas (gyuruk/kereszt/negyzet/sakktabla), fekete <-> feher kontraszt, lila szarvas leny: IMG_0836
- Voros/sarga lezer-hallo es kup-fenycsova, lencse-szemek koncentrikus gyuruvel, cinemascope sav, energia-nyalab, Viewport-clay: IMG_7563
- Zold-lila-inverz szinvaltas, zoom-blur glitch, sunburst-nyalabok, mamut-agyar emisszio, aramkor-padlo, LED-fal fekete haromszogekkel, truss + parabola: IMG_9135
- BPM, beat, loop-ablak: CIGARETTA MOLLYWOOD.wav

## 8. Nyitott kerdesek
1. A videok sajat hangsavja nincs elemezve; a WAV a vegleges zene?
2. Kimenet 9:16 1080x1920; a 9135 vizszintes, 6422/7563 4:5 es kettes retegu - atkadrazas es a "Live" reteg (also fel) kulon kezelese kell.
3. 8 s != egesz beatszam (19.1 beat); marad a 143.55 BPM crossfade-del, vagy igazitsuk 150 BPM-re (20 beat)?
4. Logok/feliratok nem masolhatok; sajat tipografia nincs - a latvanyban nem lesz szoveg.
5. A kockak 2 fps-es mintak, a pontos vagasi idok +-0.5 s pontossaguak; a Live-retegek kozonseg-arcai nem szerepelhetnek.
6. A HEX palettat PIL-lel kvantalt klaszterekbol (nem pixelpontos retusalt kepbol) vettem; a magenta/sarga ertek szemmel becsult.
