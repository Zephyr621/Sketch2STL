import cadquery as cq
# --- Part 1: Cube with corner cut off ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.4687 * sketch_scale
height = 0.2406
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(length, 0.0)
    .lineTo(length, width)
    .lineTo(0.0, width)
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
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1985.stl"output_1985.stl