import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cube with Holes ---
length = 0.75 * 0.75  # Scaled length
width = 0.4459 * 0.75  # Scaled width
height = 0.0384
hole_radius = 0.0274 * 0.75  # Scaled radius
hole1_x = 0.1364 * 0.75  # Scaled x-coordinate
hole1_y = 0.1442 * 0.75  # Scaled y-coordinate
hole2_x = 0.6151 * 0.75  # Scaled x-coordinate
hole2_y = 0.1442 * 0.75  # Scaled y-coordinate
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .hole(2 * hole_radius)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1994.stl