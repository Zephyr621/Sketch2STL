import cadquery as cq
# --- Part 1: Cylinder with a hole ---
outer_radius = 0.0625 * 0.125  # Sketch radius scaled
inner_radius = 0.0562 * 0.125  # Inner circle radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# --- Final Result ---
result = part_1
cq.cq.exporters.export(
# 导出为STL文件
cq.exporters.export(result, "output_1691.stl