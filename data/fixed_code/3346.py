import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.2383 * 0.4688  # Sketch radius scaled
part_1_height = 0.0042
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0365, 0.0365, 0.0042))
# --- Part 2: Smaller Cylinder ---
part_2_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_height = 0.0417
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0, 0, 0.0042))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.exporters.export({result_var}, "output_3346.stl"output_3346.stl