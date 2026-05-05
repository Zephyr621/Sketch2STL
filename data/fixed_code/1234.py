import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Box with Holes ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2308 * sketch_scale
height = 0.1972
# Scaled dimensions
scaled_length = length * sketch_scale
scaled_width = width * sketch_scale
# Hole parameters (scaled)
hole_radius = 0.0134 * sketch_scale
hole_centers = [
    (0.0364 * sketch_scale, 0.1213 * sketch_scale),
    (0.0364 * sketch_scale, 0.2274 * sketch_scale),
    (0.6151 * sketch_scale, 0.1213 * sketch_scale)
]
# Create the base shape
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(scaled_length, 0)
    .threePointArc((scaled_length + 0.0496 * sketch_scale, 0.0088 * sketch_scale), (scaled_length, scaled_width))
    .lineTo(0, scaled_width)
    .close()
    .extrude(height)
)
# Add holes
for center_x, center_y
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1234.stl