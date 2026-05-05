import cadquery as cq
from math import *
# --- Parameters from JSON ---
sketch_scale = 0.75
height = 0.3214
width = 0.6495
length = 0.75
thickness = 0.1607
# Scaled dimensions
scaled_x1 = 0.0 * sketch_scale
scaled_y1 = 0.3248 * sketch_scale
scaled_x2 = 0.1875 * sketch_scale
scaled_y2 = 0.0 * sketch_scale
scaled_x3 = 0.5625 * sketch_scale
scaled_y3 = 0.0 * sketch_scale
scaled_x4 = 0.75 * sketch_scale
scaled_y4 = 0.6495 * sketch_scale
scaled_x5 = 0.5625 * sketch_scale
scaled_y5 = 0.6495 * sketch_scale
scaled_x6 = 0.1875 * sketch_scale
scaled_y6 = 0.6495 * sketch_scale
# --- Create the Hexagon ---
hexagon = (
    cq.Workplane("XY")
    .moveTo(scaled_x1, scaled_y1)
    .lineTo(scaled_x2, scaled_y2)
    .lineTo(scaled_x3, scaled_y3)
    .lineTo(scaled_x4, scaled_y4)
    .lineTo(scaled_x5, scaled_y5)
    .lineTo(scaled_x6, scaled_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3355.stl