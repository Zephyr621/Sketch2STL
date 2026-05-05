import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: L-shaped Bracket ---
sketch_scale = 0.75
extrude_depth = 0.0938 * sketch_scale
# Scaled dimensions
x1 = 0.0 * sketch_scale
y1 = 0.1875 * sketch_scale
x2 = 0.5625 * sketch_scale
y2 = 0.0 * sketch_scale
x3 = 0.75 * sketch_scale
y3 = 0.1875 * sketch_scale
x4 = 0.5625 * sketch_scale
y4 = 0.4687 * sketch_scale
x5 = 0.75 * sketch_scale
y5 = 0.4688 * sketch_scale
x6 = 0.1875 * sketch_scale
y6 = 0.4688 * sketch_scale
# Hole centers (scaled)
hole1_center = (0.1312 * sketch_scale - y1, 0.125 * sketch_scale - y2)
hole2_center = (0.6151 * sketch_scale - y1, 0.125 * sketch_scale - y2)
hole3_center = (0.6151 * sketch_scale - y1, 0.625 * sketch_scale - y2)
hole_radius = 0.0312 * sketch_scale
# Create the L-shape profile
part_1 = (
    cq.Workplane("XY")
    .moveTo(x1, y1)
    .lineTo(x2, y1)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_623.stl