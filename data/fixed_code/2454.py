import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.3 * sketch_scale, 0.0)
    .threePointArc((0.375 * sketch_scale, 0.03 * sketch_scale), (0.225 * sketch_scale, 0.0))
    .lineTo(0.225 * sketch_scale, 0.45 * sketch_scale)
    .threePointArc((0.1875 * sketch_scale, 0.5625 * sketch_scale), (0.0, 0.45 * sketch_scale))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(extrude_depth)
)
# Create the hole
hole_radius = 0.075 * sketch_scale
part_1 = part_1.faces(">Z").workplane().circle(hole_radius).cutThruAll()
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2454.stl