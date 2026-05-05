import cadquery as cq
import math
from cadquery import exporters
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0433 * 0.75)
    .threePointArc((0.0951 * 0.75, 0.0), (0.2499 * 0.75, 0.0433 * 0.75))
    .lineTo(0.2499 * 0.75, 0.5402 * 0.75)
    .threePointArc((0.6916 * 0.75, 0.4884 * 0.75), (0.6867 * 0.75, 0.5402 * 0.75))
    .lineTo(0.6867 * 0.75, 0.5391 * 0.75)
    .threePointArc((0.6916 * 0.75, 0.5546 * 0.75), (0.0, 0.5391 * 0.75))
    .lineTo(0.0, 0.0433 * 0.75)
    .close()
    .extrude(0.0045)
)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.exporters.export({result_var}, "output_3404.stl"output_3404.stl