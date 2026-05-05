import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0225)
    .lineTo(0.7188, 0.0225)
    .lineTo(0.7188, 0.3315)
    .lineTo(0.5357, 0.3315)
    .lineTo(0.5357, 0.1705)
    .lineTo(0.2143, 0.1705)
    .lineTo(0.2143, 0.3523)
    .lineTo(0.0, 0.3523)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0403 * 0.75)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_46.stl"output_46.stl