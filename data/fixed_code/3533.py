import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0625 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.2812 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.4688 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.4687 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.4438 * sketch_scale)
    .lineTo(0.0, 0.4438 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.cq.exporters.export({result_var}, "output_3533.stl"output_3533.stl