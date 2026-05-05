import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_radius = 0.375 * 0.75  # Sketch radius scaled
part_1_height = 0.1562
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cube (Cutout) ---
part_2_size = 0.375 * 0.375  # Sketch size scaled
part_2_height = 0.1562
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1875, 0, 0.1875))
# --- Assembly: Cut Part 2 from Part 1 ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.
cq.
cq.cq.exporters.export({result_var}, "output_377.stl"output_377.stl