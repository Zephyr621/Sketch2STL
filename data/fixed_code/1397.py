import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.1607 * 0.3261  # Scaled length
part_1_width = 0.3261 * 0.3261  # Scaled width
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Block ---
part_2_length = 0.4286 * 0.4286  # Scaled length
part_2_width = 0.3115 * 0.4286  # Scaled width
part_2_height = 0.2247
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1397.stl