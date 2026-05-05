import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.0625 * 0.75  # Scaled width
part_1_length = 0.75 * 0.75 # Scaled length
part_1_height = 0.0625
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_length)
    .extrude(part_1_height)
)
# --- Part 2: Cutout Cylinder ---
part_2_radius = 0.0062 * 0.015  # Scaled radius
part_2_depth = 0.05
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_depth)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.0625, 0.0938, 0.18
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2550.stl