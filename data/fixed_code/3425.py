import cadquery as cq
from cadquery.vis import show
# --- Part 1: Pentagon ---
sketch_scale = 0.75
extrude_depth = 0.1095 * sketch_scale
# Scaled coordinates for the outer profile
p1 = (0.0 * sketch_scale, 0.2569 * sketch_scale)
p2 = (0.2776 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.5341 * sketch_scale, 0.0 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.2063 * sketch_scale)
p5 = (0.75 * sketch_scale, 0.5509 * sketch_scale)
p6 = (0.0 * sketch_scale, 0.5509 * sketch_scale)
# Scaled coordinates for the inner profile
inner_profile = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .threePointArc(p3, p4)
    .lineTo(p5[0], p5[1])
    .lineTo(p6[0], p6[1])
    .close()
)
# Extrude the inner profile to create the prism
part_1 = part_1.extrude(extrude_depth)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0,
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3425.stl