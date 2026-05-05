import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: Cylinder ---
sketch_scale = 0.0446
extrude_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * sketch_scale, 0.0196 * sketch_scale)
    .threePointArc((0.0058 * sketch_scale, 0.0058 * sketch_scale), (0.0196 * sketch_scale, 0.0 * sketch_scale))
    .lineTo(0.0917 * sketch_scale, 0.0 * sketch_scale)
    .threePointArc((0.0536 * sketch_scale, 0.0058 * sketch_scale), (0.0917 * sketch_scale, 0.0296 * sketch_scale))
    .lineTo(0.0356 * sketch_scale, 0.0296 * sketch_scale)
    .threePointArc((0.0166 * sketch_scale, 0.0236 * sketch_scale), (0.0 * sketch_scale, 0.0296 * sketch_scale))
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2670.stl