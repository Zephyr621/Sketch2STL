import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1463 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0625 * sketch_scale)
    .threePointArc((0.0562 * sketch_scale, 0.0), (0.0625 * sketch_scale, 0.0625 * sketch_scale))
    .lineTo(0.6875 * sketch_scale, 0.0625 * sketch_scale)
    .threePointArc((0.7083 * sketch_scale, 0.0), (0.75 * sketch_scale, 0.0625 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.2625 * sketch_scale)
    .threePointArc((0.7083 * sketch_scale, 0.1376 * sketch_scale), (0.6875 * sketch_scale, 0.2625 * sketch_scale))
    .lineTo(0.0625 * sketch_scale, 0.2625 * sketch_scale)
    .threePointArc((0.0562 * sketch_scale, 0.1376 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_801.stl