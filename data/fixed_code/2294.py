import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.4773
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0248 * sketch_scale)
    .lineTo(0.0, 0.0938 * sketch_scale)
    .threePointArc((0.0586 * sketch_scale, 0.1095 * sketch_scale), (0.0248 * sketch_scale, 0.0))
    .lineTo(0.0464 * sketch_scale, 0.0)
    .threePointArc((0.0586 * sketch_scale, 0.0586 * sketch_scale), (0.0464 * sketch_scale, 0.0248 * sketch_scale))
    .close()
    .extrude(0.75)
)
# Cutout
cutout = (
    cq.Workplane("XY")
    .moveTo(0.0156 * sketch_scale, 0.0036 * sketch_scale)
    .threePointArc((0.0586 * sketch_scale, 0.1095 * sketch_scale), (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2294.stl