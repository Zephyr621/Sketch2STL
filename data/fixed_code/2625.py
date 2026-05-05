import cadquery as cq
from math import radians
# --- Part 1: U-shaped Object ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.4342 * 0.75)
    .lineTo(0.4342 * 0.75, 0.5192 * 0.75)
    .lineTo(0.75 * 0.75, 0.5192 * 0.75)
    .lineTo(0.75 * 0.75, 0.2085 * 0.75)
    .lineTo(0.375 * 0.75, 0.2085 * 0.75)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.3354 * 0.75, 0.0)
    .lineTo(0.3354 * 0.75, 0.4342 * 0.75)
    .close()
    .extrude(0.0441)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2625.stl