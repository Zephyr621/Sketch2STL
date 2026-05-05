import cadquery as cq
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * 0.75, 0.0)
    .lineTo(0.25 * 0.75, 0.125 * 0.75)
    .lineTo(0.625 * 0.75, 0.125 * 0.75)
    .lineTo(0.625 * 0.75, 0.375 * 0.75)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.75 * 0.75, 0.5 * 0.75)
    .lineTo(0.0, 0.5 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.5)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3084.stl"output_3084.stl