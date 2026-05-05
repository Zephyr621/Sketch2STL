import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Rectangular Base ---
part_1_radius = 0.0625 * 0.75  # Sketch radius scaled
part_1_height = 0.125
cylinder_1_x = 0.0625 * 0.75
cylinder_1_y = 0.0625 * 0.75
cylinder_2_x = 0.6875 * 0.75
cylinder_2_y = 0.0625 * 0.75
cylinder_3_x = 0.6875 * 0.75
cylinder_3_y = 0.0625 * 0.75
cylinder_4_x = 0.6875 * 0.75
cylinder_4_y = 0.0625 * 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(cylinder_1_x, 0)
    .lineTo(cylinder_1_x, part_1_radius)
    .lineTo(cylinder_2_x, part_1_radius)
    .lineTo(cylinder_2_x, cylinder_2_y)
    .lineTo(0, cylinder_2_y)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3204.stl