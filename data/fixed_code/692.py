import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75
part_1_width = 0.5212 * 0.75
part_1_height = 0.0563
part_1 = cq.Workplane("XY").rect(part_1_length, part_1_width).extrude(part_1_height)
# --- Part 2: Cylindrical Protrusions ---
cylinder_radius = 0.0438 * 0.8333
cylinder_height = 0.0627
# Define cylinder positions relative to the origin
cylinder_positions = [
    (0.0438 * 0.8333, 0),  # Adjusted for arc
    (0.6853 * 0.8333, 0),  # Adjusted for arc
    (0.7163 * 0.8333, 0)   # Adjusted for arc
]
# Create cylinders by cutting cylinders
for x, y in cylinder_positions:
    cylinder = cq.Workplane("XY").circle(cylinder_radius).extrude(-cylinder_height)
    cylinder = cylinder.translate((x - part_1_length/2 + cylinder_radius, y - part_1_width/2 + cylinder_radius, part_1_height))
    part_1 = part_1.cut(cylinder)
# Export
# 定义结果变量
result = cylinder
# 导出为STL文件
cq.exporters.export(result, "output_692.stl