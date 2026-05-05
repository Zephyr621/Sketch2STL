import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.625
# Scaled dimensions
x1 = 0.0 * sketch_scale
y1 = 0.25 * sketch_scale
x2 = 0.75 * sketch_scale
y2 = 0.125 * sketch_scale
x3 = 0.25 * sketch_scale
y3 = 0.375 * sketch_scale
x4 = 0.25 * sketch_scale
y4 = 0.5 * sketch_scale
x5 = 0.0 * sketch_scale
y5 = 0.5 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(x1, y1)
    .lineTo(x2, y1)
    .lineTo(x2, y2)
    .lineTo(x3, y2)
    .lineTo(x3, y3)
    .lineTo(x4, y3)
    .lineTo(x4, y4)
    .lineTo(x1, y4)
    .close()
    .moveTo(x2, y2)
    .lineTo(x3, y3)
    .lineTo(x3, y4)
    .lineTo(x2, y4)
    .lineTo(x2, y
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1032.stl