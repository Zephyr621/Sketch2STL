import cadquery as cq
# --- Part 1: Rectangular Trough ---
part_1_width = 0.75 * 0.75  # Sketch width scaled
part_1_height = 0.625 * 0.75  # Sketch height scaled
part_1_depth = 0.2206
inner_width = (0.375 - 0.5341) * 0.75
inner_height = (0.3125 - 0.4687) * 0.75
inner_x = 0.5341 * 0.75
inner_y = 0.4687 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(part_1_depth)
)
inner_box = (
    cq.Workplane("XY")
    .rect(inner_width, inner_height)
    .extrude(part_1_depth + 0.1)  # Extrude slightly more to ensure complete cut
    .translate((-part_1_width/2 + inner_width/2 + inner_height/2, 0, part_1_depth/2))
)
part_1 = part_1.cut(inner_box
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2045.stl