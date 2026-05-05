import cadquery as cq
# --- Part 1: L-shaped profile ---
sketch_scale = 0.75
extrude_depth = 0.0171 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5263 * sketch_scale)
    .lineTo(0.0, 0.75 * sketch_scale)
    .lineTo(0.5263 * sketch_scale, 0.75 * sketch_scale)
    .lineTo(0.5263 * sketch_scale, 0.5263 * sketch_scale)
    .lineTo(0.2814 * sketch_scale, 0.5263 * sketch_scale)
    .lineTo(0.2814 * sketch_scale, 0.0)
    .lineTo(0.0937 * sketch_scale, 0.0)
    .lineTo(0.0937 * sketch_scale, 0.1889 * sketch_scale)
    .lineTo(0.1957 * sketch_scale, 0.1889 * sketch_scale)
    .lineTo(0.1957 * sketch_scale, 0.2814 * sketch_scale)
    .lineTo(0.0, 0.2814 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2742.stl