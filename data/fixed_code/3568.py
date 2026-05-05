import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.5469 * 0.75  # Scaled width
height = 0.1692
hole_center_x = 0.375 * 0.75  # Scaled hole center x
hole_center_y = 0.2771 * 0.75  # Scaled hole center y
hole_radius = 0.0625 * 0.75  # Scaled hole radius
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z").workplane()
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
cq
# 导出为STL文件
cq.exporters.export(result, "output_3568.stl