import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.0048
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0156))
# --- Part 2: Cylinder (Cut) ---
part_2_radius = 0.1504 * 0.3047  # Sketch radius scaled
part_2_height = 0.1172
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.1406, 0.6322, 0.0156))
# --- Assembly ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_2823.stl"output_2823.stl