import cadquery as cq
# --- Parameters ---
length = 0.75 * 0.75  # Scaled length
width_face1 = 0.1364 * 0.75  # Scaled width for face 1
width_face2 = 0.2479 * 0.75  # Scaled width for face 2
height_face1 = 0.1269
height_face2 = 0.2397
height_face3 = 0.2479
# --- Create Rectangular Block ---
block = cq.Workplane("XY").box(length, width_face1, height_face1)
# --- Create Corner Profile (Cut) ---
cut_profile = (
    cq.Workplane("XY")
    .moveTo(0, width_face1)
    .lineTo(0, width_face2)
    .lineTo(0, width_face3)
    .close()
)
# --- Position the Corner Profile ---
cut_profile = cut_profile.translate([0.2578 * 0.75 - length/2, 0, 0])
# --- Perform Cut Operation ---
result = block.cut(cut_profile)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_862.stl"output_862.stl