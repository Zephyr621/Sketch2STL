import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.075 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.15 * sketch_scale, 0.0)
    .lineTo(0.6 * sketch_scale, 0.0)
    .threePointArc((0.75 * sketch_scale, 0.075 * sketch_scale), (0.6 * sketch_scale, 0.075 * sketch_scale))
    .lineTo(0.15 * sketch_scale, 0.075 * sketch_scale)
    .threePointArc((0.0, 0.075 * sketch_scale), (0.15 * sketch_scale, 0.0))
    .close()
    .extrude(extrude_depth)
)
# Cut the hole
hole_radius = 0.0375 * sketch_scale
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0,
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3446.stl