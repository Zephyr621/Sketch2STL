import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0348 * 0.75)
    .lineTo(0.7059 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.1797 * 0.75), (0.7059 * 0.75, 0.3394 * 0.75))
    .lineTo(0.0, 0.3394 * 0.75)
    .lineTo(0.0, 0.0348 * 0.75)
    .close()
    .extrude(0.3643 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3643 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1521.stl