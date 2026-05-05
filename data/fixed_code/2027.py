import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1865)
    .lineTo(0.5625, 0.1865)
    .lineTo(0.5625, 0.5808)
    .lineTo(0.1865, 0.5808)
    .lineTo(0.1865, 0.1865)
    .lineTo(0.0, 0.1865)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.0143)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_2027.stl"output_2027.stl