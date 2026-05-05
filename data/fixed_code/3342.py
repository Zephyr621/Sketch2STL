import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0781)
    .lineTo(0.3712, 0.0781)
    .lineTo(0.375, 0.0781)
    .lineTo(0.3869, 0.1463)
    .lineTo(0.2468, 0.1463)
    .lineTo(0.0, 0.0781)
    .close()
    .extrude(0.0625)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3342.stl"output_3342.stl