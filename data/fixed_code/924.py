import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.5042 * 0.75)
    .lineTo(0.5522 * 0.75, 0.5042 * 0.75)
    .lineTo(0.5522 * 0.75, 0.4773 * 0.75)
    .lineTo(0.2392 * 0.75, 0.4773 * 0.75)
    .lineTo(0.2392 * 0.75, 0.5316 * 0.75)
    .lineTo(0.0, 0.5316 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0065)
)
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_924.stl"output_924.stl