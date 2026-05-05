import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0674
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Hole ---
part_2_radius = 0.3571 * 0.7143  # Sketch radius scaled
part_2_height = 0.0331
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0186, 0.0186, part_1_height))
# --- Assembly: Cut the hole from the cylinder ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3584.stl"output_3584.stl