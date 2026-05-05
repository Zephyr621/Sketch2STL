import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Base ---
part_1_length = 0.1125 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0259
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.6, 0))
# --- Part 2: Cube ---
part_2_length = 0.3 * 0.4  # Scaled length
part_2_width = 0.4 * 0.4  # Scaled width
part_2_height = 0.15
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_569.stl