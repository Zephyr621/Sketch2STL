import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Prism with Curved Top ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.4286 * 0.75  # Scaled width
part_1_height = 0.5625
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_1_length, 0)
    .threePointArc((part_1_length/2, part_1_width), (0, part_1_width))
    .close()
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.5625, 0))
# --- Part 2: Cylindrical Holes ---
hole_radius = 0.0434 * 0.6068  # Scaled radius
hole_depth = 0.2812
# Hole centers (scaled and adjusted for origin)
hole1_x = 0.0434 * 0.6068
hole
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3004.stl