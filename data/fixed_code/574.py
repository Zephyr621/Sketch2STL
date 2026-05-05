import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Block with Holes ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5 * 0.75  # Scaled width
part_1_height = 0.2075
hole_radius = 0.0625 * 0.75  # Scaled radius
hole_center_1 = (0.125 * 0.75 - part_1_length/2, 0.125 * 0.75 - part_1_width/2)  # Scaled and centered
hole_center_2 = (0.625 * 0.75 - part_1_length/2, 0.125 * 0.75 - part_1_width/2)  # Scaled and centered
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .pushPoints([hole_center_1, hole_center_2])
    .hole(2 * hole_radius)
)
# --- Coordinate
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_574.stl