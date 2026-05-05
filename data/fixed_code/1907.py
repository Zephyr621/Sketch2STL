import cadquery as cq
from cadquery.vis import show
# --- Part 1: Staircase ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0075 * 0.1807)
    .lineTo(0.0008 * 0.1807, 0.0008 * 0.1807)
    .lineTo(0.0008 * 0.1807, 0.0)
    .lineTo(0.1406 * 0.1807, 0.0)
    .lineTo(0.1406 * 0.1807, 0.1807 * 0.1807)
    .lineTo(0.0833 * 0.1807, 0.1807 * 0.1807)
    .lineTo(0.0833 * 0.1807, 0.0577 * 0.1807)
    .lineTo(0.0, 0.0577 * 0.1807)
    .lineTo(0.0, 0.0075 * 0.1807)
    .close()
    .extrude(0.1885)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.375, 0))
# --- Assembly ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1907.stl