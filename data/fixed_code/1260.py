import cadquery as cq
# --- Part 1: Rectangular Plate with Holes ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5769 * 0.75  # Scaled width
part_1_height = 0.0216
hole_center_x = 0.375 * 0.75  # Scaled x-coordinate
hole_center_y = 0.2885 * 0.75  # Scaled y-coordinate
hole_radius = 0.0188 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .moveTo(hole_center_x - part_1_length/2, hole_center_y - part_1_width/2)
    .circle(hole_radius)
    .cutThruAll()
)
# --- Part 2: Additional Feature ---
part_2_length = 0.0384 * 0.0782  # Scaled length
part_2_width = 0.0782 * 0.0782  # Scaled width
part_2_height = 0.0216
# Create the outer rectangle
outer_rect = cq.Workplane("XY").rect(part_2_length, part_2_width).extrude(part_
# Export
# 定义结果变量
result = outer_rect
# 导出为STL文件
cq.exporters.export(result, "output_1260.stl