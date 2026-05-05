import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Block with Rounded Edges ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.4286 * sketch_scale
height = 0.2143
# Define the points for the sketch
points = [
    (0.0, 0.1429),
    (0.1719 * sketch_scale, 0.0),
    (0.5357 * sketch_scale, 0.0),
    (0.7357 * sketch_scale, 0.1429),
    (0.75 * sketch_scale, 0.1429)
]
# Create the sketch using the scaled points
part_1 = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(height)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
# Export to STL
cq.exporters.export({result_var}, "output_405.stl"output_405.stl