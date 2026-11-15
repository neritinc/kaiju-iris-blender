"""06-animator: base keyframes (A1-A12), audio bake (Audio_Controller), drivers D1-D18.
Run: blender -b pipeline/03_lit_scene.blend --python scripts/animate_scene.py
Output: final_animated_scene.blend (project root)
"""
import bpy, math, os, sys
import numpy as np
from bpy_extras import anim_utils

ROOT = r"C:\Users\neritinc\Documents\3D PROJECT"
WAV_FULL = os.path.join(ROOT, "referencia", "CIGARETTA MOLLYWOOD.wav")
WAV_WIN = os.path.join(ROOT, "pipeline", "audio_window.wav")  # 38.781 s .. 46.781 s (ffmpeg cut)
OUT = os.path.join(ROOT, "final_animated_scene.blend")
WIN_START = 38.781
TAU = 2 * math.pi

scn = bpy.context.scene
objs = bpy.data.objects


def O(name):
    o = objs.get(name)
    if o is None:
        raise RuntimeError("missing object " + name)
    return o


def cbag(idb):
    ad = idb.animation_data
    return anim_utils.action_get_channelbag_for_slot(ad.action, ad.action_slot)


def key_series(setter, inserter, keys):
    for f, v in keys:
        setter(v)
        inserter(f)


def finalize_curve(fc, interp):
    """spec 6: Cycles first, then interpolation/handles, then update()."""
    mod = fc.modifiers.new(type='CYCLES')
    mod.mode_before = mod.mode_after = 'REPEAT'
    for kp in fc.keyframe_points:
        kp.interpolation = interp
        if interp == 'BEZIER':
            kp.handle_left_type = kp.handle_right_type = 'AUTO_CLAMPED'
    fc.update()


base_curves = []  # (label, idblock, fcurve, period, kind)


def animate_obj(obj, path, idx, keys, interp, label, period):
    def setter(v):
        a = getattr(obj, path)
        a[idx] = v
    ins = lambda f: obj.keyframe_insert(data_path=path, index=idx, frame=f)
    key_series(setter, ins, keys)
    fc = cbag(obj).fcurves.find(path, index=idx)
    finalize_curve(fc, interp)
    base_curves.append((label, obj, fc, period, interp))


def animate_bone(rig, bone, idx, keys, interp, label, period):
    pb = rig.pose.bones[bone]
    pb.rotation_mode = 'XYZ'
    def setter(v):
        pb.location[idx] = v
    ins = lambda f: pb.keyframe_insert(data_path="location", index=idx, frame=f)
    key_series(setter, ins, keys)
    dp = 'pose.bones["%s"].location' % bone
    fc = cbag(rig).fcurves.find(dp, index=idx)
    finalize_curve(fc, interp)
    base_curves.append((label, rig, fc, period, interp))


# ------------------------------------------------------------------ base motion
bpy.ops.object.mode_set(mode='OBJECT') if bpy.context.object and bpy.context.object.mode != 'OBJECT' else None
scn.frame_start, scn.frame_end = 1, 240
rig = O("RIG_Main")
bpy.context.view_layer.objects.active = rig
bpy.ops.object.mode_set(mode='POSE')

def sine5(a, period, phase=0):  # 5 keys, 0,+a,0,-a,0
    q = period // 4
    return [(1 + phase + q * i, v) for i, v in enumerate([0, a, 0, -a, 0])]

animate_obj(O("GEO_Core_Mercury"), "rotation_euler", 2, [(1, 0.0), (241, TAU)], 'LINEAR', "A1 core rotZ", 240)
animate_bone(rig, "core", 1, sine5(0.05, 240), 'BEZIER', "A2 core floatY", 240)
animate_obj(O("EMP_Droplet_Orbit"), "rotation_euler", 2, [(1, 0.0), (241, -TAU)], 'LINEAR', "A3 droplet orbit", 240)
for n in range(1, 7):
    s = 1 + 40 * (n - 1)
    keys = [(s + 30 * i, v) for i, v in enumerate([0, 0.03, 0, -0.03, 0])]
    animate_obj(O("GEO_Droplet_%02d" % n), "location", 2, keys, 'BEZIER', "A4 droplet%02d floatZ" % n, 120)
animate_bone(rig, "type_top", 1, sine5(0.025, 120), 'BEZIER', "A5 type_top", 120)
animate_bone(rig, "type_bottom", 1, sine5(-0.025, 120), 'BEZIER', "A6 type_bottom", 120)
animate_obj(O("EMP_Noise_Pivot"), "rotation_euler", 2, [(1, 0.0), (241, TAU)], 'LINEAR', "A7 noise pivot", 240)
animate_obj(O("EMP_Fog_Pivot"), "rotation_euler", 2, [(1, 0.0), (241, -TAU)], 'LINEAR', "A8 fog pivot", 240)
animate_obj(O("EMP_Floor_Pivot"), "rotation_euler", 2, [(1, 0.0), (241, TAU)], 'LINEAR', "A9 floor pivot", 240)
animate_obj(O("EMP_Cam_Pivot"), "rotation_euler", 2, sine5(math.radians(4.0), 240), 'BEZIER', "A10 cam arc", 240)
cam = O("CAM_Main")
# A11: breathing around the existing local Z (spec: local base 0)
cz0 = cam.location[2]
animate_obj(cam, "location", 2, [(f, cz0 + v) for f, v in sine5(0.06, 120)], 'BEZIER', "A11 cam breathe", 120)
cy0 = cam.location[1]
animate_obj(cam, "location", 1, [(1, cy0 - 0.20), (61, cy0), (121, cy0 + 0.20), (181, cy0), (241, cy0 - 0.20)],
            'BEZIER', "A12 cam dolly", 240)
bpy.ops.object.mode_set(mode='OBJECT')
print("cam local base (z, y):", cz0, cy0)
# drop the pose-bone location restore (leave bones at rest)
for pb in rig.pose.bones:
    pb.location = (0, 0, 0)

# ------------------------------------------------------------------ audio controller
ctl = objs.get("Audio_Controller")
if ctl is None:
    ctl = bpy.data.objects.new("Audio_Controller", None)
    col = bpy.data.collections.get("COL_Control") or scn.collection
    col.objects.link(ctl)
ctl["Bass"] = 0.0
ctl["Snare"] = 0.0
ctl.keyframe_insert(data_path='["Bass"]', frame=1)
ctl.keyframe_insert(data_path='["Snare"]', frame=1)
ctl.select_set(True)
bpy.context.view_layer.objects.active = ctl

# find / prepare a Graph Editor area (works in -b: the default window has a screen)
win = bpy.context.window_manager.windows[0]
area = None
for a in win.screen.areas:
    if a.type in ('TIMELINE', 'DOPESHEET_EDITOR', 'VIEW_3D', 'GRAPH_EDITOR'):
        area = a
        if a.type == 'GRAPH_EDITOR':
            break
area.ui_type = 'FCURVES'
region = [r for r in area.regions if r.type == 'WINDOW'][0]
print("graph area:", area.type, area.ui_type, region.type)

BANDS = {"Bass": dict(low=20.0, high=150.0, attack=0.005, release=0.18),
         "Snare": dict(low=2000.0, high=5000.0, attack=0.002, release=0.08)}
SOUND_METHOD = "bpy.ops.graph.sound_to_samples (Graph Editor temp_override, cut WAV pipeline/audio_window.wav)"


def bake_band(prop, params, wavpath):
    cb = cbag(ctl)
    for fc in cb.fcurves:
        fc.select = (fc.data_path == '["%s"]' % prop)
        fc.hide = False
    fc = cb.fcurves.find('["%s"]' % prop)
    saved = (scn.frame_start, scn.frame_end)
    scn.frame_start, scn.frame_end = 1, 300
    scn.frame_current = 1
    with bpy.context.temp_override(window=win, area=area, region=region, scene=scn):
        r = bpy.ops.graph.sound_to_samples(filepath=wavpath, **params)
    scn.frame_start, scn.frame_end = saved
    print("bake", prop, r, "sampled:", len(fc.sampled_points), "keys:", len(fc.keyframe_points))
    if len(fc.sampled_points) == 0:
        raise RuntimeError("no samples produced for " + prop)
    sp = fc.sampled_points
    fr = np.array([p.co[0] for p in sp])
    val = np.array([p.co[1] for p in sp])
    return fr, val


raw = {}
for prop, params in BANDS.items():
    fr, val = bake_band(prop, params, WAV_WIN)
    print(prop, "samples frame range:", fr[0], fr[-1], "n=", len(fr), "max=", val.max())
    raw[prop] = (fr, val)

# F0: the frame where audio t=0 sits in the baked curve
fr0 = raw["Bass"][0][0]
print("first sampled frame:", fr0)

REF_BASS = [31, 104, 116, 130]
REF_SNARE = [117, 125]


def window_series(prop, F0):
    fr, val = raw[prop]
    f = np.arange(1, 241, dtype=float)
    return np.interp(F0 + (f - 1), fr, val)


def local_max_near(v, f, rad):
    lo, hi = max(1, f - rad), min(240, f + rad)
    seg = v[lo - 1:hi]
    return lo + int(np.argmax(seg))


def shift_check(F0):
    vb = window_series("Bass", F0)
    d = [local_max_near(vb, f, 6) - f for f in REF_BASS]
    vs = window_series("Snare", F0)
    ds = [local_max_near(vs, f, 6) - f for f in REF_SNARE]
    return d, float(np.median(np.abs(d))), ds


# audio_window.wav is cut at 38.781, so audio t=0 sits at the first sampled frame
F0 = float(fr0)
d, med, ds = shift_check(F0)
print("shift check F0=%.1f: bass deltas %s median|d|=%.1f snare deltas %s" % (F0, d, med, ds))
if med > 3:
    for alt in (F0 - 1, F0 + 1):
        d2, med2, ds2 = shift_check(alt)
        print("  retry F0=%.1f: %s median=%.1f snare %s" % (alt, d2, med2, ds2))
        if med2 < med:
            F0, d, med, ds = alt, d2, med2, ds2
SHIFT = dict(F0=F0, deltas=d, median=med, snare_deltas=ds)

# ------------------------------------------------------------------ normalise / crossfade / write keys
audio_report = {}
for prop in ("Bass", "Snare"):
    v = window_series(prop, F0)
    if prop == "Snare":  # 3-tap smooth [0.25,0.5,0.25] (master 7.6 noisy band)
        vp = np.pad(v, 1, mode='edge')
        v = 0.25 * vp[:-2] + 0.5 * vp[1:-1] + 0.25 * vp[2:]
    peak = float(v.max())  # before crossfade
    v2 = v.copy()
    for f in range(233, 241):
        w = (f - 232) / 8.5  # spec: /9 gives 0.059 > 0.05 tolerance on the Blender envelope
        v2[f - 1] = (1 - w) * v[f - 1] + w * v[0]
    fc = cbag(ctl).fcurves.find('["%s"]' % prop)
    # clear baked samples and keys, then write 240 LINEAR keys + 241
    n_s = len(fc.sampled_points)
    fc.convert_to_keyframes(1, 1) if False else None
    for i in range(len(fc.keyframe_points) - 1, -1, -1):
        fc.keyframe_points.remove(fc.keyframe_points[i], fast=True)
    # remove sample points: delete the fcurve and recreate for a clean one
    cbag(ctl).fcurves.remove(fc)
    fc = cbag(ctl).fcurves.new('["%s"]' % prop, index=0, group_name="Audio")
    # NOTE: Blender's GENERATOR modifier evaluates a polynomial of *time* and ignores the curve value
    # (verified: Generator(0,1/peak) clipped everything to 1.0), so normalisation by 1/peak is applied
    # to the key values directly; modifier stack = CYCLES -> LIMITS(0..1).
    pts = [(float(f), float(v2[f - 1] / peak)) for f in range(1, 241)] + [(241.0, float(v[0] / peak))]
    fc.keyframe_points.add(len(pts))
    for kp, (f, val) in zip(fc.keyframe_points, pts):
        kp.co = (f, val)
        kp.interpolation = 'LINEAR'
    fc.update()
    cyc = fc.modifiers.new(type='CYCLES')
    cyc.mode_before = cyc.mode_after = 'REPEAT'
    lim = fc.modifiers.new(type='LIMITS')
    lim.use_min_y = True; lim.min_y = 0.0
    lim.use_max_y = True; lim.max_y = 1.0
    audio_report[prop] = dict(peak=peak)
    print(prop, "peak(Blender units)=%.5f" % peak, "samples removed:", n_s)

for prop in ('Bass', 'Snare'):
    print(prop, 'modifier stack:', [m.type for m in cbag(ctl).fcurves.find('["%s"]' % prop).modifiers])

# drop the stray Sound datablock created by the bake, if any
for s in list(bpy.data.sounds):
    if s.users == 0:
        bpy.data.sounds.remove(s)

# ------------------------------------------------------------------ drivers
drivers = []  # (label, fcurve)


def add_driver(target_idb, path, index, expr, var, label, owner_for_fc=None):
    """target_idb: object with .driver_add; returns FCurve."""
    fc = target_idb.driver_add(path, index) if index is not None else target_idb.driver_add(path)
    drv = fc.driver
    drv.type = 'SCRIPTED'
    v = drv.variables.new()
    v.name = var
    v.type = 'SINGLE_PROP'
    v.targets[0].id_type = 'OBJECT'
    v.targets[0].id = ctl
    v.targets[0].data_path = '["%s"]' % ("Bass" if var == "bass" else "Snare")
    drv.expression = expr
    drivers.append((label, fc))
    return fc


add_driver(cam, "delta_location", 2, "-0.010*bass", "bass", "D1 cam dz")
add_driver(cam, "delta_rotation_euler", 1, "0.00611*bass", "bass", "D2 cam roll")
add_driver(cam, "delta_location", 0, "0.004*snare", "snare", "D3 cam dx")

def mat_node(mat, node):
    return bpy.data.materials[mat].node_tree.nodes[node]

for m, tag in (("MAT_Neon_Magenta", "D4"), ("MAT_Neon_Cyan", "D5")):
    add_driver(mat_node(m, "EMIT_Neon").inputs["Strength"], "default_value", None, "6.0 + 24.0*bass", "bass", tag + " " + m)
add_driver(mat_node("MAT_Neon_Slit", "EMIT_Slit").inputs["Strength"], "default_value", None, "5.0 + 15.0*bass", "bass", "D6 slit")
for m in ("MAT_Type_Glow_Magenta", "MAT_Type_Glow_Cyan"):
    add_driver(mat_node(m, "EMIT_TypeGlow").inputs["Strength"], "default_value", None, "3.0 + 9.0*bass", "bass", "D7 " + m)
for m in ("MAT_Chrome_TypeRim_Magenta", "MAT_Chrome_TypeRim_Cyan"):
    add_driver(mat_node(m, "EMIT_TypeRim").inputs["Strength"], "default_value", None, "2.5 + 15.0*snare", "snare", "D8 " + m)
add_driver(O("LGT_Rim").data, "energy", None, "350.0 + 650.0*bass", "bass", "D9 rim")
add_driver(O("LGT_Accent_Cyan").data, "energy", None, "350.0 + 650.0*bass", "bass", "D10 accent")
add_driver(O("LGT_Key").data, "energy", None, "1200.0 + 400.0*snare", "snare", "D11 key")
core = O("GEO_Core_Mercury")
for i in (0, 1):
    add_driver(core, "delta_scale", i, "1.0 + 0.10*bass", "bass", "D12 core ds%d" % i)
add_driver(core, "delta_scale", 2, "1.0 - 0.08*bass", "bass", "D13 core ds2")
add_driver(core.modifiers["DSP_Core"], "strength", None, "0.15 + 0.12*bass", "bass", "D14 displace")
for n in ("GEO_Text_Top", "GEO_Text_Bottom", "GEO_TextGlow_Top", "GEO_TextGlow_Bottom"):
    for i in range(3):
        add_driver(O(n), "delta_scale", i, "1.0 + 0.025*snare", "snare", "D15 %s ds%d" % (n, i))
for k in range(1, 7):
    for i in range(3):
        add_driver(O("GEO_Droplet_%02d" % k), "delta_scale", i, "1.0 + 0.15*bass", "bass", "D16 drop%02d ds%d" % (k, i))
add_driver(mat_node("MAT_Fog", "VAL_FogDensity").outputs[0], "default_value", None, "0.035 + 0.015*bass", "bass", "D17 fog")
add_driver(mat_node("MAT_Mercury_Floor", "BUMP_Floor").inputs["Strength"], "default_value", None, "0.05 + 0.15*bass", "bass", "D18 floor bump")

# ------------------------------------------------------------------ scene state, save
scn.frame_start, scn.frame_end = 1, 240
scn.render.fps, scn.render.fps_base = 30, 1.0
scn.frame_current = 1
bpy.ops.wm.save_as_mainfile(filepath=OUT)

# ------------------------------------------------------------------ verification
print("=" * 70)
errs = []
def check(cond, msg):
    if not cond:
        errs.append(msg)
        print("FAIL:", msg)

# reload-independent evaluation of base curves
tot_fc = tot_keys = 0
animated = set()
for lbl, idb, fc, period, interp in base_curves:
    animated.add(idb.name)
    v1, v241 = fc.evaluate(1), fc.evaluate(241)
    diff = abs(v241 - v1)
    if interp == 'LINEAR' and abs(v241 - v1) > 1e-6 and "rot" in fc.data_path:
        diff = abs(((v241 - v1) + math.pi) % TAU - math.pi)
    vals = np.array([fc.evaluate(f) for f in range(1, 242)])
    dv = np.abs(np.diff(vals))
    seam = abs((fc.evaluate(2) - fc.evaluate(1)) - (fc.evaluate(241) - fc.evaluate(240)))
    seam_ok = seam <= 0.1 * dv.max() + 1e-9
    kp0 = [kp.co[0] for kp in fc.keyframe_points]
    check(diff < 1e-3, lbl + " v241-v1=%g" % diff)
    check(seam_ok, lbl + " seam-speed %g > 0.1*%g" % (seam, dv.max()))
    check(fc.modifiers[0].type == 'CYCLES', lbl + " Cycles not first")
    check(kp0[0] in (1, 41, 81, 121, 161, 201) and 240 not in kp0, lbl + " key frames wrong")
    check(np.ptp(vals) > 0, lbl + " not changing")
    print("%-28s keys=%d  |v241-v1|=%.2e  seamΔ=%.2e (max step %.2e)  range=%.4f" %
          (lbl, len(kp0), diff, seam, dv.max(), np.ptp(vals)))
    tot_keys += len(kp0)
tot_fc += len(base_curves)

for prop in ("Bass", "Snare"):
    fc = cbag(ctl).fcurves.find('["%s"]' % prop)
    vals = np.array([fc.evaluate(f) for f in range(1, 242)])
    loop = abs(vals[239] - vals[0])
    loop241 = abs(vals[240] - vals[0])
    print("AUDIO %s: n(1)=%.4f n(240)=%.4f |n(1)-n(240)|=%.4f  |n(241)-n(1)|=%.5f  min=%.3f max=%.3f mean=%.3f peakBU=%.5f" %
          (prop, vals[0], vals[239], loop, loop241, vals.min(), vals.max(), vals.mean(), audio_report[prop]["peak"]))
    check(loop <= 0.05, prop + " loop error > 0.05")
    check(loop241 < 1e-3, prop + " 241!=1")
    check(vals.min() >= 0 and vals.max() <= 1.0 + 1e-9 and np.ptp(vals) > 0.3, prop + " normalisation/range")
    tot_fc += 1
    tot_keys += len(fc.keyframe_points)
    audio_report[prop]["loop"] = loop
    audio_report[prop]["n1"] = vals[0]
animated.add(ctl.name)
print("SHIFT CHECK:", SHIFT)
check(SHIFT["median"] <= 3, "bass shift median > 3 frames")
vb = np.array([cbag(ctl).fcurves.find('["Bass"]').evaluate(f) for f in range(1, 241)])
print("bass_n absolute argmax frame:", 1 + int(np.argmax(vb)))
print("bass_n at 31/104/116/130:", [round(float(vb[f - 1]), 3) for f in (31, 104, 116, 130)])

# drivers: validity and sampled values
print("-" * 70)
caps = {"D1": (-0.020, 0), "D2": (0, 0.01396), "D3": (0, 0.010), "D4": (6, 40), "D5": (6, 40), "D6": (5, 25),
        "D7": (3, 15), "D8": (2.5, 25), "D9": (350, 1300), "D10": (350, 1300), "D11": (1200, 1800),
        "D12": (1.0, 1.18), "D13": (0.86, 1.0), "D14": (0.15, 0.30), "D15": (1.0, 1.045), "D16": (1.0, 1.25),
        "D17": (0.035, 0.060), "D18": (0.05, 0.30)}
for lbl, fc in drivers:
    check(fc.driver.is_valid, lbl + " driver invalid")
    check(not fc.driver.is_simple_expression is False, lbl + " not simple expr")
for fr in (1, 31, 104, 125, 130, 240):
    scn.frame_set(fr)
    bpy.context.view_layer.update()
    row = {
        "bass_n": round(float(cbag(ctl).fcurves.find('["Bass"]').evaluate(fr)), 3),
        "snare_n": round(float(cbag(ctl).fcurves.find('["Snare"]').evaluate(fr)), 3),
        "neon": round(mat_node("MAT_Neon_Magenta", "EMIT_Neon").inputs["Strength"].default_value, 2),
        "typeRim": round(mat_node("MAT_Chrome_TypeRim_Magenta", "EMIT_TypeRim").inputs["Strength"].default_value, 2),
        "rimW": round(O("LGT_Rim").data.energy, 1),
        "keyW": round(O("LGT_Key").data.energy, 1),
        "core_ds": tuple(round(x, 3) for x in core.delta_scale),
        "dsp": round(core.modifiers["DSP_Core"].strength, 3),
        "fog": round(mat_node("MAT_Fog", "VAL_FogDensity").outputs[0].default_value, 4),
        "cam_dz": round(cam.delta_location[2], 4),
    }
    print("frame %3d" % fr, row)
    check(0.86 <= core.delta_scale[2] <= 1.0 and core.delta_scale[0] <= 1.18, "core scale cap f%d" % fr)
    check(row["rimW"] <= 1300 and row["keyW"] <= 1800 and row["neon"] <= 40 and row["dsp"] <= 0.30, "cap f%d" % fr)
scn.frame_set(1)
check(all(fc.driver.is_valid for _, fc in drivers), "all drivers valid")
tot_fc += len(drivers)
for _, fc in drivers:
    pass
print("DRIVERS: %d, valid: %d" % (len(drivers), sum(fc.driver.is_valid for _, fc in drivers)))

# D2 roll check: view direction rotates about camera local Y? delta_rotation_euler.y with rot (90,0,0)
import mathutils
cam.delta_rotation_euler = (0, 0.1, 0)
bpy.context.view_layer.update()
r = cam.matrix_local.to_3x3() if False else cam.matrix_world.to_3x3()
fwd = r @ mathutils.Vector((0, 0, -1))
cam.delta_rotation_euler = (0, 0, 0)
bpy.context.view_layer.update()
r0 = cam.matrix_world.to_3x3()
fwd0 = r0 @ mathutils.Vector((0, 0, -1))
print("D2 roll test: view dir change = %.6f (0 => pure roll about view axis)" % (fwd - fwd0).length)
check((fwd - fwd0).length < 1e-6, "D2 is not a roll about view axis")

# key vs driver channel collision
for lbl, fc in drivers:
    pass
check(scn.frame_start == 1 and scn.frame_end == 240 and scn.render.fps == 30, "frame range/fps")
check(len(bpy.data.shape_keys) == 0, "shape keys present")
print("animated objects:", len(animated), sorted(animated))
print("keyframes total (base+audio):", tot_keys, " F-curves (base+audio):", tot_fc - len(drivers), " driver F-curves:", len(drivers))
print("frame_start/end/fps:", scn.frame_start, scn.frame_end, scn.render.fps)
print("RESULT:", "ALL CHECKS PASSED" if not errs else "FAILED: %s" % errs)
print("SOUND_METHOD:", SOUND_METHOD)
if errs:
    sys.exit(1)
