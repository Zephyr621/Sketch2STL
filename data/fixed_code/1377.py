import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.2143 * 0.75)
    .lineTo(0.5357 * 0.75, 0.2143 * 0.75)
    .lineTo(0.5357 * 0.75, 0.4286 * 0.75)
    .lineTo(0.1071 * 0.75, 0.4286 * 0.75)
    .lineTo(0.1071 * 0.75, 0.1071 * 0.75)
    .lineTo(0.0536 * 0.75, 0.1071 * 0.75)
    .lineTo(0.0536 * 0.75, 0.2143 * 0.75)
    .lineTo(0.0, 0.2143 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2143 * 0.75)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1377.stl