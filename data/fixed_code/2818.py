import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.0637 * 0.1213  # Sketch radius scaled
part_1_height = 0.2036
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0985, 0.2036, 0.0985))
# --- Part 2: Rectangular Prism ---
part_2_width = 0.0278 * 0.0352  # Sketch width scaled
part_2_height = 0.0352 * 0.0352  # Sketch height scaled
part_2_depth = 0.0075
part_2 = cq.Workplane("XY").rect(part_2_width, part_2_height).extrude(part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2818.stl