import cadquery as cq
# --- Part 1 ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0117 * 0.0776, 0.0)
    .lineTo(0.0117 * 0.0776, 0.0261 * 0.0776)
    .lineTo(0.0117 * 0.0776, 0.0776 * 0.0776)
    .lineTo(0.0077 * 0.0776, 0.0776 * 0.0776)
    .lineTo(0.0077 * 0.0776, 0.0261 * 0.0776)
    .lineTo(0.0, 0.0261 * 0.0776)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3079.stl