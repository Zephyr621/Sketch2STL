import cadquery as cq
# --- Part 1: Ring ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.3409 * 0.75
height = 0.0857
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(height)
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
cq.cq.exporters.export({result_var}, "output_1738.stl"output_1738.stl