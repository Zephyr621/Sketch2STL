import cadquery as cq
# --- Part 1: L-shaped extrusion ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.4687 * 0.75)
    .lineTo(0.5357 * 0.75, 0.4687 * 0.75)
    .lineTo(0.5357 * 0.75, 0.2589 * 0.75)
    .lineTo(0.2143 * 0.75, 0.2589 * 0.75)
    .lineTo(0.2143 * 0.75, 0.4687 * 0.75)
    .lineTo(0.0, 0.4687 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.2589)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_150.stl