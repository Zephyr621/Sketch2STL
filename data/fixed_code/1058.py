import cadquery as cq
# --- Part 1: Circular Object with Hole ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1714 * 0.75  # Inner hole radius scaled
height = 0.0536
wp = cq.Workplane("XY").circle(outer_radius).extrude(height)
part_1 = wp.cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1058.stl"output_1058.stl