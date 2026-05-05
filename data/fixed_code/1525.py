import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_radius = 0.25 * 0.5  # Sketch radius scaled
part_1_height = 0.75
part_1 = cq.Workplane("XY").circle(part_1_radius).extrude(part_1_height)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Cylinder with Hollow Center ---
outer_radius = 0.1125 * 0.225  # Outer radius scaled
inner_radius = 0.0937 * 0.225  # Inner radius scaled
part_2_height = 0.25
part_2 = (
    cq.Workplane("XY")
    .circle(outer_radius)
    .circle(inner_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate((0.125, 0.25, 0.125))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
exporters.
# 定义结果变量
result = part_1
# 导出为STL文件
cq.exporters.export(result, "output_1525.stl