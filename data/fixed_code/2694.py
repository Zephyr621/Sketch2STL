import cadquery as cq
# --- Part 1: L-shaped profile ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4286 * 0.75, 0.0)
    .lineTo(0.4286 * 0.75, 0.3214 * 0.75)
    .lineTo(0.3214 * 0.75, 0.3214 * 0.75)
    .lineTo(0.3214 * 0.75, 0.6429 * 0.75)
    .lineTo(0.2143 * 0.75, 0.6429 * 0.75)
    .lineTo(0.2143 * 0.75, 0.3214 * 0.75)
    .lineTo(0.0, 0.3214 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.6429)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export({result_var}, "output_2694.stl"output_2694.stl