import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0938 * 0.75)
    .lineTo(0.0295 * 0.75, 0.0)
    .threePointArc((0.375 * 0.75, 0.0306 * 0.75), (0.7222 * 0.75, 0.0295 * 0.75))
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.7222 * 0.75, 0.2597 * 0.75)
    .threePointArc((0.375 * 0.75, 0.2479 * 0.75), (0.4667 * 0.75, 0.2398 * 0.75))
    .lineTo(0.2773 * 0.75, 0.2597 * 0.75)
    .threePointArc((0.1301 * 0.75, 0.2479 * 0.75), (0.0, 0.0938 * 0.75))
    .close()
    .extrude(0.0804 + 0.0804)
)
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_3560.stl"output_3560.stl