import cadquery as cq
from cadquery.vis import show
# --- Part 1: Wrench Handle ---
sketch_scale = 0.75
extrude_depth = 0.0234 * sketch_scale
# Scaled coordinates for the outer profile
p1 = (0.0 * sketch_scale, 0.1063 * sketch_scale)
p2 = (0.1593 * sketch_scale, 0.0816 * sketch_scale)
p3 = (0.5381 * sketch_scale, 0.1432 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.1957 * sketch_scale)
p5 = (0.6331 * sketch_scale, 0.1258 * sketch_scale)
p6 = (0.1593 * sketch_scale, 0.0 * sketch_scale)
center_x = 0.375 * sketch_scale
center_y = 0.1836 * sketch_scale
radius = 0.0769 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .threePointArc((0.375 * sketch_scale, 0.0 * sketch_scale), (p3[0], p3[
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_332.stl