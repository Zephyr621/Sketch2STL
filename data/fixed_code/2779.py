import cadquery as cq
from math import radians
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4687 * 0.75  # Scaled width
part_1_height = 0.0938
inner_rect_length = (0.7188 - 0.0313) * 0.75
inner_rect_width = (0.4667 - 0.0312) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
part_1 = part_1.cut(cq.Workplane("XY").rect(inner_rect_length, inner_rect_width).translate((-part_1_length/2 + inner_rect_length/2, -part_1_width/2 + inner_rect_width/2, part_1_height/2)))
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Part 2: Rectangular Block (Cut
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2779.stl