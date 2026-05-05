import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.5433
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3214 * sketch_scale)
    .lineTo(0.0471 * sketch_scale, 0.0)
    .lineTo(0.6429 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.3214 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.6429 * sketch_scale)
    .lineTo(0.6146 * sketch_scale, 0.6429 * sketch_scale)
    .lineTo(0.6146 * sketch_scale, 0.3214 * sketch_scale)
    .lineTo(0.4286 * sketch_scale, 0.3214 * sketch_scale)
    .lineTo(0.4286 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.6429 * sketch_scale)
    .lineTo(0.0, 0.6429 * sketch_scale)
    .close()
    .moveTo(0.7143 * sketch_scale,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1742.stl