import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_size = 0.4167 * 0.4167  # Sketch size scaled
part_1_height = 0.4198
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0833, 0.0833, 0))
# --- Part 2: Cutout ---
part_2_size = 0.4167 * 0.4167  # Sketch size scaled
part_2_height = 0.4198
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0833, 0.4167, 0))
# --- Part 3
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_2708.stl