import cadquery as cq
# --- Part 1: Cup ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.2792 * 0.75
height = 0.0337
cup = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z").workplane()
    .circle(inner_radius)
    .cutThruAll()
)
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = cup
cq.
cq.
cq.
cq.
cq.
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_1962.stl