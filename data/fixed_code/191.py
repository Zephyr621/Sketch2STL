import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.2163)
    .lineTo(0.4167, 0.2163)
    .lineTo(0.4167, 0.4167)
    .lineTo(0.0, 0.4167)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1867 * 2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2917, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_191.stl"output_191.stl