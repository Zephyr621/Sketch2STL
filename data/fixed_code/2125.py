import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.3125
# Scaled dimensions
x1 = 0.0 * sketch_scale
y1 = 0.75 * sketch_scale
x2 = 0.1875 * sketch_scale
y2 = 0.0 * sketch_scale
x3 = 0.5625 * sketch_scale
y3 = 0.75 * sketch_scale
x4 = 0.375 * sketch_scale
y4 = 0.75 * sketch_scale
x5 = 0.5625 * sketch_scale
y5 = 0.0 * sketch_scale
x6 = 0.75 * sketch_scale
y6 = 0.75 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(x1, y1)
    .lineTo(x2, y2)
    .lineTo(x3, y3)
    .lineTo(x4, y4)
    .lineTo(x5, y5)
    .lineTo(x6, y6)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2125.stl