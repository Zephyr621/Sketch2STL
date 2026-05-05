import cadquery as cq
# --- Part 1 ---
outer_rect_width = 0.75 * 0.75
outer_rect_height = 0.3518 * 0.75
inner_rect_width = (0.7143 - 0.0923) * 0.75
inner_rect_height = (0.3745 - 0.1294) * 0.75
extrude_depth = 0.1471
part_1 = (
    cq.Workplane("XY")
    .rect(outer_rect_width, outer_rect_height)
    .extrude(extrude_depth)
)
inner_cut = (
    cq.Workplane("XY")
    .rect(inner_rect_width, inner_rect_height)
    .extrude(extrude_depth)
)
part_1 = part_1.cut(inner_cut)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1471, 0))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2402.stl