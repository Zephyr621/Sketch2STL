import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Rounded Corners ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.5833 * sketch_scale
height = 0.0174
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.0094 * sketch_scale, 0)
    .threePointArc((0.375 * sketch_scale, 0.0303 * sketch_scale), (0.7143 * sketch_scale, 0))
    .lineTo(0.75 * sketch_scale, 0)
    .threePointArc((0.375 * sketch_scale, 0.0208 * sketch_scale), (0.7143 * sketch_scale, 0.2917 * sketch_scale))
    .lineTo(0.0094 * sketch_scale, 0.2917 * sketch_scale)
    .threePointArc((0, 0.0208 * sketch_scale), (0, 0.2917 * sketch_scale))
    .close()
    .extrude(height)
)
# Cutout
cutout = (
    cq.Workplane("XY")
    .moveTo(0.0411 * sketch_scale, 0.2362 * sketch_scale)
    .
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1224.stl