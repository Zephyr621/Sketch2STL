import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.75
extrude_depth = 0.0968
# Circle parameters (scaled)
circle1_center = (0.1875 * sketch_scale, 0.1875 * sketch_scale)
circle2_center = (0.5625 * sketch_scale, 0.1875 * sketch_scale)
circle3_center = (0.375 * sketch_scale, 0.1875 * sketch_scale)
circle4_center = (0.5625 * sketch_scale, 0.1875 * sketch_scale)
# Create the cylinder
cylinder = cq.Workplane("XY").moveTo(circle1_center[0], circle1_center[1]).circle(extrude_depth).moveTo(circle2_center[0], circle2_center[1]).circle(extrude_depth).moveTo(circle3_center[0], circle3_center[1]).circle(extrude_depth).moveTo(circle4_center[0], circle4_center[1]).circle(extrude_depth).extrude(extrude_depth)
# Combine the parts
result = cylinder
cq.cq.exporters.export({result_var}, "output_2434.stl"output_2434.stl