import cadquery as cq
from cadquery.vis import show
# --- Part 1: S-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.0825 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0156 * sketch_scale)
    .threePointArc((0.0027 * sketch_scale, 0.0027 * sketch_scale), (0.0156 * sketch_scale, 0.0))
    .lineTo(0.7187 * sketch_scale, 0.0)
    .threePointArc((0.7455 * sketch_scale, 0.0027 * sketch_scale), (0.75 * sketch_scale, 0.0156 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.35 * sketch_scale)
    .threePointArc((0.7455 * sketch_scale, 0.3348 * sketch_scale), (0.7187 * sketch_scale, 0.3478 * sketch_scale))
    .lineTo(0.0156 * sketch_scale, 0.3478 * sketch_scale)
    .threePointArc((0.0027 * sketch_scale, 0.3348 * sketch_scale), (0.0, 0.35 * sketch_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1324.stl