import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.025 * 0.05  # Sketch radius scaled
part_1_height = 0.2778
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
part_1 = part_1.translate((0.0108, 0.0108, 0))
# --- Part 2: Rectangular Top ---
part_2_width = 0.2778 * 0.2778
part_2_length = 0.2778 * 0.2778
part_2_height = 0.0556
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(part_2_width, 0.0)
    .lineTo(part_2_width, part_2_length)
    .lineTo(0.0, part_2_length)
    .close()
    .extrude(part_2_height)
)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_193.stl