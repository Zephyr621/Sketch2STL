import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.25 * sketch_scale
# Scaled dimensions for the sketch
p1 = (0.125 * sketch_scale, 0.125 * sketch_scale)
p2 = (0.375 * sketch_scale, 0.125 * sketch_scale)
p3 = (0.625 * sketch_scale, 0.125 * sketch_scale)
p4 = (0.625 * sketch_scale, 0.0 * sketch_scale)
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
cq.cq.exporters.export({result_var}, "output_3121.stl"output_3121.stl