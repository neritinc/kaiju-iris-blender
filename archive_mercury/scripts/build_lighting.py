# 05-lighting-artist: lights, world, camera, render settings. Run in Blender 5.2 background.
# usage: blender -b pipeline/02_textured.blend --python scripts/build_lighting.py -- test_v01.png [key=val ...]
import bpy, math, sys, os, time
from mathutils import Vector, Color

ROOT = r"C:\Users\neritinc\Documents\3D PROJECT"
argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
TEST_NAME = argv[0] if argv else "test_v01.png"
P = dict(a.split("=") for a in argv[1:])


def pf(k, d):
    return float(P.get(k, d))


scene = bpy.context.scene


def lin(hexs):
    h = hexs.lstrip('#')
    c = Color([int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)])
    return c.from_srgb_to_scene_linear()


def must(name):
    o = bpy.data.objects.get(name)
    if o is None:
        raise RuntimeError("missing object " + name)
    return o


# ---------- clean previous lights (idempotent re-run) ----------
for n in ("LGT_Key", "LGT_Rim", "LGT_Accent_Cyan", "LGT_Fill"):
    o = bpy.data.objects.get(n)
    if o:
        bpy.data.objects.remove(o, do_unlink=True)
    l = bpy.data.lights.get(n)
    if l:
        bpy.data.lights.remove(l)

col = bpy.data.collections.get("COL_Lights") or bpy.data.collections.new("COL_Lights")
if col.name not in scene.collection.children:
    scene.collection.children.link(col)


def make_light(name, ltype, loc, target, hexs, power):
    ld = bpy.data.lights.new(name, ltype)
    ld.energy = power
    ld.color = lin(hexs)
    ob = bpy.data.objects.new(name, ld)
    col.objects.link(ob)
    ob.location = loc
    ob.rotation_euler = (Vector(target) - Vector(loc)).to_track_quat('-Z', 'Y').to_euler()
    return ob, ld


SRC = {"n":"Normal","g":"Generated","o":"Object","c":"Camera","w":"Window","r":"Reflection"}[P.get("src","n")]
TGT = (0, 0, 3.20)
key, kl = make_light("LGT_Key", 'SPOT', (0, -1.5, 9.0), TGT, "#F2F6FF", pf("key", 1200))
kl.spot_size = math.radians(28)
kl.spot_blend = 0.35
kl.shadow_soft_size = 0.05
rim, rl = make_light("LGT_Rim", 'AREA', (-2.0, 2.2, 3.4), TGT, "#FF1F8F", pf("rim", 350))
rl.shape = 'RECTANGLE'
rl.size = 1.5
rl.size_y = 0.15
acc, al = make_light("LGT_Accent_Cyan", 'AREA', (2.0, 2.2, 3.4), TGT, "#00E8FF", pf("rim", 350))
al.shape = 'RECTANGLE'
al.size = 1.5
al.size_y = 0.15
fill, fl = make_light("LGT_Fill", 'AREA', (0, -6.0, 4.0), TGT, "#6A00FF", pf("fill", 60))
fl.shape = 'SQUARE'
fl.size = 4.0

# ---------- Key gobo + IES simulation in light node tree (K8) ----------
try:
    try:
        kl.use_nodes = True
    except Exception:
        pass
    nt = kl.node_tree
    if nt is None:
        raise RuntimeError("light.node_tree is None in this Blender")
    nt.nodes.clear()
    N = nt.nodes
    L = nt.links

    def nn(t, name, loc):
        n = N.new(t)
        n.name = name
        n.label = name
        n.location = loc
        return n

    out = nn("ShaderNodeOutputLight", "LGT_Out", (1200, 0))
    em = nn("ShaderNodeEmission", "EMIT_Key", (950, 0))
    em.inputs["Color"].default_value = (1, 1, 1, 1)
    # node-level gain: Cycles spot (1200 W) is too weak to draw a visible cone in the capped fog
    em.inputs["Strength"].default_value = pf("kgain", 150.0)
    tc = nn("ShaderNodeTexCoord", "TC_Gobo", (-900, 0))
    mp = nn("ShaderNodeMapping", "MAP_Gobo", (-700, 100))
    mp.inputs["Scale"].default_value = (pf("gscale", 30), 1, 1)
    # NOTE: the Wave Texture node evaluates to black inside a Cycles light node tree in Blender 5.2
    # (verified by test renders), so the procedural band pattern is built from Math nodes (sine bands).
    sx = nn("ShaderNodeSeparateXYZ", "SEP_Map", (-600, 300))
    mw = nn("ShaderNodeMath", "MUL_Wave", (-550, 300)); mw.operation = 'MULTIPLY'
    mw.inputs[1].default_value = pf("wscale", 8)
    wav = nn("ShaderNodeMath", "WAV_Gobo", (-450, 100)); wav.operation = 'SINE'
    wh = nn("ShaderNodeMath", "WAV_Norm", (-350, 100)); wh.operation = 'MULTIPLY_ADD'
    wh.inputs[1].default_value = 0.5; wh.inputs[2].default_value = 0.5
    cr = nn("ShaderNodeValToRGB", "CR_Gobo", (-200, 100))
    cr.color_ramp.elements[0].position = 0.45
    cr.color_ramp.elements[0].color = (0.15, 0.15, 0.15, 1)
    cr.color_ramp.elements[1].position = 0.55
    cr.color_ramp.elements[1].color = (1, 1, 1, 1)
    sep = nn("ShaderNodeSeparateXYZ", "SEP_Gobo", (-700, -200))
    ab = nn("ShaderNodeMath", "ABS_Z", (-500, -200))
    ab.operation = 'ABSOLUTE'
    mr = nn("ShaderNodeMapRange", "MR_IES", (-300, -200))
    mr.inputs["From Min"].default_value = math.cos(math.radians(14.0))
    mr.inputs["From Max"].default_value = 1.0
    cri = nn("ShaderNodeValToRGB", "CR_IES", (-50, -200))
    cri.color_ramp.elements[0].position = 0.0
    cri.color_ramp.elements[0].color = (0.6, 0.6, 0.6, 1)
    cri.color_ramp.elements[1].position = 1.0
    cri.color_ramp.elements[1].color = (1, 1, 1, 1)
    mul = nn("ShaderNodeVectorMath", "MUL_Gobo_IES", (700, 0))
    mul.operation = 'MULTIPLY'
    L.new(tc.outputs[SRC], mp.inputs["Vector"])
    L.new(mp.outputs["Vector"], sx.inputs["Vector"])
    L.new(sx.outputs["X"], mw.inputs[0])
    L.new(mw.outputs["Value"], wav.inputs[0])
    L.new(wav.outputs["Value"], wh.inputs[0])
    L.new(wh.outputs["Value"], cr.inputs["Fac"])
    L.new(tc.outputs[SRC], sep.inputs["Vector"])
    L.new(sep.outputs["Z"], ab.inputs[0])
    L.new(ab.outputs["Value"], mr.inputs["Value"])
    L.new(mr.outputs["Result"], cri.inputs["Fac"])
    L.new(cr.outputs["Color"], mul.inputs[0])
    L.new(cri.outputs["Color"], mul.inputs[1])
    # use Color multiply into emission color (strength stays 1; light power = energy)
    mode = P.get("mode", "both")
    if mode == "both":
        L.new(mul.outputs["Vector"], em.inputs["Color"])
    elif mode == "ies":
        L.new(cri.outputs["Color"], em.inputs["Color"])
    L.new(em.outputs["Emission"], out.inputs["Surface"])
    print("GOBO/IES-sim light node tree built")
except Exception as e:
    print("GOBO_FAILED (K8):", repr(e))

# ---------- World ----------
w = scene.world or bpy.data.worlds.new("World")
scene.world = w
w.use_nodes = True
bg = w.node_tree.nodes.get("Background")
if bg is None:
    w.node_tree.nodes.clear()
    bg = w.node_tree.nodes.new("ShaderNodeBackground")
    o = w.node_tree.nodes.new("ShaderNodeOutputWorld")
    w.node_tree.links.new(bg.outputs[0], o.inputs[0])
c = lin("#040406")
bg.inputs["Color"].default_value = (c[0], c[1], c[2], 1)
bg.inputs["Strength"].default_value = 1.0

# ---------- Camera ----------
cam = must("CAM_Main")
cd = cam.data
cd.lens = 35.0
cd.sensor_width = 36.0
cd.sensor_height = 36.0
cd.sensor_fit = 'VERTICAL'
cd.clip_start = 0.1
cd.clip_end = 40.0
cd.dof.use_dof = True
cd.dof.focus_object = must("EMP_Cam_Target")
cd.dof.aperture_fstop = 4.0
for cn in list(cam.constraints):
    cam.constraints.remove(cn)
scene.camera = cam

# ---------- Render ----------
r = scene.render
r.engine = 'CYCLES'
r.resolution_x = 1080
r.resolution_y = 1920
r.resolution_percentage = 100
r.fps = 30
r.fps_base = 1.0
scene.frame_start = 1
scene.frame_end = 240
r.use_motion_blur = True
r.motion_blur_shutter = 0.5
r.image_settings.file_format = 'PNG'
r.image_settings.color_depth = '16'
r.filepath = "//pipeline/renders/frames/MW_####.png"
scene.view_settings.view_transform = 'AgX'
looks = [i.identifier for i in scene.view_settings.bl_rna.properties['look'].enum_items]
print("AgX looks:", looks)
for cand in ("AgX - Punchy", "Punchy", "AgX - Base Contrast", "Base Contrast"):
    try:
        scene.view_settings.look = cand
        break
    except TypeError:
        continue
print("Look used:", scene.view_settings.look)
scene.view_settings.exposure = pf("exposure", 0.0)

cy = scene.cycles
cy.samples = 48
cy.use_denoising = True
try:
    cy.denoiser = 'OPENIMAGEDENOISE'
except Exception as e:
    print("denoiser:", e)
for prop, val in (("volume_step_rate", 2.0), ("volume_max_steps", 512)):
    if hasattr(cy, prop):
        setattr(cy, prop, val)
    else:
        print("MISSING cycles prop (K8):", prop)

# ---------- GPU ----------
backend_used = "CPU"
prefs = bpy.context.preferences.addons['cycles'].preferences
order = ['METAL'] if sys.platform == 'darwin' else ['OPTIX', 'CUDA', 'HIP', 'ONEAPI']
for be in order:
    try:
        prefs.compute_device_type = be
        prefs.get_devices()
        devs = [d for d in prefs.devices if d.type == be]
        if devs:
            for d in prefs.devices:
                d.use = (d.type == be)
            backend_used = be
            break
    except Exception as e:
        print("backend", be, "failed:", e)
if backend_used == "CPU":
    prefs.compute_device_type = 'NONE'
    cy.device = 'CPU'
    print("WARNING: no GPU, falling back to CPU")
else:
    cy.device = 'GPU'
print("GPU backend:", backend_used, [(d.name, d.type, d.use) for d in prefs.devices])

# ---------- Save ----------
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(ROOT, "pipeline", "03_lit_scene.blend"))

# ---------- Test render (50%, 48 spl) ----------
if "norender" not in P:
    os.makedirs(os.path.join(ROOT, "pipeline", "renders"), exist_ok=True)
    scene.frame_set(int(pf("frame", 1)))
    r.resolution_percentage = 50
    r.use_motion_blur = False
    cy.samples = int(pf("samples", 48))
    r.image_settings.color_depth = '8'
    r.filepath = os.path.join(ROOT, "pipeline", "renders", TEST_NAME)
    t = time.time()
    bpy.ops.render.render(write_still=True)
    print("TEST RENDER SECONDS: %.1f" % (time.time() - t))
