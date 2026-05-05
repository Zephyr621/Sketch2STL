import cadquery as cq
# --- Part 1: Cube with Cutout ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.625 * sketch_scale
height = 0.25
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length, 0.125 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.375 * sketch_scale, width)
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2409.stl"output_2409.stl