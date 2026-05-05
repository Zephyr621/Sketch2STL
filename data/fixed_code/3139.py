import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0429 * 0.75)
    .lineTo(0.7295 * 0.75, 0.0429 * 0.75)
    .lineTo(0.7295 * 0.75, 0.4615 * 0.75)
    .lineTo(0.75 * 0.75, 0.4615 * 0.75)
    .lineTo(0.75 * 0.75, 0.3771 * 0.75)
    .lineTo(0.0, 0.3771 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4996 * 0.75)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export({result_var}, "output_3139.stl"output_3139.stl