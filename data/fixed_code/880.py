import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.0297 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.3103 * sketch_scale)
    .threePointArc((0.0047 * sketch_scale, 0.0047 * sketch_scale), (0.0388 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.7496 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7469 * sketch_scale, 0.0047 * sketch_scale), (0.7497 * sketch_scale, 0.1577 * sketch_scale))
    .lineTo(0.7496 * sketch_scale, 0.4699 * sketch_scale)
    .threePointArc((0.7469 * sketch_scale, 0.4465 * sketch_scale), (0.7498 * sketch_scale, 0.4152 * sketch_scale))
    .lineTo(0.0388 * sketch_scale, 0.4152 * sketch_scale)
    .threePointArc((0.0047 * sketch_scale, 0.4465 * sketch_scale), (0.0 * sketch_scale, 0.4699 * sketch_scale))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_880.stl