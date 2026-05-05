import cadquery as cq
from cadquery.vis import show
# --- Part 1: S-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.0197 * sketch_scale
# Scaled coordinates for the outer profile
p1 = (0.0 * sketch_scale, 0.0 * sketch_scale)
p2 = (0.1752 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.3512 * sketch_scale, 0.6382 * sketch_scale)
p4 = (0.1752 * sketch_scale, 0.75 * sketch_scale)
p5 = (0.0 * sketch_scale, 0.75 * sketch_scale)
p6 = (0.0 * sketch_scale, 0.7222 * sketch_scale)
center1 = (0.1752 * sketch_scale, 0.375 * sketch_scale)
center2 = (0.1752 * sketch_scale, 0.5526 * sketch_scale)
center3 = (0.1752 * sketch_scale, 0.75 * sketch_scale)
radius1 = 0.1752 * sketch_scale
radius2 = 0.1752 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc(p2, p3)
    .lineTo(p4[0], p4[1])
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2433.stl