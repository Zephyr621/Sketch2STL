import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0625)
    .lineTo(0.5938, 0.0625)
    .lineTo(0.5938, 0.125)
    .lineTo(0.4576, 0.125)
    .lineTo(0.4576, 0.0625)
    .lineTo(0.3125, 0.0625)
    .lineTo(0.3125, 0.1875)
    .lineTo(0.0363, 0.1875)
    .lineTo(0.0363, 0.125)
    .lineTo(0.0, 0.125)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.375/2)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1613.stl