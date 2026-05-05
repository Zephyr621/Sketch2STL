import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.375
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder (Hole) ---
part_2_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_height = 0.375
part_2 = cq.Workplane("XY").circle(part_2_radius).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0, 0.375, 0))
# --- Assembly: Cut the hole from the cube ---
result = part_1.cut(part_2)
# --- Export to STL ---
cq.
cq.cq.exporters.export({result_var}, "output_1125.stl"output_1125.stl