import cadquery as cq
from math import radians
# --- Part 1: Rectangular Top ---
part_1_length = 0.1438 * 0.4286  # Scaled length
part_1_width = 0.4286 * 0.4286  # Scaled width
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0057 * 0.0171  # Scaled radius
part_2_height = 0.1875 + 0.1875  # Total extrusion depth
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3470.stl