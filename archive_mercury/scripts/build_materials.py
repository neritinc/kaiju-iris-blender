"""04-lookdev-artist: procedural PBR materials for Mercury Totem.
Run: blender -b pipeline/01_model.blend --python scripts/build_materials.py
Saves pipeline/02_textured.blend. No external images/textures.
"""
import bpy, os, sys
from mathutils import Color

ROOT = r"C:\Users\neritinc\Documents\3D PROJECT"
OUT = os.path.join(ROOT, "pipeline", "02_textured.blend")

# ---------------------------------------------------------------- palette
def hexcol(h):
    h = h.lstrip('#')
    r, g, b = (int(h[i:i + 2], 16) / 255.0 for i in (0, 2, 4))
    c = Color((r, g, b)).from_srgb_to_scene_linear()
    return (c.r, c.g, c.b, 1.0)

VOID, SMOKE = "#040406", "#15141B"
CONC, CONC2 = "#1C1C21", "#26262C"
CHROME, GUNMETAL = "#D7DBE3", "#3A3E48"
MAGENTA, CYAN, UV, WHITEHOT = "#FF1F8F", "#00E8FF", "#6A00FF", "#F2F6FF"

# ---------------------------------------------------------------- helpers
class B:
    def __init__(self, mat):
        self.mat = mat
        mat.use_nodes = True
        self.nt = mat.node_tree
        self.nt.nodes.clear()
        self.x = 0

    def node(self, idname, name, loc=(0, 0), **props):
        n = self.nt.nodes.new(idname)
        n.name = name
        n.label = name
        n.location = loc
        for k, v in props.items():
            setattr(n, k, v)
        return n

    def link(self, a, b):
        self.nt.links.new(a, b)

    def tc(self, name, obj=None, loc=(-1400, 0)):
        n = self.node('ShaderNodeTexCoord', name, loc)
        if obj is not None:
            n.object = bpy.data.objects[obj]
        return n

    def noise(self, name, tcn, scale, detail, rough=0.5, loc=(0, 0), out="Fac"):
        n = self.node('ShaderNodeTexNoise', name, loc, noise_dimensions='3D')
        n.inputs["Scale"].default_value = scale
        n.inputs["Detail"].default_value = detail
        n.inputs["Roughness"].default_value = rough
        self.link(tcn.outputs["Object"], n.inputs["Vector"])
        return n

    def ramp(self, name, src, stops, loc=(0, 0)):
        """stops: [(pos, rgba)]"""
        n = self.node('ShaderNodeValToRGB', name, loc)
        cr = n.color_ramp
        while len(cr.elements) > len(stops):
            cr.elements.remove(cr.elements[-1])
        while len(cr.elements) < len(stops):
            cr.elements.new(0.5)
        for e, (p, c) in zip(cr.elements, stops):
            e.position = p
            e.color = c
        if src is not None:
            self.link(src, n.inputs["Fac"])
        return n

    def maprange(self, name, src, fmin, fmax, tmin, tmax, loc=(0, 0)):
        n = self.node('ShaderNodeMapRange', name, loc)
        n.clamp = True
        n.inputs["From Min"].default_value = fmin
        n.inputs["From Max"].default_value = fmax
        n.inputs["To Min"].default_value = tmin
        n.inputs["To Max"].default_value = tmax
        if src is not None:
            self.link(src, n.inputs["Value"])
        return n

    def mixc(self, name, blend, fac, loc=(0, 0)):
        n = self.node('ShaderNodeMix', name, loc, data_type='RGBA', blend_type=blend)
        n.inputs[0].default_value = fac
        return n

    @staticmethod
    def A(n): return n.inputs[6]
    @staticmethod
    def Bs(n): return n.inputs[7]
    @staticmethod
    def R(n): return n.outputs[2]

    def out(self, loc=(1600, 0)):
        return self.node('ShaderNodeOutputMaterial', "Material Output", loc)

    def principled(self, loc=(1200, 0)):
        return self.node('ShaderNodeBsdfPrincipled', "Principled BSDF", loc)

    def emission(self, name, hexc, strength, loc=(1200, -500)):
        n = self.node('ShaderNodeEmission', name, loc)
        n.inputs["Color"].default_value = hexcol(hexc)
        n.inputs["Strength"].default_value = strength   # never linked: driver target
        return n


def grey(v):
    return (v, v, v, 1.0)

BLACK, WHITE = grey(0.0), grey(1.0)

# ---------------------------------------------------------------- chrome core
def chrome_tree(b, tcname="TC_Chrome"):
    tc = b.tc(tcname, None, (-1500, 0))
    # roughness
    nr = b.noise("NOI_Rough", tc, 4.0, 2.0, 0.5, (-1100, 600))
    cr = b.ramp("CR_Rough", nr.outputs["Fac"], [(0.35, BLACK), (0.65, WHITE)], (-800, 600))
    ns = b.noise("NOI_Smudge", tc, 2.0, 1.0, 0.5, (-1100, 300))
    cs = b.ramp("CR_Smudge", ns.outputs["Fac"], [(0.45, BLACK), (0.60, WHITE)], (-800, 300))
    mr_ = b.mixc("MIX_Rough", 'LIGHTEN', 1.0, (-500, 450))
    b.link(cr.outputs["Color"], b.A(mr_))
    b.link(cs.outputs["Color"], b.Bs(mr_))
    mr = b.maprange("MR_Rough", None, 0.0, 1.0, 0.02, 0.08, (-250, 450))
    b.link(b.R(mr_), mr.inputs["Value"])
    # tint
    nt = b.noise("NOI_Tint", tc, 1.5, 2.0, 0.5, (-1100, 0))
    ct = b.ramp("CR_Tint", nt.outputs["Fac"], [(0.0, BLACK), (1.0, grey(0.15))], (-800, 0))
    mb = b.mixc("MIX_Base", 'MIX', 0.0, (-500, 0))
    mb.inputs[6].default_value = hexcol(CHROME)
    mb.inputs[7].default_value = hexcol(GUNMETAL)
    b.link(ct.outputs["Color"], mb.inputs[0])
    # bump
    nb = b.noise("NOI_Bump", tc, 9.0, 3.0, 0.5, (-1100, -350))
    bm = b.node('ShaderNodeBump', "BUMP_Chrome", (-500, -350))
    bm.inputs["Strength"].default_value = 0.02
    bm.inputs["Distance"].default_value = 0.005
    b.link(nb.outputs["Fac"], bm.inputs["Height"])
    # principled
    p = b.principled((-100, 0))
    p.inputs["Metallic"].default_value = 1.0
    p.inputs["Anisotropic"].default_value = 0.15
    p.inputs["Coat Weight"].default_value = 0.0
    b.link(b.R(mb), p.inputs["Base Color"])
    b.link(mr.outputs["Result"], p.inputs["Roughness"])
    b.link(bm.outputs["Normal"], p.inputs["Normal"])
    return p


def mat_chrome_liquid():
    m = bpy.data.materials.new("MAT_Chrome_Liquid")
    b = B(m)
    p = chrome_tree(b)
    o = b.out(); b.link(p.outputs["BSDF"], o.inputs["Surface"])
    return m


def mat_type_rim(name, rimhex):
    m = bpy.data.materials.new(name)
    b = B(m)
    p = chrome_tree(b)
    lw = b.node('ShaderNodeLayerWeight', "LW_Rim", (-1100, -700))
    lw.inputs["Blend"].default_value = 0.22
    cr = b.ramp("CR_Rim", lw.outputs["Facing"], [(0.55, BLACK), (0.90, WHITE)], (-800, -700))
    mx = b.mixc("MIX_RimColor", 'MULTIPLY', 1.0, (-500, -700))
    mx.inputs[6].default_value = hexcol(rimhex)
    b.link(cr.outputs["Color"], b.Bs(mx))
    em = b.emission("EMIT_TypeRim", rimhex, 2.5, (-100, -700))
    b.link(b.R(mx), em.inputs["Color"])
    add = b.node('ShaderNodeAddShader', "ADD_Rim", (300, 0))
    b.link(p.outputs["BSDF"], add.inputs[0])
    b.link(em.outputs["Emission"], add.inputs[1])
    o = b.out((600, 0)); b.link(add.outputs["Shader"], o.inputs["Surface"])
    return m


def mat_emit(name, nodename, hexc, strength, glow=False):
    """Pure emission; strength socket left unlinked for drivers."""
    m = bpy.data.materials.new(name)
    b = B(m)
    em = b.emission(nodename, hexc, strength, (0, 0))
    o = b.out((300, 0)); b.link(em.outputs["Emission"], o.inputs["Surface"])
    return m


def mat_floor():
    m = bpy.data.materials.new("MAT_Mercury_Floor")
    b = B(m)
    tc = b.tc("TC_Floor", "EMP_Floor_Orbit")
    nr = b.noise("NOI_FloorRipple", tc, 0.9, 1.0, 0.4, (-1000, 500))
    wv = b.node('ShaderNodeTexWave', "WAV_Floor", (-1000, 200), wave_type='RINGS')
    wv.inputs["Scale"].default_value = 0.45
    wv.inputs["Distortion"].default_value = 2.0
    wv.inputs["Detail"].default_value = 1.0
    b.link(tc.outputs["Object"], wv.inputs["Vector"])
    mh = b.node('ShaderNodeMix', "MIX_FloorH", (-650, 350), data_type='FLOAT')
    mh.inputs[0].default_value = 0.5
    b.link(nr.outputs["Fac"], mh.inputs[2])
    b.link(wv.outputs["Fac"], mh.inputs[3])
    bm = b.node('ShaderNodeBump', "BUMP_Floor", (-350, 350))
    bm.inputs["Strength"].default_value = 0.05       # driver target (unlinked)
    bm.inputs["Distance"].default_value = 0.02
    b.link(mh.outputs[0], bm.inputs["Height"])
    nt = b.noise("NOI_FloorTint", tc, 0.3, 2.0, 0.5, (-1000, -150))
    ct = b.ramp("CR_FloorTint", nt.outputs["Fac"], [(0.0, BLACK), (1.0, grey(0.35))], (-700, -150))
    mb = b.mixc("MIX_FloorBase", 'MIX', 0.0, (-400, -150))
    mb.inputs[6].default_value = hexcol(VOID)
    mb.inputs[7].default_value = hexcol(GUNMETAL)
    b.link(ct.outputs["Color"], mb.inputs[0])
    nrr = b.noise("NOI_FloorRough", tc, 3.0, 2.0, 0.5, (-1000, -500))
    mr = b.maprange("MR_FloorRough", nrr.outputs["Fac"], 0.0, 1.0, 0.02, 0.05, (-700, -500))
    p = b.principled((0, 0))
    p.inputs["Metallic"].default_value = 1.0
    b.link(b.R(mb), p.inputs["Base Color"])
    b.link(mr.outputs["Result"], p.inputs["Roughness"])
    b.link(bm.outputs["Normal"], p.inputs["Normal"])
    o = b.out((400, 0)); b.link(p.outputs["BSDF"], o.inputs["Surface"])
    return m


def mat_concrete():
    m = bpy.data.materials.new("MAT_Concrete_Dark")
    b = B(m)
    tc = b.tc("TC_Concrete")
    nc = b.noise("NOI_Concrete", tc, 4.0, 8.0, 0.6, (-1100, 500))
    vo = b.node('ShaderNodeTexVoronoi', "VOR_Pores", (-1100, 150), feature='F1')
    vo.inputs["Scale"].default_value = 60.0
    b.link(tc.outputs["Object"], vo.inputs["Vector"])
    mk = b.mixc("MIX_ConcreteMask", 'OVERLAY', 0.5, (-750, 350))
    b.link(nc.outputs["Fac"], b.A(mk))
    b.link(vo.outputs["Distance"], b.Bs(mk))
    cc = b.ramp("CR_ConcreteCol", None, [(0.0, hexcol(CONC)), (1.0, hexcol(CONC2))], (-450, 500))
    b.link(b.R(mk), cc.inputs["Fac"])
    mrr = b.maprange("MR_ConcreteRough", None, 0.0, 1.0, 0.75, 0.95, (-450, 150))
    b.link(b.R(mk), mrr.inputs["Value"])
    bp = b.node('ShaderNodeBump', "BUMP_Concrete", (-450, -150), invert=True)
    bp.inputs["Strength"].default_value = 0.15
    bp.inputs["Distance"].default_value = 0.01
    b.link(vo.outputs["Distance"], bp.inputs["Height"])
    # edge wear
    bv = b.node('ShaderNodeBevel', "BVN_Wear", (-1100, -400))
    bv.inputs["Radius"].default_value = 0.02
    bv.samples = 8
    gm = b.node('ShaderNodeNewGeometry', "GEO_Normal", (-1100, -650))
    dt = b.node('ShaderNodeVectorMath', "VM_Dot", (-800, -500), operation='DOT_PRODUCT')
    b.link(bv.outputs["Normal"], dt.inputs[0])
    b.link(gm.outputs["Normal"], dt.inputs[1])
    mw = b.maprange("MR_Wear", dt.outputs["Value"], 1.0, 0.92, 0.0, 1.0, (-550, -500))
    cw = b.ramp("CR_Wear", mw.outputs["Result"], [(0.0, BLACK), (1.0, WHITE)], (-300, -500))
    mx = b.mixc("MIX_Wear", 'MIX', 0.0, (-50, 300))
    # Spec says B=#26262C, which is practically indistinguishable from the base;
    # use GUNMETAL (palette) for a visible lighter-grey edge wear. Reported as deviation.
    mx.inputs[7].default_value = hexcol(GUNMETAL)
    b.link(cc.outputs["Color"], b.A(mx))
    b.link(cw.outputs["Color"], mx.inputs[0])
    p = b.principled((300, 0))
    p.inputs["Metallic"].default_value = 0.0
    b.link(b.R(mx), p.inputs["Base Color"])
    b.link(mrr.outputs["Result"], p.inputs["Roughness"])
    b.link(bp.outputs["Normal"], p.inputs["Normal"])
    o = b.out((700, 0)); b.link(p.outputs["BSDF"], o.inputs["Surface"])
    return m


def mat_fog():
    m = bpy.data.materials.new("MAT_Fog")
    b = B(m)
    tc = b.tc("TC_Fog", "EMP_Fog_Orbit")
    nf = b.noise("NOI_Fog", tc, 0.45, 3.0, 0.55, (-900, 200))
    cr = b.ramp("CR_FogMask", nf.outputs["Fac"], [(0.35, grey(0.5)), (0.70, grey(1.0))], (-600, 200))
    vd = b.node('ShaderNodeValue', "VAL_FogDensity", (-600, -100))
    vd.outputs[0].default_value = 0.035             # driver target
    mu = b.node('ShaderNodeMath', "VOL_Density", (-300, 100), operation='MULTIPLY')
    b.link(vd.outputs[0], mu.inputs[0])
    b.link(cr.outputs["Color"], mu.inputs[1])
    mc = b.mixc("MIX_FogColor", 'MIX', 0.08, (-300, -250))
    mc.inputs[6].default_value = hexcol(SMOKE)
    mc.inputs[7].default_value = hexcol(UV)
    pv = b.node('ShaderNodeVolumePrincipled', "VOL_Fog", (100, 0))
    pv.inputs["Anisotropy"].default_value = 0.62
    pv.inputs["Absorption Color"].default_value = hexcol(VOID)
    pv.inputs["Emission Strength"].default_value = 0.0
    b.link(mu.outputs["Value"], pv.inputs["Density"])
    b.link(b.R(mc), pv.inputs["Color"])
    o = b.out((450, 0)); b.link(pv.outputs["Volume"], o.inputs["Volume"])
    return m


# ---------------------------------------------------------------- build
for m in list(bpy.data.materials):
    bpy.data.materials.remove(m)

mats = {}
mats["MAT_Chrome_Liquid"] = mat_chrome_liquid()
mats["MAT_Chrome_TypeRim_Magenta"] = mat_type_rim("MAT_Chrome_TypeRim_Magenta", MAGENTA)
mats["MAT_Chrome_TypeRim_Cyan"] = mat_type_rim("MAT_Chrome_TypeRim_Cyan", CYAN)
mats["MAT_Type_Glow_Magenta"] = mat_emit("MAT_Type_Glow_Magenta", "EMIT_TypeGlow", MAGENTA, 3.0)
mats["MAT_Type_Glow_Cyan"] = mat_emit("MAT_Type_Glow_Cyan", "EMIT_TypeGlow", CYAN, 3.0)
mats["MAT_Mercury_Floor"] = mat_floor()
mats["MAT_Concrete_Dark"] = mat_concrete()
mats["MAT_Neon_Magenta"] = mat_emit("MAT_Neon_Magenta", "EMIT_Neon", MAGENTA, 6.0)
mats["MAT_Neon_Cyan"] = mat_emit("MAT_Neon_Cyan", "EMIT_Neon", CYAN, 6.0)
mats["MAT_Neon_Slit"] = mat_emit("MAT_Neon_Slit", "EMIT_Slit", WHITEHOT, 5.0)      # K3 provisional
mats["MAT_ReflCard"] = mat_emit("MAT_ReflCard", "EMIT_ReflCard", WHITEHOT, 8.0)    # K3 provisional
mats["MAT_Fog"] = mat_fog()

ASSIGN = {
    "MAT_Chrome_Liquid": ["GEO_Core_Mercury"] + ["GEO_Droplet_%02d" % i for i in range(1, 7)],
    "MAT_Chrome_TypeRim_Magenta": ["GEO_Text_Top"],
    "MAT_Chrome_TypeRim_Cyan": ["GEO_Text_Bottom"],
    "MAT_Type_Glow_Magenta": ["GEO_TextGlow_Top"],
    "MAT_Type_Glow_Cyan": ["GEO_TextGlow_Bottom"],
    "MAT_Mercury_Floor": ["GEO_Floor_Mercury"],
    "MAT_Concrete_Dark": ["GEO_Slab_L", "GEO_Slab_R", "GEO_Wall_Back"],
    "MAT_Neon_Magenta": ["GEO_NeonStrip_L"],
    "MAT_Neon_Cyan": ["GEO_NeonStrip_R"],
    "MAT_Neon_Slit": ["GEO_NeonSlit_Back"],
    "MAT_ReflCard": ["GEO_ReflCard_Top_%02d" % i for i in range(1, 4)] +
                    ["GEO_ReflCard_Back_%02d" % i for i in range(1, 4)],
    "MAT_Fog": ["GEO_Fog_Volume"],
}
for mn, objs in ASSIGN.items():
    for on in objs:
        ob = bpy.data.objects[on]          # KeyError if missing -> hard fail
        ob.data.materials.clear()
        ob.data.materials.append(mats[mn])
        ob.active_material_index = 0

for on in ASSIGN["MAT_ReflCard"]:
    ob = bpy.data.objects[on]
    ob.visible_camera = False
    # glossy/diffuse/transmission/shadow stay True; volume scatter default

# ---------------------------------------------------------------- verify
errs = []
def chk(c, msg):
    if not c: errs.append(msg)

for mn, m in mats.items():
    chk(m.name == mn, "name " + mn)
    for n in m.node_tree.nodes:
        chk(n.name == n.label or n.type == 'OUTPUT_MATERIAL' or n.name.startswith("Principled"),
            "label %s/%s" % (mn, n.name))
driven = {
    "MAT_Neon_Magenta": "EMIT_Neon", "MAT_Neon_Cyan": "EMIT_Neon", "MAT_Neon_Slit": "EMIT_Slit",
    "MAT_Type_Glow_Magenta": "EMIT_TypeGlow", "MAT_Type_Glow_Cyan": "EMIT_TypeGlow",
    "MAT_Chrome_TypeRim_Magenta": "EMIT_TypeRim", "MAT_Chrome_TypeRim_Cyan": "EMIT_TypeRim",
    "MAT_ReflCard": "EMIT_ReflCard",
}
for mn, nn in driven.items():
    s = mats[mn].node_tree.nodes[nn].inputs["Strength"]
    chk(not s.is_linked, "linked strength " + mn)
    print("DRIVER_TARGET %s %s Strength=%.3f" % (mn, nn, s.default_value))
chk(not mats["MAT_Mercury_Floor"].node_tree.nodes["BUMP_Floor"].inputs["Strength"].is_linked, "BUMP_Floor linked")
vd = mats["MAT_Fog"].node_tree.nodes["VAL_FogDensity"]
print("DRIVER_TARGET MAT_Fog VAL_FogDensity=%.3f" % vd.outputs[0].default_value)
for o in bpy.data.objects:
    if o.type in {'MESH', 'CURVE', 'FONT'}:
        chk(len(o.material_slots) == 1 and o.material_slots[0].material is not None, "slot " + o.name)
chk(len([i for i in bpy.data.images if i.name not in ("Render Result", "Viewer Node")]) == 0, "images present")
chk(not any("." in m.name[-4:] and m.name[-3:].isdigit() for m in bpy.data.materials), "dup mat names")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("SAVED", OUT)
for mn, objs in ASSIGN.items():
    print("ASSIGN %-28s -> %s" % (mn, ", ".join(objs)))
if errs:
    print("ERRORS:", errs)
    sys.exit(1)
print("OK")
