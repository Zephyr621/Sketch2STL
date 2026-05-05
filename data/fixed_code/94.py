import cadquery as cq
from math import radians
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.2812 * 0.75
part_1_inner_radius = 0.0938 * 0.75
part_1_height = 0.1312
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1312, 0))
# --- Part 2: Cut Feature ---
part_2_scale = 0.75
part_2_depth = 0.1326
# Define the points for the sketch
points = [
    (0.0, 0.3281),
    (0.0087, 0.1897),
    (0.1406, 0.0),
    (0.6068, 0.0),
    (0.75, 0.3281),
]
# Scale the points
scaled_points
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_94.stl