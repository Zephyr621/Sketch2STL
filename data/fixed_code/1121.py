import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6034 * 0.75  # Scaled width
part_1_height = 0.1659
inner_rect_offset = 0.0107 * 0.75
inner_rect_length = (0.7083 - 0.0107) * 0.75
inner_rect_width = (0.5357 - 0.0107) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .rect(inner_rect_length, inner_rect_width)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1659, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_1121.stl"output_1121.stl