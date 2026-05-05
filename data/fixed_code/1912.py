import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0714
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Hole (Cut) ---
part_2_radius = 0.2143 * 0.4286  # Sketch radius scaled
part_2_height = 0.0357
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)  # Extrude in the opposite direction for cutting
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1071, 0.1071, part_1_height))
# --- Assembly: Cut the hole from the cylinder ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.
# --- Final Result ---
cq.
# --- Export to STL ---
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_1912.stl