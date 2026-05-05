import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Cutout ---
sketch_scale = 0.75
extrude_depth = 0.0208 * sketch_scale
# Scaled dimensions
x1 = 0.0 * sketch_scale
y1 = 0.0 * sketch_scale
x2 = 0.6867 * sketch_scale
y2 = 0.0 * sketch_scale
x3 = 0.75 * sketch_scale
y3 = 0.0 * sketch_scale
x4 = 0.6867 * sketch_scale
y4 = 0.3409 * sketch_scale
x5 = 0.0 * sketch_scale
y5 = 0.3409 * sketch_scale
x6 = 0.0 * sketch_scale
y6 = 0.3409 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(x1, y1)
    .lineTo(x2, y2)
    .lineTo(x3, y3)
    .lineTo(x4, y4)
    .threePointArc((x5, y5), (x6, y6))
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_449.stl