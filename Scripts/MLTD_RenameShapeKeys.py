# Rename MLTD's facial shape keys with confusing names to something you can read!

import bpy
context = bpy.context
obj = context.object

# This script renames MLTD model's facial shape keys / morph targets, which are obfuscated
# by shape key index numbers, to matching names in readable English.
# This script also adheres to PAST FUTURE's shape keys naming convention. You can modify
# the names if you want to.
# Select the face mesh before executing this script!

# This array is the template used for the batch rename script.
# The format for the array element goes like this:
#           ("old name","new name")
# Quote mark is not omitted. Add comma if there's a new shape key you want to rename.
sknames = [
        ("100.000000",  "Mouth - A"),
        ("100.001",     "Mouth - I"),
        ("100.002",     "Mouth - U"),
        ("100.003",     "Mouth - E"),
        ("100.004",     "Mouth - O"),
        ("100.005",     "Mouth - Flat"),
        ("100.006",     "Mouth - Wide Open"),
        ("100.007",     "Mouth - Frown"),
        ("100.008",     "Mouth - Grin"),
        ("100.009",     "Mouth - Up"),
        ("100.010",     "Mouth - Doubt"),
        ("100.011",     "Mouth - Down"),
        ("100.012",     "Mouth - Shocked"),
        ("100.013",     "Mouth - Tiny Grin"),
        ("100.014",     "Brows - Angry R"),
        ("100.015",     "Brows - Angry L"),
        ("100.016",     "Brows - Frown R"),
        ("100.017",     "Brows - Frown L"),
        ("100.018",     "Brows - Happy R"),
        ("100.019",     "Brows - Happy L"),
        ("100.020",     "Brows - Doubt R"),
        ("100.021",     "Brows - Doubt L"),
        ("100.022",     "Brows - Down"),
        ("100.023",     "Brows - Narrow"),
        ("100.024",     "Eyes - Close Down R"),
        ("100.025",     "Eyes - Close Down L"),
        ("100.026",     "Eyes - Close Up R"),
        ("100.027",     "Eyes - Close Up L"),
        ("100.028",     "Eyes - Shocked R"),
        ("100.029",     "Eyes - Shocked L")
]

for name, newname in sknames:
    # Get shape keys in the mesh
    keys = selected_object.data.shape_keys.key_blocks
    for key in keys:
        # Validate key name before renaming it
        if key.name == name:
            key.name = key.name.replace(name, newname)
        else:
            continue
    
