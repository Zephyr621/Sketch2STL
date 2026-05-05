import cadquery as cq
# --- Part 1: Rectangular Prism with Rectangular Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.25 * 0.75   # Scaled width
height = 0.1875 + 0.1875  # Total extrusion depth
inner_rect_x = 0.0937 * 0.75
inner_rect_y = 0.0417 * 0.75
inner_rect_size = (0.2812 - 0.0937) * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
cutout = (
    cq.Workplane("XY")
    .rect(inner_rect_size, inner_rect_size)
    .extrude(height)
    .translate((inner_rect_x - length/2, inner_rect_y - width/2, 0))
)
part_1 = part_1.cut(cutout)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_837.stl