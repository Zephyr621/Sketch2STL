import cadquery as cq
# --- Part 1: Cube with Cutout ---
cube_size = 0.75 * 0.75  # Scaled cube size
cutout_width = (0.5 - 0.2812) * 0.75  # Scaled cutout width
cutout_height = (0.625 - 0.0313) * 0.75  # Scaled cutout height
depth = 0.5
# Create the cube
cube = cq.Workplane("XY").box(cube_size, cube_size, depth)
# Create the cutout
cutout = (
    cq.Workplane("XY")
    .moveTo(0, 0.25)
    .lineTo(0.375 * 0.75, 0.25)
    .lineTo(0.375 * 0.75, 0.0313 * 0.75)
    .lineTo(0.125 * 0.75, 0.0313 * 0.75)
    .lineTo(0.125 * 0.75, 0.25)
    .close()
    .extrude(-depth)  # Extrude in the opposite direction
)
# Subtract the cutout from the cube
result = cube.cut(cutout)
# Export the result to a STL file
cq.
# --- Final Result ---
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_2252.stl