import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.0845 * 0.1685  # Sketch radius scaled
part_1_height = 0.4483
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1038, 0.1038, 0))
# --- Part 2: Smaller Cylinder (Neck) ---
part_2_radius = 0.0188 * 0.0375  # Sketch radius scaled
part_2_height = 0.0625
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0469, 0.7188, 0.0281))
# --- Part 3: Even Smaller Cylinder (Cut) ---
part_3_radius = 0.0188 * 0.0375  # Sketch radius scaled
part_3_height = 0.3125
part_3 =
# Export
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_684.stl