import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.1089 * 0.1935, 0.0079 * 0.1935)
    .lineTo(0.0104 * 0.1935, 0.1793 * 0.1935)
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
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2791.stl"output_2791.stl