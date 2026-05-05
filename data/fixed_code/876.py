import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism with Curved Edges ---
part_1_length = 0.0192 * 0.0385  # Scaled length
part_1_width = 0.0385 * 0.0385  # Scaled width
part_1_height = 0.1875 + 0.1875  # Total height (both directions)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .threePointArc((part_1_length/2, part_1_width), (part_1_length, part_1_width))
    .lineTo(0, part_1_width)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.375))
# --- Part 2: Cutout ---
part_2_length = 0.0226 * 0.0226  # Scaled length
part_2_width = 0.0226 * 0.0226  # Scaled width
part_2_height = 0.0057
part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_876.stl