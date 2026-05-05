import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Curved Top ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.4125 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.2188 * 0.75), (0.5 * 0.75, 0.3 * 0.75))
    .lineTo(0.3375 * 0.75, 0.3 * 0.75)
    .lineTo(0.3375 * 0.75, 0.4125 * 0.75)
    .lineTo(0.0, 0.4125 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1329)
)
# --- Coordinate System Transformation for Part 1 ---
part_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2606.stl