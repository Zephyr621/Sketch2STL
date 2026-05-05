import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.2707 * 0.5183  # Sketch radius scaled
part_1_inner_radius = 0.1878 * 0.5183  # Hole radius scaled
part_1_height = 0.5554
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.2182, 0.5554, 0.2182))
# --- Part 2: Cube with Circular Hole ---
part_2_size = 0.75 * 0.75  # Sketch size scaled
part_2_hole_radius = 0.1429 * 0.75  # Hole radius scaled
part_2_height = 0.555
part_2 = (
    cq.Workplane("XY")
    .rect(part_2_size, part_2_
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3179.stl