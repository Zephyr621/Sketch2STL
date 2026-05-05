import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.3088 * 0.6048  # Sketch radius scaled
part_1_height = 0.4839
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.4286))
# --- Part 2: Small Cylinder (Cutout) ---
part_2_radius = 0.0757 * 0.1579  # Sketch radius scaled
part_2_height = 0.1579
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.2257, 0.5047, 0.4286))
# ---
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_6.stl