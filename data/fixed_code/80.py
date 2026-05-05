import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.1154 * 0.2368  # Sketch radius scaled
part_1_height = 0.2368
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Protrusion ---
part_2_x = 0.1917 * 0.1816
part_2_y = 0.1816 * 0.1816
part_2_z = 0.6316
part_2 = cq.Workplane("XY").rect(part_2_x, part_2_y).extrude(part_2_z)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1366, 0, 0.1366))
# --- Part 3: Circular Hole ---
part_3_radius = 0.0234 * 0.0533
part_3_depth = 0.
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_80.stl