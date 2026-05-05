import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.4125)
    .lineTo(0.4375, 0.4125)
    .lineTo(0.4375, 0.2031)
    .lineTo(0.0, 0.2031)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.3409 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3409 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3068.stl"output_3068.stl