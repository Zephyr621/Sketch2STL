import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.1071 * 0.2143  # Sketch radius scaled
part_1_height = 0.0536
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.0179 * 0.0357  # Sketch radius scaled
part_2_height = 0.7143
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0536, 0, 0.0536))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.cq.exporters.export({result_var}, "output_353.stl"output_353.stl