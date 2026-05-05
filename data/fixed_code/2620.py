import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder with Rounded Ends ---
part_1_radius = 0.0749 * 0.75  # Sketch radius scaled
part_1_height = 0.6624
# Define the points for the sketch
points = [
    (0.0749 * 0.75, 0),
    (0.6761 * 0.75, 0),
    (0.6761 * 0.75, 0.1457 * 0.75),
    (0.6761 * 0.75, 0.1502 * 0.75),
    (0.0749 * 0.75, 0.1502 * 0.75),
    (0, 0.1457 * 0.75)
]
# Create the sketch using the points
sketch = cq.Workplane("XY")
# Create the sketch using the points
part_1 = (
    sketch.moveTo(points[0][0], points[0][1])
    .threePointArc((0.0297 * 0.75, 0.0187 * 0.75), (points[1][0], points[1][1]))
    .lineTo(points[2][0], points[2][1])
    .threePointArc((0.7299
# Export
# 定义结果变量
result = sketch
# 导出为STL文件
cq.exporters.export(result, "output_2620.stl