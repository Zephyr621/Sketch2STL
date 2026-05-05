import cadquery as cq
# --- Part 1: L-shaped CAD Model ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75, 0.0)
    .lineTo(0.75, 0.1875)
    .lineTo(0.5625, 0.1875)
    .lineTo(0.5625, 0.375)
    .lineTo(0.1875, 0.375)
    .lineTo(0.1875, 0.1875)
    .lineTo(0.0, 0.1875)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0078 * 0.75)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1675.stl