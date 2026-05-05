import cadquery as cq
# --- Part 1: Rectangular Bracket ---
length = 0.75 * 0.75  # Scaled length
width = 0.4687 * 0.75  # Scaled width
height = 0.1042
hole_1_center_x = 0.375 * 0.75
hole_1_center_y = 0.225 * 0.75
hole_2_center_x = 0.375 * 0.75
hole_2_center_y = 0.225 * 0.75
hole_radius = 0.0234 * 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Add holes to part 1
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .pushPoints([(hole_1_center_x - length/2, hole_1_center_y - width/2)])
    .hole(2 * hole_radius)
)
part_1 = (
    part_1.faces(">Z")
    .workplane()
    .pushPoints([(hole_2_center_x - length/2, hole_2_center_y - width
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3213.stl