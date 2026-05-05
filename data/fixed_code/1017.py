import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Circular Disk with Hole ---
part_1_outer_radius = 0.375 * 0.75
part_1_inner_radius = 0.0938 * 0.75
part_1_height = 0.0562
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0562, 0.0078, 0.0078))
# --- Part 2: Ring ---
part_2_outer_radius = 0.075 * 0.3188
part_2_inner_radius = 0.0463 * 0.3188
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1017.stl