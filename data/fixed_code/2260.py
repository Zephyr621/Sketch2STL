import cadquery as cq
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1875)
    .lineTo(0.5156, 0.4687)
    .lineTo(0.2511, 0.4687)
    .lineTo(0.0, 0.2812)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0191 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0191 * 0.75, 0))
# --- Assembly ---
assembly = part_1
cq.
cq.
cq.
cq.exporters
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2260.stl