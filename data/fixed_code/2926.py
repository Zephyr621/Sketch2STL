import cadquery as cq
# --- Part 1: Rectangular Block with Circular Hole ---
block_length = 0.75 * 0.75  # Scaled length
block_width = 0.2647 * 0.75  # Scaled width
block_height = 0.4412
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.1324 * 0.75  # Scaled center y
hole_radius = 0.0882 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(block_length, block_width)
    .extrude(block_height)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center_x - block_length/2, hole_center_y - block_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_2926.stl