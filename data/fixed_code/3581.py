import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Bar with Holes ---
length = 0.75
width = 0.2679
height = 0.0179
sketch_scale = 0.75
hole1_center = (0.1637, 0.1309)
hole2_center = (0.5862, 0.1289)
hole_radius = 0.0511
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length * sketch_scale, 0)
    .threePointArc((length * sketch_scale, 0.1071), (length * sketch_scale, width * sketch_scale))
    .lineTo(0, width * sketch_scale)
    .threePointArc((0, 0.1071), (0, 0))
    .close()
    .extrude(height)
    .faces(">Z").workplane().pushPoints([hole1_center]).hole(2 * hole_radius)
    .faces(">Z").workplane().pushPoints([hole2_center]).hole(2 * hole_radius)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3581.stl