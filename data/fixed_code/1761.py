import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.225 * 0.45  # Sketch radius scaled
part_1_height = 0.3
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Rectangular Block with Curved Edges ---
part_2_scale = 0.15
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.075 * part_2_scale, 0.075 * part_2_scale)
    .lineTo(0.15 * part_2_scale, 0.075 * part_2_scale)
    .threePointArc((0.075 * part_2_scale, 0), (0.15 * part_2_scale, 0.075 * part_2_scale))
    .close()
    .extrude(-0.225)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1761.stl