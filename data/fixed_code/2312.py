import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: S-shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.15
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.2962 * sketch_scale)
    .threePointArc((0.0033 * sketch_scale, 0.0008 * sketch_scale), (0.2962 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.7347 * sketch_scale, 0.0008 * sketch_scale), (0.75 * sketch_scale, 0.2962 * sketch_scale))
    .lineTo(0.2962 * sketch_scale, 0.2962 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# Add holes to part 1
hole_center1 = (0.375 * sketch_scale, 0.09 * sketch_scale)
hole_radius2 = 0.03 * sketch_scale
part_1 = part_1.faces(">Z").workplane().pushPoints([hole_center1]).hole(2 * hole
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2312.stl