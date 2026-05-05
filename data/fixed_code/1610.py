import cadquery as cq
from math import radians
# --- Part 1: Support Bracket ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0341 * 0.75)
    .threePointArc((0.0226 * 0.75, 0.0226 * 0.75), (0.0341 * 0.75, 0.0))
    .lineTo(0.7361 * 0.75, 0.0)
    .threePointArc((0.7266 * 0.75, 0.0226 * 0.75), (0.75 * 0.75, 0.0341 * 0.75))
    .lineTo(0.75 * 0.75, 0.4232 * 0.75)
    .threePointArc((0.7266 * 0.75, 0.4315 * 0.75), (0.7361 * 0.75, 0.4078 * 0.75))
    .lineTo(0.0341 * 0.75, 0.4078 * 0.75)
    .threePointArc((0.0226 * 0.75, 0.4315 * 0.75), (0.0, 0.4232 * 0.75))
    .lineTo(0.0, 0.0341 * 0.75)
    .close()
    .extr
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1610.stl