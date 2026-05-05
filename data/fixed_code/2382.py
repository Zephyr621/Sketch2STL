import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.3471 * 0.6895  # Sketch radius scaled
part_1_inner_radius = 0.0716 * 0.6895
part_1_height = 0.2282
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.0089, 0.2282, 0.0089))
# --- Part 2: Ring ---
part_2_outer_radius = 0.2761 * 0.5455  # Sketch radius scaled
part_2_inner_radius = 0.1744 * 0.5455
part_2_height = 0.0453
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2382.stl