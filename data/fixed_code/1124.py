import cadquery as cq
# --- Part 1: Cube with Curved Edges ---
length = 0.75 * 0.75  # Scaled length
width = 0.5 * 0.75  # Scaled width
height = 0.25
inner_rect_length = (0.4962 - 0.1453) * 0.75
inner_rect_width = (0.4817 - 0.0359) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .rect(inner_rect_length, inner_rect_width)
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
cq.cq.exporters.export(result
# 导出为STL文件
cq.exporters.export(result, "output_1124.stl