import cadquery as cq
# --- Part 1: Cube with Cut Off ---
cube_size = 0.75 * 0.75  # Scaled cube size
hole_radius = 0.1875 * 0.75  # Scaled hole radius
cube_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(cube_height)
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1196.stl"output_1196.stl