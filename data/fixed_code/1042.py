import cadquery as cq
# --- Part 1: Cube ---
part_1_size = 0.75 * 0.75  # Sketch size scaled
part_1_height = 0.0377
part_1 = cq.Workplane("XY").box(part_1_size, part_1_size, part_1_height)
# --- Part 2: Rectangular Prism ---
part_2_x_offset = 0.5357
part_2_y_offset = 0.0
part_2_z_offset = 0.0377
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_x_offset, 0)
    .lineTo(part_2_x_offset + 0.5357, part_2_y_offset)
    .lineTo(0, part_2_y_offset)
    .close()
    .extrude(-part_2_height)  # Extrude in the opposite direction for a cut
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((part_2_x_offset, part_2_y_offset, part_2_z_offset))
# --- Assembly ---
assembly = part_1.union(part_2)
cq.cq.exporters.export({result_var}, "output_1042.stl"output_1042.stl