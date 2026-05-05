import cadquery as cq
from math import *
# --- Part 1: Hexagonal Prism ---
part_1_points = [
    (0.0, 0.3248),
    (0.1875, 0.0),
    (0.5625, 0.0),
    (0.75, 0.3248),
    (0.5625, 0.6495),
    (0.1875, 0.6495)
]
sketch_scale_1 = 0.75
extrusion_depth_1 = 0.2537
scaled_points = [(x * sketch_scale_1, y * sketch_scale_1) for x, y in part_1_points]
part_1 = (
    cq.Workplane("XY")
    .polyline(scaled_points)
    .close()
    .extrude(extrusion_depth_1)
)
# --- Part 2: Cylinder Cutout ---
part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1504.stl