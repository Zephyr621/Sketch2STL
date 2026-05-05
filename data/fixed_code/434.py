import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.317 * 0.6977  # Scaled length
part_1_width = 0.6977 * 0.6977   # Scaled width
part_1_height = 0.625
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Part 2: Holes ---
hole_radius = 0.0375 * 0.7493  # Scaled radius
hole_depth = 0.75
# Hole positions (scaled and translated)
hole_positions = [
    (0.0375 * 0.7493, 0.0375 * 0.7493),  # Scaled x-coordinate
    (-0.0375 * 0.7493, 0.3125 * 0.7493),  # Scaled y-coordinate
    (0.1875 * 0.7493, 0.0375 * 0.7493),  # Scaled x-coordinate
]
# Create holes by cutting cylinders
for pos in hole_positions:
    hole = (
        cq.Workplane("XY")
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_434.stl