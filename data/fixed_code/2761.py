import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Rectangular Plate with Curved Top ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.2888 * sketch_scale
height = 0.0042
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(0.375 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.1406 * sketch_scale), (0.375 * sketch_scale, 0.2888 * sketch_scale))
    .lineTo(0, 0.2888 * sketch_scale)
    .lineTo(0, 0)
    .close()
    .extrude(-height)
)
# Create the cutout
cutout = (
    cq.Workplane("XY")
    .moveTo(0.375 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0.1406 * sketch_scale)
    .threePointArc((0.75 * sketch_scale, 0.2847 * sketch_scale), (0.375 * sketch_scale, 0.2888 * sketch_scale))
    .lineTo(0.375 * sketch_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2761.stl