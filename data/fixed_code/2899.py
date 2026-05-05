import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3488 * 0.75)
    .lineTo(0.0, 0.3488 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1741)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2899.stl"output_2899.stl