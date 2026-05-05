import cadquery as cq
# --- Part 1: Cylinder with Rectangular Section ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_rect_width = (0.4687 - 0.1312) * 0.75
inner_rect_height = (0.5294 - 0.0052) * 0.75
extrude_depth = 0.375
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(extrude_depth)
    .cut(cq.Workplane("XY").moveTo(inner_rect_width/2, inner_rect_height/2).extrude(extrude_depth))
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
cq.cq.exporters.export({result_var}, "output_194.stl"output_194.stl