import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.6324 * 0.75, 0.0)
    .lineTo(0.6324 * 0.75, 0.5867 * 0.75)
    .lineTo(0.0, 0.5867 * 0.75)
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
cq.cq.exporters.export({result_var}, "output_305.stl"output_305.stl