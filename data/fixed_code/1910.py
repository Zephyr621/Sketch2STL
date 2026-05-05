import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Block ---
part_1_length = 0.7297 * 0.7297  # Scaled length
part_1_width = 0.3649 * 0.7297  # Scaled width
part_1_height = 0.1824
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1824, 0))
# --- Part 2: Triangular Prism (Cut) ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.1762 * 0.75  # Scaled width
part_2_height = 0.0214
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1910.stl