import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube with Rounded Edges ---
part_1_length = 0.75 * 0.75
part_1_width = 0.7047 * 0.75
part_1_height = 0.0528
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .threePointArc((part_1_length/2, 0.0109 * 0.75), (0.7047 * 0.75, part_1_width))
    .lineTo(0.6958 * 0.75, part_1_width)
    .threePointArc((0.7316 * 0.75, 0.0109 * 0.75), (0.75 * 0.75, 0))
    .lineTo(0.75 * 0.75, part_1_length)
    .lineTo(0, part_1_length)
    .lineTo(0, 0)
    .close()
    .extrude(part_1_height)
)
# Add holes to part 1
hole_radius = 0.0285 * 0.75
part_1 = (
    part_1.faces(">Z")
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_724.stl