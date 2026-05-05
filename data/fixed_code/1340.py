import cadquery as cq
# --- Part 1: Rectangular Box with Cutout ---
outer_width = 0.75 * 0.75  # Scaled width
outer_height = 0.5625 * 0.75  # Scaled height
inner_offset = 0.0274 * 0.75  # Scaled offset for inner rectangle
extrude_depth = 0.1875 + 0.1875  # Total extrusion depth (both directions)
outer_rect = cq.Workplane("XY").rect(outer_width, outer_height).extrude(extrude_depth)
inner_rect = cq.Workplane("XY").rect(outer_width - 2 * inner_offset, outer_height - 2 * inner_offset).extrude(extrude_depth)
part_1 = outer_rect.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.exporters
# 定义结果变量
result = inner_rect
# 导出为STL文件
cq.exporters.export(result, "output_1340.stl