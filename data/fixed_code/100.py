import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0484 * 0.75)
    .lineTo(0.0484 * 0.75, 0.0484 * 0.75)
    .lineTo(0.0484 * 0.75, 0.1792 * 0.75)
    .lineTo(0.0234 * 0.75, 0.1792 * 0.75)
    .lineTo(0.0234 * 0.75, 0.0)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0816)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0816, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_100.stl"output_100.stl