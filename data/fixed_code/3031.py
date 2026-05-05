import cadquery as cq
import math
from cadquery.vis import show
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7188 * 0.75, 0.0)
    .threePointArc((0.6929 * 0.75, 0.1395 * 0.75), (0.75 * 0.75, 0.3735 * 0.75))
    .lineTo(0.75 * 0.75, 0.3845 * 0.75)
    .threePointArc((0.6877 * 0.75, 0.3472 * 0.75), (0.7188 * 0.75, 0.3915 * 0.75))
    .lineTo(0.0, 0.3915 * 0.75)
    .threePointArc((0.0014 * 0.75, 0.3472 * 0.75), (0.0, 0.3735 * 0.75))
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0128)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3031.stl