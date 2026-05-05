import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.3516 * 0.6964  # Sketch radius scaled
part_1_height = 0.0142
hole_center_x1 = 0.1366 * 0.6964
hole_center_y1 = 0.1042 * 0.6964
hole_center_x2 = 0.6136 * 0.6964
hole_center_y2 = 0.0977 * 0.6964
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.3067 * 0.6964, 0.3259 * 0.6964)
    .circle(part_1_radius)
    .extrude(part_1_height)
)
# Create the hole
part_1 = part_1.faces(">Z").workplane().pushPoints([(hole_center_x1 - (0.6964/0.6964)/2, hole_center_y1 - (0.5248/0.6964)/2)]).hole(hole_radius*2)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2326.stl