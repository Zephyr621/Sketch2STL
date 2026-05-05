import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.1594 * 0.3091  # Sketch radius scaled
part_1_height = 0.0703
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0703, 0.75, 0.0197))
# --- Part 2: Cylinder ---
part_2_radius = 0.0852 * 0.1765  # Sketch radius scaled
part_2_height = 0.0703
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0703, 0.75, 0.0703))
# --- Part 3: Cylinder ---
part_3_radius = 0.
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1008.stl