import cadquery as cq
# --- Part 1: Rectangular Prism with Cutout ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.375 * sketch_scale
height = 0.0056
cutout_x = 0.3409 * sketch_scale
cutout_y = 0.2308 * sketch_scale
cutout_width = (0.4655 - 0.0417) * sketch_scale
cutout_height = (0.2531 - 0.2308) * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .rect(cutout_width, cutout_height)
    .cutThruAll()
)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_442.stl"output_442.stl