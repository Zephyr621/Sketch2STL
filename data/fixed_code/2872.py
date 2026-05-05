import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.45 * 0.75  # Scaled width
part_1_height = 0.0694
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0694, 0))
# --- Part 2: Cylinders ---
cylinder_radius = 0.03 * 0.6176  # Scaled radius
cylinder_height = 0.0908
cylinder1 = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)
cylinder2 = cq.Workplane("XY").circle(cylinder_radius).extrude(cylinder_height)
# --- Assembly ---
assembly = part_1.union(cylinder1).union(cylinder2)
# --- Export to STL ---
cq.
cq.cq.exporters.export({result_var}, "output_2872.stl"output_2872.stl