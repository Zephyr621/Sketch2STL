import cadquery as cq
from math import radians
# --- Part 1: Square Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.6797 * 0.75  # Scaled width
part_1_height = 0.0231
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cube (Cutout) ---
part_2_size = 0.6961 * 0.6961  # Scaled size
part_2_depth = 0.0111
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(-part_2_depth)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0357, 0.0111, 0.0357))
# --- Assembly: Cut Part 2 from Part 1 ---
assembly = part_1.cut(part_2)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_373.stl