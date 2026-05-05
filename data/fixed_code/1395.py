import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.0625)
    .lineTo(0.5625, 0.0625)
    .lineTo(0.5625, 0.2109)
    .lineTo(0.1875, 0.2109)
    .lineTo(0.1875, 0.0625)
    .lineTo(0.0, 0.0625)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0625 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0625, 0))
# --- Part 2: Cylindrical Rod with Rounded Top ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1395.stl