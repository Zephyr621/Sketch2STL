import cadquery as cq
# --- Part 1: Rectangular Plate with Hole ---
plate_length = 0.4286 * 0.4286  # Scaled length
plate_width = 0.2514 * 0.4286   # Scaled width
plate_height = 0.0536
hole_center_x = 0.2143 * 0.4286  # Scaled center x
hole_center_y = 0.1257 * 0.4286  # Scaled center y
hole_radius = 0.0656 * 0.4286   # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(plate_length, plate_width)
    .extrude(plate_height)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center_x - plate_length/2, hole_center_y - plate_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# 导出为STL文件
cq.exporters.export(result, "output_54.stl