import cadquery as cq
from math import *
# --- Part 1: Hexagonal Cylinder ---
part_1_scale = 0.4432
part_1_height = 0.1875 + 0.1875
hexagon_points = [
    (0.0, 0.0),
    (0.2196, 0.0),
    (0.2196, 0.2196),
    (0.2196, 0.4432),
    (0.0, 0.4432)
]
part_1 = (
    cq.Workplane("XY")
    .polyline(hexagon_points)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.375, 0.0, 0.0))
# --- Part 2: Cylinder with Hole ---
part_2_scale = 0.75
part_2_height = 0.5625
part_2 = (
    cq.Workplane("XY")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1049.stl