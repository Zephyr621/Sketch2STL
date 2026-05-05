import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1905)
    .lineTo(0.3125, 0.1905)
    .lineTo(0.3125, 0.1688)
    .lineTo(0.2591, 0.1688)
    .lineTo(0.2591, 0.3938)
    .lineTo(0.0, 0.3938)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3398 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3398 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1689.stl"output_1689.stl