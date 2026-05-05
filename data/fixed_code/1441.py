import cadquery as cq
# --- Part 1: Rectangular Frame ---
outer_width = 0.75 * 0.75  # Scaled width
outer_height = 0.375 * 0.75  # Scaled height
inner_offset = 0.0012 * 0.75  # Scaled offset
depth = 0.0013 * 2  # Total depth (both directions)
part_1 = (
    cq.Workplane("XY")
    .rect(outer_width, outer_height)
    .extrude(depth)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(outer_width - 2 * inner_offset, outer_height - 2 * inner_offset)
    .extrude(depth)
)
part_1 = part_1.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0025, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.cq.exporters.export({result_var}, "output_1441.stl"output_1441.stl