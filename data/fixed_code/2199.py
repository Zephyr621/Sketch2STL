import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
# Scaled dimensions
arc_1_start = (0.0948 * sketch_scale, 0.0)
arc_1_mid = (0.375 * sketch_scale, 0.0603 * sketch_scale)
arc_1_end = (0.6571 * sketch_scale, 0.0)
arc_2_start = (0.6571 * sketch_scale, 0.0)
arc_2_mid = (0.75 * sketch_scale, 0.0705 * sketch_scale)
arc_2_end = (0.6571 * sketch_scale, 0.1408 * sketch_scale)
arc_3_start = (0.6571 * sketch_scale, 0.1408 * sketch_scale)
arc_3_mid = (0.375 * sketch_scale, 0.0705 * sketch_scale)
arc_3_end = (0.0948 * sketch_scale, 0.1408 * sketch_scale)
arc_4_start = (0.0948 * sketch_scale, 0.1408 * sketch_scale)
arc_4_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2199.stl