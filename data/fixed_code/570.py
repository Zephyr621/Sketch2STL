import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1: S shaped Object ---
sketch_scale = 0.75
extrude_depth = 0.375
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0469 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0)
    .lineTo(0.75 * sketch_scale, 0.0188 * sketch_scale)
    .threePointArc((0.7083 * sketch_scale, 0.0343 * sketch_scale), (0.7188 * sketch_scale, 0.1875 * sketch_scale))
    .lineTo(0.7188 * sketch_scale, 0.0938 * sketch_scale)
    .lineTo(0.0469 * sketch_scale, 0.0938 * sketch_scale)
    .lineTo(0.0469 * sketch_scale, 0.1875 * sketch_scale)
    .threePointArc((0, 0.0343 * sketch_scale), (0.0469 * sketch_scale, 0))
    .close()
    .extrude(extrude_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_570.stl