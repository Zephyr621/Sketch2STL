import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5625 * 0.75  # Scaled width
part_1_height = 0.4688
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cutout ---
part_2_length = 0.1875 * 0.4375  # Scaled length
part_2_width = 0.4375 * 0.4375  # Scaled width
part_2_height = 0.4688
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(-part_2_height)
)
# --- Part 3: Cutout ---
part_3_length = 0.1875 * 0.2812  # Scaled length
part_3_width =
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_685.stl