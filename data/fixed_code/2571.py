import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.5 * 0.5  # Scaled length
part_1_width = 0.375 * 0.5  # Scaled width
part_1_height = 0.25
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cutout ---
part_2_length = 0.625 * 0.625  # Scaled length
part_2_width = 0.375 * 0.625  # Scaled width
part_2_height = 0.125
part_2 = cq.Workplane("XY").moveTo(0.0, 0.0).lineTo(0.25 * 0.625, 0.0).lineTo(0.25 * 0.625, 0.125 * 0.625).lineTo(0.0, 0.125 * 0.625).close().extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2571.stl