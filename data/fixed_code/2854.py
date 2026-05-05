import cadquery as cq
from math import radians
# --- Part 1: Rectangular Frame ---
part_1_length = 0.6964 * 0.6964  # Scaled length
part_1_width = 0.4286 * 0.6964  # Scaled width
part_1_height = 0.0536
inner_length = (0.6964 - 0.0222) * 0.6964
inner_width = (0.3914 - 0.0138) * 0.6964
outer_rect = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
inner_rect = cq.Workplane("XY").rect(inner_length, inner_width).translate((inner_length/2 - (part_1_length/2), inner_width/2 - (part_1_width/2), -0.0042*0.6964))
part_1 = outer_rect.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0026, 0.0536, 0.0138))
# --- Part 2: Cut Feature ---
part_2
# Export
# 定义结果变量
result = inner_rect
# 导出为STL文件
cq.exporters.export(result, "output_2854.stl