import cadquery as cq
# --- Part 1: Cube with Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.1875
inner_rect_x = 0.1034 * 0.75
inner_rect_y = 0.1034 * 0.75
inner_rect_width = (0.2159 - 0.1034) * 0.75
inner_rect_height = (0.3969 - 0.1034) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
hole = (
    cq.Workplane("XY")
    .rect(inner_rect_width, inner_rect_height)
    .translate([inner_rect_x - length/2 + inner_rect_width / 2, inner_rect_y - width/2 + inner_rect_height / 2, 0])
    .extrude(height + 0.001)  # Extrude slightly more to ensure complete cut
)
part_1 = part_1.cut(hole)
# --- Coordinate System Transformation for
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2135.stl