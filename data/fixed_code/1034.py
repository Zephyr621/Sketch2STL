import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Block with Cutout ---
length = 0.75
width = 0.2893
height = 0.2709
sketch_scale = 0.75
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
hole1_x = 0.1406 * sketch_scale
hole1_y = 0.0446 * sketch_scale
hole2_x = 0.6066 * sketch_scale
hole2_y = 0.0 * sketch_scale
hole3_x = 0.7031 * sketch_scale
hole3_y = 0.0446 * sketch_scale
hole4_x = 0.6048 * sketch_scale
hole4_y = 0.0446 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .rect(scaled_length, scaled_width)
    .extrude(scaled_height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - scaled_length/2, hole1_y - scaled_width/2), (hole2_x - scaled_length/2, hole2_y - scaled_width/2), (hole3_x - scaled_length/2, hole3_y
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1034.stl