import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0074 * 0.0074, 0.0)
    .lineTo(0.0074 * 0.0074, 0.0074 * 0.0074)
    .lineTo(0.0013 * 0.0074, 0.0074 * 0.0074)
    .lineTo(0.0013 * 0.0074, 0.0273 * 0.0074)
    .lineTo(0.0, 0.0273 * 0.0074)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1104.stl"output_1104.stl