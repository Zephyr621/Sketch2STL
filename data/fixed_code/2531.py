import cadquery as cq
from cadquery.vis import show
# --- Part 1: Hexagonal Cylinder ---
sketch_scale = 0.75
height = 0.3214
# Scaled coordinates for the hexagon
points = [
    (0.0 * sketch_scale, 0.3214 * sketch_scale),
    (0.1875 * sketch_scale, 0.0 * sketch_scale),
    (0.5625 * sketch_scale, 0.0 * sketch_scale),
    (0.75 * sketch_scale, 0.3214 * sketch_scale),
    (0.5625 * sketch_scale, 0.6495 * sketch_scale)
]
# Create the hexagonal base
hex_base = cq.Workplane("XY").polyline(points).close().extrude(height)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = hex_base
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_2531.stl"output_2531.stl