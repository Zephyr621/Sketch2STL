import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4464 * 0.75)
    .lineTo(0.5182 * 0.75, 0.4464 * 0.75)
    .lineTo(0.5182 * 0.75, 0.4523 * 0.75)
    .lineTo(0.1817 * 0.75, 0.4523 * 0.75)
    .lineTo(0.1817 * 0.75, 0.4464 * 0.75)
    .lineTo(0.0, 0.4464 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0135)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0135, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_2093.stl"output_2093.stl