import cadquery as cq
from math import radians
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3439 * 0.3439, 0.0)
    .lineTo(0.3439 * 0.3439, 0.0271 * 0.3439)
    .lineTo(0.2445 * 0.3439, 0.0271 * 0.3439)
    .lineTo(0.2445 * 0.3439, 0.1981 * 0.3439)
    .lineTo(0.0, 0.1981 * 0.3439)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75 * 0.3439)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2 ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.1429 * 0.1429, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1033.stl