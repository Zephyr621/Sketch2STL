import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.075 * 0.15  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Part 2: Recessed Cylinder ---
part_2_radius = 0.03 * 0.06  # Sketch radius scaled
part_2_height = 0.15
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0225, 0.15, 0.0225))
# --- Part 3: Cut Cylinder ---
part_3_radius = 0.03 * 0.06  # Sketch radius scaled
part_3_height = 0.15
part_3 = cq.Workplane("XY").circle(part_3_radius).extrude(-part_3_height)
# --- Coordinate System Transformation for Part 3 ---
part_3 = part_3.rotate((0, 0, 0), (0, 0, 1), -90)
part_3 = part_3.rotate((0, 0, 0), (1, 0, 0
# Export
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_605.stl