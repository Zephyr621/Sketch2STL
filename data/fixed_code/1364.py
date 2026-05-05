import cadquery as cq
# --- Part 1: Rectangular Block with Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.5294 * 0.75  # Scaled width
height = 0.0816
hole_radius = 0.0232 * 0.75  # Scaled radius
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.2167 * 0.75  # Scaled center y
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center_x - length/2, hole_center_y - width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0477))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1364.stl"output_1364.stl