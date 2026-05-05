import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_length = 0.713 * 0.713  # Scaled length
part_1_width = 0.6806 * 0.713  # Scaled width
part_1_height = 0.1272
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0385, 0.1272, 0))
# --- Part 2: Cutout ---
part_2_length = 0.0577 * 0.0577  # Scaled length
part_2_width = 0.0577 * 0.0577  # Scaled width
part_2_height = 0.1318
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_111.stl