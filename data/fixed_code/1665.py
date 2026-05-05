import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Bar with Circular Hole ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.075 * 0.75  # Scaled width
part_1_height = 0.0141
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.0375 * 0.75  # Scaled center y
hole_radius = 0.0094 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - part_1_length/2, hole_center_y - part_1_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Part 2: Rectangular Block with Open Front ---
part_2_length = 0.75 * 0.75  # Scaled length
part_2_width = 0.075 * 0.75  # Scaled width
part_2_height = 0.15
hole_center_x = 0.375 * 0.75  # Scaled center x
hole_center_y = 0.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1665.stl