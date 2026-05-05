import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3375 * 0.6675, 0.0)
    .lineTo(0.3375 * 0.6675, 0.6675 * 0.6675)
    .lineTo(0.0, 0.6675 * 0.6675)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2145.stl"output_2145.stl