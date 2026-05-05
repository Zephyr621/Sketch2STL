import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.375 * 0.375  # Sketch size scaled
part_1_height = 0.1875 + 0.1875
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.375))
# --- Part 2: Rectangular Block (Cutout) ---
part_2_size = 0.25 * 0.25  # Sketch size scaled
part_2_height = 0.125 + 0.125
part_2 = cq.Workplane("XY").box(part_2_size, part_2_size, part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0625, 0.25, 0))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.
cq.
cq.cq.exporters.export({result_var}, "output_268.stl"output_268.stl