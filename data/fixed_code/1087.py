import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.3248 * 0.75  # Sketch radius scaled
part_1_height = 0.6
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.3))
# --- Part 2: Hexagonal Prism ---
hex_scale = 0.6089
hex_points = [
    (0.0, 0.3248 * hex_scale),
    (0.0795 * hex_scale, 0.0),
    (0.6495 * hex_scale, 0.0047 * hex_scale),
    (0.6089 * hex_scale, 0.3248 * hex_scale),
    (0.0795 * hex_scale, 0.6495 * hex_scale),
]
part_2 = (
    cq.Workplane("XY")
    .polyline(hex_points)
    .close()
    .extr
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1087.stl