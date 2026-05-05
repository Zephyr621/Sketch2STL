import cadquery as cq
from math import tan, radians
# --- Part 1: Hexagonal Prism ---
part_1_points = [
    (0.0, 0.3248),
    (0.1875, 0.0),
    (0.5625, 0.0),
    (0.75, 0.3248),
    (0.5625, 0.6495),
    (0.1875, 0.6495)
]
part_1_height = 0.2537
part_1_scale = 0.75
scaled_points = [(x * part_1_scale, y * part_1_scale) for x, y in part_1_points]
part_1 = (
    cq.Workplane("XY")
    .polyline(scaled_points)
    .close()
    .extrude(part_1_height)
)
# --- Part 2: Cylinder ---
part_2_radius = 0.3045 * 0.6089  # Sketch radius scaled
part_2_height = 0.1269
part_2_translation = (0.0705, 0.0203, 0.2537)
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2782.stl