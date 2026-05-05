import cadquery as cq
# --- Part 1: Rectangular Plate ---
part_1_length = 0.3937 * 0.75
part_1_width = 0.75 * 0.75
part_1_height = 0.0391
part_1 = (
    cq.Workplane("XY")
    .rect(part_1_length, part_1_width)
    .extrude(-part_1_height)
)
# --- Coordinate System Transformation for Part 1 ---
part_1 = part_1.translate((0, 0, 0.0391))
# --- Part 2: Cylinder ---
part_2_radius = 0.1758 * 0.4091
part_2_height = 0.0391
part_2 = (
    cq.Workplane("XY")
    .circle(part_2_radius)
    .extrude(part_2_height)
)
# --- Coordinate System Transformation for Part 2 ---
part_2 = part_2.rotate((0, 0, 0), (1, 0, 0), -90)
part_2 = part_2.rotate((0, 0, 0), (0, 0, 1), -90)
part_2 = part_2.translate
# Export
# 定义结果变量
result = result
# 导出为STL文件
cq.exporters.export(result, "output_2863.stl