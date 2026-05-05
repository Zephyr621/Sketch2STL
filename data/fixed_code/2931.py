import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Rectangular Prism ---
part_2_x_size = 0.375 * 0.375  # Sketch size scaled
part_2_y_size = 0.375 * 0.375  # Sketch size scaled
part_2_z_size = 0.375
part_2 = cq.Workplane("XY").rect(part_2_x_size, part_2_y_size).extrude(part_2_z_size)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.375, 0.75, 0))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.cq.exporters.export({result_var}, "output_2931.stl"output_2931.stl