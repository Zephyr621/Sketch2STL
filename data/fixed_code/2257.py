import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.25 * 0.5  # Sketch radius scaled
inner_radius = 0.125 * 0.5  # Inner radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# --- Final Result ---
result = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq
# 导出为STL文件
cq.exporters.export(result, "output_2257.stl