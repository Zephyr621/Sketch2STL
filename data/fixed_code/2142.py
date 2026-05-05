import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1667)
    .threePointArc((0.5738, 0.2126), (0.5931, 0.4687))
    .lineTo(0.2383, 0.4687)
    .lineTo(0.0, 0.2417)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1071 + 0.1071)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1071, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_2142.stl"output_2142.stl