#
# @file    batch_fbx_to_blend.py
# @version 1.0
#
# Traverse a directory tree and convert all FBX files into Blend files.
# Do not reconvert if the .blend file already exists. Map "<name>.fbx" to
# "<name>.blend".
#
# Example usage:
#
#   blender empty.blend --background --python batch_fbx_to_blend.py
#
import bpy
from pathlib import Path

# Location prefix of the input FBX files.
# Windows and macOS.
p = Path.home() / Path("Documents/Motion/take/2019-07-09")
# Linux.
#p = Path.home() / Path("Motion/take")

# Reload the startup file for every conversion.
scene_filepath = bpy.data.filepath

for pathname in p.glob("**/*.fbx"):
    blend_pathname = pathname.with_suffix(".blend")
    if blend_pathname.exists():
        continue

    bpy.ops.import_scene.fbx(
        filepath=str(pathname),
        automatic_bone_orientation=True)

    bpy.ops.wm.save_as_mainfile(filepath=str(blend_pathname))

    bpy.ops.wm.open_mainfile(filepath=scene_filepath)
