import cadquery as cq
# --- Part 1: Rectangular Bracket ---
outer_rect_width = 0.75 * 0.75  # Scaled width
outer_rect_height = 0.3545 * 0.75  # Scaled height
inner_rect_x1 = 0.0214 * 0.75  # Scaled x-coordinate of inner rectangle
inner_rect_y1 = 0.3271 * 0.75  # Scaled y-coordinate of inner rectangle
inner_rect_x2 = 0.7286 * 0.75  # Scaled x-coordinate of inner rectangle
inner_rect_y2 = 0.3976 * 0.75  # Scaled y-coordinate of inner rectangle
extrude_depth = 0.0214
part_1 = (
    cq.Workplane("XY")
    .rect(outer_rect_width, outer_rect_height)
    .moveTo(inner_rect_x1 - outer_rect_width/2, inner_rect_y1 - outer_rect_height/2)
    .lineTo(inner_rect_x2 - outer_rect_width/2, inner_rect_y2 - outer_rect_height/2)
    .lineTo(inner_rect_x2 - outer_rect_width/2, inner_rect_y3 - outer
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1955.stl