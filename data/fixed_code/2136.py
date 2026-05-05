import cadquery as cq
# --- Part 1: Cylinder with Hole ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1364 * 0.75
height = 0.2386
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .cut(cq.Workplane("XY").circle(inner_radius).extrude(height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.2386))
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.
cq.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2136.stl