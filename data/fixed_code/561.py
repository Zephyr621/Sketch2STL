import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5625 * 0.75  # Scaled width
part_1_height = 0.0625
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylindrical Protrusion ---
part_2_radius = 0.0081 * 0.0112  # Scaled radius
part_2_height = 0.0938
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformations ---
# Part 1: Rotate and Translate
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# Part 2: Rotate and Translate
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0312, 0.0938, 0.0312))
# --- Assembly ---
assembly = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_561.stl