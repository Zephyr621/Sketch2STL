import cadquery as cq
# --- Part 1: Base ---
part_1_length = 0.4554 * 0.7472  # Scaled length
part_1_width = 0.7472 * 0.7472   # Scaled width
part_1_height = 0.0252
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(part_1_height)
)
# --- Part 2: Top Extension ---
part_2_length = 0.5452 * 0.75  # Scaled length
part_2_width = 0.75 * 0.75   # Scaled width
part_2_height = 0.0083
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_length, part_2_width)
    .extrude(part_2_height)
)
# --- Assembly ---
# Translate part_2 to its position relative to part_1
part_2 = part_2.translate((0, 0, part_1_height))
# Union the two parts
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.
# --- Export to
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1035.stl