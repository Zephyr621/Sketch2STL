import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75  # Scaled width
part_1_height = 0.0188
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Holes ---
hole_radius = 0.0094 * 0.7188  # Scaled radius
hole_depth = 0.0112
# Hole centers (scaled and translated)
hole1_x = 0.0149 * 0.7188 - part_1_length/2
hole1_y = 0.0149 * 0.7188 - part_1_width/2
hole2_x = 0.7319 * 0.7188 - part_1_length/2
hole2_y = 0.0149 * 0.7188 - part_1_width/2
part_2 = (
    cq.Workplane("XY")
    .pushPoints([(hole1_x, hole1_y), (hole2_x, hole2_y)])
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2274.stl