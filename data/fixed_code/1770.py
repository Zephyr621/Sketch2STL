import cadquery as cq
from math import tan, radians
# --- Parameters from JSON ---
sketch_scale = 0.75
extrude_depth = 0.2462
# Scaled coordinates for the hexagon
points = [
    (0.0 * sketch_scale, 0.3248 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3248 * sketch_scale),
    (0.5625 * sketch_scale, 0.6495 * sketch_scale),
    (0.1875 * sketch_scale, 0.6495 * sketch_scale)
]
# --- Create the Hexagon ---
hex_points = [(x * sketch_scale, y * sketch_scale) for x, y in points]
part_1 = (
    cq.Workplane("XY")
    .polyline(hex_points)
    .close()
    .extrude(extrude_depth)
)
# --- Apply Translation ---
part_1 = part_1.translate((0, 0, 0.1261))
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1770.stl"output_1770.stl