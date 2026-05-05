import cadquery as cq
# --- Part 1: U-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.4342 * sketch_scale
# Scaled coordinates
p1 = (0.0 * sketch_scale, 0.2386 * sketch_scale)
p2 = (0.0 * sketch_scale, 0.3214 * sketch_scale)
p3 = (0.7222 * sketch_scale, 0.3343 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.3214 * sketch_scale)
p5 = (0.75 * sketch_scale, 0.4342 * sketch_scale)
p6 = (0.0234 * sketch_scale, 0.4342 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .lineTo(p3[0], p3[1])
    .lineTo(p4[0], p4[1])
    .lineTo(p5[0], p5[1])
    .lineTo(p6[0], p6[1])
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3024.stl