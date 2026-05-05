import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.1614 * sketch_scale)
    .threePointArc((0.0486 * sketch_scale, 0.1645 * sketch_scale), (0.1607 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.7446 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7431 * sketch_scale, 0.1645 * sketch_scale), (0.75 * sketch_scale, 0.1614 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.1773 * sketch_scale)
    .threePointArc((0.7431 * sketch_scale, 0.2908 * sketch_scale), (0.7446 * sketch_scale, 0.3333 * sketch_scale))
    .lineTo(0.1607 * sketch_scale, 0.3333 * sketch_scale)
    .threePointArc((0.0486 * sketch_scale, 0.2908 * sketch_scale), (0.0 * sketch_scale, 0.1773 * sketch_scale))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1527.stl