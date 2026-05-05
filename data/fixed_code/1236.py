import cadquery as cq
# --- Part 1: Rectangular Beam ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.0161 * 0.05, 0.0)
    .lineTo(0.0161 * 0.05, 0.0161 * 0.05)
    .lineTo(0.0161 * 0.05, 0.05 * 0.05)
    .lineTo(0.0, 0.05 * 0.05)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.75)
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
cq.
cq.
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_1236.stl