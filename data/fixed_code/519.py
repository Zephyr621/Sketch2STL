import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder with Curved Top ---
sketch_scale = 0.75
extrude_depth = 0.25 * 2  # Total extrusion depth (towards + opposite normal)
# Define the points for the sketch
points = [
    (0.0, 0.375),
    (0.375, 0.0),
    (0.75, 0.375),
    (0.75, 0.625),
    (0.0, 0.625),
    (0.0, 0.0)
]
# Create the sketch using the points
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(extrude_depth)
)
# Apply rotations
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.25, 0))
# --- Assembly ---
assembly = part_1
# Export the result to a STL file
cq.
# Export the result to
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_519.stl