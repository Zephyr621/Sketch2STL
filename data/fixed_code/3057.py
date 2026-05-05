import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.1038 * 0.2077  # Sketch radius scaled
part_1_height = 0.1875 + 0.1875
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.375))
# --- Part 2: Cut Cylinder ---
part_2_radius = 0.0604 * 0.1247  # Sketch radius scaled
part_2_height = 0.75
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0517, 0.2438, 0.375))
# --- Assembly ---
assembly = part_1.cut(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_3057.stl"output_3057.stl