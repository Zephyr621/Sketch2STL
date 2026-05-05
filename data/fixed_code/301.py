import cadquery as cq
# --- Part 1: Cube with Hole ---
side_length = 0.75 * 0.75  # Sketch side length scaled
hole_size = (0.5 - 0.2188) * 0.75  # Sketch side length scaled
cube_height = 0.0312
# Create the basic cube
cube = cq.Workplane("XY").rect(side_length, side_length).extrude(cube_height)
# Create the hole
hole = cq.Workplane("XY").rect(hole_size, hole_size).extrude(cube_height + 0.1) # Extrude slightly more to ensure full cut
# Cut the hole from the cube
result = cube.cut(hole)
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union()
# 导出为STL文件
cq.exporters.export(result, "output_301.stl