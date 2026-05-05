import cadquery as cq
from math import radians
# --- Parameters from JSON ---
cube_size = 0.75 * 0.75  # Scaled cube size
hole_radius = 0.0833 * 0.75  # Scaled hole radius
extrude_depth = 0.3333
# --- Part 1: Cube with Holes ---
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(extrude_depth)
)
# Hole positions (scaled and translated)
hole_positions = [
    (0.0417 * 0.75 - cube_size/2, 0.4167 * 0.75 - cube_size/2),
    (0.2433 * 0.75 - cube_size/2, 0.5667 * 0.75 - cube_size/2),
    (0.4842 * 0.75 - cube_size/2, 0.5667 * 0.75 - cube_size/2),
    (0.5077 * 0.75 - cube_size/2, 0.4167 * 0.75 - cube_size/2)
]
for x, y in hole_positions:
    part_1 = part_1.faces(">Z").workplane().pushPoints([(x, y)]).hole(2 * hole_radius)
# --- Part 2: Cylindrical Holes ---
cylinder_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2156.stl