import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Bracket ---
sketch_scale = 0.75
extrude_depth = 0.0943 * sketch_scale
hole_radius = 0.0417 * sketch_scale
corner_radius = 0.0833 * sketch_scale
# Scaled hole centers
hole1_center = (0.0383 * sketch_scale, 0.1062 * sketch_scale)
hole2_center = (0.6964 * sketch_scale, 0.1062 * sketch_scale)
hole3_center = (0.6791 * sketch_scale, 0.1062 * sketch_scale)
hole_radius_scaled = hole_radius * sketch_scale
# Create the base shape with rounded edges
part_1 = (
    cq.Workplane("XY")
    .moveTo(corner_radius, 0)
    .lineTo(0.0542 * sketch_scale, 0)
    .threePointArc((0.375 * sketch_scale, corner_radius), (0.6818 * sketch_scale, 0.1289 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.1289 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, corner_radius), (0.6964 * sketch_scale, 0.1062 * sketch_scale))
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_530.stl