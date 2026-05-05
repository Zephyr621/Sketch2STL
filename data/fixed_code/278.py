import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.0354 * 0.0354  # Scaled length
part_1_width = 0.0247 * 0.0354   # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.cq.exporters.export({result_var}, "output_278.stl"output_278.stl