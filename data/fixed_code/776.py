import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1835)
    .threePointArc((0.5586, 0.1346), (0.5625, 0.1765))
    .lineTo(0.375, 0.1765)
    .lineTo(0.375, 0.0625)
    .lineTo(0.0, 0.0625)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0978 + 0.0978)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1838, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_776.stl