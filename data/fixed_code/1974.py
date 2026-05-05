import cadquery as cq
from math import *
# --- Part 1: Hexagonal Prism ---
part_1_points = [
    (0.0, 0.3187),
    (0.1446, 0.0),
    (0.6495, 0.1545),
    (0.5335, 0.4286),
    (0.4471, 0.6187)
]
part_1_points = [(x * 0.7145, y * 0.7145) for x, y in part_1_points]  # Scale the points
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .polyline(part_1_points)
    .close()
    .extrude(part_1_height)
)
# --- Part 2: Hexagonal Prism ---
part_2_points = [
    (0.0, 0.0),
    (0.6923, 0.0),
    (0.6923, 0.6218),
    (0.0, 0.6218)
]
part_2_points = [(x * 0.6218, y * 0.6218) for x, y
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1974.stl