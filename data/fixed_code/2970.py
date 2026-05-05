import cadquery as cq
from cadquery.vis import show
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3 * 0.75)
    .lineTo(0.45 * 0.75, 0.6 * 0.75)
    .lineTo(0.0, 0.6 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.225)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.225, 0))
# --- Part 2: Triangular Prism ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3 * 0.3, 0.15 * 0.3)
    .lineTo(0.3 * 0.3, 0.15 * 0.3)
    .lineTo(0.0, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2970.stl