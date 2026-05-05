import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped base ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.375 * 0.5625, 0.0)
    .lineTo(0.375 * 0.5625, 0.2812 * 0.5625)
    .lineTo(0.1875 * 0.5625, 0.2812 * 0.5625)
    .lineTo(0.1875 * 0.5625, 0.5625 * 0.5625)
    .lineTo(0.0, 0.5625 * 0.5625)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.5625)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder on top ---
part_2_radius = 0.0937 * 0.1875
part_2_height = 0.125
part_2 = (
    cq.Workplane("XY")
    .workplane(offset=0.1875)
    .moveTo(
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1027.stl