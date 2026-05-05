import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0075 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.2508 * sketch_scale)
    .lineTo(0.0104 * sketch_scale, 0.2508 * sketch_scale)
    .lineTo(0.0104 * sketch_scale, 0.5294 * sketch_scale)
    .lineTo(0.7125 * sketch_scale, 0.5294 * sketch_scale)
    .lineTo(0.7125 * sketch_scale, 0.1296 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.1296 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.7125 * sketch_scale, 0.0)
    .lineTo(0.7125 * sketch_scale, 0.2508 * sketch_scale)
    .lineTo(0.0104 * sketch_scale, 0.2508 * sketch_scale)
    .lineTo(0.0104 * sketch_scale, 0.5294 * sketch_scale)
    .lineTo(0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2716.stl