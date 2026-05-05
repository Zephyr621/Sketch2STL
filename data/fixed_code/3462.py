import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4286 * 0.75  # Scaled width
part_1_height = 0.4286
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4286, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
cq.
# Export to STL
cq.
cq.
# --- Final Result ---
result = assembly
cq.cq.exporters.export({result_var}, "output_3462.stl"output_3462.stl