import cadquery as cq
# --- Part 1: Rectangular Frame ---
outer_rect_width = 0.5 * 0.75  # Scaled width
outer_rect_height = 0.75 * 0.75 # Scaled height
inner_rect_x_offset = 0.0138 * 0.75
inner_rect_y_offset = 0.0313 * 0.75
frame_thickness = 0.0312
part_1 = (
    cq.Workplane("XY")
    .rect(outer_rect_width, outer_rect_height)
    .extrude(frame_thickness)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(inner_rect_width, inner_rect_height)
    .translate((inner_rect_x_offset - outer_rect_width/2 + inner_rect_x_offset, inner_rect_y_offset - outer_rect_height/2 + inner_rect_y_offset, 0))
)
part_1 = part_1.cut(inner_rect)
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_726.stl