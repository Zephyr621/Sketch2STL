import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Bar ---
sketch_scale = 0.75
extrude_depth = 0.0179
# Scaled dimensions
arc1_start = (0.0449 * sketch_scale, 0.0313 * sketch_scale)
arc1_mid = (0.0 * sketch_scale, 0.0 * sketch_scale)
arc1_end = (0.7292 * sketch_scale, 0.0313 * sketch_scale)
line1_end = (0.7292 * sketch_scale, 0.0313 * sketch_scale)
line2_end = (0.7292 * sketch_scale, 0.1516 * sketch_scale)
arc2_mid = (0.75 * sketch_scale, 0.1516 * sketch_scale)
arc2_end = (0.7292 * sketch_scale, 0.1405 * sketch_scale)
line3_end = (0.7292 * sketch_scale, 0.1405 * sketch_scale)
line4_end = (0.7292 * sketch_scale, 0.1516 * sketch_scale)
arc3_mid = (0.375 * sketch_scale, 0.1405 * sketch_scale)
arc3_end = (0.0449 * sketch_scale, 0.14
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2193.stl