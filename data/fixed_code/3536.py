import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder with Rectangular Slit ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.75 * sketch_scale
height = 0.5581
arc1_start = (0.1749 * sketch_scale, 0.0903 * sketch_scale)
arc1_mid = (0.375 * sketch_scale, 0.0303 * sketch_scale)
arc1_end = (0.5751 * sketch_scale, 0.0903 * sketch_scale)
line1_end = (0.5751 * sketch_scale, 0.6562 * sketch_scale)
line2_end = (0.5751 * sketch_scale, 0.75 * sketch_scale)
line3_end = (0.1749 * sketch_scale, 0.75 * sketch_scale)
arc2_start = (0.1749 * sketch_scale, 0.75 * sketch_scale)
arc2_mid = (0.0 * sketch_scale, 0.6989 * sketch_scale)
arc2_end = (0.1749 * sketch_scale, 0.6562 * sketch_scale)
line4_end = (0.1749 * sketch_scale, 0.6562 * sketch_scale)
line5_end = (0.1749 * sketch_scale, 0.6562 * sketch_scale)
circle_center = (0.375 * sketch_scale, 0.675 * sketch_scale)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3536.stl