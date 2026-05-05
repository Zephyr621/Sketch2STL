import cadquery as cq
# --- Part 1: Rectangular Hollow Section ---
outer_rect_width = 0.0312 * 0.075  # Scaled width
outer_rect_height = 0.075 * 0.075  # Scaled height
inner_rect_offset = 0.0156 * 0.075  # Scaled offset
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(outer_rect_width, outer_rect_height)
    .extrude(extrude_depth)
    .faces(">Z").workplane()
    .rect(outer_rect_width - 2 * inner_rect_offset, outer_rect_height - 2 * inner_rect_offset)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
#
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_979.stl