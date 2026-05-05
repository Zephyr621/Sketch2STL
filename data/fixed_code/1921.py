import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.0364 * 0.7282  # Scaled length
part_1_width = 0.7282 * 0.7282  # Scaled width
part_1_height = 0.0364
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0105, 0.0105, 0))
# --- Part 2: Vertical Extension ---
part_2_length = 0.0332 * 0.0332  # Scaled length
part_2_width = 0.0469 * 0.0332  # Scaled width
part_2_height = 0.75
part_2 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(part_2_length, 0)
    .lineTo(part_2_length, part_2_width)
    .lineTo(0, part_2_width)
    .close()
    .extrude(part_2_height)
)
# --- Coordinate System
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1921.stl