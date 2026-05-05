import cadquery as cq
# --- Part 1: Cube with Hole ---
cube_size = 0.75 * 0.75  # Scaled cube size
hole_size = (0.525 - 0.1875) * 0.75  # Scaled hole size
extrude_depth = 0.075
# Create the cube
part_1 = cq.Workplane("XY").rect(cube_size, cube_size).extrude(extrude_depth)
# Create the hole
hole = cq.Workplane("XY").moveTo(0.5625 * 0.75 - cube_size/2, 0.1875 * 0.75 - cube_size/2).rect(hole_size, hole_size).extrude(extrude_depth + 0.1) # Extrude slightly more to ensure full cut
# Cut the hole from the cube
result = part_1.cut(hole)
cq.
# Export to STL
cq.
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
# 导出为STL文件
cq.exporters.export(result, "output_3035.stl