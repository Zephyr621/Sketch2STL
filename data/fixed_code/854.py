import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0833)
    .lineTo(0.6667, 0.0833)
    .lineTo(0.6667, 0.4167)
    .lineTo(0.1667, 0.4167)
    .lineTo(0.1667, 0.3733)
    .lineTo(0.0, 0.3733)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1705)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_854.stl"output_854.stl