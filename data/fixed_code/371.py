import cadquery as cq
from cadquery import exporters
# --- Part 1: Cube ---
part_1_size = 0.5651 * 0.75  # Sketch size scaled
part_1_height = 0.1906
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3938, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0464 * 0.0865  # Sketch radius scaled
part_2_height = 0.2259
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.2055, 0.3938, 0.2055))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_371.stl"output_371.stl