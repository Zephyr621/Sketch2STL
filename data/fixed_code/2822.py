import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.0577 * 0.75  # Sketch radius scaled
inner_radius = 0.0234 * 0.75  # Inner radius scaled
height = 0.0059
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0059, 0.0139, 0.0397))
# --- Assembly ---
assembly = part_1
# Export to STL
# Export to STL
# Export to STL
# Export to STL
cq.exporters.export({result_var}, "output_2822.stl"output_2822.stl