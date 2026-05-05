import cadquery as cq
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1875 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * sketch_scale, 0.0)
    .lineTo(0.375 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.625 * sketch_scale, 0.125 * sketch_scale)
    .lineTo(0.625 * sketch_scale, 0.25 * sketch_scale)
    .lineTo(0.0, 0.25 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_3308.stl"output_3308.stl