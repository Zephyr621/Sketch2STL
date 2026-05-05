import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.3214)
    .lineTo(0.6429, 0.3214)
    .threePointArc((0.375, 0.2143), (0.3214, 0.4286))
    .lineTo(0.0, 0.4286)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1071 * 0.75)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1924.stl"output_1924.stl