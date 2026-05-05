import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0904 * 0.75, 0.0)
    .threePointArc((0.0904 * 0.75, 0.1446 * 0.75), (0.1881 * 0.75, 0.6098 * 0.75))
    .lineTo(0.1705 * 0.75, 0.6098 * 0.75)
    .threePointArc((0.0895 * 0.75, 0.7132 * 0.75), (0.0703 * 0.75, 0.7031 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0325 + 0.0325)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0336, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1750.stl"output_1750.stl