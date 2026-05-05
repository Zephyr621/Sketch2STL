import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.25)
    .threePointArc((0.5, 0.3438), (0.375, 0.5656))
    .lineTo(0.0, 0.5656)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.4687 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.4687 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.cq.exporters.export({result_var}, "output_1970.stl"output_1970.stl