import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0433 * 0.6933, 0.0)
    .threePointArc((0.3281 * 0.6933, 0.0189 * 0.6933), (0.6091 * 0.6933, 0.0))
    .lineTo(0.6466 * 0.6933, 0.0)
    .threePointArc((0.5118 * 0.6933, 0.0189 * 0.6933), (0.6333 * 0.6933, 0.0021 * 0.6933))
    .lineTo(0.0, 0.0021 * 0.6933)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1),
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_321.stl