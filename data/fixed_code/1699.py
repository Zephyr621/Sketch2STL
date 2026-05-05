import cadquery as cq
# --- Part 1: Rectangular Frame ---
outer_rect_width = 0.5625 * 0.75  # Scaled width
outer_rect_length = 0.75 * 0.75  # Scaled length
inner_rect_offset = 0.0188 * 0.75  # Scaled offset for inner rectangle
height = 0.0188
part_1 = (
    cq.Workplane("XY")
    .rect(outer_rect_width, outer_rect_length)
    .extrude(height)
)
inner_rect = (
    cq.Workplane("XY")
    .rect(outer_rect_width - 2 * inner_rect_offset, outer_rect_length - 2 * inner_rect_offset)
    .extrude(height)
)
part_1 = part_1.cut(inner_rect)
# --- Part 2: Rectangular Block ---
block_width = 0.0562 * 0.75  # Scaled width
block_length = 0.75 * 0.75  # Scaled length
block_height = 0.01875
part_2 = (
    cq.Workplane("XY")
    .rect(block_width, block_length)
    .extrude(block_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1699.stl