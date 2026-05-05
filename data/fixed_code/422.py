import cadquery as cq
from cadquery import exporters
# --- Part 1: Cylinder ---
part_1_outer_radius = 0.15 * 0.3  # Sketch radius scaled
part_1_inner_radius = 0.075 * 0.3
part_1_height = 0.75
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .extrude(part_1_height)
    .cut(cq.Workplane("XY").circle(part_1_inner_radius).extrude(part_1_height))
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0, 0.75, 0))
# --- Part 2: Smaller Cylinder on Top ---
part_2_radius = 0.075 * 0.15  # Sketch radius scaled
part_2_height = 0.2
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(-part_2_height)
)
# --- Coordinate System
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_422.stl