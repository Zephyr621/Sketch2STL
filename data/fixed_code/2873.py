import cadquery as cq
# --- Part 1: L-shaped profile ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.5627 * 0.75)
    .lineTo(0.1804 * 0.75, 0.5627 * 0.75)
    .lineTo(0.1804 * 0.75, 0.75 * 0.75)
    .lineTo(0.0, 0.75 * 0.75)
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
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_2873.stl