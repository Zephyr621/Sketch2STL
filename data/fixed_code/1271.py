import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2143
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Small Cylinder (Cut) ---
part_2_radius = 0.1071 * 0.4286  # Sketch radius scaled
part_2_height = 0.2143
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1071, 0.1071, 0.2143))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1271.stl"output_1271.stl