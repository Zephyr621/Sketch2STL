import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_size = 0.4042 * 0.4042  # Sketch size scaled
part_1_height = 0.0438
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0219, 0.0, 0.0219))
# --- Part 2: Cylinder ---
part_2_radius = 0.1569 * 0.3695  # Sketch radius scaled
part_2_height = 0.0966
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0392, 0.0, 0.0392))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_2839.stl"output_2839.stl