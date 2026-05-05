import cadquery as cq
# --- Part 1: Flat Washer ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_radius = 0.1714 * 0.75  # Inner hole radius scaled
height = 0.0536
# Create the washer by making a circle and then cutting out a smaller circle
washer = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .circle(inner_radius)
    .cutThruAll()
)
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
cq.
# Export to STL
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_322.stl