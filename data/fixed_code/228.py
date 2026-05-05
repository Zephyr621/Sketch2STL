import cadquery as cq
from cadquery.vis import show
# --- Part 1: Cylinder ---
part_1_outer_radius = 0.25 * 0.5  # Sketch radius scaled
part_1_inner_radius = 0.125 * 0.5
part_1_height = 0.3
part_1 = (
    cq.Workplane("XY")
    .circle(part_1_outer_radius)
    .circle(part_1_inner_radius)
    .extrude(part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.rotate((0, 0, 0), (0, 0, 1), -90)
part_1 = part_1.translate((0.15, 0.3, 0))
# --- Part 2: Cut Cylinder ---
part_2_outer_radius = 0.375 * 0.75  # Sketch radius scaled
part_2_inner_radius = 0.125 * 0.75
part_2_height = 0.075
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_outer_radius)
    .circle(part_2_inner_radius)
    .extrude(-part_2_height)  # Extrude in the opposite direction for cutting
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_228.stl