import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0469 * 0.75, 0.0)
    .lineTo(0.746 * 0.75, 0.0)
    .threePointArc((0.7457 * 0.75, 0.0089 * 0.75), (0.746 * 0.75, 0.5196 * 0.75))
    .lineTo(0.0469 * 0.75, 0.75 * 0.75)
    .lineTo(0.0469 * 0.75, 0.5833 * 0.75)
    .threePointArc((0.0156 * 0.75, 0.6741 * 0.75), (0.0469 * 0.75, 0.5833 * 0.75))
    .lineTo(0.0469 * 0.75, 0.4891 * 0.75)
    .threePointArc((0.0157 * 0.75, 0.7448 * 0.75), (0.0469 * 0.75, 0.7455 * 0.75))
    .lineTo(0.0469 * 0.75, 0.6897 * 0.75)
    .threePoint
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_606.stl