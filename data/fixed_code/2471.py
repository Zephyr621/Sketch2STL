import cadquery as cq
from cadquery import exporters
# --- Part 1: Pentagonal Prism ---
part_1_scale = 0.75
part_1_height = 0.0502
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.1293 * part_1_scale)
    .lineTo(0.1293 * part_1_scale, 0.0)
    .lineTo(0.6495 * part_1_scale, 0.1293 * part_1_scale)
    .lineTo(0.75 * part_1_scale, 0.1293 * part_1_scale)
    .lineTo(0.75 * part_1_scale, 0.2499 * part_1_scale)
    .lineTo(0.0, 0.2499 * part_1_scale)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0502))
# --- Part 2: Rectangular Prism ---
part_2_scale = 0.75
part_2_height = 0.0502
part_2 = (
    cq.Workplane("XY")
    .rect(0.75 * part_2_scale, 0.24
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2471.stl