import cadquery as cq
from math import radians
# --- Part 1: Rectangular Prism ---
part_1_length = 0.1489 * 0.1489  # Scaled length
part_1_width = 0.0718 * 0.1489   # Scaled width
part_1_height = 0.0431
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0234, 0.75, 0))
# --- Part 2: Rectangular Protrusion ---
part_2_length = 0.1489 * 0.1489  # Scaled length
part_2_width = 0.0254 * 0.1489   # Scaled width
part_2_height = 0.001
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_0.stl