import cadquery as cq
# --- Part 1: Rectangular Box ---
length = 0.75 * 0.75  # Scaled length
width = 0.625 * 0.75  # Scaled width
height = 0.5
inner_length = 0.7125 * 0.75
inner_width = 0.625 * 0.75
outer_rect = cq.Workplane("XY").rect(length, width).extrude(height)
inner_rect = cq.Workplane("XY").rect(inner_length, inner_width).translate((0,0,0))
part_1 = outer_rect.cut(inner_rect)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.cq.exporters.export(assembly,
# 定义结果变量
result = inner_rect
# 导出为STL文件
cq.exporters.export(result, "output_2795.stl