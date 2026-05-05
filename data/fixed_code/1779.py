import cadquery as cq
from math import radians
# --- Part 1: Rectangular Box with Curved Top ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.0375 * 0.75), (0.5 * 0.75, 0.0625 * 0.75))
    .lineTo(0.0, 0.0625 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4412)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4412, 0))
# --- Part 2: Cube ---
part_2_size = 0.5625 * 0.5625
part_2 = cq.Workplane("XY").box(part_2_size, part_2
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1779.stl