import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Base ---
part_1_width = 0.4342 * 0.75
part_1_length = 0.75 * 0.75
part_1_height = 0.0197
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_length)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2984, 0))
# --- Part 2: Vertical Extension ---
part_2_width = 0.4342 * 0.4714
part_2_length = 0.4714 * 0.4714
part_2_height = 0.4948
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_width, part_2_length)
    .
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1068.stl