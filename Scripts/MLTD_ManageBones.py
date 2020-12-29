# Manage the cluster of bones in MLTD Models!

import bpy
context = bpy.context
scene = context.scene
obj = context.object

# NOTE:
#   This manager script is written with Unreal Engine 4 standards in mind.
#   Also, some Unity ripper tools may scramble the bone hierarchy a bit.

# This script will clean up bone after joining the body armature and the rig armature.
# Before you use the script, make sure you have joined the body armature to the head armature.
# You may also need to reparent the body mesh to the newly joint armature if it doesn't
# respond to the bones.
# Make sure you have applied the transform of the model and the armature!

# TODO: We might automate the joining process once we turn this script suite into add-on.

# What the script does:

# 1. Obliterate all Empty junks. All the Empties built into the MLTD models are unusable
# for Blender.

for objs in scene.objects:
    if objs.type == 'EMPTY':
        bpy.data.objects.remove(objs)

# 2. Get rid of duplicate bones. KUBI.001 and ATAMA.001 is the usual suspects.

if obj.type == 'ARMATURE':
    armature = obj.data

bpy.ops.object.mode_set(mode='EDIT')

for bone in armature.edit_bones:
    if bone.name == "KUBI.001": 
        armature.edit_bones.remove(bone)
    elif bone.name == "ATAMA.001":
        armature.edit_bones.remove(bone)
    else:
        continue

# 3. Parent KUBI to MUNE2, connecting the head with the spine bone

armature.edit_bones["KUBI"].parent = armature.edit_bones["MUNE2"]
bpy.ops.object.mode_set(mode='POSE')