"""03-modeler: Mercury Totem modell + minimal rig. Blender 5.2, spec: pipeline/02_design_spec.md
Futtatas: blender.exe -b --factory-startup --python scripts/build_model.py
"""
import bpy, bmesh, math, re, os, sys
from mathutils import Vector, Matrix

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "pipeline", "01_model.blend")
D = math.radians
scene = bpy.context.scene

# ---------------------------------------------------------------- cleanup
for o in list(bpy.data.objects):
    bpy.data.objects.remove(o, do_unlink=True)
for c in list(bpy.data.collections):
    bpy.data.collections.remove(c)
for coll in (bpy.data.meshes, bpy.data.materials, bpy.data.cameras, bpy.data.lights):
    for d in list(coll):
        coll.remove(d)

# ---------------------------------------------------------------- collections
COLS = {}
for n in ["COL_Control", "COL_Hero", "COL_Type", "COL_Environment", "COL_ReflCards",
          "COL_Atmosphere", "COL_Lights", "COL_Camera"]:
    c = bpy.data.collections.new(n)
    scene.collection.children.link(c)
    COLS[n] = c


def link(obj, col):
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    COLS[col].objects.link(obj)
    return obj


# ---------------------------------------------------------------- helpers
def mesh_obj(name, bm_builder, loc, scale=(1, 1, 1), col="COL_Environment"):
    me = bpy.data.meshes.new(name)
    bm = bmesh.new()
    bm_builder(bm)
    bm.to_mesh(me)
    bm.free()
    ob = bpy.data.objects.new(name, me)
    ob.location = loc
    ob.scale = scale
    link(ob, col)
    return ob


def b_cube(bm):
    bmesh.ops.create_cube(bm, size=1.0)


def b_plane_up(bm):  # unit plane, normal +Z
    bmesh.ops.create_grid(bm, x_segments=1, y_segments=1, size=0.5)


def b_sphere(u, v, r):
    def f(bm):
        bmesh.ops.create_uvsphere(bm, u_segments=u, v_segments=v, radius=r)
    return f


def empty(name, loc, col, rot=(0, 0, 0), display='PLAIN_AXES', size=0.3, parent=None):
    e = bpy.data.objects.new(name, None)
    e.empty_display_type = display
    e.empty_display_size = size
    e.location = loc
    e.rotation_euler = rot
    link(e, col)
    if parent is not None:
        e.parent = parent
    return e


objs = {}
# --- Environment
objs["floor"] = mesh_obj("GEO_Floor_Mercury", b_plane_up, (0, 3.0, 0.0), (16, 16, 1))
slabs = {}
for nm, x in (("GEO_Slab_L", -2.55), ("GEO_Slab_R", 2.55)):
    slabs[nm] = mesh_obj(nm, b_cube, (x, 1.5, 4.5), (0.9, 0.9, 9.0))
for nm, x in (("GEO_NeonStrip_L", -2.09), ("GEO_NeonStrip_R", 2.09)):
    mesh_obj(nm, b_cube, (x, 1.04, 4.5), (0.03, 0.03, 8.0))
mesh_obj("GEO_Wall_Back", b_cube, (0, 7.0, 6.0), (12, 0.5, 12))
mesh_obj("GEO_NeonSlit_Back", b_cube, (0, 6.74, 3.20), (6.0, 0.05, 0.06))

# --- Reflection cards (flat planes; set normals via flip)
card_top = []
for i, y in enumerate((-1.0, -0.4, 0.2), 1):
    o = mesh_obj("GEO_ReflCard_Top_%02d" % i, b_plane_up, (0, y, 8.5), (6.0, 0.08, 1), "COL_ReflCards")
    card_top.append(o)
card_back = []
for i, z in enumerate((2.4, 2.9, 3.4), 1):
    o = mesh_obj("GEO_ReflCard_Back_%02d" % i, b_plane_up, (0, -11.0, z), (4.0, 0.10, 1), "COL_ReflCards")
    card_back.append(o)
# Top cards: normal -Z -> flip. Back cards: plane in XY -> rotate vertices to XZ (done in mesh data) with +Y normal.
for o in card_top:
    bm = bmesh.new(); bm.from_mesh(o.data)
    bmesh.ops.reverse_faces(bm, faces=bm.faces[:])
    bm.to_mesh(o.data); bm.free()
for o in card_back:
    # mesh is (+-0.5, +-0.5, 0) normal +Z. Rotate -90 about X: y->-z?? we want normal +Y:
    # rotation about X by -90deg maps +Z -> +Y, scale dims then: X=4.0, Y(unit)->Z=0.10 handled below
    bm = bmesh.new(); bm.from_mesh(o.data)
    bmesh.ops.rotate(bm, verts=bm.verts[:], cent=(0, 0, 0), matrix=Matrix.Rotation(D(-90), 3, 'X'))
    bm.to_mesh(o.data); bm.free()
    o.scale = (4.0, 1, 0.10)   # after rotation the unit height lies on Z

objs["fog"] = mesh_obj("GEO_Fog_Volume", b_cube, (0, -2.0, 5.5), (12, 22, 11), "COL_Atmosphere")

# --- Hero
objs["core"] = mesh_obj("GEO_Core_Mercury", b_sphere(64, 32, 0.75), (0, 0, 3.20), col="COL_Hero")
DROPS = [(1, 0.06, 1.15, 0), (2, 0.08, 1.20, 60), (3, 0.10, 1.25, 120),
         (4, 0.12, 1.30, 180), (5, 0.09, 1.20, 240), (6, 0.14, 1.35, 300)]
drops = []
for n, r, orb, ang in DROPS:
    p = (orb * math.cos(D(ang)), orb * math.sin(D(ang)), 0.0)
    drops.append(mesh_obj("GEO_Droplet_%02d" % n, b_sphere(32, 16, r), p, col="COL_Hero"))

# --- apply scale/rotation on all meshes BEFORE modifiers
bpy.ops.object.select_all(action='DESELECT')
for o in bpy.data.objects:
    if o.type == 'MESH':
        o.select_set(True)
bpy.context.view_layer.objects.active = objs["core"]
bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
bpy.ops.object.select_all(action='DESELECT')

# --- shading
for o in [objs["core"]] + drops:
    o.data.shade_smooth()

# ---------------------------------------------------------------- Empties
ctl = "COL_Control"
e_noise_p = empty("EMP_Noise_Pivot", (0, 0, 3.20), ctl)
e_noise_o = empty("EMP_Noise_Orbit", (0.60, 0, 0), ctl, parent=e_noise_p)
e_fog_p = empty("EMP_Fog_Pivot", (0, 0, 5.50), ctl)
e_fog_o = empty("EMP_Fog_Orbit", (1.50, 0, 0), ctl, parent=e_fog_p)
e_floor_p = empty("EMP_Floor_Pivot", (0, 3.0, 0.0), ctl)
e_floor_o = empty("EMP_Floor_Orbit", (0.80, 0, 0), ctl, parent=e_floor_p)
e_tilt = empty("EMP_Droplet_Tilt", (0, 0, 3.20), ctl, rot=(D(18), 0, 0))
e_orbit = empty("EMP_Droplet_Orbit", (0, 0, 0), ctl, parent=e_tilt)
for d in drops:
    d.parent = e_orbit          # orbit-local coords, identity parent inverse
e_cam_p = empty("EMP_Cam_Pivot", (0, 0, 2.90), "COL_Camera")
e_cam_t = empty("EMP_Cam_Target", (0, 0, 2.90), "COL_Camera", display='SPHERE', size=0.1)

# ---------------------------------------------------------------- Camera
cam_data = bpy.data.cameras.new("CAM_Main")
cam_data.lens = 35.0
cam_data.sensor_width = 36.0
cam_data.sensor_height = 36.0
cam_data.sensor_fit = 'VERTICAL'
cam_data.clip_start = 0.1
cam_data.clip_end = 40.0
cam = bpy.data.objects.new("CAM_Main", cam_data)
cam.location = (0, -8.0, 0)
cam.rotation_euler = (D(90), 0, 0)
link(cam, "COL_Camera")
cam.parent = e_cam_p

# ---------------------------------------------------------------- Text (builtin Bfont)
def new_text(name, body, loc, col):
    bpy.ops.object.text_add(location=loc, rotation=(D(90), 0, 0))
    ob = bpy.context.active_object
    ob.name = name
    ob.data.name = name
    ob.data.body = body
    link(ob, col)
    bpy.ops.object.select_all(action='DESELECT')
    return ob


def cfg_main(ob, size):
    c = ob.data
    c.size = size
    c.extrude = 0.14
    c.bevel_depth = 0.015
    c.bevel_resolution = 4
    c.offset = 0.008
    c.space_character = 0.90
    c.align_x = 'CENTER'
    c.align_y = 'CENTER'


def bounds(ob):
    dg = bpy.context.evaluated_depsgraph_get()
    ev = ob.evaluated_get(dg)
    me = ev.to_mesh()
    xs = [v.co.x for v in me.vertices]; ys = [v.co.y for v in me.vertices]; zs = [v.co.z for v in me.vertices]
    r = (min(xs), max(xs), min(ys), max(ys), min(zs), max(zs))
    ev.to_mesh_clear()
    return r


t_top = new_text("GEO_Text_Top", "MOLLY", (0, 0.60, 5.00), "COL_Type")
t_bot = new_text("GEO_Text_Bottom", "WOOD", (0, 0.60, 1.50), "COL_Type")
size = 0.65 / 0.7
for ob in (t_top, t_bot):
    cfg_main(ob, size)
for _ in range(6):
    bpy.context.view_layer.update()
    x0, x1, y0, y1, _, _ = bounds(t_top)
    h = y1 - y0
    size *= 0.65 / h
    for ob in (t_top, t_bot):
        ob.data.size = size
bpy.context.view_layer.update()
TEXT_REPORT = {}
for ob in (t_top, t_bot):
    x0, x1, y0, y1, z0, z1 = bounds(ob)
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    if abs(cy) > 0.005:
        ob.data.offset_y -= cy
    if abs(cx) > 0.02:
        ob.data.offset_x -= cx
    bpy.context.view_layer.update()
    x0, x1, y0, y1, z0, z1 = bounds(ob)
    TEXT_REPORT[ob.name] = dict(size=size, width=x1 - x0, height=y1 - y0, depth=z1 - z0,
                                cx=(x0 + x1) / 2, cy=(y0 + y1) / 2)

glow = []
for src, nm, y in ((t_top, "GEO_TextGlow_Top", 0.78), (t_bot, "GEO_TextGlow_Bottom", 0.78)):
    g = src.copy()
    g.data = src.data.copy()
    g.name = nm
    g.data.name = nm
    link(g, "COL_Type")
    g.location = (0, y, src.location.z)
    g.data.offset = 0.025
    g.data.extrude = 0.02
    g.data.bevel_depth = 0.0
    glow.append(g)
g_top, g_bot = glow

# ---------------------------------------------------------------- Modifiers (after apply)
for o in slabs.values():
    m = o.modifiers.new("BVL_Slab", 'BEVEL')
    m.width = 0.02
    m.segments = 3
    m.limit_method = 'ANGLE'
    m.angle_limit = D(30)
    m.harden_normals = True

core = objs["core"]
m = core.modifiers.new("SUB_Main", 'SUBSURF')
m.levels = 2
m.render_levels = 3
tex = bpy.data.textures.new("TEX_Core_Clouds", type='CLOUDS')
tex.noise_scale = 0.65
tex.noise_depth = 1
tex.noise_basis = 'ORIGINAL_PERLIN'
m = core.modifiers.new("DSP_Core", 'DISPLACE')
m.texture = tex
m.texture_coords = 'OBJECT'
m.texture_coords_object = e_noise_o
m.direction = 'NORMAL'
m.mid_level = 0.5
m.strength = 0.15
for d in drops:
    m = d.modifiers.new("SUB_Main", 'SUBSURF')
    m.levels = 1
    m.render_levels = 2

# ---------------------------------------------------------------- Rig
arm = bpy.data.armatures.new("RIG_Main")
rig = bpy.data.objects.new("RIG_Main", arm)
link(rig, "COL_Control")
bpy.context.view_layer.objects.active = rig
rig.select_set(True)
bpy.ops.object.mode_set(mode='EDIT')
eb = arm.edit_bones
BONES = [("root", (0, 0, 0), (0, 0, 0.5), None),
         ("core", (0, 0, 3.20), (0, 0, 3.50), "root"),
         ("type_top", (0, 0.60, 5.00), (0, 0.60, 5.30), "root"),
         ("type_bottom", (0, 0.60, 1.50), (0, 0.60, 1.80), "root")]
for n, h, t, p in BONES:
    b = eb.new(n)
    b.head, b.tail = h, t
    b.roll = 0.0
    b.use_deform = False
    if p:
        b.parent = eb[p]
        b.use_connect = False
bpy.ops.object.mode_set(mode='OBJECT')
rig.select_set(False)
bpy.context.view_layer.update()


def bone_parent(ob, bone):
    ob.parent = rig
    ob.parent_type = 'BONE'
    ob.parent_bone = bone
    b = rig.data.bones[bone]
    ob.matrix_parent_inverse = (rig.matrix_world @ b.matrix_local @ Matrix.Translation((0, b.length, 0))).inverted()


for ob, bn in ((core, "core"), (e_tilt, "core"), (e_noise_p, "core"),
               (t_top, "type_top"), (g_top, "type_top"),
               (t_bot, "type_bottom"), (g_bot, "type_bottom")):
    bone_parent(ob, bn)

# ---------------------------------------------------------------- Scene
r = scene.render
r.resolution_x, r.resolution_y, r.resolution_percentage = 1080, 1920, 100
r.fps, r.fps_base = 30, 1.0
scene.frame_start, scene.frame_end, scene.frame_current = 1, 240, 1
scene.unit_settings.system = 'METRIC'
scene.unit_settings.scale_length = 1.0

bpy.data.orphans_purge(do_local_ids=True, do_linked_ids=True, do_recursive=True)
bpy.context.view_layer.update()

# ---------------------------------------------------------------- VALIDATION
errors, info = [], []
EXPECT_POS = {
    "GEO_Floor_Mercury": (0, 3.0, 0), "GEO_Core_Mercury": (0, 0, 3.2),
    "GEO_Text_Top": (0, .6, 5), "GEO_Text_Bottom": (0, .6, 1.5),
    "GEO_TextGlow_Top": (0, .78, 5), "GEO_TextGlow_Bottom": (0, .78, 1.5),
    "GEO_Slab_L": (-2.55, 1.5, 4.5), "GEO_Slab_R": (2.55, 1.5, 4.5),
    "GEO_NeonStrip_L": (-2.09, 1.04, 4.5), "GEO_NeonStrip_R": (2.09, 1.04, 4.5),
    "GEO_Wall_Back": (0, 7, 6), "GEO_NeonSlit_Back": (0, 6.74, 3.2),
    "GEO_ReflCard_Top_01": (0, -1.0, 8.5), "GEO_ReflCard_Top_02": (0, -0.4, 8.5), "GEO_ReflCard_Top_03": (0, 0.2, 8.5),
    "GEO_ReflCard_Back_01": (0, -11, 2.4), "GEO_ReflCard_Back_02": (0, -11, 2.9), "GEO_ReflCard_Back_03": (0, -11, 3.4),
    "GEO_Fog_Volume": (0, -2, 5.5), "CAM_Main": (0, -8, 2.9), "EMP_Cam_Pivot": (0, 0, 2.9), "EMP_Cam_Target": (0, 0, 2.9),
    "EMP_Noise_Pivot": (0, 0, 3.2), "EMP_Noise_Orbit": (0.6, 0, 3.2),
    "EMP_Fog_Pivot": (0, 0, 5.5), "EMP_Fog_Orbit": (1.5, 0, 5.5),
    "EMP_Floor_Pivot": (0, 3, 0), "EMP_Floor_Orbit": (0.8, 3, 0),
    "EMP_Droplet_Tilt": (0, 0, 3.2), "EMP_Droplet_Orbit": (0, 0, 3.2),
}
EXPECT_DIM = {
    "GEO_Floor_Mercury": (16, 16, 0), "GEO_Core_Mercury": (1.5, 1.5, 1.5),
    "GEO_Slab_L": (.9, .9, 9), "GEO_Slab_R": (.9, .9, 9),
    "GEO_NeonStrip_L": (.03, .03, 8), "GEO_NeonStrip_R": (.03, .03, 8),
    "GEO_Wall_Back": (12, .5, 12), "GEO_NeonSlit_Back": (6, .05, .06),
    "GEO_ReflCard_Top_01": (6, .08, 0), "GEO_ReflCard_Top_02": (6, .08, 0), "GEO_ReflCard_Top_03": (6, .08, 0),
    "GEO_ReflCard_Back_01": (4, 0, .10), "GEO_ReflCard_Back_02": (4, 0, .10), "GEO_ReflCard_Back_03": (4, 0, .10),
    "GEO_Fog_Volume": (12, 22, 11),
}
for n, r_, orb, ang in DROPS:
    EXPECT_POS["GEO_Droplet_%02d" % n] = (orb * math.cos(D(ang)), orb * math.sin(D(ang)), 0)
    EXPECT_DIM["GEO_Droplet_%02d" % n] = (2 * r_,) * 3
# droplet world pos: tilt rotated + offset
tilt = Matrix.Translation((0, 0, 3.2)) @ Matrix.Rotation(D(18), 4, 'X')
for n, r_, orb, ang in DROPS:
    nm = "GEO_Droplet_%02d" % n
    EXPECT_POS[nm] = tuple(tilt @ Vector(EXPECT_POS[nm]))

PREFIX = re.compile(r"^(GEO_|RIG_|LGT_|CAM_|EMP_)|^Audio_Controller$")
bpy.context.view_layer.update()
nmesh = ngon = 0
tri_total = faces_total = 0
for o in bpy.data.objects:
    if not PREFIX.match(o.name):
        errors.append("bad name: " + o.name)
    if re.search(r"\.\d{3}$", o.name):
        errors.append("dup suffix: " + o.name)
    if o.data is not None and o.data.name != o.name:
        errors.append("datablock name mismatch: %s / %s" % (o.name, o.data.name))
    if o.constraints:
        errors.append("constraint on " + o.name)
    if not o.users_collection or o.users_collection[0].name not in COLS:
        errors.append("collection problem: " + o.name)
    if o.type == 'MESH':
        nmesh += 1
        if any(abs(s - 1) > 1e-6 for s in o.scale) or any(abs(a) > 1e-6 for a in o.rotation_euler):
            errors.append("unapplied transform: " + o.name)
        me = o.data
        ng = sum(1 for p in me.polygons if len(p.vertices) > 4)
        ngon += ng
        faces_total += len(me.polygons)
        if me.shape_keys:
            errors.append("shape key on " + o.name)
        bm = bmesh.new(); bm.from_mesh(me)
        nonman = sum(1 for e in bm.edges if not e.is_manifold)
        bm.free()
        planar = o.name.startswith(("GEO_Floor", "GEO_ReflCard"))
        if nonman and not planar:
            errors.append("non-manifold edges (%d) on %s" % (nonman, o.name))
        if planar and nonman == 0:
            pass
        # dims from mesh data
        xs = [v.co.x for v in me.vertices]; ys = [v.co.y for v in me.vertices]; zs = [v.co.z for v in me.vertices]
        dim = (max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs))
        if o.name in EXPECT_DIM:
            ex = EXPECT_DIM[o.name]
            tol = 0.001 if not o.name.startswith("GEO_Core") and not o.name.startswith("GEO_Droplet") else 0.002
            for a, b_ in zip(dim, ex):
                if abs(a - b_) > tol:
                    errors.append("dim mismatch %s: %s vs %s" % (o.name, tuple(round(v, 4) for v in dim), ex)); break
        # normals of cards
        if o.name.startswith("GEO_ReflCard_Top") and me.polygons[0].normal.z > -0.99:
            errors.append("card top normal not -Z: " + o.name)
        if o.name.startswith("GEO_ReflCard_Back") and me.polygons[0].normal.y < 0.99:
            errors.append("card back normal not +Y: " + o.name)
    if o.type == 'FONT':
        if o.data.font is None or o.data.font.filepath != '<builtin>':
            errors.append("font not builtin: " + o.name)
        if o.data.body != o.data.body.upper() or not o.data.body.isascii():
            errors.append("text body not upper ASCII")
    if o.name in EXPECT_POS:
        d_ = (o.matrix_world.translation - Vector(EXPECT_POS[o.name])).length
        if d_ > 0.001:
            errors.append("world pos %s off by %.4f m" % (o.name, d_))

for dtype in (bpy.data.meshes, bpy.data.materials, bpy.data.curves, bpy.data.armatures, bpy.data.collections,
              bpy.data.textures, bpy.data.cameras):
    for d in dtype:
        if re.search(r"\.\d{3}$", d.name):
            errors.append("dup datablock: " + d.name)
for f in bpy.data.fonts:
    if f.filepath != '<builtin>':
        errors.append("external font " + f.name)
for im in bpy.data.images:
    if im.name not in ("Render Result", "Viewer Node"):
        errors.append("external image: %s (%s)" % (im.name, im.filepath))
if len(bpy.data.materials):
    errors.append("materials present (04 owns them)")
if ngon:
    errors.append("n-gons on meshes: %d" % ngon)

# Rig
if sorted(b.name for b in rig.data.bones) != sorted(["root", "core", "type_top", "type_bottom"]):
    errors.append("bone set wrong")
if any(b.use_deform for b in rig.data.bones):
    errors.append("deform bone present")
exp_parent = {"GEO_Core_Mercury": "core", "EMP_Droplet_Tilt": "core", "EMP_Noise_Pivot": "core",
              "GEO_Text_Top": "type_top", "GEO_TextGlow_Top": "type_top",
              "GEO_Text_Bottom": "type_bottom", "GEO_TextGlow_Bottom": "type_bottom"}
for n, bn in exp_parent.items():
    o = bpy.data.objects[n]
    if not (o.parent is rig and o.parent_type == 'BONE' and o.parent_bone == bn):
        errors.append("bone parent wrong: " + n)
for d in drops:
    if d.parent is not e_orbit:
        errors.append("droplet parent wrong " + d.name)
mods = [m.name for m in core.modifiers]
if mods != ["SUB_Main", "DSP_Core"]:
    errors.append("core modifier order " + str(mods))
if not (core.modifiers["DSP_Core"].texture and core.modifiers["DSP_Core"].texture.type == 'CLOUDS'):
    errors.append("displace texture")
if abs(cam.matrix_world.to_euler().x - D(90)) > 1e-4 or cam.parent is not e_cam_p:
    errors.append("camera setup")
if any(o.type == 'LIGHT' for o in bpy.data.objects):
    errors.append("light present")
if (r.resolution_x, r.resolution_y, r.fps, scene.frame_start, scene.frame_end) != (1080, 1920, 30, 1, 240):
    errors.append("scene settings")

# Info: text -> mesh n-gons (FONT objects stay FONT, exempt per spec 2.4)
for t in (t_top, t_bot):
    dg = bpy.context.evaluated_depsgraph_get()
    ev = t.evaluated_get(dg); me = ev.to_mesh()
    info.append("%s evaluated: %d faces, %d n-gons, %d tris (info only, FONT exempt)" % (
        t.name, len(me.polygons), sum(1 for p in me.polygons if len(p.vertices) > 4),
        sum(1 for p in me.polygons if len(p.vertices) == 3)))
    ev.to_mesh_clear()

# Composition / collision report
th = TEXT_REPORT["GEO_Text_Top"]; tb = TEXT_REPORT["GEO_Text_Bottom"]
info.append("TEXT size=%.4f MOLLY w=%.3f h=%.3f d=%.3f (center %.3f,%.3f) | WOOD w=%.3f h=%.3f"
            % (size, th["width"], th["height"], th["depth"], th["cx"], th["cy"], tb["width"], tb["height"]))
info.append("MOLLY height 0.65+-0.02: %s | width 3.0-3.4: %s | WOOD width 2.6-3.0: %s" % (
    abs(th["height"] - 0.65) <= 0.02, 3.0 <= th["width"] <= 3.4, 2.6 <= tb["width"] <= 3.0))
info.append("MOLLY top Z = %.3f, WOOD bottom Z = %.3f (safe band 0.44..5.79)" % (5.0 + th["height"] / 2, 1.5 - tb["height"] / 2))
info.append("core extent Z 2.45..3.95; max core radius w/ caps = %.3f" % (0.75 * 1.18 + 0.5 * 0.30 * 1.18))
for n, r_, orb, ang in DROPS:
    info.append("droplet %02d inner edge (cap) %.3f > 1.062: %s" % (n, orb - r_ * 1.25, orb - r_ * 1.25 > 1.062))

print("=" * 60)
print("OBJECTS: %d (MESH %d)  base faces: %d  n-gons: %d" % (len(bpy.data.objects), nmesh, faces_total, ngon))
dg = bpy.context.evaluated_depsgraph_get()
evtri = 0
for o in bpy.data.objects:
    if o.type == 'MESH':
        ev = o.evaluated_get(dg); me = ev.to_mesh(); evtri += len(me.polygons); ev.to_mesh_clear()
print("evaluated (with modifiers, viewport levels) faces: %d" % evtri)
for i in info:
    print("INFO:", i)
if errors:
    for e in errors:
        print("ERROR:", e)
    print("VALIDATION: FAIL (%d)" % len(errors))
else:
    print("VALIDATION: PASS")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=OUT)
print("SAVED", OUT)
sys.exit(1 if errors else 0)
