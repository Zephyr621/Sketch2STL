import cadquery as cq
# --- Part 1: U-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.4286 * sketch_scale
# Scaled dimensions
x1 = 0.0 * sketch_scale
y1 = 0.0 * sketch_scale
x2 = 0.5357 * sketch_scale
y2 = 0.0 * sketch_scale
x3 = 0.75 * sketch_scale
y3 = 0.3214 * sketch_scale
x4 = 0.5357 * sketch_scale
y4 = 0.3214 * sketch_scale
x5 = 0.0 * sketch_scale
y5 = 0.3214 * sketch_scale
x6 = 0.5357 * sketch_scale
y6 = 0.3214 * sketch_scale
x7 = 0.75 * sketch_scale
y7 = 0.3314 * sketch_scale
x8 = 0.5357 * sketch_scale
y8 = 0.3314 * sketch_scale
x9 = 0.75 * sketch_scale
y9 = 0.3214 * sketch_scale
x10 = 0.5357 * sketch_scale
y10 = 0.3314 * sketch_scale
x11 = 0.5357 * sketch_scale
y11 = 0.3214 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1830.stl