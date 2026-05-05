import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.15
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0816 * sketch_scale)
    .lineTo(0.0262 * sketch_scale, 0.0816 * sketch_scale)
    .lineTo(0.0262 * sketch_scale, 0.0231 * sketch_scale)
    .lineTo(0.7295 * sketch_scale, 0.0231 * sketch_scale)
    .lineTo(0.7295 * sketch_scale, 0.0586 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.0586 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.0231 * sketch_scale)
    .lineTo(0.7295 * sketch_scale, 0.0231 * sketch_scale)
    .lineTo(0.7295 * sketch_scale, 0.1619 * sketch_scale)
    .lineTo(0.0 * sketch_scale, 0.1619 * sketch_scale)
    .lineTo(0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1479.stl