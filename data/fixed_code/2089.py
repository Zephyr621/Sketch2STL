import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder with Hole ---
part_1_outer_radius = 0.1038 * 0.2075  # Sketch radius scaled
part_1_inner_radius = 0.0536 * 0.2075  # Inner radius scaled
part_1_height = 0.2075
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0.2177, 0.2177, 0))
# --- Part 2: Cylinder with Hole ---
part_2_outer_radius = 0.1037 * 0.2075  # Sketch radius scaled
part_2_inner_radius = 0.0536 * 0.2075  # Inner radius scaled
part_2_height = 0.2075
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).extrude(part_2_height
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2089.stl