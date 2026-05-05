import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1807)
    .lineTo(0.5357, 0.1807)
    .lineTo(0.5357, 0.1442)
    .lineTo(0.2816, 0.1442)
    .lineTo(0.2816, 0.1807)
    .lineTo(0.0, 0.1807)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0547 + 0.0547)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0547, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_750.stl"output_750.stl