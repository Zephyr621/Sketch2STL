import cadquery as cq
# --- Part 1: Cube with Rounded Corners ---
length = 0.75 * 0.75  # Scaled length
width = 0.6281 * 0.75  # Scaled width
height = 0.3719
part_1 = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(length, 0)
    .lineTo(length / 2, width)
    .lineTo(0, width)
    .close()
    .extrude(height)
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
# 导出为STL文件
cq.exporters.export(result, "output_614.stl