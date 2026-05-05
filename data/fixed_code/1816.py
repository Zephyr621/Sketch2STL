import cadquery as cq
from math import tan, radians, sqrt
# --- Part 1: Hexagonal Prism ---
part_1_scale = 0.75
part_1_height = 0.2537
hexagon_points = [
    (0.0 * part_1_scale, 0.3248 * part_1_scale),
    (0.1875 * part_1_scale, 0.0 * part_1_scale),
    (0.5625 * part_1_scale, 0.0 * part_1_scale),
    (0.75 * part_1_scale, 0.3248 * part_1_scale),
    (0.5625 * part_1_scale, 0.6495 * part_1_scale)
]
part_1 = (
    cq.Workplane("XY")
    .polyline(hexagon_points)
    .close()
    .extrude(part_1_height)
)
# --- Part 2: Cylinder ---
part_2_radius = 0.3045 * 0.6089
part_2_height = 0.1269
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1816.stl