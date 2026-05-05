import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.0052 * 0.75  # Scaled width
part_1_height = 0.0052
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cylinder (Hole) ---
part_2_radius = 0.3198 * 0.6198  # Scaled radius
part_2_height = 0.0104
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0001, 0.0001, part_1_height))
# --- Assembly: Cut the hole from the rectangular prism ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_985.stl"output_985.stl