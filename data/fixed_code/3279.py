import cadquery as cq
# --- Part 1: Rectangular Block with Holes ---
part_1_length = 0.5 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.125
hole_radius = 0.0312 * 0.75  # Scaled radius
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for a hole
)
# Add holes to part 1
hole_centers = [
    (0.0833 * 0.75 - part_1_length/2, 0.0833 * 0.75 - part_1_width/2),
    (0.0833 * 0.75 - part_1_length/2, 0.4167 * 0.75 - part_1_width/2),
    (0.6667 * 0.75 - part_1_length/2, 0.0833 * 0.75 - part_1_width/2),
    (0.6667 * 0.75 - part_1_length/2, 0.4167 * 0.75 - part_1_width/2)
]
for center_x, center_y in hole_centers:
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3279.stl