import cadquery as cq
# --- Part 1: Square Base ---
part_1_width = 0.4177 * 0.75  # Scaled width
part_1_height = 0.4177 * 0.75  # Scaled height
part_1_thickness = 0.1125
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(part_1_thickness)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.1125, 0))
# --- Part 2: Cylinder ---
part_2_radius = 0.1607 * 0.75  # Scaled radius
part_2_height = 0.0586
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)  # Extrude in the opposite direction for a cylinder
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_657.stl