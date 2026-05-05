import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.0337 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0978 * sketch_scale, 0)
    .threePointArc((0.375 * sketch_scale, 0.0306 * sketch_scale), (0.6563 * sketch_scale, 0))
    .threePointArc((0.75 * sketch_scale, 0.1705 * sketch_scale), (0.6563 * sketch_scale, 0.3414 * sketch_scale))
    .lineTo(0.0978 * sketch_scale, 0.3414 * sketch_scale)
    .threePointArc((0, 0.1705 * sketch_scale), (0.0978 * sketch_scale, 0))
    .close()
    .add(cq.Workplane("XY").circle(0.059 * sketch_scale).val().move(cq.Location(cq.Vector(0.0441 * sketch_scale, 0.0899 * sketch_scale, 0))))
    .add(cq.Workplane("XY").circle(0.059 * sketch_scale).val().move(cq.Location(cq.Vector(0.6977 * sketch_scale,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_116.stl