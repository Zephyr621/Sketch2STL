import cadquery as cq
# --- Part 1: Square Ring ---
outer_size = 0.75 * 0.75  # Scaled outer square size
inner_radius = 0.1458 * 0.75
height = 0.0357
part_1 = (
    cq.Workplane("XY")
    .rect(outer_size, outer_size)
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
cq.
cq.cq.exporters.export({result_var}, "output_1768.stl"output_1768.stl