import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5625 * 0.75  # Scaled width
part_1_height = 0.4688
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4688, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.1406 * 0.2812  # Scaled radius
part_2_height = 0.2812
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.75, 0.2344, 0.0938))
# --- Assembly ---
assembly = part_1.union(part_2)
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_996.stl