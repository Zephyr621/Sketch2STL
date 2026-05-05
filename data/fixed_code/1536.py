import cadquery as cq
# --- Part 1 ---
length = 0.75 * 0.75  # Scaled length
width = 0.25 * 0.75  # Scaled width
height = 0.375
hole_radius = 0.05 * 0.75
hole1_x = 0.125 * 0.75
hole1_y = 0.125 * 0.75
hole2_x = 0.625 * 0.75
hole2_y = 0.125 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole1_x - length/2, hole1_y - width/2), (hole2_x - length/2, hole2_y - width/2)])
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
cq.cq.exporters.export({result_var}, "output_1536.stl"output_1536.stl