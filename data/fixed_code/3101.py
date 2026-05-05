import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.2893 * 0.5769  # Sketch radius scaled
part_1_height = 0.0385
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0495, 0.0495, 0.0385))
# --- Part 2: Cylinder ---
part_2_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_height = 0.1526
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0, 0.5897, 0))
# --- Part 3: Cylinder ---
part_3_radius = 0.3581 * 0.7105  # Sketch radius scaled
part_3
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3101.stl