import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.1
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1, 0))
# --- Part 2: Curved Shape ---
sketch_scale = 0.5
# Scaled coordinates
p1 = (0.0 * sketch_scale, 0.15 * sketch_scale)
p2 = (0.25 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.5 * sketch_scale, 0.15 * sketch_scale)
p4 = (0.5 * sketch_scale, 0.5 * sketch_scale)
p5 = (0.0 * sketch_scale, 0.5 * sketch_scale)
part_2 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .threePointArc(p2, p3)
    .lineTo(p4[0], p4[1])
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_79.stl