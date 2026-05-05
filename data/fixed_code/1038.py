import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.0853 * 0.75  # Sketch radius scaled
part_1_height = 0.1584
# Create the first cylinder
cylinder1 = cq.Workplane("XY").moveTo(0.162 * 0.75, 0.162 * 0.75).circle(part_1_radius).extrude(part_1_height)
# Create the second cylinder
cylinder2 = cq.Workplane("XY").moveTo(0.6852 * 0.75, 0.162 * 0.75).circle(part_1_radius).extrude(part_1_height)
# Combine the two cylinders
result = cylinder1.union(cylinder2)
cq.
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1038.stl"output_1038.stl