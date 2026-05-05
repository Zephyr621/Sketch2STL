import cadquery as cq
from math import radians
# --- Part 1: Ring ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.2679 * 0.75
height = 0.0311
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(height)
)
# --- Part 2: Cylinder ---
cylinder_radius = 0.2679 * 0.5357  # Sketch radius scaled
cylinder_height = 0.2143
part_2 = (
    cq.Workplane("XY")
    .circle(cylinder_radius)
    .extrude(cylinder_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.1071, 0.1071, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3238.stl"output_3238.stl