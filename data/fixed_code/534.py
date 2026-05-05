import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Triangle Bracket ---
sketch_scale = 0.75
extrude_depth = 0.0547 * sketch_scale
# Scaled coordinates
p1 = (0.0 * sketch_scale, 0.1556 * sketch_scale)
p2 = (0.1358 * sketch_scale, 0.1866 * sketch_scale)
p3 = (0.4392 * sketch_scale, 0.0 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.0961 * sketch_scale)
p5 = (0.6321 * sketch_scale, 0.0857 * sketch_scale)
p6 = (0.3746 * sketch_scale, 0.2316 * sketch_scale)
p7 = (0.2422 * sketch_scale, 0.1179 * sketch_scale)
p8 = (0.1202 * sketch_scale, 0.2634 * sketch_scale)
hole1_center = (0.0951 * sketch_scale, 0.1556 * sketch_scale)
hole2_center = (0.5986 * sketch_scale, 0.1556 * sketch_scale)
hole3_center = (0.6593 * sketch_scale, 0.1866 * sketch_scale)
hole_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_534.stl