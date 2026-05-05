import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3 * 0.75  # Scaled width
part_1_height = 0.0325
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0352 * 0.4583  # Scaled radius
cylinder_height = 0.0978
# Define cylinder positions relative to the part's origin
cylinder_positions = [
    (0.0352 * 0.4583 - part_1_length / 2, 0.0352 * 0.4583 - part_1_width / 2),
    (0.0352 * 0.4583 - part_1_length / 2, 0.1562 * 0.4583 - part_1_width / 2),
    (0.1562 * 0.4583 - part_1_length / 2, 0.0352 * 0.4583 - part_1_width / 2),
]
# Create cylinders and translate them
cylinders = []
for x, y in cylinder_positions:
    cylinder =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1170.stl