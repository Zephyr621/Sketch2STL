import cadquery as cq
# --- Part 1: Cup ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.3261 * 0.75
height = 0.1814
cup = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = cup
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3269.stl"output_3269.stl