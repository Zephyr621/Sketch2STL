import cadquery as cq
import math
from cadquery import exporters
# --- Part 1: Rectangular Block with Circular Hole ---
part_1_length = 0.625 * 0.625  # Scaled length
part_1_width = 0.4167 * 0.625  # Scaled width
part_1_height = 0.125
hole_center_x = 0.25 * 0.625  # Scaled center x
hole_center_y = 0.2167 * 0.625  # Scaled center y
hole_radius = 0.0633 * 0.625  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - part_1_length/2, hole_center_y - part_1_width/2).circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.125, 0))
# --- Part 2: Cut Feature ---
sketch_scale = 0.337
part_2_depth =
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2529.stl