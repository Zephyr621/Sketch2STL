import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.5 * 0.75  # Scaled width
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.025 * 0.05  # Scaled radius
part_2_depth = 0.125
part_2 = (
    cq.Workplane("XY")
    .workplane()
    .moveTo(0.025 * 0.05, 0.025 * 0.05)
    .circle(part_2_radius)
    .extrude(-part_2_depth)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1680.stl