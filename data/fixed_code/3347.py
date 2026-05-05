import cadquery as cq
# --- Part 1: Cup ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.3435 * 0.75
height = 0.0134
cup = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Final Result ---
result = cup
cq.
cq.
cq.
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3347.stl"output_3347.stl