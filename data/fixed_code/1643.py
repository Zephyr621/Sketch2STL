import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3648 * 0.75  # Scaled width
part_1_height = 0.1607
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.1607, 0, 0))
# --- Part 2: Cylindrical Protrusions ---
part_2_radius = 0.1292 * 0.2077  # Scaled radius
part_2_height = 0.1431
# Define cylinder positions relative to part_1's coordinate system
cylinder_positions = [
    (0.1292 * 0.2077, 0.1136 * 0.2077),
    (0.1292 * 0.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1643.stl