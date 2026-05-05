import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Hexagonal Column ---
part_1_scale = 0.75
part_1_height = 0.1462 * 2 # Extrude depth towards and opposite normal
# Scaled dimensions
scaled_x1 = 0.0 * part_1_scale
scaled_y1 = 0.1875 * part_1_scale
scaled_x2 = 0.1875 * part_1_scale
scaled_y2 = 0.0 * part_1_scale
scaled_x3 = 0.5625 * part_1_scale
scaled_y3 = 0.0 * part_1_scale
scaled_x4 = 0.75 * part_1_scale
scaled_y4 = 0.5625 * part_1_scale
scaled_x5 = 0.375 * part_1_scale
scaled_y5 = 0.5625 * part_1_scale
scaled_x6 = 0.0 * part_1_scale
scaled_y6 = 0.625 * part_1_scale
# Create the hexagonal face
hex_face = (
    cq.Workplane("XY")
    .moveTo(scaled_x1, scaled_y1)
    .lineTo(scaled_x2, scaled_y2)
    .lineTo(scaled_x3, scaled_y3)
    .lineTo(scaled_x4
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2291.stl