import cadquery as cq
from cadquery import exporters
# --- Part 1: Base Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.7406
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylinder ---
part_2_radius = 0.3884 * 0.6629  # Scaled radius
part_2_height = 0.6629
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformations ---
# Part 1: Rotation and Translation
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Part 2: Rotation and Translation
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1346.stl