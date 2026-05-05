import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.5938 * 0.5938  # Scaled length
part_1_width = 0.2769 * 0.5938  # Scaled width
part_1_height = 0.1364
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.2432, 0.1364, 0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0118 * 0.0268  # Scaled radius
part_2_depth = 0.116
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_423.stl