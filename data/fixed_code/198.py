import cadquery as cq
from math import tan, radians
# --- Part 1: Octagonal Prism ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1875 * 0.75)
    .lineTo(0.3248 * 0.75, 0.0)
    .lineTo(0.6495 * 0.75, 0.1875 * 0.75)
    .lineTo(0.6495 * 0.75, 0.5625 * 0.75)
    .lineTo(0.3248 * 0.75, 0.75 * 0.75)
    .lineTo(0.0, 0.5625 * 0.75)
    .close()
    .extrude(0.2537)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2537, 0))
# --- Part 2: Rectangular Plate ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.375 * 0.75)
    .lineTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_198.stl