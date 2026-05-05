import cadquery as cq
from cadquery.vis import show
# --- Part 1: Hexagonal Nut ---
sketch_scale = 0.75
height = 0.2471
# Scaled coordinates for the hexagon
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3248 * sketch_scale)
]
center_x = 0.375 * sketch_scale
center_y = 0.3248 * sketch_scale
radius = 0.2165 * sketch_scale
# Create the hexagonal profile using the scaled points
hex_profile = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
)
# Extrude the hexagonal profile
part_1 = hex_profile.extrude(height)
# Create the hole
hole = cq.Workplane("XY").circle(radius).extrude(height)
# Subtract the hole from the hexagon
result = part_1.cut(hole)
# Export the result to a STL file
cq.
# Export the result to a
# 导出为STL文件
cq.exporters.export(result, "output_1174.stl