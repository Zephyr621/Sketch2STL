import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Block ---
part_1_length = 0.015 * 0.2625  # Scaled length
part_1_width = 0.2625 * 0.2625  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Slot ---
slot_length = 0.0234 * 0.0766  # Scaled length
slot_width = 0.0766 * 0.0766  # Scaled width
slot_height = 0.0057
slot = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0234 * 0.0766, 0.0)
    .lineTo(0.0234 * 0.0766, 0.0353 * 0.0766)
    .lineTo(0.0, 0.0353 *
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_313.stl