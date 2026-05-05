import cadquery as cq
# --- Part 1: Base ---
part_1_width = 0.6996 * 0.6996  # Scaled width
part_1_height = 0.6996 * 0.6996  # Scaled height
part_1_depth = 0.5247
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0117, 0.0117, 0))
# --- Part 2: Vertical Extension ---
part_2_width = 0.0165 * 0.0165  # Scaled width
part_2_height = 0.0165 * 0.0165  # Scaled height
part_2_depth = 0.0075
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_width, part_2_height)
    .extrude(-part_2_depth)
)
# --- Coordinate System Transformation for Part 2 ---
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_999.stl