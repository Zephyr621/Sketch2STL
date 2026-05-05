import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.4412 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.0221
hole_radius = 0.0183 * 0.75  # Scaled radius
hole_centers = [
    (0.0391 * 0.75 - part_1_length/2, 0.0183 * 0.75 - part_1_width/2),
    (0.0391 * 0.75 - part_1_length/2, 0.7083 * 0.75 - part_1_width/2),
    (0.7083 * 0.75 - part_1_length/2, 0.0183 * 0.75 - part_1_width/2)
]
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
for center in hole_centers:
    part_1 = part_1.faces(">Z").workplane().center(center[0] - part_1_length/2, center[1] - part_1_width/2).circle(hole_radius).cutThruAll()
# Export
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1677.stl