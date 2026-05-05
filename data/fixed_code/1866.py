import cadquery as cq
from cadquery.vis import show
# --- Part 1: Square Plate ---
sketch_scale = 0.7497
extrude_depth = 0.0144 * sketch_scale
# Scaled dimensions
arc_radius = 0.3598 * sketch_scale
length = 0.7497 * sketch_scale
width = 0.7229 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, arc_radius)
    .threePointArc((arc_radius, 0), (0.0054 * sketch_scale, 0.0054 * sketch_scale))
    .lineTo(length - arc_radius, 0)
    .threePointArc((length, arc_radius), (length - 0.0054 * sketch_scale, 0.0054 * sketch_scale))
    .lineTo(length, width - arc_radius)
    .threePointArc((length - arc_radius, width), (length - 0.0054 * sketch_scale, width - 0.0054 * sketch_scale))
    .lineTo(arc_radius, width)
    .threePointArc((0, width - arc_radius), (0.0054 * sketch_scale, width - 0.0054 * sketch_scale))
    .close()
    .extrude(extrude_depth)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1866.stl