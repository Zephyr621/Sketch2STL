import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.5357 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.1844 * 0.75), (0.5357 * 0.75, 0.5636 * 0.75))
    .lineTo(0.2802 * 0.75, 0.5636 * 0.75)
    .lineTo(0.2802 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.0)
    .lineTo(0.375 * 0.75, 0.4286 * 0.75)
    .lineTo(0.0, 0.4286 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1419 * 0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3529.stl