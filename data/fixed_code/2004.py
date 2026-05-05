import cadquery as cq
# --- Part 1: Wedge-shaped block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3696 * 0.75  # Scaled width
part_1_height = 0.2898
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .lineTo(part_1_length, 0.2908 * 0.75)
    .lineTo(0.5357 * 0.75, 0.2908 * 0.75)
    .lineTo(0.5357 * 0.75, part_1_width)
    .lineTo(0, part_1_width)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2898, 0))
# --- Assembly ---
assembly = part_1
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_2004.stl"output_2004.stl