import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3173 * 0.75)
    .lineTo(0.7375 * 0.75, 0.4303 * 0.75)
    .lineTo(0.6 * 0.75, 0.4641 * 0.75)
    .lineTo(0.0, 0.4641 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2033.stl"output_2033.stl