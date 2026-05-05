import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0938 * sketch_scale
# Scaled dimensions
x1 = 0.0 * sketch_scale
y1 = 0.0 * sketch_scale
x2 = 0.125 * sketch_scale
y2 = 0.0 * sketch_scale
x3 = 0.625 * sketch_scale
y3 = 0.0 * sketch_scale
x4 = 0.75 * sketch_scale
y4 = 0.5 * sketch_scale
x5 = 0.625 * sketch_scale
y5 = 0.5 * sketch_scale
center1 = (0.25 * sketch_scale, 0.25 * sketch_scale)
center2 = (0.625 * sketch_scale, 0.25 * sketch_scale)
radius = 0.0625 * sketch_scale
# Create the L-shape profile
part_1 = (
    cq.Workplane("XY")
    .moveTo(x1, y1)
    .lineTo(x2, y2)
    .lineTo(x3, y3)
    .lineTo(x4, y4)
    .lineTo(x5, y5)
    .lineTo(x1, y5)
    .close()
    .moveTo(
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1882.stl