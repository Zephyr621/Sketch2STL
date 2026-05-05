import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: U-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.3373 * sketch_scale
# Scaled coordinates for the base profile
p0 = (0.0 * sketch_scale, 0.1132 * sketch_scale)
p1 = (0.0493 * sketch_scale, 0.1249 * sketch_scale)
p2 = (0.7159 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.75 * sketch_scale, 0.0298 * sketch_scale)
p4 = (0.7159 * sketch_scale, 0.4439 * sketch_scale)
p5 = (0.4709 * sketch_scale, 0.4439 * sketch_scale)
p6 = (0.4709 * sketch_scale, 0.1607 * sketch_scale)
p7 = (0.375 * sketch_scale, 0.2308 * sketch_scale)
p8 = (0.2429 * sketch_scale, 0.2274 * sketch_scale)
p9 = (0.1552 * sketch_scale, 0.1917 * sketch_scale)
p10 = (0.0863 * sketch_scale, 0.2288 * sketch_scale)
p11 = (0.0 * sketch_scale, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3321.stl