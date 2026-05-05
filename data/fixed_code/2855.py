import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1592 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0477 * sketch_scale, 0.1826 * sketch_scale)
    .threePointArc((0.0, 0.3796 * sketch_scale), (0.0477 * sketch_scale, 0.3177 * sketch_scale))
    .lineTo(0.4773 * sketch_scale, 0.3177 * sketch_scale)
    .threePointArc((0.4799 * sketch_scale, 0.375 * sketch_scale), (0.75 * sketch_scale, 0.1826 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.6667 * sketch_scale, 0.0)
    .threePointArc((0.7333 * sketch_scale, 0.1953 * sketch_scale), (0.5881 * sketch_scale, 0.1953 * sketch_scale))
    .lineTo(0.5881 * sketch_scale, 0.2845 * sketch_scale)
    .threePointArc((0.4682 * sketch_scale
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2855.stl