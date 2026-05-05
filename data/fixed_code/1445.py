import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.2027 * 0.4054  # Sketch radius scaled
part_1_height = 0.1419
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1419, 0))
# --- Part 2: Top Tall ---
part_2_scale = 0.1875
part_2_depth = 0.0374
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.1744 * part_2_scale, 0.0)
    .threePointArc((0.0937 * part_2_scale, 0.0937 * part_2_scale), (0.1582 * part_2_scale, 0.0
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1445.stl