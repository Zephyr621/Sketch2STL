import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_length = 0.4688 * 0.5625  # Sketch length scaled
part_1_width = 0.5625 * 0.5625  # Sketch width scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0118 * 0.0219  # Sketch radius scaled
part_2_height = 0.2337
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0469, 0, 0.0469))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_872.stl"output_872.stl