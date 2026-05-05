import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.2982)
    .lineTo(0.5713, 0.2982)
    .lineTo(0.5713, 0.2143)
    .lineTo(0.3723, 0.2143)
    .lineTo(0.3723, 0.4286)
    .lineTo(0.0, 0.4286)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2679 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2679 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_815.stl"output_815.stl