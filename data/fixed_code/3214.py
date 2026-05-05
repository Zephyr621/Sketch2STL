import cadquery as cq
from math import radians
# --- Part 1: Cube ---
part_1_size = 0.6136 * 0.6136  # Sketch scale applied
part_1_height = 0.6591
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0759 * 0.1591  # Sketch radius scaled
part_2_height = 0.6591
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0794, 0.6497, 0.0794))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3214.stl"output_3214.stl