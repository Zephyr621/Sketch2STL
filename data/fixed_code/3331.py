import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Block with Holes ---
length = 0.75
width = 0.3871
height = 0.0257
sketch_scale = 0.75
hole1_center = (0.1476 * sketch_scale, 0.1476 * sketch_scale)
hole2_center = (0.6081 * sketch_scale, 0.1476 * sketch_scale)
hole3_center = (0.6111 * sketch_scale, 0.1476 * sketch_scale)
hole_radius = 0.0234 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .rect(length * sketch_scale, width * sketch_scale)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .pushPoints([hole1_center])
    .hole(2 * hole_radius)
    .faces("<Z")
    .workplane()
    .pushPoints([hole2_center])
    .hole(2 * hole_radius)
    .faces(">Z")
    .workplane()
    .pushPoints([hole3_center])
    .hole(2 * hole_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3331.stl