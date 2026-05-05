import cadquery as cq
from math import radians
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1031 * 0.75)
    .lineTo(0.3281 * 0.75, 0.1031 * 0.75)
    .threePointArc((0.1667 * 0.75, 0.0803 * 0.75), (0.0469 * 0.75, 0.0562 * 0.75))
    .lineTo(0.0234 * 0.75, 0.0562 * 0.75)
    .threePointArc((0.0056 * 0.75, 0.0803 * 0.75), (0.0, 0.1031 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2812)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2812, 0))
# --- Assembly ---
assembly = part_1
cq.
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_378.stl