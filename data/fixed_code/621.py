import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Triangle Bracket ---
sketch_scale = 0.75
extrude_depth = 0.0063 * sketch_scale
# Scaled coordinates for the points
p1 = (0.0 * sketch_scale, 0.0636 * sketch_scale)
p2 = (0.0893 * sketch_scale, 0.0568 * sketch_scale)
p3 = (0.6697 * sketch_scale, 0.1049 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.0 * sketch_scale)
p5 = (0.6697 * sketch_scale, 0.1753 * sketch_scale)
p6 = (0.3267 * sketch_scale, 0.1753 * sketch_scale)
p7 = (0.3267 * sketch_scale, 0.5129 * sketch_scale)
p8 = (0.0733 * sketch_scale, 0.5129 * sketch_scale)
p9 = (0.0 * sketch_scale, 0.1665 * sketch_scale)
# Hole parameters (scaled)
hole1_center = (0.0311 * sketch_scale, 0.0489 * sketch_scale)
hole1_radius = 0.0138 * sketch_scale
hole2_center = (0.375 * sketch_scale, 0.1459 * sketch_scale)
hole2_radius = 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_621.stl