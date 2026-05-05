import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.3981 * sketch_scale
# Scaled dimensions
p1 = (0.0 * sketch_scale, 0.2982 * sketch_scale)
p2 = (0.2812 * sketch_scale, 0.0 * sketch_scale)
p3 = (0.7395 * sketch_scale, 0.1488 * sketch_scale)
p4 = (0.75 * sketch_scale, 0.4687 * sketch_scale)
p5 = (0.3717 * sketch_scale, 0.4615 * sketch_scale)
p6 = (0.0 * sketch_scale, 0.4615 * sketch_scale)
part_1 = (
    cq.Workplane("XY")
    .moveTo(p1[0], p1[1])
    .lineTo(p2[0], p2[1])
    .lineTo(p3[0], p3[1])
    .lineTo(p4[0], p4[1])
    .lineTo(p5[0], p5[1])
    .lineTo(p6[0], p6[1])
    .close()
    .moveTo(p6[0], p6[1])
    .circle(0.0785 * sketch_scale)
    .extr
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1473.stl