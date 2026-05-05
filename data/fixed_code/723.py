import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_inner_radius = 0.3562 * 0.75
part_1_height = 0.0156
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0156, 0, 0))
# --- Part 2: Cut Feature ---
part_2_size = 0.1395 * 0.1395
part_2_depth = 0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_723.stl