import cadquery as cq
# --- Part 1: Cylinder with Hollow Center ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1988 * 0.75  # Inner radius scaled
height = 0.25
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.25, 0))
# --- Assembly (if needed, based on the single part) ---
# In this case, there's only one part, so no assembly is needed.
# If there were multiple parts, you would use .union() or .cut() to combine them.
# --- Final Result ---
result = part_1
cq.
cq.
cq.
# 导出为STL文件
cq.exporters.export(result, "output_1695.stl