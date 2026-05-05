import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Hexagonal Prism ---
hex_width = 0.6495 * 0.75
hex_height = 0.2537
hex_points = [
    (0.0, 0.3248 * 0.75),
    (0.1875 * 0.75, 0.0),
    (0.5625 * 0.75, 0.0),
    (0.75 * 0.75, 0.3248 * 0.75),
    (0.5625 * 0.75, 0.6495 * 0.75),
    (0.1875 * 0.75, 0.6495 * 0.75)
]
part_1 = (
    cq.Workplane("XY")
    .polyline(hex_points)
    .close()
    .extrude(hex_height)
)
# --- Part 2: Cylinder ---
cylinder_radius = 0.3045 * 0.6089
cylinder_height = 0.1269
part_2 = (
    cq.Workplane("XY")
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.07
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1067.stl