import cadquery as cq
# --- Part 1: Cube with Circular Hole ---
length = 0.75 * 0.75  # Scaled length
width = 0.4412 * 0.75  # Scaled width
height = 0.0125
hole_radius = 0.0058 * 0.75  # Scaled radius
hole_center1_x = 0.375 * 0.75  # Scaled x-coordinate of the hole center
hole_center1_y = 0.2188 * 0.75  # Scaled y-coordinate of the hole center
hole_center2_x = 0.7125 * 0.75  # Scaled x-coordinate of the hole center 2
hole_center2_y = 0.2188 * 0.75  # Scaled y-coordinate of the hole center 3
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .moveTo(hole_center1_x - length/2, hole_center1_y - width/2)
    .circle(hole_radius)
    .cutThruAll()
    .faces(">Z")
    .workplane()
    .moveTo(hole_center2_x - length/2, hole_center2_y -
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3054.stl