import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0099 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.3103 * sketch_scale)
    .threePointArc((0.0635 * sketch_scale, 0.0635 * sketch_scale), (0.3103 * sketch_scale, 0.0))
    .lineTo(0.7467 * sketch_scale, 0.0)
    .threePointArc((0.7031 * sketch_scale, 0.0635 * sketch_scale), (0.75 * sketch_scale, 0.3103 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.4687 * sketch_scale)
    .threePointArc((0.7031 * sketch_scale, 0.4032 * sketch_scale), (0.7467 * sketch_scale, 0.3937 * sketch_scale))
    .lineTo(0.0, 0.3937 * sketch_scale)
    .lineTo(0.0, 0.3103 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_3574.stl"output_3574.stl