import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Block with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.6635 * sketch_scale
height = 0.4163
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length/2, 0.0437 * sketch_scale), (0.4167 * sketch_scale, 0))
    .lineTo(0.75 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, width)
    .lineTo(0, width)
    .lineTo(0, 0)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_826.stl