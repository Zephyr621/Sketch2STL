import cadquery as cq
from math import *
# --- Part 1: Bracket ---
length = 0.75
width = 0.5
height = 0.0159
sketch_scale = 0.75
# Scaled dimensions
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
scaled_height = height
# Hole parameters (scaled)
hole1_center = (0.0305 * sketch_scale, 0.0625 * sketch_scale)
hole2_center = (0.7098 * sketch_scale, 0.0625 * sketch_scale)
hole3_center = (0.6951 * sketch_scale, 0.0625 * sketch_scale)
hole4_center = (0.6896 * sketch_scale, 0.0625 * sketch_scale)
hole5_center = (0.6611 * sketch_scale, 0.0625 * sketch_scale)
hole6_center = (0.6786 * sketch_scale, 0.0625 * sketch_scale)
hole7_center = (0.6947 * sketch_scale, 0.0625 * sketch_scale)
hole8_center = (0.6563 * sketch_scale, 0.0625 * sketch_scale)
#
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_506.stl