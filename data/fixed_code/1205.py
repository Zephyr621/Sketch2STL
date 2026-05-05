import cadquery as cq
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Curved Edges ---
sketch_scale = 0.75
extrude_depth = 0.0375
# Scaled dimensions
length = 0.75 * sketch_scale
width = 0.4687 * sketch_scale
arc_mid_x = 0.375 * sketch_scale
arc_mid_y = 0.2344 * sketch_scale
hole_center_x = 0.1875 * sketch_scale
hole_center_y = 0.1719 * sketch_scale
hole_radius = 0.0188 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .threePointArc((length + arc_mid_x, arc_mid_y), (length, width))
    .lineTo(0, width)
    .close()
    .extrude(extrude_depth)
)
# Create the holes
part_1 = part_1.faces(">Z").workplane().pushPoints([(hole_center_x - length/2, hole_center_y - width/2)]).hole(2 * hole_radius)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_1205.stl"output_1205.stl