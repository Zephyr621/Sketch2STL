import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.375
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * sketch_scale, 0.0)
    .lineTo(0.25 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.5 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.5 * sketch_scale, 0.25 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.25 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.625 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.625 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.0, 0.0)
    .close()
    .moveTo(0.125 * sketch_scale, 0.0625 * sketch_scale)
    .circle(0.0562 * sketch_scale)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2886.stl