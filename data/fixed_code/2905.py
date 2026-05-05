import cadquery as cq
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
extrude_depth = 0.5
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.6 * sketch_scale)
    .lineTo(0.3 * sketch_scale, 0.6 * sketch_scale)
    .lineTo(0.3 * sketch_scale, 0.25 * sketch_scale)
    .lineTo(0.125 * sketch_scale, 0.25 * sketch_scale)
    .lineTo(0.125 * sketch_scale, 0.6 * sketch_scale)
    .lineTo(0.0, 0.6 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_2905.stl"output_2905.stl