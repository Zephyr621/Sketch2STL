import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0625)
    .lineTo(0.5938, 0.0625)
    .threePointArc((0.375, 0.0369), (0.3913, 0.0625))
    .lineTo(0.3913, 0.075)
    .lineTo(0.7188, 0.075)
    .threePointArc((0.375, 0.0369), (0.7188, 0.15))
    .lineTo(0.0, 0.15)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0625)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_2575.stl"output_2575.stl