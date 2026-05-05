import cadquery as cq
from math import radians
# --- Part 1: Rectangular Plate ---
part_1_length = 0.4615 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.0679
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Holes ---
hole_radius = 0.0033 * 0.75
hole_depth = 0.0134
# Hole centers (scaled and translated)
hole_centers = [
    (0.0033 * 0.75, 0.0033 * 0.75),
    (0.0033 * 0.75, 0.7317 * 0.75),
    (0.3094 * 0.75, 0.0033 * 0.75),
    (0.3094 * 0.75, 0.7317 * 0.75)
]
# Create holes
for x, y in hole_centers:
    part_1 = part_1.faces(">Z").workplane().hole(2 * hole_radius)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1133.stl