import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1771)
    .lineTo(0.6563, 0.1771)
    .lineTo(0.6563, 0.3513)
    .lineTo(0.4167, 0.3513)
    .lineTo(0.4167, 0.1667)
    .lineTo(0.2167, 0.1667)
    .lineTo(0.2167, 0.1771)
    .lineTo(0.0, 0.1771)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4583)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4583, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_861.stl"output_861.stl