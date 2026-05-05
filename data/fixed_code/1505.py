import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Hexagonal Nut ---
sketch_scale = 0.75
height = 0.375
# Scaled coordinates for the hexagon
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3248 * sketch_scale),
    (0.5625 * sketch_scale, 0.6495 * sketch_scale)
]
# Create the hexagonal profile using the points
hex_profile = cq.Workplane("XY").polyline(points).close()
# Extrude the hexagonal profile
hex_nut = hex_profile.extrude(height)
# Subtract the hexagon from the nut
result = hex_nut.cut(hex_nut.extrude(height))
# Export the result to a STL file
cq.
# Export the result to a STL file
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_1505.stl