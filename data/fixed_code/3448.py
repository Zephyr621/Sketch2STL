import cadquery as cq
from cadquery.vis import show
# --- Part 1: Square Block with Circular Hole ---
block_length = 0.75 * 0.75  # Scaled length
block_width = 0.7188 * 0.75  # Scaled width
block_height = 0.2344
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.3439 * 0.75  # Scaled center y
hole_radius = 0.1172 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(block_length, block_width)
    .extrude(block_height)
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
cq.
# Export to STL
cq.exporters.
# 导出为STL文件
cq.exporters.export(result, "output_3448.stl