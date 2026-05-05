import cadquery as cq
from cadquery import exporters
# --- Part 1: Rectangular Prism with Holes ---
part_1_length = 0.4286 * 0.4286  # Scaled length
part_1_width = 0.4286 * 0.4286   # Scaled width
part_1_height = 0.7284
hole_radius = 0.0232 * 0.4286  # Scaled radius
hole_center_1_x = 0.2143 * 0.4286  # Scaled center x
hole_center_1_y = 0.1429 * 0.4286  # Scaled center y
hole_center_2_x = 0.3036 * 0.4286  # Scaled center x
hole_center_2_y = 0.1429 * 0.4286  # Scaled center y
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole_center_1_x - part_1_length/2, hole_center_1_y - part_1_width/2), (hole_center_2_x - part_1_length/2, hole_center_
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_205.stl