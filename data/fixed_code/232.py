import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.45
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.5625 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.5625 * sketch_scale, 0.375 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.375 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.0, 0.1875 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .moveTo(0.0938 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.1875 * sketch_scale)
    .lineTo(0.1875 * sketch_scale, 0.3125 * sketch
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_232.stl