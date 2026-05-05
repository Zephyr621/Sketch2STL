import cadquery as cq
# --- Part 1: Rectangular Block ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.1562 * 0.75)
    .lineTo(0.4563 * 0.75, 0.1562 * 0.75)
    .lineTo(0.4563 * 0.75, 0.3125 * 0.75)
    .lineTo(0.2188 * 0.75, 0.3125 * 0.75)
    .lineTo(0.2188 * 0.75, 0.1562 * 0.75)
    .lineTo(0.0, 0.1562 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0625)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_173.stl