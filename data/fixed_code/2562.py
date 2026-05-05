import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.2917 * 0.5893  # Sketch radius scaled
part_1_height = 0.3214
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.1372, 0.4773, 0.1372))
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.1576 * 0.3806  # Sketch radius scaled
part_2_height = 0.1607
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0386, 0.4773, 0.0386))
# --- Assembly ---
assembly
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2562.stl