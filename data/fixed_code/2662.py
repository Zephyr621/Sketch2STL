import cadquery as cq
from cadquery import exporters
# --- Part 1: Triangular Prism ---
part_1_scale = 0.5
part_1_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0 * part_1_scale, 0.0 * part_1_scale)
    .lineTo(0.25 * part_1_scale, 0.0 * part_1_scale)
    .lineTo(0.25 * part_1_scale, 0.125 * part_1_scale)
    .lineTo(0.0 * part_1_scale, 0.5 * part_1_scale)
    .close()
    .extrude(part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cube ---
part_2_scale = 0.375
part_2_depth = 0.25
part_2 = (
    cq.Workplane("XY")
    .moveTo(0.0 * part_2_scale, 0.375 * part_2_scale)
    .lineTo(
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2662.stl