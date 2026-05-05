import cadquery as cq
from cadquery.vis import show
# --- Part 1: U-shaped Bracket ---
sketch_scale = 0.75
extrude_depth = 0.1765 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.2119 * sketch_scale)
    .lineTo(0.0904 * sketch_scale, 0.2119 * sketch_scale)
    .lineTo(0.0904 * sketch_scale, 0.4773 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.2435 * sketch_scale), (0.7105 * sketch_scale, 0.4773 * sketch_scale))
    .lineTo(0.7105 * sketch_scale, 0.4731 * sketch_scale)
    .lineTo(0.7105 * sketch_scale, 0.4731 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.4731 * sketch_scale)
    .lineTo(0.75 * sketch_scale, 0.2119 * sketch_scale)
    .lineTo(0.6958 * sketch_scale, 0.2119 * sketch_scale)
    .lineTo(0.6958 * sketch_scale, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3294.stl