import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Hexagonal Ring ---
sketch_scale = 0.75
height = 0.1636
# Scaled coordinates for the outer hexagon
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3248 * sketch_scale),
    (0.5625 * sketch_scale, 0.6495 * sketch_scale),
    (0.1875 * sketch_scale, 0.6495 * sketch_scale)
]
# Scaled circle parameters
circle1_center = (0.2812 * sketch_scale, 0.3248 * sketch_scale)
circle2_center = (0.375 * sketch_scale, 0.6495 * sketch_scale)
circle3_center = (0.5303 * sketch_scale, 0.3248 * sketch_scale)
circle4_center = (0.5563 * sketch_scale, 0.3248 * sketch_scale)
circle5_center =
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3475.stl