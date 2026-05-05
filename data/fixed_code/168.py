import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.15 * 0.75), (0.525 * 0.75, 0.075 * 0.75))
    .lineTo(0.0, 0.075 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.075)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_168.stl"output_168.stl