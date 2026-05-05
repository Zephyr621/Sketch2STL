import cadquery as cq
# --- Part 1: Cube with Protrusion ---
part_1 = (
    cq.Workplane("XY")
    .moveTo(0.0, 0.0)
    .lineTo(0.75 * 0.75, 0.0)
    .lineTo(0.75 * 0.75, 0.3 * 0.75)
    .lineTo(0.375 * 0.75, 0.3 * 0.75)
    .lineTo(0.375 * 0.75, 0.4 * 0.75)
    .lineTo(0.0, 0.4 * 0.75)
    .lineTo(0.0, 0.0)
    .close()
    .extrude(0.25)
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
cq
# 导出为STL文件
cq.exporters.export(result, "output_297.stl