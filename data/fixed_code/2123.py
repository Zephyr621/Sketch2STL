import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.3333 * 0.6667  # Sketch radius scaled
part_1_height = 0.0333
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0383, 0.0383, 0))
# --- Part 2: Disk ---
part_2_radius = 0.0833 * 0.6667  # Sketch radius scaled
part_2_height = 0.0333
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0383, 0.0417, 0.0417))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.
cq.cq.exporters.export({result_var}, "output_2123.stl"output_2123.stl