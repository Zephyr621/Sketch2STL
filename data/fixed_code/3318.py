import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5357 * 0.75  # Scaled width
part_1_height = 0.3214
inner_rect_offset = 0.0268 * 0.75
inner_rect_width = (0.6136 - 0.0134) * 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, part_1_width)
    .lineTo(inner_rect_offset, inner_rect_width)
    .lineTo(inner_rect_offset, inner_rect_width + (0.4286 - 0.0134)) * 0.75
    .lineTo(0, inner_rect_width)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3214, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_3318.stl"output_3318.stl