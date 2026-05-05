import cadquery as cq
from math import radians
# --- Part 1: Cube Column ---
part_1_size = 0.2795 * 0.2795  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.1172 * 0.2344  # Sketch radius scaled
part_2_depth = 0.75
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0341, 0, 0.0341))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.
cq.cq.exporters.export({result_var}, "output_3421.stl"output_3421.stl