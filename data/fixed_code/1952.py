import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.2205882352941176 * 0.220588  # Scaled length
part_1_width = 0.05882352941176469
part_1_height = 0.1109807384615592
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0337, 0.0, 0.0045))
# --- Part 2: Triangle Top ---
part_2_length = 0.0444791395421667 * 0.044479  # Scaled length
part_2_width = 0.019977141 * 0.044479  # Scaled width
part_2_height = 0.0357363912984319
part_2 = (
    cq
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1952.stl