import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cube with Triangular Cutout ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.681 * 0.682, 0.0)
    .lineTo(0.681 * 0.682, 0.4453 * 0.682)
    .lineTo(0.0, 0.4453 * 0.682)
    .close()
    .extrude(-0.1047)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Triangular Prism ---
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.681 * 0.681, 0.0)
    .lineTo(0.681 * 0.681, 0.3865 * 0.681)
    .lineTo(0.0, 0.3865 * 0.681)
    .close()
    .extrude(0.0391)
)
#
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1534.stl