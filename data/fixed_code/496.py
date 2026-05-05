import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Hexagonal Prism ---
part_1_scale = 0.1805
part_1_height = 0.0836
hexagon_points = [
    (0.0 * part_1_scale, 0.0643 * part_1_scale),
    (0.0905 * part_1_scale, 0.0107 * part_1_scale),
    (0.1789 * part_1_scale, 0.0 * part_1_scale),
    (0.1805 * part_1_scale, 0.0652 * part_1_scale),
    (0.1805 * part_1_scale, 0.1934 * part_1_scale),
    (0.0905 * part_1_scale, 0.1934 * part_1_scale)
]
part_1 = (
    cq.Workplane("XY")
    .polyline(hexagon_points)
    .close()
    .extrude(-part
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_496.stl