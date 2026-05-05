import cadquery as cq
import math
from cadquery import exporters
# --- Part 1 ---
sketch_scale = 0.3239
extrude_depth = 0.2143 * sketch_scale
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0286 * sketch_scale)
    .lineTo(0.0171 * sketch_scale, 0.0)
    .threePointArc((0.1829 * sketch_scale, 0.0764 * sketch_scale), (0.0536 * sketch_scale, 0.0286 * sketch_scale))
    .lineTo(0.1667 * sketch_scale, 0.0286 * sketch_scale)
    .threePointArc((0.1089 * sketch_scale, 0.0469 * sketch_scale), (0.0354 * sketch_scale, 0.0286 * sketch_scale))
    .lineTo(0.0286 * sketch_scale, 0.0286 * sketch_scale)
    .lineTo(0.0286 * sketch_scale, 0.0286 * sketch_scale)
    .close()
    .extrude(extrude_depth)
)
# Create holes
hole_radius = 0.0058 * sketch_scale
hole_center1 = (0.0166 * sketch_scale, 0.0166 * sketch_scale)
hole_center2 = (0.3239 * sketch_scale, 0.0166 * sketch_scale)
part_1 =
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3265.stl