import cadquery as cq
from math import radians
# --- Part 1: Cube with Circular Hole ---
part_1_length = 0.75 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.25
hole_center_x = 0.375 * 0.75
hole_center_y = 0.3125 * 0.75
hole_radius = 0.15 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center_x - part_1_length/2, hole_center_y - part_1_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.25, 0))
# --- Part 2: Cut Feature ---
part_2_length = 0.15 * 0.5
part_2_width = 0.5 * 0.5
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3190.stl