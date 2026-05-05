import cadquery as cq
from cadquery.vis import show
# --- Part 1: S-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.2454
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4286 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.1765 * sketch_scale), (0.4286 * sketch_scale, 0.3489 * sketch_scale))
    .lineTo(0.2143 * sketch_scale, 0.3489 * sketch_scale)
    .lineTo(0.2143 * sketch_scale, 0.3938 * sketch_scale)
    .lineTo(0.3145 * sketch_scale, 0.3938 * sketch_scale)
    .lineTo(0.3145 * sketch_scale, 0.1229 * sketch_scale)
    .threePointArc((0.2885 * sketch_scale, 0.1446 * sketch_scale), (0.2082 * sketch_scale, 0.1941 * sketch_scale))
    .lineTo(0.0, 0.1807 * sketch_scale)
    .lineTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_642.stl