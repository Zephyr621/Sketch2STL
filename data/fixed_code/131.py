import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.0099 * 0.0121  # Sketch radius scaled
part_1_height = 0.2903
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0313, 0.0313, 0.0313))
# --- Part 2: Cylinder ---
part_2_radius = 0.0122 * 0.0465  # Sketch radius scaled
part_2_height = 0.1534
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), 90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_131.stl