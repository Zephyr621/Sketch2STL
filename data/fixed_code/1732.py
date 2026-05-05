import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.3 * 0.6  # Sketch radius scaled
inner_radius = 0.15 * 0.6  # Inner radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
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
cq.cq.exporters.export({result_var}, "output_1732.stl"output_1732.stl