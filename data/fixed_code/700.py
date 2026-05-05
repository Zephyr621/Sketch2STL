import cadquery as cq
# --- Part 1: Cylinder ---
part_1_outer_radius = 0.075 * 0.15  # Sketch radius scaled
part_1_inner_radius = 0.0625 * 0.15
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .faces(">Z")
    .workplane()
    .circle(part_1_inner_radius)
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
cq.
# 导出为STL文件
cq.exporters.export(result, "output_700.stl