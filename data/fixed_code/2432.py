import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1667)
    .lineTo(0.5833, 0.1667)
    .threePointArc((0.375, 0.0833), (0.3173, 0.3214))
    .lineTo(0.2167, 0.3214)
    .threePointArc((0.1253, 0.0934), (0.0, 0.1667))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0536)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0536, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_2432.stl"output_2432.stl