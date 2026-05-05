import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.1562 * 0.3125  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1875, 0.1875, 0))
# --- Part 2: Cube ---
part_2_size = 0.1875 * 0.375  # Sketch size scaled
part_2_height = 0.5625
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(part_2_height)
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
# --- Export to STL ---
# --- Export to STL ---
cq.exporters.export({result_var}, "output_229.stl"output_229.stl