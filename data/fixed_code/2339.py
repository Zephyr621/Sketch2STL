import cadquery as cq
# --- Part 1: Rectangular Prism with Holes ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.2893 * 0.75  # Scaled width
part_1_height = 0.1269
hole_radius = 0.0188 * 0.75  # Scaled radius
hole_center1_x = 0.1446 * 0.75  # Scaled x-coordinate
hole_center1_y = 0.1446 * 0.75  # Scaled y-coordinate
hole_center2_x = 0.6097 * 0.75  # Scaled x-coordinate
hole_center2_y = 0.1446 * 0.75  # Scaled y-coordinate
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .pushPoints([(hole_center1_x - part_1_length/2, hole_center1_y - part_1_width/2), (hole_center2_x - part_1_length/2, hole_center2_y - part_1_width/2)])
    .hole(hole_radius * 2)
)
# --- Part 2: Cylinder ---
part_2_radius
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2339.stl