import cadquery as cq
from math import tan, radians
# --- Part 1: Hexagonal Rod ---
outer_points = [
    (0.0, 0.1875),
    (0.0938, 0.0),
    (0.5625, 0.0),
    (0.75, 0.1875),
    (0.5625, 0.75),
    (0.0, 0.75)
]
inner_points = [
    (0.0144, 0.0144),
    (0.7498, 0.0144),
    (0.5687, 0.0144),
    (0.6562, 0.0144),
    (0.5687, 0.7498),
    (0.0144, 0.7498)
]
sketch_scale = 0.75
extrude_depth = 0.375
scaled_outer_points = [(x * sketch_scale, y * sketch_scale) for x, y in outer_points]
scaled_inner_points = [(x * sketch_scale, y * sketch_scale) for x, y in inner_points]
part_1 = (
    cq.Workplane("XY")
    .polyline(scaled_outer_points)
    .close()
    .polyline(scaled_inner_points)
    .close()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2568.stl