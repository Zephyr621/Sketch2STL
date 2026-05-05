import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Rounded Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.5 * 0.75  # Scaled width
height = 0.375
# Define corner radius (scaled)
corner_radius = min(length, width) / 10  # Adjust as needed
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, corner_radius)
    .lineTo(length - corner_radius, 0)
    .threePointArc((length, corner_radius), (length - corner_radius, width))
    .lineTo(corner_radius, width)
    .threePointArc((0, corner_radius), (0, corner_radius))
    .close()
    .extrude(height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_3043.stl"output_3043.stl