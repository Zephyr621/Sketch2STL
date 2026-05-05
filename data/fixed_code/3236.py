import cadquery as cq
# --- Part 1: Cylinder ---
part_1_radius_outer = 0.375 * 0.75  # Sketch radius scaled
part_1_radius_inner = 0.3188 * 0.75
part_1_height = 0.0094
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_radius_outer)
    .extrude(part_1_height)
    .faces(">Z").workplane()
    .circle(part_1_radius_inner)
    .cutThruAll()
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
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_3236.stl