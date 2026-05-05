import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6589 * 0.75  # Scaled width
part_1_height = 0.4929
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1577))
# --- Part 2: Cut Feature (Slightly Faces) ---
sketch_scale = 0.6495
depth = 0.1577
# Define the points for the sketch
points = [
    (0.0, 0.3248),
    (0.0187, 0.0),
    (0.0188, 0.3248),
    (0.0188, 0.6495),
    (0.0, 0.6495)
]
# Create the sketch using the points
part_2_sketch = cq.Workplane("XY")
for point in points:
    part_2_sketch = part_2_sketch.moveTo(point[0], point[1]).lineTo(point[0], point[1
# Export
# 定义结果变量
result = part_2_sketch
# 导出为STL文件
cq.exporters.export(result, "output_1330.stl