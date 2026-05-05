import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.5357 * 0.5357  # Sketch size scaled
part_1_height = 0.525
part_1 = cq.Workplane("XY").rect(part_1_size, part_1_size).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.525))
# --- Part 2: Cutout ---
part_2_size = 0.75 * 0.75  # Sketch size scaled
part_2_height = 0.075
part_2 = cq.Workplane("XY").rect(part_2_size, part_2_size).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0, 0.525, 0))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.
cq.
cq.cq.exporters.export({result_var}, "output_564.stl"output_564.stl