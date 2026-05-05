import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.1071 * 0.2143  # Sketch radius scaled
part_1_height = 0.1154
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.1154, 0.0536, 0.0536))
# --- Part 2: Cut (Top Post) ---
part_2_radius = 0.1071 * 0.2143  # Sketch radius scaled
part_2_height = 0.1731
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1154, 0.0536, 0.0536))
# --- Part 3: Cut (Bottom Post) ---
part_3_radius = 0.1071 *
# 定义结果变量
result = part_2
# 导出为STL文件
cq.exporters.export(result, "output_3477.stl