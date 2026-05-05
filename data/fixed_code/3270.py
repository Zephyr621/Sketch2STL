import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.2308 * sketch_scale
# Scaled dimensions
width = 0.75 * sketch_scale
height = 0.4687 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(width, 0)
    .lineTo(width, height)
    .lineTo(0.375 * sketch_scale, height)
    .lineTo(0.375 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.5625 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.5625 * sketch_scale, height)
    .lineTo(0, height)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3270.stl