import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1562 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0563 * sketch_scale)
    .lineTo(0.0352 * sketch_scale, 0.0)
    .lineTo(0.7353 * sketch_scale, 0.0)
    .lineTo(0.75 * sketch_scale, 0.0563 * sketch_scale)
    .lineTo(0.7353 * sketch_scale, 0.3125 * sketch_scale)
    .lineTo(0.0, 0.3125 * sketch_scale)
    .close()
    .moveTo(0.375 * sketch_scale, 0.0625 * sketch_scale)
    .circle(0.015 * sketch_scale)
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1562 * sketch_scale, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_2122.stl"output_2122.stl