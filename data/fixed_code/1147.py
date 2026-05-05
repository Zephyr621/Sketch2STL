import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.25 * 0.75)
    .lineTo(0.5 * 0.75, 0.25 * 0.75)
    .lineTo(0.5 * 0.75, 0.75 * 0.75)
    .lineTo(0.25 * 0.75, 0.75 * 0.75)
    .lineTo(0.25 * 0.75, 0.625 * 0.75)
    .lineTo(0.0, 0.625 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.45)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1147.stl"output_1147.stl