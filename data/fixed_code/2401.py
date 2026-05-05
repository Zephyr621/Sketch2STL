import cadquery as cq
# --- Part 1: Cube with Rectangular Frame ---
length = 0.75 * 0.75  # Scaled length
width = 0.3 * 0.75  # Scaled width
height = 0.2
inner_rect_x = 0.3214 * 0.75
inner_rect_y = 0.15 * 0.75
inner_rect_length = (0.7159 - 0.3214) * 0.75
inner_rect_width = (0.3036 - 0.15) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(inner_rect_length, inner_rect_width)
    .extrude(height + 0.1)  # Extrude slightly more to ensure complete cut
)
part_1 = part_1.cut(inner_rect)
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to ST
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2401.stl