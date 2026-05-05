import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.5107 * 0.7027  # Scaled length
part_1_width = 0.7027 * 0.7027  # Scaled width
part_1_height = 0.0139
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0033, 0.0033, 0))
# --- Part 2: Cylinder (Cut) ---
part_2_radius = 0.0274 * 0.0437  # Scaled radius
part_2_depth = 0.0044
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)
)
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_261.stl