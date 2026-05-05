import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0357 * 0.75)
    .threePointArc((0.0051 * 0.75, 0.0051 * 0.75), (0.0357 * 0.75, 0.0))
    .lineTo(0.7357 * 0.75, 0.0)
    .threePointArc((0.7467 * 0.75, 0.0051 * 0.75), (0.75 * 0.75, 0.0357 * 0.75))
    .lineTo(0.75 * 0.75, 0.6207 * 0.75)
    .threePointArc((0.7467 * 0.75, 0.6818 * 0.75), (0.7357 * 0.75, 0.6429 * 0.75))
    .lineTo(0.0357 * 0.75, 0.6429 * 0.75)
    .threePointArc((0.0051 * 0.75, 0.6818 * 0.75), (0.0, 0.6207 * 0.75))
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_480.stl