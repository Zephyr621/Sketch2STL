import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.5357 * 0.75  # Scaled width
height = 0.1071
inner_rect_x = 0.2047 * 0.75
inner_rect_y = 0.2143 * 0.75
inner_rect_size = (0.5357 - 0.2047) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(inner_rect_size, inner_rect_size)
    .extrude(height)
    .translate([inner_rect_x - length/2, inner_rect_y - width/2, 0])
)
part_1 = part_1.cut(inner_rect)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
cq.
# Export
# 导出为STL文件
cq.exporters.export(result, "output_2267.stl