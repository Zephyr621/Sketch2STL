import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4261 * 0.4412, 0.0)
    .lineTo(0.4261 * 0.4412, 0.1364 * 0.4412)
    .lineTo(0.0397 * 0.4412, 0.1364 * 0.4412)
    .lineTo(0.0397 * 0.4412, 0.2211 * 0.4412)
    .lineTo(0.0, 0.2211 * 0.4412)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1126.stl"output_1126.stl