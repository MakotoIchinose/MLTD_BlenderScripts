# Rename Million Live Theater Days armatures to MMD compatible!

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
#  4. Join both head and body armature, starting with the head armature as the base.
#  5. Delete duplicate bones created from the merger.
#     Usually the bones are: KUBI.001 and ATAMA.001

# WARNING:
#  MLTD models do not use bones for the iris position - the game relies on shifting the
#  eye texture instead. If you want to use iris bones , try separating the iris texture
#  from the sclera.