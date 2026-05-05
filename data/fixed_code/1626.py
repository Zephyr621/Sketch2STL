import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Prism with Curved Top ---
part_1_length = 0.75 * 0.75
part_1_width = 0.4745 * 0.75
part_1_height = 0.0469
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .threePointArc((part_1_length/2, part_1_width/2), (0, part_1_width))
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0469, 0))
# --- Part 2: Curved Shape ---
part_2_length = 0.75 * 0.75
part_2_width = 0.4745 * 0.75
part_2_height = 0.15
part_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1626.stl