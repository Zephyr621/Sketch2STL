import cadquery as cq
# --- Part 1: Ring ---
outer_radius = 0.0589 * 0.1178  # Sketch radius scaled
inner_radius = 0.0352 * 0.1178
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(height)
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
cq.
cq.exporters.
# 导出为STL文件
cq.exporters.export(result, "output_1507.stl