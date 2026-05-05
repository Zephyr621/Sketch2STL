import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.375 * 0.75   # Scaled width
part_1_height = 0.075
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.075))
# --- Part 2: Rectangular Plate ---
part_2_length = 0.675 * 0.675  # Scaled length
part_2_width = 0.3125 * 0.675   # Scaled width
part_2_height = 0.15
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.075, 0.3125, 0.075))
# --- Assembly
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_908.stl