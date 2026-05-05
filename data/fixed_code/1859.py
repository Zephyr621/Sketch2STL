import cadquery as cq
from math import *
# --- Part 1: Heart Shape ---
sketch_scale = 0.75
extrude_depth = 0.0115
# Scaled coordinates
arc1_start = (0.0 * sketch_scale, 0.1762 * sketch_scale)
arc1_mid = (0.0344 * sketch_scale, 0.0289 * sketch_scale)
arc1_end = (0.3592 * sketch_scale, 0.0 * sketch_scale)
line1_start = (0.3592 * sketch_scale, 0.0 * sketch_scale)
line1_end = (0.5577 * sketch_scale, 0.1762 * sketch_scale)
arc2_start = (0.5577 * sketch_scale, 0.1762 * sketch_scale)
arc2_mid = (0.7264 * sketch_scale, 0.75 * sketch_scale)
arc2_end = (0.5756 * sketch_scale, 0.5816 * sketch_scale)
arc3_start = (0.5756 * sketch_scale, 0.5816 * sketch_scale)
arc3_mid = (0.6718 * sketch_scale, 0.7304 * sketch_scale)
arc3_end = (0.0528
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1859.stl