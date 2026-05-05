import cadquery as cq
# --- Part 1: Rectangular Plate ---
length = 0.75 * 0.75  # Scaled length
width = 0.3571 * 0.75  # Scaled width
height = 0.0062
part_1 = (
    cq.Workplane("XY")
    .rect(length, width)
    .extrude(height)
)
# Add rounded corners
corner_radius = min(length, width) / 10  # Adjust as needed; avoid large values
part_1 = part_1.edges("|Z and >X").fillet(corner_radius)
part_1 = part_1.edges("|Z and <X").fillet(corner_radius)
# Add small protrusion
protrusion_width = 0.0405 * 0.75
protrusion_height = 0.0269 * 0.75
protrusion_x = 0.7023 * 0.75
protrusion_y = 0.0311 * 0.75
protrusion_z = height
part_1 = part_1.faces(">Z").workplane().moveTo(protrusion_x - length/2, protrusion_y - width/2).lineTo(protrusion_x + protrusion_width/2, protrusion_y - width/2).lineTo(protrusion_x + protrusion_width/
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1901.stl