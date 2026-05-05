import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3587 * 0.75  # Scaled width
part_1_height = 0.1957
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for a cut
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder (Hole) ---
part_2_radius = 0.0141 * 0.0278  # Scaled radius
part_2_depth = 0.5581
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)  # Extrude in the opposite direction for a cut
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_727.stl