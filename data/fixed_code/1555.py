import cadquery as cq
# --- Part 1: Cube ---
part_1_length = 0.75 * 0.75  # Sketch length scaled
part_1_width = 0.5 * 0.75  # Sketch width scaled
part_1_height = 0.625
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(-part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Cutout ---
part_2_length = 0.3125 * 0.3125  # Sketch length scaled
part_2_width = 0.25 * 0.3125  # Sketch width scaled
part_2_height = 0.5
part_2 = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(-part_2_height)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.1562, 0, 0.1562))
# --- Assembly ---
assembly = part_1.cut(part_2)
cq.
cq.cq.exporters.export({result_var}, "output_1555.stl"output_1555.stl