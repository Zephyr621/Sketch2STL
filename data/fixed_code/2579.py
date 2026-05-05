import cadquery as cq
from math import tan, radians
# --- Part 1: Hexagonal Washer ---
outer_points = [
    (0.0, 0.3248),
    (0.1875, 0.0),
    (0.5625, 0.0),
    (0.75, 0.3248),
    (0.5625, 0.6495),
    (0.1875, 0.6495)
]
inner_radius = 0.175 * 0.75
height = 0.05
outer_poly = cq.Workplane("XY").polyline(outer_points).close()
inner_poly = cq.Workplane("XY").polyline(inner_points).close()
washer = outer_poly.extrude(height)
# Subtract inner circle from the outer polygon
part_1 = part_1.cut(inner_poly.extrude(height))
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2579.stl"output_2579.stl