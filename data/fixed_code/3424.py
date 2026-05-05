import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Bar with Holes ---
part_1_length = 0.75 * 0.75
part_1_width = 0.1071 * 0.75
part_1_height = 0.0522
hole_radius = 0.0429 * 0.75
hole_center_1_x = 0.1607 * 0.75 - (0.375 * 0.75)/2
hole_center_1_y = 0.0937 * 0.75 - (0.375 * 0.75)/2
hole_center_2_x = 0.5869 * 0.75 - (0.375 * 0.75)/2
hole_center_2_y = 0.0937 * 0.75 - (0.375 * 0.75)/2
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_1_x - part_1_length/2, hole_center_1_y - part_1_width/2).circle(hole_radius).cutThruAll()
    .faces(">Z").workplane()
    .moveTo
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3424.stl