import cadquery as cq
from math import radians
# --- Part 1: Rectangular Section ---
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0367 * 0.75  # Scaled height
part_1_depth = 0.0367  # Extrusion depth
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(-part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cutout ---
part_2_width = 0.0156 * 0.0156  # Scaled width
part_2_height = 0.0156 * 0.0156  # Scaled height
part_2_depth = 0.0805  # Extrusion depth
part_2 = (
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2842.stl