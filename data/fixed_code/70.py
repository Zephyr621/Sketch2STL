import cadquery as cq
from math import radians
# --- Part 1: Triangular Prism ---
part_1_scale = 0.4688
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4688 * part_1_scale, 0.0)
    .lineTo(0.4687 * part_1_scale, 0.4544 * part_1_scale)
    .lineTo(0.0, 0.4687 * part_1_scale)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
#
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_70.stl