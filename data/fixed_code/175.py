import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1355 * 0.75)
    .lineTo(0.2344 * 0.75, 0.1355 * 0.75)
    .lineTo(0.2344 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2727 * 0.75)
    .lineTo(0.0, 0.2727 * 0.75)
    .close()
    .extrude(0.0056)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0056, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_175.stl"output_175.stl