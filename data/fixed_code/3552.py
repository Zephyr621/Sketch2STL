import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Prism ---
part_1_length = 0.6346 * 0.6346  # Scaled length
part_1_width = 0.6073 * 0.6346  # Scaled width
part_1_height = 0.468
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0418, 0.4687, 0.0418))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.045 * 0.091  # Scaled radius
part_2_depth = 0.0197
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3552.stl