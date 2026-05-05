import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Holes ---
cube_size = 0.649 * 0.649  # Scaled cube size
hole1_center = (0.0711 * 0.649, 0.3236 * 0.649)  # Scaled center
hole2_center = (0.3036 * 0.649, 0.6984 * 0.649)  # Scaled center
hole_radius = 0.0385 * 0.649  # Scaled radius
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(extrude_depth)
    .faces(">Z")
    .workplane()
    .pushPoints([hole1_center, hole2_center])
    .hole(hole_radius * 2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export({result_var}, "output_1469.stl"output_1469.stl