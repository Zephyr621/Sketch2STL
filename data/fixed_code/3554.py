import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Curved Top ---
sketch_scale = 0.75
extrude_depth = 0.45 * sketch_scale
# Scaled dimensions for the outer profile
outer_radius = 0.375 * sketch_scale
inner_radius = 0.225 * sketch_scale
line_start_x = 0.375 * sketch_scale
line_end_x = 0.75 * sketch_scale
arc_mid_y = 0.375 * sketch_scale
arc_end_y = 0.375 * sketch_scale
line2_end_x = 0.75 * sketch_scale
line2_end_y = 0.375 * sketch_scale
arc2_mid_x = 0.375 * sketch_scale
arc2_mid_y = 0.75 * sketch_scale
line2_end_x = 0.375 * sketch_scale
line2_end_y = 0.525 * sketch_scale
line3_end_x = 0.0 * sketch_scale
line3_end_y = 0.525 * sketch_scale
# Create the outer profile
outer_profile = (
    cq.Workplane("XY")
    .moveTo(line_start_x, line_end_y)
    .threePointArc((arc_mid_x, arc_mid_y), (line_start_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3554.stl