import cadquery as cq
# --- Part 1: Rectangular Prism ---
part_1_width = 0.0217 * 0.0833  # Scaled width
part_1_height = 0.0833 * 0.0833 # Scaled height
part_1_depth = 0.75
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_width, part_1_height)
    .extrude(part_1_depth)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# --- Export to STL ---
cq.
# ---
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3582.stl