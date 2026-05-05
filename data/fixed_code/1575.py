import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.1031 * 0.2056  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Washer ---
outer_radius = 0.0469 * 0.0937
inner_radius = 0.0281 * 0.0937
part_2_height = 0.0313
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0094,
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1575.stl