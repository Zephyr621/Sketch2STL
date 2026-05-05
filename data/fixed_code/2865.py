import cadquery as cq
# --- Part 1: Rectangular Prism with Cutout ---
length = 0.75 * 0.75  # Scaled length
width = 0.2753 * 0.75  # Scaled width
height = 0.0833
cutout_x1 = 0.0417 * 0.75
cutout_y1 = 0.1042 * 0.75
cutout_x2 = 0.6151 * 0.75
cutout_y2 = 0.2083 * 0.75
cutout_x3 = 0.6618 * 0.75
cutout_y3 = 0.2083 * 0.75
outer_rect = cq.Workplane("XY").rect(length, width).extrude(height)
inner_rect = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(cutout_x1 - length/2, 0)
    .lineTo(cutout_x1 - length/2, width)
    .lineTo(0, width)
    .close()
    .extrude(height + 0.001)  # Extrude slightly more to ensure complete cut
)
part_1 = outer_rect.cut(inner_rect)
# --- Coordinate System Transformation for Part
# Export
# 定义结果变量
result = outer_rect
# 导出为STL文件
cq.exporters.export(result, "output_2865.stl