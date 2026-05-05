import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.5 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.3
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Part 2: Rectangular Block (Cut) ---
part_2_length = 0.15 * 0.4687  # Scaled length
part_2_width = 0.4687 * 0.4687  # Scaled width
part_2_height = 0.075
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.225, 0.225, part_1_height))
# --- Part 3: Cylinder (Hole) ---
part_3_radius = 0.0375 * 0.075  # Scaled radius
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_290.stl