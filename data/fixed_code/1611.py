import cadquery as cq
# --- Part 1: Cube with Corner Cut Off ---
cube_size = 0.5 * 0.5  # Scaled cube size
cutout_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(-cutout_depth)
)
# Create the first cutout
cutout_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0.25 * 0.5)
    .lineTo(0.25 * 0.5, 0.25 * 0.5)
    .close()
    .extrude(-cutout_depth)
)
# Create the second cutout
cutout_2 = (
    cq.Workplane("XY")
    .moveTo(0.25 * 0.5, 0.25 * 0.5)
    .lineTo(0.5 * 0.5, 0.25 * 0.5)
    .close()
    .extrude(-cutout_depth)
)
# Combine the parts
result = part_1.cut(cutout_1).cut(cutout_2)
# Export the result to a STL file
cq.cq.exporters.export({result_var}, "output_1611.stl"output_1611.stl