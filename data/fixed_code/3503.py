import cadquery as cq
# --- Part 1: Rectangular Box ---
part_1_length = 0.5625 * 0.75  # Scaled length
part_1_width = 0.75 * 0.75  # Scaled width
part_1_height = 0.375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0, 0))
# --- Part 2: Triangular Prism (Joined) ---
part_2_length = 0.2812 * 0.2812  # Scaled length
part
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3503.stl