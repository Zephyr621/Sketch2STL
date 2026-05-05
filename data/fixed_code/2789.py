import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3 * 0.75  # Scaled width
part_1_height = 0.0375
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0.1594, 0))
# --- Part 2: Cutout ---
part_2_length = 0.375 * 0.375  # Scaled length
part_2_width = 0.2812 * 0.375  # Scaled width
part_2_height = 0.0156
part_2 = (
    cq.Workplane("
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2789.stl