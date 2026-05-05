import cadquery as cq
from math import *
# --- Part 1 ---
sketch_scale = 0.0114
extrude_depth = 0.0278
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0074 * sketch_scale, 0.0)
    .lineTo(0.0074 * sketch_scale, 0.0114 * sketch_scale)
    .lineTo(0.0, 0.0114 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# Add holes
hole_radius = 0.0037 * sketch_scale
part_1 = part_1.faces(">Z").workplane().pushPoints([(0.0074 * sketch_scale - (0.0074 * sketch_scale)/2, 0.0074 * sketch_scale - (0.0074 * sketch_scale)/2)]).hole(2 * hole_radius)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.0698, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.cq.exporters.export({result_var}, "output_715.stl"output_715.stl