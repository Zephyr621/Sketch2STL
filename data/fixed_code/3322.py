import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.2263 * 0.2263  # Scaled length
part_1_width = 0.1293 * 0.2263  # Scaled width
part_1_height = 0.0413
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Rectangular Block ---
part_2_length = 0.2155 * 0.2155  # Scaled length
part_2_width = 0.1078 * 0.2155  # Scaled width
part_2_height = 0.0085
part_2 = (
    cq.Workplane
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3322.stl