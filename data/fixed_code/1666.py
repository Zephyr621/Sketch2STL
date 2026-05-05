import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0375 * 0.75)
    .threePointArc((0.0063 * 0.75, 0.0063 * 0.75), (0.0375 * 0.75, 0.0))
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1231 * 0.75)
    .lineTo(0.6958 * 0.75, 0.1231 * 0.75)
    .lineTo(0.6958 * 0.75, 0.3488 * 0.75)
    .lineTo(0.7187 * 0.75, 0.3488 * 0.75)
    .lineTo(0.7187 * 0.75, 0.2625 * 0.75)
    .threePointArc((0.7399 * 0.75, 0.3347 * 0.75), (0.7399 * 0.75, 0.3 * 0.75))
    .lineTo(0.0375 * 0.75, 0.3 * 0.75)
    .lineTo(0.0375 * 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1666.stl