import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
sketch_scale = 0.75
extrude_depth = 0.3176 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.1749 * sketch_scale, 0)
    .lineTo(0.5751 * sketch_scale, 0)
    .threePointArc((0.75 * sketch_scale, 0.1607 * sketch_scale), (0.5751 * sketch_scale, 0.3203 * sketch_scale))
    .lineTo(0.1749 * sketch_scale, 0.3203 * sketch_scale)
    .threePointArc((0, 0.1607 * sketch_scale), (0.1749 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# Add holes
hole_center_x = 0.375 * sketch_scale
hole_center_y = 0.1588 * sketch_scale
hole_radius = 0.0586 * sketch_scale
part_1 = (
    part_1.faces(">Z")
    .workplane()
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2533.stl