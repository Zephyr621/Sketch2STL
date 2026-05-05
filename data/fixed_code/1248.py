import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .threePointArc((0.375 * 0.75, 0.1692 * 0.75), (0.4687 * 0.75, 0.0824 * 0.75))
    .lineTo(0.4687 * 0.75, 0.5653 * 0.75)
    .threePointArc((0.75 * 0.75, 0.5694 * 0.75), (0.75 * 0.75, 0.3248 * 0.75))
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)
    .threePointArc((0.6125 * 0.75, 0.2855 * 0.75), (0.375 * 0.75, 0.3248 * 0.75))
    .lineTo(0.0, 0.4687 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(-0.1299)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1248.stl