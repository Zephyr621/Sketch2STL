import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.25 * 0.75), (0.125 * 0.75, 0.625 * 0.75))
    .lineTo(0.0, 0.625 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.5)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.cq.exporters.export({result_var}, "output_763.stl"output_763.stl