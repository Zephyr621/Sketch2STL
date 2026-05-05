import cadquery as cq
# --- Part 1: Cylinder with Hole ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1687 * 0.75  # Inner hole radius scaled
height = 0.375
wp = cq.Workplane("XY").circle(outer_radius).extrude(height)
hole = cq.Workplane("XY").circle(inner_radius).extrude(height)
part_1 = wp.cut(hole)
# --- Final Result ---
result = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.
cq.
# Export to STL
cq.
cq.
cq.
# Export to STL
cq.exp
# 导出为STL文件
cq.exporters.export(result, "output_1518.stl