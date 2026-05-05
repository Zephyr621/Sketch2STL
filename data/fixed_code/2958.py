import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Star-shaped Object ---
sketch_scale = 0.75
# Scaled dimensions
arc_radius1 = 0.0162 * sketch_scale
arc_radius2 = 0.0163 * sketch_scale
arc_radius3 = 0.0162 * sketch_scale
line_length = 0.75 * sketch_scale
line_width = 0.7125 * sketch_scale
extrude_depth = 0.0024
# Create the base shape
base_shape = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius1)
    .threePointArc((arc_radius1, 0), (0.0022 * sketch_scale, 0.0022 * sketch_scale))
    .lineTo(line_length, line_width)
    .lineTo(line_length, line_width + arc_radius1)
    .threePointArc((arc_radius1, line_width + arc_radius1), (0.0022 * sketch_scale, line_width + arc_radius1))
    .close()
)
# Extrude the base shape
part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2958.stl