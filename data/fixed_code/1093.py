import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Box ---
part_1_length = 0.4687 * 0.4687  # Scaled length
part_1_width = 0.4687 * 0.4687  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder (Cutout) ---
part_2_radius = 0.0013 * 0.0027  # Scaled radius
part_2_depth
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1093.stl