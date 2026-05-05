import cadquery as cq
# --- Part 1: Cylinder ---
part_1_radius = 0.0469 * 0.0937  # Sketch radius scaled
part_1_height = 0.1875 + 0.1875
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
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
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2709.stl"output_2709.stl