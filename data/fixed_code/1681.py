import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1642 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0015 * sketch_scale)
    .lineTo(0.0368 * sketch_scale, 0.0015 * sketch_scale)
    .lineTo(0.7188 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.4375 * sketch_scale)
    .lineTo(0.7188 * sketch_scale, 0.5047 * sketch_scale)
    .lineTo(0.0, 0.5047 * sketch_scale)
    .lineTo(0.0, 0.0015 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1642 * sketch_scale, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_1681.stl"output_1681.stl