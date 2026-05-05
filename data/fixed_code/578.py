import cadquery as cq
# --- Part 1: Cylinder with Hollow Interior ---
outer_radius = 0.2679 * 0.5357  # Sketch radius scaled
inner_radius = 0.1071 * 0.5357  # Inner radius scaled
height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z").workplane()
    .circle(inner_radius)
    .cutThruAll()
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# --- Export to STL ---
cq.
# --- Final Result ---
result = assembly
cq.
cq.
cq.cq.exporters.export(result,
# 导出为STL文件
cq.exporters.export(result, "output_578.stl