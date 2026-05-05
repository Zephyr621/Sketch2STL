import cadquery as cq
# --- Part 1: Pentagonal Prism ---
sketch_scale = 0.75
extrude_depth = 0.03
# Scaled coordinates
p1 = (0.0 * sketch_scale, 0.375 * sketch_scale)
p2 = (0.15 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.6 * sketch_scale, 0.375 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.75 * sketch_scale)
p5 = (0.0 * sketch_scale, 0.375 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .lineTo(p3[0], p3[1])
    .lineTo(p4[0], p4[1])
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.03, 0))
# --- Assembly ---
assembly = part_1
# Export
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_812.stl