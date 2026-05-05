import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Box ---
part_1_length = 0.5388 * 0.5388  # Scaled length
part_1_width = 0.2308 * 0.5388  # Scaled width
part_1_height = 0.546
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0208, 0.0208, 0.546))
# --- Part 2: Cylinder ---
part_2_radius = 0.1078 * 0.2082  # Scaled radius
part_2_height = 0.375
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2949.stl