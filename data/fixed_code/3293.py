import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.0625 * 0.125  # Sketch radius scaled
part_1_height = 0.1786
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1786, 0))
# --- Part 2: Smaller Cylinder on Top ---
part_2_radius = 0.0469 * 0.0937  # Sketch radius scaled
part_2_height = 0.75
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.1786, 0.1479))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
# --- Export to STL ---
cq.exporters.export({result_var}, "output_3293.stl"output_3293.stl