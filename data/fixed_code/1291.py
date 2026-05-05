import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.6342
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.2455 * sketch_scale)
    .threePointArc((0.0089 * sketch_scale, 0.0089 * sketch_scale), (0.2455 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.4837 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7494 * sketch_scale, 0.0089 * sketch_scale), (0.75 * sketch_scale, 0.2455 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.6225 * sketch_scale)
    .threePointArc((0.7494 * sketch_scale, 0.6252 * sketch_scale), (0.4837 * sketch_scale, 0.6225 * sketch_scale))
    .lineTo(0.2455 * sketch_scale, 0.6225 * sketch_scale)
    .threePointArc((0.0089 * sketch_scale, 0.6252 * sketch_scale), (0.0 * sketch_scale, 0.6225 * sketch_scale))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1291.stl