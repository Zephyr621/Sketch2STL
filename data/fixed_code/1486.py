import cadquery as cq
from cadquery.vis import show
# --- Part 1: Octagonal Prism ---
sketch_scale = 0.75
height = 0.2499
# Scaled coordinates for the octagon
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3248 * sketch_scale),
    (0.5625 * sketch_scale, 0.6495 * sketch_scale),
    (0.1875 * sketch_scale, 0.6495 * sketch_scale)
]
# Create the octagon using the points
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2499, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_1486.stl"output_1486.stl