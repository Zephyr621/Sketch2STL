import cadquery as cq
from cadquery import exporters
# --- Part 1: Disk ---
part_1_outer_radius = 0.2707 * 0.5591  # Sketch radius scaled
part_1_inner_radius = 0.1364 * 0.5591
part_1_height = 0.0818
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.1167, 0.1167, 0.0818))
# --- Part 2: Cylinder ---
part_2_outer_radius = 0.2679 * 0.5357  # Sketch radius scaled
part_2_inner_radius = 0.1339 * 0.5357
part_2_height = 0.0214
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(part_2_height)
)
# --- Assembly ---
assembly = part_1.union(part_2)
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2567.stl