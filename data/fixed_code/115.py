import cadquery as cq
from cadquery import exporters
# --- Part 1: Base Cube ---
part_1_length = 0.4415 * 0.7457  # Scaled length
part_1_width = 0.7457 * 0.7457  # Scaled width
part_1_height = 0.4353
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4353, 0))
# --- Part 2: Top Cube ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.2812 * 0.75  # Scaled width
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for a cutout
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_115.stl