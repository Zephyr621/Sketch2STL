import cadquery as cq
from math import *
# --- Part 1: Ring ---
outer_points = [
    (0.0, 0.27),
    (0.375, 0.27),
    (0.375, 0.4687),
    (0.3125, 0.4687)
]
inner_points = [
    (0.0208, 0.0469),
    (0.7159, 0.0208),
    (0.75, 0.0469),
    (0.75, 0.3356),
    (0.7159, 0.3356),
    (0.7159, 0.4744),
    (0.0208, 0.4744)
]
sketch_scale = 0.75
extrude_depth = 0.1023
scaled_outer_points = [(x * sketch_scale, y * sketch_scale) for x, y in outer_points]
scaled_inner_points = [(x * sketch_scale, y * sketch_scale) for x, y in inner_points]
part_1 = (
    cq.Workplane("XY")
    .polyline(scaled_outer_points)
    .close()
    .polyline(scaled_inner_points
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1192.stl