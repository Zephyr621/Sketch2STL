import cadquery as cq
# --- Part 1: Base ---
part_1_length = 0.75 * 0.75
part_1_width = 0.5625 * 0.75
part_1_height = 0.4687
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cutout ---
part_2_length = 0.375 * 0.5156
part_2_width = 0.5156 * 0.5156
part_2_height = 0.2812
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), 180)
part_2 = part_2.translate((0.0938, 0.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1533.stl