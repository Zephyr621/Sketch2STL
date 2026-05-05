import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0312 * 0.75)
    .lineTo(0.0312 * 0.75, 0.0312 * 0.75)
    .lineTo(0.0312 * 0.75, 0.2577 * 0.75)
    .lineTo(0.0, 0.2577 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0104)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2663.stl"output_2663.stl