import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.3125 * 0.75  # Scaled width
height = 0.0625
inner_offset = 0.0312 * 0.75  # Scaled offset
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(length - 2 * inner_offset, width - 2 * inner_offset)
    .extrude(height + 0.1)  # Extrude slightly more to ensure complete cut
)
part_1 = part_1.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_2792.stl"output_2792.stl