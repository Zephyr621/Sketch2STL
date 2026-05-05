import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.0656 * 0.1316  # Sketch radius scaled
part_1_height = 1.1842
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0082, 0.75, 0.0082))
# --- Part 2: Rentagon ---
part_2_scale = 0.0078
outer_radius = 0.0078 * part_2_scale
inner_radius = 0.0081 * part_2_scale
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, outer_radius)
    .threePointArc((outer_radius, 0), (0.0078 * part_2_scale, 0.0078 * part_2_scale))
    .lineTo(0, inner_radius)
    .close()
    .extrude(-0.0195)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_2121.stl