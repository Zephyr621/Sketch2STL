import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.5625 * sketch_scale
height = 0.1875
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length + 0.5 * sketch_scale, 0.375 * sketch_scale), (length/2, width))
    .lineTo(0, width)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
# Export to STL
# Export to STL
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1336.stl