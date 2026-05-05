import cadquery as cq
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1251 * 0.75)
    .lineTo(0.5357 * 0.75, 0.1251 * 0.75)
    .lineTo(0.5357 * 0.75, 0.2586 * 0.75)
    .lineTo(0.2344 * 0.75, 0.2586 * 0.75)
    .lineTo(0.2344 * 0.75, 0.1251 * 0.75)
    .lineTo(0.0, 0.1251 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.375/2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2133.stl