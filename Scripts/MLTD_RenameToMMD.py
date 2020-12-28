# Rename Million Live Theater Days armatures to MMD compatible!

import bpy
context = bpy.context
obj = context.object

# NOTE:
#  This user script is meant to use in conjunction with MMD Tools and base MMD armature,
#  quickly renaming MLTD bones to MMD compatible armature. Please note that this script
#  is for use with translated bone names in mind, so you can rename it to Japanese names
#  by modifying this script.
#  Renaming bones alse renames the corresponding weight automatically, so it's useful
#  for applying proper MMD armature to a MLTD model.

# PREREQUISITES:
#  1. Rip the models from the game. You should have matching body and head for each
#     character. Because the game uses Unity engine, you can rip them using your favourite
#     Unity ripper tools.
#  2. Import the models you've ripped from the package into Blender.
#  3. If the model is to small, scale it up to 100x.
#  4. Join the body armature to the head armature.
#  5. Delete duplicate bones created from the merger.
#     Usually the bones are: KUBI.001 and ATAMA.001

# WARNING:
#  MLTD models do not use bones for the iris position - the game relies on shifting the
#  eye texture instead. If you want to use iris bones , try separating the iris texture
#  from the sclera.



# This array is the template used for the batch rename script.
# The format for the array element goes like this:
#           ("old name","new name")
# Quote mark is not omitted. Add comma if there's a new bone you want to rename.
bonenames = [
    ("BASE",                    "ParentNode"),
    ("MUNE1",                   "UpperBody"),
    ("MUNE2",                   "UpperBody2"),
    ("KUBI",                    "Neck"),
    ("ATAMA",                   "Head"),
    ("SAKOTSU_L",               "Shoulder_L"),
    ("KATA_L",                  "Arm_L"),
    ("KATA_MD_L__twist_x50",    "ArmTwistAxis_L"),
    ("KATA_RT_L__twist_x0",     "ArmTwist_L"),
    ("UDE_L",                   "Elbow_L"),
    ("TEKUBI_L__rot_TE_L__x100","HandTwistAxis_L"),
    ("UDE_MD_L__rot_TE_L__x50", "HandTwist_L"),
    ("TE_L",                    "Wrist_L"),
    ("OYA2_L",                  "Thumb1_L"), # Increment this index if you're including thumb palm
    ("OYA1_L",                  "Thumb2_L"), # Increment this index if you're including thumb palm
    ("HITO3_L",                 "IndexFinger1_L"),
    ("HITO2_L",                 "IndexFinger2_L"),
    ("HITO1_L",                 "IndexFinger3_L"),
    ("NAKA3_L",                 "MiddleFinger1_L"),
    ("NAKA2_L",                 "MiddleFinger2_L"),
    ("NAKA1_L",                 "MiddleFinger3_L"),
    ("KUSU3_L",                 "RingFinger1_L"),
    ("KUSU2_L",                 "RingFinger2_L"),
    ("KUSU1_L",                 "RingFinger3_L"),
    ("KO3_L",                   "LittleFinger1_L"),
    ("KO2_L",                   "LittleFinger2_L"),
    ("KO1_L",                   "LittleFinger3_L"),
    ("SAKOTSU_R",               "Shoulder_R"),
    ("KATA_R",                  "Arm_R"),
    ("KATA_MD_R__twist_x50",    "ArmTwistAxis_R"),
    ("KATA_RT_R__twist_x0",     "ArmTwist_R"),
    ("UDE_R",                   "Elbow_R"),
    ("TEKUBI_R__rot_TE_R__x100","HandTwistAxis_R"),
    ("UDE_MD_R__rot_TE_R__x50", "HandTwist_R"),
    ("TE_R",                    "Wrist_R"),
    ("OYA2_R",                  "Thumb1_R"), # Increment this index if you're including thumb palm
    ("OYA1_R",                  "Thumb2_R"), # Increment this index if you're including thumb palm
    ("HITO3_R",                 "IndexFinger1_R"),
    ("HITO2_R",                 "IndexFinger2_R"),
    ("HITO1_R",                 "IndexFinger3_R"),
    ("NAKA3_R",                 "MiddleFinger1_R"),
    ("NAKA2_R",                 "MiddleFinger2_R"),
    ("NAKA1_R",                 "MiddleFinger3_R"),
    ("KUSU3_R",                 "RingFinger1_R"),
    ("KUSU2_R",                 "RingFinger2_R"),
    ("KUSU1_R",                 "RingFinger3_R"),
    ("KO3_R",                   "LittleFinger1_R"),
    ("KO2_R",                   "LittleFinger2_R"),
    ("KO1_R",                   "LittleFinger3_R"),
    ("KOSHI",                   "LowerBody"),
    ("MOMO_L",                  "Leg_L"),
    ("HIZA_L",                  "Knee_L"),
    ("ASHI_L",                  "Ankle_L"),
    ("TSUMASAKI_L",             "Toe_L"),
    ("MOMO_R",                  "Leg_R"),
    ("HIZA_R",                  "Knee_R"),
    ("ASHI_R",                  "Ankle_R"),
    ("TSUMASAKI_R",             "Toe_R")

]

for oldname, newname in bonenames:
    # Get the pose bone with name
    pb = obj.pose.bones.get(oldname)
    # Move on if no matching bone found
    if pb is None:
        continue
    # rename
    pb.oldname = newname