import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1_length = 0.75 * 0.75  # Scaled length
part_1_width = 0.3387 * 0.75  # Scaled width
part_1_height = 0.1089
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)  # Extrude in the opposite direction
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.1089))
# --- Part 2: Cube ---
part_2_size = 0.4687 * 0.4687  # Scaled size
part_2_height = 0.1089
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_size)
    .extrude(part_2_height)
)
# --- Assembly ---
assembly = part_2.union(part_1)
cq.
# --- Export to STL ---
cq.
# --- Export to
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1991.stl