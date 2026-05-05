import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.1337 * 2  # Total extrusion depth (towards + opposite normal)
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3125 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.2771 * sketch_scale), (0.6643 * sketch_scale, 0.4687 * sketch_scale))
    .lineTo(0.1562 * sketch_scale, 0.4687 * sketch_scale)
    .threePointArc((0.0937 * sketch_scale, 0.2346 * sketch_scale), (0.0625 * sketch_scale, 0.4738 * sketch_scale))
    .lineTo(0.0, 0.4738 * sketch_scale)
    .lineTo(0.0, 0.0)
    .close()
    .add(cq.Workplane("XY").circle(0.0544 * sketch_scale).val().move(cq.Location(cq.Vector(0.0482 * sketch_scale, 0.2103 * sketch_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2229.stl