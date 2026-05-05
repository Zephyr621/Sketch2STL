import cadquery as cq
from math import tan, radians
# --- Part 1: Hexagonal Prism ---
sketch_scale = 0.1425
# Scaled dimensions
scaled_x1 = 0.0 * sketch_scale
scaled_y1 = 0.0521 * sketch_scale
scaled_x2 = 0.0703 * sketch_scale
scaled_y2 = 0.0 * sketch_scale
scaled_x3 = 0.1425 * sketch_scale
scaled_y3 = 0.0 * sketch_scale
scaled_x4 = 0.1193 * sketch_scale
scaled_y4 = 0.1071 * sketch_scale
scaled_x5 = 0.1295 * sketch_scale
scaled_y5 = 0.1364 * sketch_scale
scaled_x6 = 0.0 * sketch_scale
scaled_y6 = 0.1295 * sketch_scale
scaled_x7 = 0.1425 * sketch_scale
scaled_y7 = 0.1364 * sketch_scale
scaled_x8 = 0.1425 * sketch_scale
scaled_y8 = 0.1071 * sketch_scale
extrude_depth = 0.75
# Create the hexagon
hexagon = (
    cq.Workplane("XY")
    .moveTo(scaled_x1, scaled_y1)
    .lineTo(scaled_x2, scaled_y2)
    .lineTo(scaled_x3, scaled_y3)
    .lineTo(scaled_x4
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1396.stl