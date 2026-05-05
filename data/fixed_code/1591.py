import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.2323 * 0.75  # Sketch radius scaled
part_1_height = 0.0221
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0429, 0))
# --- Part 2: Rectangular Plate ---
part_2_width = 0.2216 * 0.2216
part_2_length = 0.2393 * 0.2216
part_2_height = 0.0221
part_2 = cq.Workplane("XY").rect(part_2_width, part_2_length).extrude(-part_2_height)
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_1591.stl