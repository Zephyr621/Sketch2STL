import cadquery as cq
from cadquery.vis import show
# --- Part 1: Ring-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.0804 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0583 * sketch_scale)
    .threePointArc((0.0147 * sketch_scale, 0.0147 * sketch_scale), (0.0583 * sketch_scale, 0.0))
    .lineTo(0.6649 * sketch_scale, 0.0)
    .threePointArc((0.7382 * sketch_scale, 0.0147 * sketch_scale), (0.75 * sketch_scale, 0.0583 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.6429 * sketch_scale)
    .threePointArc((0.7382 * sketch_scale, 0.6429 * sketch_scale), (0.6649 * sketch_scale, 0.6429 * sketch_scale))
    .lineTo(0.0583 * sketch_scale, 0.6429 * sketch_scale)
    .threePointArc((0.0147 * sketch_scale, 0.6429 * sketch_scale), (0.0, 0.6429 * sketch_scale))
    .lineTo(0.0, 0.0583 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_846.stl