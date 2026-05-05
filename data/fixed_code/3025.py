import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.3702 * sketch_scale
height = 0.0344
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .threePointArc((0.375 * sketch_scale, 0), (length, 0))
    .lineTo(length, width)
    .threePointArc((0.75 * sketch_scale, width/2), (0, width))
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3025.stl"output_3025.stl