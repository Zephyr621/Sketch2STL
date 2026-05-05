import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1295 * 0.75)
    .lineTo(0.5357 * 0.75, 0.1295 * 0.75)
    .lineTo(0.5357 * 0.75, 0.3409 * 0.75)
    .lineTo(0.2536 * 0.75, 0.3409 * 0.75)
    .lineTo(0.2536 * 0.75, 0.0604 * 0.75)
    .lineTo(0.125 * 0.75, 0.0604 * 0.75)
    .lineTo(0.125 * 0.75, 0.1295 * 0.75)
    .lineTo(0.0, 0.1295 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2499)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2158.stl