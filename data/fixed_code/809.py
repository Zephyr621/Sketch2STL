import cadquery as cq
from math import radians
# --- Part 1: Rectangular Block ---
part_1_length = 0.375 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.0015
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0015, 0))
# --- Part 2: Cylindrical Holes ---
hole_radius = 0.0056 * 0.015
hole_depth = 0.0015
hole_centers = [
    (0.0056 * 0.015, 0.0056 * 0.015),
    (0.0056 * 0.015, 0.5944 * 0.015),
    (0.5944 * 0.015, 0.0056 * 0.015),
    (0.5944 * 0.015, 0.5944 * 0.015)
]
# Create holes
for x, y in hole_centers:
    hole = (
        cq.Workplane("XY")
        .moveTo(x, y
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_809.stl