import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2468 * sketch_scale
height = 0.0417
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length/2, 0), (0.6094 * sketch_scale, 0.2468 * sketch_scale))
    .lineTo(length - 0.0833 * sketch_scale, width)
    .threePointArc((length - 0.0833 * sketch_scale, width), (0, width))
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0417, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1279.stl"output_1279.stl