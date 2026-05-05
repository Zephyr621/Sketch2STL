import cadquery as cq
# --- Part 1: Rectangular Prism ---
length = 0.75 * 0.75  # Scaled length
width = 0.375 * 0.75  # Scaled width
height = 0.1875
inner_offset = 0.0188 * 0.75
inner_width = (0.7031 - 0.0188) * 0.75
inner_height = (0.375 - 0.0188) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
part_1 = part_1.cut(cq.Workplane("XY").rect(inner_width, inner_height).translate((inner_offset - length/2 + inner_width/2, inner_offset - width/2 + inner_height/2, 0)).extrude(height + 0.001))
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1875, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_3292.stl