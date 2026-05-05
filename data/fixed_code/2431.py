import cadquery as cq
from cadquery import exporters
# --- Part 1: Base ---
part_1_length = 0.1406 * 0.1406  # Scaled length
part_1_width = 0.1406 * 0.1406  # Scaled width
part_1_height = 0.0234
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0536))
# --- Part 2: Cutout 1 ---
part_2_length = 0.0937 * 0.1875  # Scaled length
part_2_width = 0.1875 * 0.1875  # Scaled width
part_2_height = 0.0187
part_2 = (
    cq.Workplane("XY")
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2431.stl