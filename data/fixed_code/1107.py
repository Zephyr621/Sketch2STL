import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.25, 0.0)
    .lineTo(0.25, 0.0664)
    .lineTo(0.375, 0.0664)
    .lineTo(0.375, 0.125)
    .lineTo(0.25, 0.125)
    .lineTo(0.25, 0.0664)
    .lineTo(0.3125, 0.0664)
    .lineTo(0.3125, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.5357)
    .lineTo(0.0, 0.5357)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.1071 * 0.75)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1107.stl