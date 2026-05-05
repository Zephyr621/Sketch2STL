import cadquery as cq
from math import radians
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1804)
    .lineTo(0.5625, 0.1804)
    .threePointArc((0.375, 0.0938), (0.2859, 0.1804))
    .lineTo(0.1804, 0.1804)
    .lineTo(0.0, 0.1804)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1489 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_43.stl