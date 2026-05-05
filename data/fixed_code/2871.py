import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3696 * 0.75)
    .lineTo(0.375 * 0.75, 0.6387 * 0.75)
    .lineTo(0.0, 0.6387 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0064)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2871.stl"output_2871.stl