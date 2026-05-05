import cadquery as cq
# --- Part 1: T-shaped Bracket ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.7161 * 0.75, 0.0)
    .lineTo(0.7161 * 0.75, 0.3478 * 0.75)
    .lineTo(0.375 * 0.75, 0.3478 * 0.75)
    .lineTo(0.375 * 0.75, 0.5 * 0.75)
    .lineTo(0.0, 0.5 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.0937)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_3524.stl