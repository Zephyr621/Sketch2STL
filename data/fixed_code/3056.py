import cadquery as cq
from cadquery.vis import show
# --- Part 1: Triangle ---
sketch_scale = 0.75
extrude_depth = 0.0375
# Scaled dimensions
p1 = (0.0 * sketch_scale, 0.5 * sketch_scale)
p2 = (0.375 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.75 * sketch_scale, 0.5 * sketch_scale)
p4 = (0.375 * sketch_scale, 0.2812 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .lineTo(p3[0], p3[1])
    .lineTo(p4[0], p4[1])
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.cq.exporters.export({result_var}, "output_3056.stl"output_3056.stl