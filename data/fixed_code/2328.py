import cadquery as cq
import math
from cadquery import exporters
# --- Part 1 ---
sketch_scale = 0.75
length = 0.75 * sketch_scale
width = 0.1607 * sketch_scale
height = 0.1071
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0536 * sketch_scale, 0)
    .lineTo(0.6923 * sketch_scale, 0)
    .threePointArc((0.7286 * sketch_scale, 0.0872 * sketch_scale), (0.75 * sketch_scale, 0.1607 * sketch_scale))
    .lineTo(0.75 * sketch_scale, 0.1607 * sketch_scale)
    .threePointArc((0.7286 * sketch_scale, 0.0434 * sketch_scale), (0.6923 * sketch_scale, 0.0188 * sketch_scale))
    .lineTo(0.0536 * sketch_scale, 0.0188 * sketch_scale)
    .threePointArc((0, 0.0434 * sketch_scale), (0.0536 * sketch_scale, 0))
    .close()
    .extrude(height)
)
# Add holes
hole_radius = 0.0268 * sketch_scale
part_1 = part_1.faces
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2328.stl