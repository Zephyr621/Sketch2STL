import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.5644 * 0.5876, 0.0)
    .lineTo(0.5644 * 0.5876, 0.1678 * 0.5876)
    .lineTo(0.1678 * 0.5876, 0.1678 * 0.5876)
    .lineTo(0.1678 * 0.5876, 0.5607 * 0.5876)
    .lineTo(0.0, 0.5607 * 0.5876)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_2963.stl"output_2963.stl