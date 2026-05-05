import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Plate ---
part_1_length = 0.3088 * 0.3088  # Scaled length
part_1_width = 0.0799 * 0.3088   # Scaled width
part_1_height = 0.1969
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0234, 0.1969, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.0141 * 0.0342  # Scaled radius
part_2_height = 0.1969
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_665.stl