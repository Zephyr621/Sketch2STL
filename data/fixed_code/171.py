import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: S shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.3396 * 2  # Total extrusion depth (both directions)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1154 * sketch_scale, 0)
    .lineTo(0.6207 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.1518 * sketch_scale), (0.6207 * sketch_scale, 0.3914 * sketch_scale))
    .lineTo(0.1154 * sketch_scale, 0.3914 * sketch_scale)
    .threePointArc((0, 0.1518 * sketch_scale), (0.1154 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0477))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_171.stl"output_171.stl