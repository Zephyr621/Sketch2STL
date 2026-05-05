import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.2812 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.075
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# Hole parameters (scaled)
hole_center_x = 0.0937 * 0.75
hole_center_y = 0.1875 * 0.75
hole_radius = 0.0188 * 0.75
# Create holes
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .hole(2 * hole_radius)
)
# Apply rotation: Euler angles (-90, 0, -90 degrees)
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# Apply translation: (0.0313, 0.075, 0.0313)
part_1 = part_1.translate((0.0313, 0.075, 0))
# Export to STL
cq.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1618.stl