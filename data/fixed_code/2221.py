import cadquery as cq
from math import radians
# --- Part 1: Base Cube with Curved Edges ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0536 * 0.1186)
    .lineTo(0.0014 * 0.1186, 0.0536 * 0.1186)
    .threePointArc((0.0719 * 0.1186, 0.0151 * 0.1186), (0.0288 * 0.1186, 0.0536 * 0.1186))
    .lineTo(0.0852 * 0.1186, 0.0)
    .lineTo(0.1186 * 0.1186, 0.0)
    .lineTo(0.1186 * 0.1186, 0.0536 * 0.1186)
    .close()
    .extrude(0.0954)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1355, 0.1355, 0.0))
# --- Part 2: Top Cube with Cutout ---
part_2 = (
    cq
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2221.stl