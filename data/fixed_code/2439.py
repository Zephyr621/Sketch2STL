import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Box ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3768 * 0.75  # Scaled width
part_1_height = 0.2386
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2386, 0))
# --- Part 2: Cutout ---
part_2_length = 0.6107 * 0.6107  # Scaled length
part_2_width = 0.3281 * 0.6107  # Scaled width
part_2_height = 0.2478
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2439.stl