import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.1071 * 0.2143  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
part_1 = part_1.translate((0, 0, 0.75))
# --- Part 2: Cylinder (Cut) ---
part_2_radius = 0.0333 * 0.067  # Sketch radius scaled
part_2_height = 1.0157
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0714, 0, 0.0429))
# --- Part 3: Cylinder (Cut) ---
part_3_radius = 0.0234 * 0.0469  # Sketch radius scaled
part_3_height = 0.0056
part_3 = cq.Workplane("XY").
# 定义结果变量
result = part_3
# 导出为STL文件
cq.exporters.export(result, "output_2731.stl