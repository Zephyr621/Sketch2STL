import cadquery as cq
from cadquery import exporters
# --- Part 1: Base Rectangular Prism ---
part_1_length = 0.6042 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0417 + 0.0417  # Total extrusion depth
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0921))
# --- Part 2: Cutout ---
part_2_length = 0.6042 * 0.6042  # Scaled length
part_2_width = 0.7188 * 0.6042  # Scaled width
part_2_height = 0.0091  # Height
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 =
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3544.stl