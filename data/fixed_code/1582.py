import cadquery as cq
from math import radians
# --- Part 1: Cube with Circular Hole ---
part_1_length = 0.4486 * 0.4486  # Scaled length
part_1_width = 0.3275 * 0.4486  # Scaled width
part_1_height = 0.2068
hole_center_x = 0.2143 * 0.4486  # Scaled center x
hole_center_y = 0.1607 * 0.4486  # Scaled center y
hole_radius = 0.1071 * 0.4486  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - part_1_length/2, hole_center_y - part_1_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2068, 0))
# --- Part 2: Square Plate with Circular Hole ---
part_2_length = 0.3014 * 0.322  # Scaled length
part_2_width = 0.322 * 0.322  # Scaled width
part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1582.stl