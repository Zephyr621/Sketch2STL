import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Scaled size
part_1_height = 0.0937
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0937, 0))
# --- Part 2: Top Cube ---
part_2_size = 0.5625 * 0.5625  # Scaled size
part_2_height = 0.6562
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1875, 0.0937, 0.1875))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_225.stl"output_225.stl