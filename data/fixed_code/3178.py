import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube ---
part_1_size = 0.5 * 0.5  # Sketch size scaled
part_1_height = 0.1027
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1027, 0))
# --- Part 2: Cut Feature ---
part_2_radius = 0.275 * 0.55  # Sketch radius scaled
part_2_depth = 0.1536
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), 90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3178.stl