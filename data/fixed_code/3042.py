import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.375
hole_radius = 0.0469 * 0.75  # Scaled radius
small_hole_x = 0.2437 * 0.75  # Scaled x position
small_hole_y = 0.1875 * 0.75  # Scaled y position
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .moveTo(small_hole_x - length/2, small_hole_y - width/2)
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
# Export to ST
# 导出为STL文件
cq.exporters.export(result, "output_3042.stl