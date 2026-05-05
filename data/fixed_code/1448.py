import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Block ---
part_1_length = 0.4407 * 0.4773  # Scaled length
part_1_width = 0.4773 * 0.4773  # Scaled width
part_1_height = 0.0634
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for a cut
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.3214, 0.0, 0.1093))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0757 * 0.1513  # Scaled radius
part_2_depth = 0.0303
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1448.stl