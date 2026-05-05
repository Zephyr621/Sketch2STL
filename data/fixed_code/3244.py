import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3947 * 0.75  # Scaled width
part_1_height = 0.3158
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3158, 0))
# --- Part 2: Cutout 1 ---
cutout_size = 0.7143 * 0.7143  # Scaled size
cutout_depth = 0.1577
cutout_1 = (
    cq.Workplane("XY")
    .moveTo(0, cutout_size)
    .lineTo(cutout_size, cutout_size)
    .lineTo(cutout_size, 0.3071 * 0.7143)
    .threePointArc((0.3701 * 0.7143, 0.2288 * 0.7143), (0.6286 * 0.7143, 0.2906 * 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3244.stl