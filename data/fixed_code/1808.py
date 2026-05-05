import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1406)
    .lineTo(0.5156, 0.1406)
    .lineTo(0.5156, 0.2873)
    .lineTo(0.3268, 0.2873)
    .lineTo(0.3268, 0.1406)
    .lineTo(0.2587, 0.1406)
    .lineTo(0.2587, 0.1406)
    .lineTo(0.0, 0.1406)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2143 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2143 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_1808.stl"output_1808.stl