import cadquery as cq
# --- Part 1: Cylinder with Hole ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1364 * 0.75
height = 0.2386
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
# Export to STL
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_430.stl"output_430.stl