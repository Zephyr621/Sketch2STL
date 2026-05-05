import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.25 * 0.75)
    .lineTo(0.0, 0.25 * 0.75)
    .threePointArc((0.375 * 0.75, 0.2435 * 0.75), (0.75 * 0.75, 0.25 * 0.75))
    .lineTo(0.75 * 0.75, 0.5 * 0.75)
    .threePointArc((0.375 * 0.75, 0.3965 * 0.75), (0.0, 0.5 * 0.75))
    .lineTo(0.0, 0.25 * 0.75)
    .close()
    .extrude(0.05)
)
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_3440.stl"output_3440.stl