import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Holes ---
sketch_scale = 0.75
extrude_depth = 0.0127 * sketch_scale
# Scaled dimensions
arc_start_x = 0.1353 * sketch_scale
arc_mid_y1 = 0.1531 * sketch_scale
arc_end_x = 0.5151 * sketch_scale
arc_mid_y2 = 0.0 * sketch_scale
arc_end_y = 0.3879 * sketch_scale
arc_end_x2 = 0.6186 * sketch_scale
arc_mid_y3 = 0.4687 * sketch_scale
arc_end_y2 = 0.4597 * sketch_scale
arc_end_x3 = 0.5893 * sketch_scale
arc_mid_y4 = 0.6196 * sketch_scale
hole_center_x = 0.5151 * sketch_scale
hole_center_y = 0.1531 * sketch_scale
hole_radius = 0.0476 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(arc_start_x, arc_start_y)
    .threePointArc((arc_mid_y1, arc_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2141.stl