import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.2708 * 0.75)
    .lineTo(0.1868 * 0.75, 0.1363 * 0.75)
    .lineTo(0.375 * 0.75, 0.1363 * 0.75)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)
    .lineTo(0.0, 0.4687 * 0.75)
    .close()
    .extrude(0.3693)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3693, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_1383.stl"output_1383.stl