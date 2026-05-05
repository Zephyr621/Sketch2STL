import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3214 * 0.75  # Scaled width
part_1_height = 0.375
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Part 2: Cylinder ---
part_2_radius = 0.0179 * 0.0357  # Scaled radius
part_2_height = 0.1607
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.3309, 0.1071, 0.375))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_1881.stl"output_1881.stl