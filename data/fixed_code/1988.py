import cadquery as cq
# --- Part 1: Disk with Line ---
outer_radius = 0.375 * 0.75  # Sketch radius scaled
inner_width = (0.4286 - 0.2812) * 0.75
inner_height = (0.1406 - 0.0107) * 0.75
extrude_depth = 0.0188
part_1 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .extrude(extrude_depth)
    .cut(cq.Workplane("XY").rect(inner_width, inner_height).extrude(extrude_depth))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (1, 0, 0), -90)
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
# --- Assembly ---
assembly = part_1
cq.
# Export to STL
cq.
# Export to STL
cq.exporters.
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_1988.stl