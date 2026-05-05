import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.1154 * 0.75  # Scaled width
part_1_height = 0.1154
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Cube ---
part_2_length = 0.2923 * 0.2923  # Scaled length
part_2_width = 0.1534 * 0.2923  # Scaled width
part_2_height = 0.1154
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0705, 0.0304, 0))
# --- Part 3: Cube ---
part_3_length = 0.2923 * 0.2923  # Scaled length
part_3_width = 0.1534 * 0.2923  # Scaled width
part_3_height = 0.1154
part_3 =
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1588.stl