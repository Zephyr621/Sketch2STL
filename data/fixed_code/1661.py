import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2679 * 0.75  # Scaled width
part_1_height = 0.0033
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0429 * 0.75)
    .lineTo(0.0429 * 0.75, 0.0)
    .lineTo(0.7295 * 0.75, 0.0)
    .threePointArc((0.75 * 0.75, 0.1071 * 0.75), (0.7295 * 0.75, 0.2679 * 0.75))
    .lineTo(0.0429 * 0.75, part_1_width)
    .lineTo(0.0, part_1_width)
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0033, 0))
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1661.stl