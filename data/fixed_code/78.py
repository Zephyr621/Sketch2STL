import cadquery as cq
# --- Part 1: L-shaped extrusion ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.2212 * 0.2812, 0.0)
    .lineTo(0.2212 * 0.2812, 0.0469 * 0.2812)
    .lineTo(0.0, 0.0469 * 0.2812)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_78.stl"output_78.stl