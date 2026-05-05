import cadquery as cq
# --- Part 1: L-shaped profile ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25 * 0.75, 0.0)
    .lineTo(0.25 * 0.75, 0.125 * 0.75)
    .lineTo(0.5 * 0.75, 0.125 * 0.75)
    .lineTo(0.5 * 0.75, 0.375 * 0.75)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.75 * 0.75, 0.625 * 0.75)
    .lineTo(0.0, 0.625 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.5)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_799.stl"output_799.stl