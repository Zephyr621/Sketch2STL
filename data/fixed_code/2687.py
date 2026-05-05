import cadquery as cq
# --- Part 1 ---
outer_rect_width = 0.1594 * 0.75
outer_rect_height = 0.1875 * 0.75
inner_rect_x = 0.2257 * 0.75
inner_rect_y = 0.0937 * 0.75
inner_rect_length = (0.4565 - 0.1928) * 0.75
extrude_depth = 0.1562
wp = cq.Workplane("XY")
outer_rect = wp.moveTo(0, 0).lineTo(outer_rect_width, 0).lineTo(outer_rect_width, outer_rect_height).lineTo(0, outer_rect_height).close()
inner_rect = cq.Workplane("XY").moveTo(inner_rect_x, inner_rect_y).lineTo(inner_rect_length, inner_rect_y).lineTo(inner_rect_length, inner_rect_width).lineTo(inner_rect_x, inner_rect_y).lineTo(inner_rect_x, inner_rect_y).close()
part_1 = outer_rect.extrude(extrude_depth)
# Cut out the inner rectangles
part_1 = part_1.cut(inner_rect.extrude(extrude_depth + 0.1)) # Extrude slightly more to ensure complete cut
# Export
# 定义结果变量
result = inner_rect
# 导出为STL文件
cq.exporters.export(result, "output_2687.stl