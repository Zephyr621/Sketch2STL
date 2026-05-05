import cadquery as cq
# --- Part 1: Cylinder with Hollow Interior ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1988 * 0.75  # Inner radius scaled
height = 0.3482
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.3482, 0))
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
# Export to STL
cq
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1980.stl