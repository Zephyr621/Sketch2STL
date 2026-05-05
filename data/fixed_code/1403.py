import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1071
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0621 * sketch_scale)
    .lineTo(0.0621 * sketch_scale, 0.0 * sketch_scale)
    .lineTo(0.5938 * sketch_scale, 0.0 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.0621 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.2761 * sketch_scale)
    .lineTo(0.5938 * sketch_scale, 0.3571 * sketch_scale)
    .lineTo(0.6964 * sketch_scale, 0.3571 * sketch_scale)
    .lineTo(0.6964 * sketch_scale, 0.2357 * sketch_scale)
    .lineTo(0.0542 * sketch_scale, 0.2357 * sketch_scale)
    .lineTo(0.0542 * sketch_scale, 0.0914 * sketch_scale)
    .lineTo(0.0 * sketch_scale, 0.0914 * sketch_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1403.stl