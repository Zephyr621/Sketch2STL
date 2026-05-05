import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2917
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2917, 0))
# --- Part 2: Hole ---
part_2_radius = 0.0312 * 0.0625  # Sketch radius scaled
part_2_height = 0.7958
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0156, 0.2917, 0.0156))
# --- Part 3: Cut ---
part_3_outer_radius = 0.0313 * 0.0625
part_3_inner_radius = 0.0312 * 0.0625
part_3_height = 0.7958
part_3 = (
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1418.stl