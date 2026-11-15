import bpy, os
R = r"C:\Users\neritinc\Documents\3D PROJECT\pipeline\renders"
s = bpy.context.scene
s.render.resolution_percentage = 25
s.cycles.samples = 16
s.render.use_motion_blur = False
s.render.image_settings.file_format = 'PNG'
s.render.image_settings.color_depth = '8'
try: s.cycles.volume_step_rate = 2.0
except Exception: pass
for f in (104, 125, 130):
    s.frame_set(f)
    s.render.filepath = os.path.join(R, "anim_test_f%03d.png" % f)
    bpy.ops.render.render(write_still=True)
    print("rendered", f)
