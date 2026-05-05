import cadquery as cq
# --- Part 1: Cylinder with Hole ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.125 * 0.75  # Inner hole radius scaled
height = 0.2462
wp = cq.Workplane("XY")
outer_circle = wp.circle(outer_radius).extrude(height)
inner_circle = wp.workplane().circle(inner_radius).extrude(height)
part_1 = outer_circle.cut(inner_circle)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.2462, 0))
# --- Assembly ---
assembly = part_1
# Export to STL
cq.
# Export to STL
cq.
cq.
# Export to STL
cq.
cq.
cq.cq.exporters.export(assembly,
# 定义结果变量
result = wp
# 导出为STL文件
cq.exporters.export(result, "output_2107.stl