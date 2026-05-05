import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(1.125 * 0.9419, 0.0)
    .lineTo(1.125 * 0.9419, 0.9419 * 0.9419)
    .lineTo(0.75 * 0.9419, 0.9419 * 0.9419)
    .lineTo(0.75 * 0.9419, 0.0)
    .lineTo(0.0179 * 0.9419, 0.0)
    .lineTo(0.0179 * 0.9419, 0.9419 * 0.9419)
    .lineTo(0.0, 0.9419 * 0.9419)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0785)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0785, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_394.stl"output_394.stl