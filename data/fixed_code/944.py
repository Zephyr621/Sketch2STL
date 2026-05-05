import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.0417 * 0.0876  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Block (Cut) ---
part_2_width = 0.0281 * 0.0876
part_2_height = 0.0865 * 0.0876
part_2_depth = 0.7498
part_2 = cq.Workplane("XY").rect(part_2_width, part_2_height).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0054, 0, 0.0054))
# --- Assembly ---
assembly = part_1.
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_944.stl