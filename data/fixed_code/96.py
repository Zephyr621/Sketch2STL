import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.4167 * 0.75  # Scaled width
height = 0.0833
hole_radius = 0.0417 * 0.75  # Scaled radius
hole_center_x = 0.375 * 0.75  # Scaled x-coordinate of the hole center
hole_center_y = 0.2167 * 0.75  # Scaled y-coordinate of the hole center
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - length/2, hole_center_y - width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0833, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.cq.exporters.export({result_var}, "output_96.stl"output_96.stl