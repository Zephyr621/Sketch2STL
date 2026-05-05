import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube with Circular Hole ---
part_1_length = 0.6 * 0.6  # Scaled length
part_1_width = 0.6 * 0.6   # Scaled width
part_1_height = 0.75
hole_center_x = 0.3 * 0.6  # Scaled center x
hole_center_y = 0.15 * 0.6  # Scaled center y
hole_radius = 0.225 * 0.6   # Scaled radius
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
part_1 = part_1.rotate((0, 0, 0), (0, 0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2060.stl