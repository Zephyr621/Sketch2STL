import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_length = 0.7458 * 0.7458  # Scaled length
part_1_width = 0.2626 * 0.7458   # Scaled width
part_1_height = 0.1734
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.0091, 0.0361, 0))
# --- Part 2: Rectangular Block ---
part_2_length = 0.7458 * 0.7458  # Scaled length
part_2_width = 0.2626 * 0.7458   # Scaled width
part_2_height = 0.0156
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2627.stl