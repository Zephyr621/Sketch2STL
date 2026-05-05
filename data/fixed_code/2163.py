import cadquery as cq
# --- Part 1: Rectangular Object with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.1364 * 0.75  # Scaled width
height = 0.0268
cutout_x = 0.2382 * 0.75  # Scaled cutout x
cutout_y = 0.0536 * 0.75  # Scaled cutout y
cutout_size = (0.4286 - 0.2382) * 0.75  # Scaled cutout size
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
    .rect(cutout_size, cutout_size, centered=False).cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0268, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.cq.exporters.export({result_var}, "output_2163.stl"output_2163.stl