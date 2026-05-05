import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Pentagon with holes ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.6387 * sketch_scale
height = 0.0091
hole_radius = 0.0104 * sketch_scale
hole_centers = [
    (0.0563 * sketch_scale - length / 2, 0.0562 * sketch_scale - width / 2),
    (0.0563 * sketch_scale - length / 2, 0.3988 * sketch_scale - width / 2),
    (0.6961 * sketch_scale - length / 2, 0.0562 * sketch_scale - width / 2),
    (0.6961 * sketch_scale - length / 2, 0.3988 * sketch_scale - width / 2)
]
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0563 * sketch_scale, 0)
    .lineTo(length, 0)
    .threePointArc((length + 0.0563 * sketch_scale, 0.0562 * sketch_scale), (length/2, width))
    .lineTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3087.stl