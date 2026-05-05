import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.5
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.0 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.5625 * sketch_scale)
    .lineTo(0.0 * sketch_scale, 0.5625 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# Create the cutout feature
cutout_feature = (
    cq.Workplane("XY")
    .moveTo(0.1875 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.375 * sketch_scale, 0.5625 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.5625 * sketch_scale)
    .close()
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3583.stl