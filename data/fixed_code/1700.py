import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .threePointArc((0.5609 * 0.75, 0.1154 * 0.75), (0.75 * 0.75, 0.1883 * 0.75))
    .lineTo(0.75 * 0.75, 0.2679 * 0.75)
    .threePointArc((0.5609 * 0.75, 0.1356 * 0.75), (0.375 * 0.75, 0.1336 * 0.75))
    .lineTo(0.0, 0.1336 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2143)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2143, 0))
# --- Assembly ---
assembly = part_1
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1700.stl