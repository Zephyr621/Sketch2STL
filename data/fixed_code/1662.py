import cadquery as cq
# --- Part 1: Rectangular Box with Cutouts ---
length = 0.75 * 0.75  # Scaled length
width = 0.4167 * 0.75  # Scaled width
height = 0.3333  # Height
inner_offset = 0.0167 * 0.75  # Scaled offset for inner rectangle
outer_rect = cq.Workplane("XY").rect(length, width).extrude(height)
inner_rect = (
    cq.Workplane("XY")
    .moveTo(0, width - inner_offset)
    .lineTo(length - inner_offset, width - inner_offset)
    .lineTo(length - inner_offset, width)
    .lineTo(length, width)
    .close()
    .extrude(height + 0.1)  # Extrude slightly more to ensure complete cut
)
part_1 = outer_rect.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3333, 0))
# --- Assembly ---
assembly = part_1
# --- Export to STL ---
cq
# Export
# 定义结果变量
result = outer_rect
# 导出为STL文件
cq.exporters.export(result, "output_1662.stl