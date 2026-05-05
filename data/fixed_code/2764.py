import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1821 * 0.75)
    .lineTo(0.1079 * 0.75, 0.0)
    .lineTo(0.5059 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1821 * 0.75)
    .lineTo(0.75 * 0.75, 0.5639 * 0.75)
    .lineTo(0.0, 0.5639 * 0.75)
    .lineTo(0.0, 0.1821 * 0.75)
    .close()
    .extrude(0.0065)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0065, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_2764.stl"output_2764.stl