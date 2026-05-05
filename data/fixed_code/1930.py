import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Bar with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.0818 * sketch_scale
height = 0.0402
radius = 0.0083 * sketch_scale
corner_radius = 0.0106 * sketch_scale
hole_center_x1 = 0.0106 * sketch_scale
hole_center_x2 = 0.7052 * sketch_scale
hole_center_y = 0.0106 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(hole_center_x1, hole_center_y)
    .lineTo(hole_center_x2, hole_center_y)
    .threePointArc((hole_center_x2 + corner_radius, hole_center_y), (hole_center_x2, width))
    .lineTo(hole_center_x1, width)
    .threePointArc((hole_center_x1 - corner_radius, hole_center_y), (hole_center_x1, width))
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1930.stl