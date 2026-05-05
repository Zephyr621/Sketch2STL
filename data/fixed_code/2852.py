import cadquery as cq
# --- Part 1: Cube with L-shaped Extensions ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.375 * 0.75)
    .lineTo(0.5 * 0.75, 0.375 * 0.75)
    .lineTo(0.5 * 0.75, 0.75 * 0.75)
    .lineTo(0.25 * 0.75, 0.75 * 0.75)
    .lineTo(0.25 * 0.75, 0.375 * 0.75)
    .lineTo(0.0, 0.375 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.375)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_2852.stl