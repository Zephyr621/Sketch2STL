import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1875)
    .threePointArc((0.6125, 0.1562), (0.5625, 0.375))
    .lineTo(0.375, 0.375)
    .lineTo(0.1875, 0.375)
    .threePointArc((0.0375, 0.1562), (0.0, 0.1875))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0625)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1720.stl"output_1720.stl