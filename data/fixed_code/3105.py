import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
sketch_scale = 0.75
extrude_depth = 0.0225 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.4687 * sketch_scale, 0)
    .lineTo(0.4687 * sketch_scale, 0.025 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.025 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.375 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.5625 * sketch_scale)
    .lineTo(0.4687 * sketch_scale, 0.5625 * sketch_scale)
    .lineTo(0.4687 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0.5 * sketch_scale)
    .lineTo(0, 0.5 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3105.stl