import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.05
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.05, 0))
# --- Part 2: Rectangular Top ---
part_2_width = 0.025 * 0.025  # Sketch width scaled
part_2_height = 0.025 * 0.025  # Sketch height scaled
part_2_depth = 0.025
part_2 = cq.Workplane("XY").rect(part_2_width, part_2_height).extrude(part_2_depth)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1875, 0.05, 0.1875))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_1413.stl"output_1413.stl