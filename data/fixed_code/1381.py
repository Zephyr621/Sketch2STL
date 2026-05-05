import cadquery as cq
from cadquery.vis import show
# --- Part 1: Hook ---
sketch_scale = 0.75
extrude_depth = 0.0926 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.1429 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.2037 * sketch_scale), (0.5735 * sketch_scale, 0.0))
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.3173 * sketch_scale)
    .lineTo(0.6089 * sketch_scale, 0.3173 * sketch_scale)
    .threePointArc((0.375 * sketch_scale, 0.4506 * sketch_scale), (0.2893 * sketch_scale, 0.3173 * sketch_scale))
    .lineTo(0.1827 * sketch_scale, 0.3173 * sketch_scale)
    .lineTo(0.1786 * sketch_scale, 0.3173 * sketch_scale)
    .threePointArc((0.0, 0.2037 * sketch_scale), (0.0, 0.0))
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1381.stl