import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.25 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.125 * sketch_scale, 0)
    .lineTo(0.625 * sketch_scale, 0)
    .threePointArc((0.5644 * sketch_scale, 0.0113 * sketch_scale), (0.625 * sketch_scale, 0.375 * sketch_scale))
    .lineTo(0.625 * sketch_scale, 0.75 * sketch_scale)
    .lineTo(0.625 * sketch_scale, 0.75 * sketch_scale)
    .lineTo(0.125 * sketch_scale, 0.75 * sketch_scale)
    .threePointArc((0, 0.0113 * sketch_scale), (0.125 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# Add holes
hole_centers = [
    (0.0625 * sketch_scale, 0.0938 * sketch_scale),
    (0.5625 * sketch_scale, 0.0938 * sketch_scale),
    (0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1716.stl