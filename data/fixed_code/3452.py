import cadquery as cq
# --- Part 1: Rectangular Block with Circular Holes ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.25 * 0.75   # Scaled width
part_1_height = 0.625
hole_radius = 0.0625 * 0.75  # Scaled radius
hole_center_1_x = 0.1875 * 0.75  # Scaled x-coordinate
hole_center_1_y = 0.125 * 0.75  # Scaled y-coordinate
hole_center_2_x = 0.5625 * 0.75  # Scaled x-coordinate
hole_center_2_y = 0.125 * 0.75  # Scaled y-coordinate
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole_center_1_x - part_1_length/2, hole_center_1
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3452.stl