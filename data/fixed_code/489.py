import cadquery as cq
from math import radians
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3169 * 0.75  # Scaled width
part_1_height = 0.6972
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.6972, 0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0156 * 0.0313  # Scaled radius
part_2_depth = 0.0224
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_489.stl