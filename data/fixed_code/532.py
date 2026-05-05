import cadquery as cq
from math import radians
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.2062
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2062, 0))
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.2917 * 0.582  # Sketch radius scaled
part_2_height = 0.0938
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1453, 0, 0.1453))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_532.stl"output_532.stl