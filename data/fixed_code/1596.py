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
sketch_scale_1 = 0.75
part_1_points_scaled = [(x * sketch_scale_1, y * sketch_scale_1) for x, y in part_1_points]
part_1 = (
    cq.Workplane("XY")
    .polyline(part_1_points_scaled)
    .close()
    .extrude(part_1_height)
)
# --- Part 2: Cylinder ---
part_2_radius = 0.3248 * 0.6495
part_2_height = 0.2537
translation_vector = (0.0705, 0.0203, 0.2537)
part_2_x_offset = 0.0705
part_2_y_offset = 0.0203
part_2 = (
    cq.Work
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1596.stl