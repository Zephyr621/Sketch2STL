import cadquery as cq
from cadquery import exporters
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.75 * 0.75, 0)
    .lineTo(0.75 * 0.75, 0.225 * 0.75)
    .lineTo(0.525 * 0.75, 0.225 * 0.75)
    .lineTo(0.525 * 0.75, 0.45 * 0.75)
    .lineTo(0, 0.45 * 0.75)
    .close()
    .extrude(0.375/2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Part 2: Rectangular protrusion ---
part_2 = (
    cq.Workplane("XY")
    .rect(0.225 * 0.525, 0.525 * 0.525)
    .extrude(0.225)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_817.stl