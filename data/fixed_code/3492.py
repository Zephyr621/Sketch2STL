import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Block with Circular Holes ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5625 * 0.75  # Scaled width
part_1_height = 0.0938
hole_radius = 0.0417 * 0.75  # Scaled radius
hole_center_1 = (0.1875 * 0.75 - part_1_length / 2, 0.1875 * 0.75 - part_1_width / 2)  # Scaled and centered
hole_center_2 = (0.5625 * 0.75 - part_1_length / 2, 0.1875 * 0.75 - part_1_width / 2)  # Scaled and centered
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .pushPoints([hole_center_1, hole_center_2])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3492.stl