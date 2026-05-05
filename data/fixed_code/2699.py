import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0517 * 0.75)
    .lineTo(0.0354 * 0.75, 0.0)
    .lineTo(0.7359 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.0484 * 0.75), (0.6958 * 0.75, 0.1538 * 0.75))
    .lineTo(0.7265 * 0.75, 0.3889 * 0.75)
    .threePointArc((0.7267 * 0.75, 0.3734 * 0.75), (0.6835 * 0.75, 0.3946 * 0.75))
    .lineTo(0.1051 * 0.75, 0.4547 * 0.75)
    .threePointArc((0.0183 * 0.75, 0.4481 * 0.75), (0.0, 0.0517 * 0.75))
    .close()
    .extrude(-0.1631)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2699.stl