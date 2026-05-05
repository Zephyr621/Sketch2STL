import cadquery as cq
from math import radians
# --- Part 1: Rectangular T-Shape ---
part_1_length = 0.4799 * 0.6307  # Scaled length
part_1_width = 0.6307 * 0.6307  # Scaled width
part_1_height = 0.0938
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.0938, 0))
# --- Part 2: Cutout ---
part_2_length = 0.0588 * 0.531  # Scaled length
part_2_width = 0.531 * 0.531  # Scaled width
part_2_height = 0.0375
part_2 = (
    cq.Workplane("XY")
    .moveTo
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_615.stl