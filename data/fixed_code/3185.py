import cadquery as cq
from cadquery import exporters
# --- Part 1: Cone Body ---
part_1_outer_radius = 0.375 * 0.75
part_1_inner_radius = 0.0375 * 0.75
part_1_height = 0.12
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Cylinder Cutout ---
part_2_radius = 0.0375 * 0.0625
part_2_height = 0.12
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)
)
# --- Part 3: Cylinder Cutout ---
part_3_radius = 0.0188 * 0.0238
part_3_height = 0.1031
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_3185.stl