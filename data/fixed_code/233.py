import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.27 * 0.75   # Inner radius scaled
height = 0.5714
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z").workplane()
    .circle(inner_radius)
    .cutThruAll()
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
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_233.stl