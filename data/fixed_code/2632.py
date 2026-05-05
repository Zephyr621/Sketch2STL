import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
cube_size = 0.75 * 0.75  # Sketch size scaled
hole_radius = 0.1875 * 0.75  # Sketch radius scaled
cube_height = 0.3
part_1 = (
    cq.Workplane("XY")
    .rect(cube_size, cube_size)
    .extrude(cube_height)
    .faces(">Z").workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2632.stl