import cadquery as cq
# --- Part 1: Cube with Cylindrical Top and Hole ---
cube_length = 0.75 * 0.75  # Scaled length
cube_width = 0.375 * 0.75  # Scaled width
cube_height = 0.375
hole_center_x = 0.1875 * 0.75  # Scaled hole center x
hole_center_y = 0.1875 * 0.75  # Scaled hole center y
hole_radius = 0.0938 * 0.75  # Scaled hole radius
part_1 = (
    cq.Workplane("XY")
    .rect(cube_length, cube_width)
    .extrude(cube_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - cube_length/2, hole_center_y - cube_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_2169.stl