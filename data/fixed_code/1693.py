import cadquery as cq
# --- Part 1: Triangle Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3271 * 0.75)
    .lineTo(0.0, 0.3271 * 0.75)
    .close()
    .extrude(0.1429)
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
cq.
cq.cq.exporters.export({result_var}, "output_1693.stl"output_1693.stl