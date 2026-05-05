import cadquery as cq
# --- Part 1: Circular Plate ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.0476 * 0.75  # Inner hole radius scaled
plate_height = 0.0144
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(plate_height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(plate_height))
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
cq.
cq.cq.exporters.export({result_var}, "output_1057.stl"output_1057.stl