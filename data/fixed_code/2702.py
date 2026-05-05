import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.1136 * 0.1136  # Scaled length
part_1_width = 0.0534 * 0.1136  # Scaled width
part_1_height = 0.0931
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0, 0.0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0062 * 0.0063  # Scaled radius
part_2_depth = 0.0214
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1976, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2702.stl