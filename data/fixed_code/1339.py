import cadquery as cq
# --- Part 1: Rectangular Section ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5455 * 0.75  # Scaled width
part_1_height = 0.0156  # Height
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_1339.stl"output_1339.stl