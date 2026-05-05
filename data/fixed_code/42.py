import cadquery as cq
from math import radians
# --- Part 1: Base Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.075
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Part 2: Top Cube ---
part_2_size = 0.525 * 0.525  # Sketch size scaled
part_2_height = 0.075
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.375, 0.0, 0.075))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_42.stl"output_42.stl