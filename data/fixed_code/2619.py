import cadquery as cq
from math import radians
# --- Part 1: Ring Base ---
part_1_outer_radius = 0.2945 * 0.589
part_1_inner_radius = 0.1178 * 0.589
part_1_height = 0.1178
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Part 2: Cylinder ---
part_2_outer_radius = 0.216 * 0.4388
part_2_inner_radius = 0.1178 * 0.4388
part_2_height = 0.1178
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .extrude(part_2_height)
    .cut(cq.Workplane("XY").circle(part_2_inner_radius).extrude(part_2_height))
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.translate((0.0785, 0.0785, 0.1178))
# --- Assembly ---
assembly = part_1.union(part_2)
# --- Export to STL ---
cq.cq.exporters.export(assembly
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2619.stl