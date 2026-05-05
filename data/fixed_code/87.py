import cadquery as cq
# --- Part 1: Cube with Hole ---
length = 0.5785 * 0.5785  # Scaled length
width = 0.2708 * 0.5785  # Scaled width
height = 0.75
hole_radius = 0.1607 * 0.5785  # Scaled radius
hole_center_x = 0.2885 * 0.5785  # Scaled center x
hole_center_y = 0.1351 * 0.5785  # Scaled center y
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
cq.
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_87.stl