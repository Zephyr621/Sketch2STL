import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Cube with Circular Hole ---
part_1_size = 0.3214 * 0.3214  # Sketch size scaled
part_1_height = 0.1607
hole_radius = 0.0536 * 0.3214  # Sketch radius scaled
hole_center_x = 0.1607 * 0.3214
hole_center_y = 0.1607 * 0.3214
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_size, part_1_size)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1561, 0.0, 0.1607))
# --- Part 2: Rectangular Plate with Cutout ---
part_2_size_x = 0.75 * 0.75  # Sketch size scaled
part_2_size_y = 0.3214 * 0.75  # Sketch size scaled
part_2_depth = 0.1071
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size_x, part
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_41.stl