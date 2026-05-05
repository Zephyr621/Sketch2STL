import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder with Hexagonal Hole ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_hex_side = (0.4992 - 0.1406) * 0.75 # Approximate side length based on the provided coordinates
height = 0.0938
# Create the hexagon profile
hexagon = cq.Workplane("XY").polygon(6, 2*outer_radius/2)
# Create the hole by extruding the hexagon
hole = cq.Workplane("XY").moveTo(0.0706 * 0.75, 0.1406 * 0.75).lineTo(0.6495 * 0.75, 0.1406 * 0.75).threePointArc((0.75 * 0.75, 0.375 * 0.75), (0.6495 * 0.75, 0.1406 * 0.75)).close().extrude(height)
# Subtract the hole from the hexagon
result = hexagon.cut(hole)
# Export the result to a STL file
cq.
# --- Coordinate System Transformation for Part 1 ---
result = result.rotate((0, 0, 0), (0, 0, 1), -90)
result = result.translate((0, 0.0938, 0))
# Export the result to a STL file
cq.cq.exporters.export({result_var}, "output_3539.stl"output_3539.stl